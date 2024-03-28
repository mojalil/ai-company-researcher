from job_manager import append_event


class CompanyReseachCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id

    def setup_crew(self, companies: list[str], positions: list[str]):
        print(f'Running crew with job_id: {self.job_id}')
        print(f'Companies: {companies}')
        print(f'Positions: {positions}')

        # TODO: Setup agents
        # TODO: Setup task
        # TODO: Setup crew

    def kickoff_crew(self):
        if not self.crew:
            print(f'Crew with job_id: {self.job_id} not setup')
            return
        
        append_event(self.job_id, 'CREW STARTED')
        try:
            print(f'Running crew with job_id: {self.job_id}')
            result = self.crew.kickoff()
            append_event(self.job_id, 'CREW COMPLETED')
            return result
        except Exception as e:
            print(f'Error running crew with job_id: {self.job_id}')
            append_event(self.job_id, f'CREW ERROR: {str(e)}')
            return str(e)