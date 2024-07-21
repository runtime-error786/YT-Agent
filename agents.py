from crewai import Agent, Task, Crew

from langchain.llms import Ollama

from tools import youtube_tool

import os


llm = Ollama(model="llama3")



researcher_agent = Agent(
    role="Researcher",
    goal="Search for videos related to the given {topic} on the specified YouTube channel and extract key points.",
    backstory="You are a researcher tasked with finding and summarizing video content from a specific YouTube channel.",
    tools=[youtube_tool],
    verbose=True,
    allow_delegation=True,
    llm=llm
)

writer_agent = Agent(
    role="Writer",
    goal="Write a summary or article based on the research findings provided.",
    backstory="You are a writer who specializes in creating content based on research data.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)