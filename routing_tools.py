# routing_tools.py
"""Tools for routing user queries and handling agent launches."""

from typing import Dict, Any
from . import config


def route_to_agent(user_query: str) -> Dict[str, Any]:
    """Routes the user query to the appropriate specialized agent based on keywords."""
    query = user_query.lower()

    # Check for policy-related intent
    if any(keyword in query for keyword in config.POLICY_KEYWORDS):
        return {
            "status": config.STATUS_SUCCESS,
            "routing": {
                "target_agent": config.POLICY_AGENT_NAME,
                "action": config.ACTION_HANDLE_QUERY,
                "confidence": config.CONFIDENCE_HIGH,
            },
        }

    # Check for claim-related intent
    if any(keyword in query for keyword in config.CLAIM_KEYWORDS):
        return {
            "status": config.STATUS_SUCCESS,
            "routing": {
                "target_agent": config.CLAIMS_AGENT_NAME,
                "action": config.ACTION_HANDLE_QUERY,
                "confidence": config.CONFIDENCE_HIGH,
            },
        }

    # Default response for unclear intent
    return {
        "status": config.STATUS_SUCCESS,
        "routing": {
            "target_agent": config.ROOT_AGENT_NAME,
            "action": config.ACTION_CLARIFY_INTENT,
            "confidence": config.CONFIDENCE_LOW,
            "message": "I'm not sure if you need help with insurance policies or claims. Could you please clarify?",
        },
    }


def handle_agent_launch(agent_name: str) -> Dict[str, Any]:
    """Handles the launching of specialized agents based on user intent."""
    if agent_name not in [config.POLICY_AGENT_NAME, config.CLAIMS_AGENT_NAME]:
        valid_agents = f"'{config.POLICY_AGENT_NAME}' and '{config.CLAIMS_AGENT_NAME}'"
        # Use the utility function for consistency, although it's simple here
        from . import utils

        return utils.create_error_response(
            f"Unknown agent: {agent_name}. Valid agents are {valid_agents}."
        )

    launch_messages = {
        config.POLICY_AGENT_NAME: "Launching the policy specialist to help you with quotes and coverage options.",
        config.CLAIMS_AGENT_NAME: "Launching the claims specialist to assist with your insurance claim.",
    }

    return {
        "status": config.STATUS_SUCCESS,
        "launch": {"agent": agent_name, "message": launch_messages[agent_name]},
    }
