from crewai import Agent, Task, Crew
from agents import researcher_agent,writer_agent

research_task = Task(
    description="Search for YouTube videos related to '{topic}' on YouTube channel and summarize the key points in detail.",
    expected_output="Summary of key points from the YouTube videos in detail.",
    agent=researcher_agent,
)

writing_task = Task(
    description="Write a summary or article based on the research findings from the Researcher Agent about '{topic}'.",
    expected_output="A well-written summary or article about the topic.",
    agent=writer_agent,
    context=[research_task],
    output_file='ai_news_summary.txt'
)
