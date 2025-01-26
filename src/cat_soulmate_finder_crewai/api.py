from typing import Union

from fastapi import FastAPI

from dotenv import load_dotenv
import agentops
from crewai import Crew, Process
from cat_soulmate_finder_crewai.agents import research_Agent, writer_Agent, editor_Agent
from cat_soulmate_finder_crewai.tasks import cat_internet_research_task, cat_human_comparison_task, generate_report_task
#import weave

app = FastAPI()

crew = Crew(
    agents=[research_Agent, writer_Agent, editor_Agent],
    tasks=[cat_internet_research_task, cat_human_comparison_task, generate_report_task],
    process=Process.hierarchical,  
    manager_llm="gemini/gemini-2.0-flash-thinking-exp-1219",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

agentops.init()
load_dotenv(override=True)

#@weave.op()
@app.post("/soulmate")
def get_soulmate(human_input:str)->str:
    #weave.init("mfmezger/nnagel-llmcourse")
    
    results = crew.kickoff(inputs={'human_input': human_input})

    print(results.raw)
    return results.raw
    
