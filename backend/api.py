from datetime import datetime
import json
from threading import Thread
from uuid import uuid4
from flask import Flask, abort, jsonify, request
from flask_cors import CORS

from job_manager import append_event, jobs_lock, jobs, Event
from crew import CompanyFundingCrew, CompanyReseachCrew

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


def kickoff_crew(job_id: str, companies: list[str], positions: list[str]):
    print(
        f"Running crew with job_id: {job_id} with companies: {companies} and positions: {positions}"
    )

    results = None
    funding_results = None
    try:

        # Setup the Research Crew
        company_research_crew = CompanyReseachCrew(job_id)
        company_research_crew.setup_crew(companies, positions)
        results = company_research_crew.kickoff()

        # Setup the Funding Crew
        company_funding_crew = CompanyFundingCrew(job_id)
        company_funding_crew.setup_crew(companies)
        funding_results = company_funding_crew.kickoff()

    except Exception as e:
        print(f"CREW FAILED : with error {str(e)} and job_id: {job_id}")
        append_event(job_id, f"CREW ERROR: {str(e)}")
        with jobs_lock:
            jobs[job_id].status = "ERROR"
            jobs[job_id].result = str(e)
            

    with jobs_lock:
        jobs[job_id].status = "COMPLETED"
        jobs[job_id].result = [*results, *funding_results]
        jobs[job_id].events.append(
            Event(data="CREW COMPLETED", timestamp=datetime.now())
        )

    # Let app know we are done


@app.route("/api/crew", methods=["POST"])
def run_crew():
    data = request.json
    if not data or "companies" not in data or "positions" not in data:
        abort(400, description="Invalid request data or missing required fields")

    job_id = str(uuid4())
    companies = data["companies"]
    positions = data["positions"]

    # run the crew
    thread = Thread(target=kickoff_crew, args=(job_id, companies, positions))
    thread.start()

    return jsonify({"job_id": job_id}), 200


@app.route("/api/crew/<job_id>", methods=["GET"])
def get_crew(job_id):

    # TODO: Lock the job
    with jobs_lock:
        if job_id not in jobs:
            abort(404, description="Job not found")

        job = jobs[job_id]

    # Parse the json data
    try:
        job.result = json.loads(job.result)
    except:
        result_json = job.result

    # Return the job status
    return jsonify(
        {
            "job_id": job_id,
            "status": job.status,
            "result": job.result,
            "events": [
                {"timestamp": event.timestamp.isoformat(), "data": event.data}
                for event in job.events
            ],
        }
    )


# run the server
if __name__ == "__main__":
    app.run(debug=True, port=3001)
