from threading import Thread
from uuid import uuid4
from flask import Flask, abort, jsonify, request

app = Flask(__name__)

def kickoff_crew(job_id: str, companies: list[str], positions: list[str]):
    print(f'Running crew with job_id: {job_id}')
    print(f'Companies: {companies}')
    print(f'Positions: {positions}')

    # run the crew here
    print('Crew finished')

    # Setup the crew

    # Run the crew

    # Let app know we are done

@app.route('/api/crew', methods=['POST'])
def run_crew():
    data = request.json
    if not data or 'companies' not in data or 'positions' not in data:
        abort(400, description='Invalid request data or missing required fields')
    
    job_id = str(uuid4())
    companies = data['companies']
    positions = data['positions']

    # run the crew
    thread = Thread(target=kickoff_crew, args=(job_id, companies, positions))
    thread.start()

    return jsonify({'job_id': job_id}), 200

@app.route('/api/crew/<job_id>', methods=['GET'])
def get_crew(job_id):
    return jsonify({'status': f'getting status of {job_id}'}), 200

# run the server
if __name__ == '__main__':
    app.run(debug=True, port=3001)