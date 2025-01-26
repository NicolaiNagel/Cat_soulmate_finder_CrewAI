from dotenv import load_dotenv
import agentops
from crewai import Crew, Process
from cat_soulmate_finder_crewai.agents import research_Agent, writer_Agent, editor_Agent
from cat_soulmate_finder_crewai.tasks import cat_internet_research_task, cat_human_comparison_task, generate_report_task

agentops.init()
load_dotenv(override=True)

def main():
    crew = Crew(
    agents=[research_Agent, writer_Agent, editor_Agent],
    tasks=[cat_internet_research_task, cat_human_comparison_task, generate_report_task],
    process=Process.hierarchical,  
    manager_llm="gemini/gemini-2.0-flash-thinking-exp-1219",
    )
    results_1 = crew.kickoff(inputs={'human_input': 'Im living in a 1 room flat and am chill and dont like noise, but want to cuddle with my cat often. Im out of my home for most of the day due to work and can only pay up to 1000 euro for the cat.'})
    #results_2 = crew.kickoff(inputs={'human_input': 'Im living in a big house with big garden with young and middle age kids, who can be loud. We also have a dog.'})
    print(results_1.raw)
    #print(results_2.raw)


if __name__ == "__main__":
    main()
    
    



