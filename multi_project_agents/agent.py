from google.adk import Agent
from google.adk.models.anthropic_llm import Claude
from google.adk.models.google_llm import Gemini

# Test your new feature
claude_agent_location = Agent(
    model=Claude(model="claude-sonnet-4",location="us-east5"),
    description="Location agent",
    instruction=("You are a helpful Location agent, that can answer questions, and transfer back to a gemini agent"),
    name="test_claude_different_location"
)

claude_agent_project = Agent(
    model=Claude(model="claude-3-7-sonnet",project_id="some-project",location="us-east5"),
    description="Project agent",
    instruction=("You are a helpful Project agent, that can answer questions, and transfer back to a gemini agent"),
    name="test_claude_different_project"
)


root_agent = Agent(
    name="gemini_default_location_and_project",
    model="gemini-2.0-flash",
    instruction=("You are a helpful agent, that can answer questions,when asked about location transfer to the location agent. When asked about project, transfer to the project agent"),
    sub_agents= [claude_agent_location,claude_agent_project]
)