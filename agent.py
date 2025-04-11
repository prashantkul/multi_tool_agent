# agent.py
"""Defines the Agents for the insurance application using sequential execution."""

# Import the standard Agent class
from google.adk.agents import LlmAgent

# Import configurations
from . import config

# Import tools from their respective modules
from .policy_tools import get_insurance_quotes, purchase_policy
from .claim_tools import file_claim, check_claim_status
from .routing_tools import route_to_agent  # Removed handle_agent_launch if not needed

# --- Agent Definitions ---

# Use standard Agent for sequential tool execution
policy_agent = LlmAgent(
    name=config.POLICY_AGENT_NAME,
    # model=config.DEFAULT_AGENT_MODEL, # Removed model parameter
    description="Agent to help customers get insurance quotes and purchase policies",
    instruction="I can help you get insurance quotes and purchase a policy. I can provide quotes for auto, home, health, and life insurance.",
    tools=[get_insurance_quotes, purchase_policy],
)

# Use standard Agent for sequential tool execution
claims_agent = LlmAgent(
    name=config.CLAIMS_AGENT_NAME,
    # model=config.DEFAULT_AGENT_MODEL, # Removed model parameter
    description="Agent to help customers file and track insurance claims",
    instruction="I can help you file a new insurance claim or check the status of an existing claim.",
    tools=[file_claim, check_claim_status],
)

# Use standard Agent for sequential tool execution
root_agent = LlmAgent(
    name=config.ROOT_AGENT_NAME,
    # model=config.DEFAULT_AGENT_MODEL, # Removed model parameter
    description="Main insurance agent that directs users to specialized agents for policies and claims",
    instruction=f"""
    You are the main insurance assistant. Your primary job is to understand the user's request and route them to the correct specialized agent (policy or claims) using the 'route_to_agent' tool.

    Analyze the user's query.
    - If it's about getting quotes, buying insurance, or general policy questions, use the 'route_to_agent' tool to direct them to the '{config.POLICY_AGENT_NAME}'.
    - If it's about filing a claim, checking claim status, or reporting an incident, use the 'route_to_agent' tool to direct them to the '{config.CLAIMS_AGENT_NAME}'.
    - If the intent is unclear, use the 'route_to_agent' tool to ask for clarification (which will keep them with you, the '{config.ROOT_AGENT_NAME}').

    **Mandatory Action:** Call the 'route_to_agent' tool. Do not generate conversational text before the tool call.
    """,
    tools=[route_to_agent],  # Only include route_to_agent
)
