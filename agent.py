# agent.py
"""Defines the Agents for the insurance application using sequential execution."""

# Import the standard Agent class
from google.adk.agents import LlmAgent, Agent

# Import configurations
from . import config

# Import tools from their respective modules
from .policy_tools import get_insurance_quotes, purchase_policy
from .claim_tools import file_claim, check_claim_status
from .routing_tools import route_to_agent  # Removed handle_agent_launch if not needed

# --- Agent Definitions ---

# Use standard Agent for sequential tool execution
policy_agent = Agent(
    name=config.POLICY_AGENT_NAME,
    model=config.DEFAULT_AGENT_MODEL,
    description="Agent to help customers get insurance quotes and purchase policies. It can also help with changes to existing policies.",
    instruction=f"""I can help you get insurance quotes and purchase a policy. I can provide quotes for auto, home, health, and life insurance. 
            If you'd like to make changes to an existing policy, I can help as well.""",
    tools=[get_insurance_quotes, purchase_policy],
)

# Use standard Agent for sequential tool execution
claims_agent = Agent(
    name=config.CLAIMS_AGENT_NAME,
    model=config.DEFAULT_AGENT_MODEL, 
    description="Agent to help customers file and track insurance claims",
    instruction="I can help you file a new insurance claim or check the status of an existing claim.",
    tools=[file_claim, check_claim_status],
)

# Use standard Agent for sequential tool execution
root_agent = Agent(
    name=config.ROOT_AGENT_NAME,
    model=config.DEFAULT_AGENT_MODEL,
    description="Main insurance agent that directs users to specialized agents for policies and claims",
    instruction=f"""
    You are the main insurance assistant. Your primary job is to understand the user's request and route them to the correct specialized agent (policy or claims).

    If the user's intent is unclear, ask them to clarify their request.

    """,
    sub_agents=[
        policy_agent,
        claims_agent,
    ],  # Specify sub-agents
)
