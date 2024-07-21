from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew
from agents import researcher_agent,writer_agent
from tasks import research_task,writing_task

my_crew = Crew(
    agents=[researcher_agent, writer_agent],
    tasks=[research_task, writing_task],
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

inputs = {"topic": "Dictionary in python"}
crew = my_crew.kickoff(inputs=inputs)
