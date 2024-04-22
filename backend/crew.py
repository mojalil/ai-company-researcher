from agents import CompanyResearchAgents
from task import CompanyResearchTask, FundingInformationTask
from job_manager import append_event
from crewai import Crew


class CompanyReseachCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id

    def setup_crew(self, companies: list[str], positions: list[str]):
        print(f"Running crew with job_id: {self.job_id}")
        print(f"Companies: {companies}")
        print(f"Positions: {positions}")

        agents = CompanyResearchAgents()
        research_manager = agents.research_manager(companies, positions)
        company_research_agent = agents.company_research_agent()
        
        tasks = CompanyResearchTask(self.job_id)

        company_research_task = [
            tasks.company_research(company_research_agent, company, positions)
            for company in companies
        ]

        manage_research_task = tasks.manage_research(
            research_manager, companies, positions, company_research_task
        )

        # TODO: Setup crew

        self.crew = Crew(
            agents=[research_manager, company_research_agent],
            tasks=[*company_research_task, manage_research_task ],
            verbose=2
        )

    def kickoff(self):
        if not self.crew:
            print(f"Crew with job_id: {self.job_id} not setup")
            return

        append_event(self.job_id, "CREW STARTED")
        try:
            print(f"Running crew with job_id: {self.job_id}")
            result = self.crew.kickoff()
            append_event(self.job_id, "CREW COMPLETED")
            return result
        except Exception as e:
            print(f"Error running crew with job_id: {self.job_id}")
            append_event(self.job_id, f"CREW ERROR: {str(e)}")
            return str(e)

# Create a crew for the finding company funding
class CompanyFundingCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id

    def setup_crew(self, companies: list[str]):
        print(f"Running crew with job_id: {self.job_id}")
        print(f"Companies: {companies}")

        agents = CompanyResearchAgents()
        funding_manager = agents.funding_manager(companies)
        funding_agent = agents.funding_research_agent()

        tasks = FundingInformationTask(self.job_id)

        funding_tasks = [
            tasks.extract_funding_details(funding_agent, company)
            for company in companies
        ]

        manage_funding_task = tasks.manage_funding(
            funding_manager, companies, funding_tasks
        )

        self.crew = Crew(
            agents=[funding_manager, funding_agent],
            tasks=[*funding_tasks, manage_funding_task],
            verbose=2
        )

    def kickoff(self):
        if not self.crew:
            print(f"Crew with job_id: {self.job_id} not setup")
            return

        append_event(self.job_id, "CREW STARTED")
        try:
            print(f"Running crew with job_id: {self.job_id}")
            result = self.crew.kickoff()
            append_event(self.job_id, "CREW COMPLETED")
            return result
        except Exception as e:
            print(f"Error running crew with job_id: {self.job_id}")
            append_event(self.job_id, f"CREW ERROR: {str(e)}")
            return str(e)
        
