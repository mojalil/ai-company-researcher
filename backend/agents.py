from typing import List
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

from tools.youtube_search_tools import YoutubeVideoSearchTool
class CompanyResearchAgents():
    def __init__(self):

        self.youtubeSearchTool = YoutubeVideoSearchTool()
        self.searchInternetTool = SerperDevTool()
        self.llm = ChatOpenAI(model="gpt-4-turbo-preview")

    def research_manager(self, companies: List[str], positions: List[str]) -> Agent:
        return Agent(
            role="Company Research Manager",
            goal=f"""Generate a list of JSON objects containing the urls for 3 recent blog articles and 
                the url and title for 3 recent YouTube interview, for each position in each company.
             
                Companies: {companies}
                Positions: {positions}

                Important:
                - The final list of JSON objects must include all companies and positions. Do not leave any out.
                - If you can't find information for a specific position, fill in the information with the word "MISSING".
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information for each position in each company.
                - All the companies and positions exist so keep researching until you find the information for each one.
                - Make sure you each researched position for each company contains 3 blog articles and 3 YouTube interviews.
                """,
            backstory="""As a Company Research Manager, you are responsible for aggregating all the researched information
                into a list.""",
            llm=self.llm,
            tools=[self.searchInternetTool, self.youtubeSearchTool], 
            verbose=True,
            allow_delegation=True
        )
    
    def company_research_agent(self) -> Agent:
        return Agent(
            role="Company Research Agent",
            goal="""Look up the specific positions for a given company and find urls for 3 recent blog articles and 
                the url and title for 3 recent YouTube interview for each person in the specified positions. It is your job to return this collected 
                information in a JSON object""",
            backstory="""As a Company Research Agent, you are responsible for looking up specific positions 
                within a company and gathering relevant information.
                
                Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Make sure you find the persons name who holds the position.
                - Do not generate fake information. Only return the information you find. Nothing else!
                """,
            tools=[self.searchInternetTool, self.youtubeSearchTool],
            llm=self.llm,
            verbose=True
    )

    # Agents to get company funding, funding rounds, revenue, employees, acquisition, IPO, and competitors

    def funding_details_agent(self) -> Agent:
        return Agent(
            role="Funding Details Agent",
            goal="""Extract detailed information on each funding round for a given company, including the round type 
            (e.g., Seed, Series A), the amount raised, the names of the investors, and the date of the funding round. 
            Structure this information in a detailed report, presented as a list of JSON objects where each object 
            represents a funding round.""",
            backstory="""As a Funding Details Agent, your expertise lies in unraveling the financial journey of startups. 
            You meticulously comb through financial databases, news articles, and investment trackers to compile the most 
            accurate and up-to-date funding data. Your reports illuminate the financial path a startup has navigated, showcasing 
            the confidence and investment it has garnered from the financial community over time.""",
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True,
            allow_delegation=True,
            memory=True,  # Considering memory might help in keeping track of previous searches and data extracted.
            goal_specifics={
                "expected_output": """A list of JSON objects, each representing a funding round with the following keys: 
                'round_type', 'amount_raised_usd', 'investors', and 'date'. Example format:
                [
                    {
                        'round_type': 'Seed',
                        'amount_raised_usd': 2000000,
                        'investors': ['Investor A', 'Investor B'],
                        'date': '2021-06-15'
                    },
                    ...
                ]""",
                "output_format": "JSON",
                "data_sources": ["financial databases", "official press releases", "trusted news outlets"]
            }
        )

    def company_funding_agent(self) -> Agent:
        return Agent(
            role="Company Funding Agent",
            goal="""Find the total funding amount for a given company and return the amount in USD""",
            backstory="""As a Company Funding Agent, you are responsible for finding the total funding amount for a company.
                
                Important:
                - Only return the total funding amount in USD. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the funding amount, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
    def company_funding_rounds_agent(self) -> Agent:
        return Agent(
            role="Company Funding Rounds Agent",
            goal="""Find the various funding rounds for a given company and return the rounds in a list""",
            backstory="""As a Company Funding Rounds Agent, you are responsible for finding the various funding rounds for a company.
                
                Important:
                - Only return the funding rounds in a list. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the funding rounds, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
        # Add an agent that can find the company's valuation
    def company_valuation_agent(self) -> Agent:
        return Agent(
            role="Company Valuation Agent",
            goal="""Find the valuation of a given company and return the amount in USD""",
            backstory="""As a Company Valuation Agent, you are responsible for finding the valuation of a company.
                
                Important:
                - Only return the valuation amount in USD. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the valuation amount, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )

    def company_revenue_agent(self) -> Agent:
        return Agent(
            role="Company Revenue Agent",
            goal="""Find the total revenue for a given company and return the amount in USD""",
            backstory="""As a Company Revenue Agent, you are responsible for finding the total revenue for a company.
                
                Important:
                - Only return the total revenue amount in USD. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the revenue amount, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
    def company_employees_agent(self) -> Agent:
        return Agent(
            role="Company Employees Agent",
            goal="""Find the total number of employees for a given company and return the number""",
            backstory="""As a Company Employees Agent, you are responsible for finding the total number of employees for a company.
                
                Important:
                - Only return the total number of employees. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the number of employees, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
    def company_acquisition_agent(self) -> Agent:
        return Agent(
            role="Company Acquisition Agent",
            goal="""Find the acquisition details for a given company and return the company that acquired them, the acquisition amount in USD, and the acquisition date""",
            backstory="""As a Company Acquisition Agent, you are responsible for finding the acquisition details for a company.
                
                Important:
                - Only return the company that acquired them, the acquisition amount in USD, and the acquisition date. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the acquisition details, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
    def company_ipo_agent(self) -> Agent:
        return Agent(
            role="Company IPO Agent",
            goal="""Find the IPO details for a given company and return the IPO date and the IPO price""",
            backstory="""As a Company IPO Agent, you are responsible for finding the IPO details for a company.
                
                Important:
                - Only return the IPO date and the IPO price. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the IPO details, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
    def company_competitor_agent(self) -> Agent:
        return Agent(
            role="Company Competitor Agent",
            goal="""Find the top 3 competitors for a given company and return the competitors in a list""",
            backstory="""As a Company Competitor Agent, you are responsible for finding the top 3 competitors for a company.
                
                Important:
                - Only return a list of the top 3 competitors. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the competitors, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
    def company_reviews_agent(self) -> Agent:
        return Agent(
            role="Company Reviews Agent",
            goal="""Find the reviews for a given company and return the reviews in a list""",
            backstory="""As a Company Reviews Agent, you are responsible for finding the reviews for a company.
                
                Important:
                - Only return a list of reviews. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the reviews, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
    def company_location_agent(self) -> Agent:
        return Agent(
            role="Company Location Agent",
            goal="""Find the location of a given company and return the location""",
            backstory="""As a Company Location Agent, you are responsible for finding the location of a company.
                
                Important:
                - Only return the location. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the location, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
    def company_founder_agent(self) -> Agent:
        return Agent(
            role="Company Founder Agent",
            goal="""Find the name of the founder of a given company and return the name""",
            backstory="""As a Company Founder Agent, you are responsible for finding the name of the founder of a company.
                
                Important:
                - Only return the name of the founder. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the founder's name, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
    
    def company_product_agent(self) -> Agent:
        return Agent(
            role="Company Product Agent",
            goal="""Find the main product of a given company and return the product name""",
            backstory="""As a Company Product Agent, you are responsible for finding the main product of a company.
                
                Important:
                - Only return the product name. Nothing else!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - If you can't find the product name, return "MISSING".
                """,
            tools=[self.searchInternetTool],
            llm=self.llm,
            verbose=True
        )
