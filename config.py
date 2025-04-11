# config.py
"""Configuration constants for the insurance agent application."""

# Agent Names
ROOT_AGENT_NAME = "insurance_root_agent"
POLICY_AGENT_NAME = "insurance_policy_agent"
CLAIMS_AGENT_NAME = "insurance_claims_agent"
AGENT_NAMES = [ROOT_AGENT_NAME, POLICY_AGENT_NAME, CLAIMS_AGENT_NAME]

# Status Messages
STATUS_SUCCESS = "success"
STATUS_ERROR = "error"

# Routing Actions & Confidence
ACTION_HANDLE_QUERY = "handle_query"
ACTION_CLARIFY_INTENT = "clarify_intent"
CONFIDENCE_HIGH = "high"
CONFIDENCE_LOW = "low"

# Policy & Claim Prefixes
POLICY_PREFIX = "POL-"
CLAIM_PREFIX = "CLM-"

# Supported Insurance Types
SUPPORTED_INSURANCE_TYPES = ["auto", "home", "health", "life"]

# Routing Keywords
POLICY_KEYWORDS = [
    "quote",
    "quotes",
    "policy",
    "purchase",
    "buy",
    "coverage",
    "premium",
    "insurance plan",
    "sign up",
    "enroll",
    "new customer",
    "auto insurance",
    "home insurance",
    "life insurance",
    "health insurance",
]
CLAIM_KEYWORDS = [
    "claim",
    "file a claim",
    "report",
    "incident",
    "damage",
    "accident",
    "status",
    "check claim",
    "claim number",
    "reimbursement",
    "payment",
    "approved",
    "denied",
    "processing",
    "under review",
]

# Claim Statuses (Example)
CLAIM_STATUS_REVIEW = "under_review"
CLAIM_STATUS_INFO_NEEDED = "additional_info_needed"
CLAIM_STATUS_APPROVED = "approved"
CLAIM_STATUS_COMPLETED = "completed"

# Agent Models (Example - can be customized per agent if needed)
DEFAULT_AGENT_MODEL = "gemini-2.0-flash-exp"

# Other Constants
DEFAULT_ESTIMATED_PROCESSING_TIME = "5-7 business days"
