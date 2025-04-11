# claim_tools.py
"""Tools for handling insurance claim filing and status checks."""

from typing import Dict, Any
from . import config
from . import utils


def file_claim(policy_number: str, incident_details: Dict[str, Any]) -> Dict[str, Any]:
    """Files an insurance claim for a given policy."""
    if not policy_number or not policy_number.startswith(config.POLICY_PREFIX):
        return utils.create_error_response(
            f"Valid policy number starting with '{config.POLICY_PREFIX}' is required."
        )

    incident_date = incident_details.get("date")
    incident_description = incident_details.get("description")
    if not incident_date or not incident_description:
        return utils.create_error_response(
            "Incident details must include date and description."
        )

    claim_number = utils.generate_pseudo_unique_id(
        config.CLAIM_PREFIX, policy_number, incident_date
    )

    return {
        "status": config.STATUS_SUCCESS,
        "claim": {
            "claim_number": claim_number,
            "policy_number": policy_number,
            "status": config.CLAIM_STATUS_REVIEW,
            "submission_date": utils.get_current_date(),
            "incident_date": incident_date,
            "estimated_processing_time": config.DEFAULT_ESTIMATED_PROCESSING_TIME,
        },
    }


def check_claim_status(claim_number: str) -> Dict[str, Any]:
    """Checks the status of an existing insurance claim."""
    if not claim_number or not claim_number.startswith(config.CLAIM_PREFIX):
        return utils.create_error_response(
            f"Valid claim number starting with '{config.CLAIM_PREFIX}' is required."
        )

    # --- Claim Status Logic (Example based on last digit) ---
    try:
        # Use hash for pseudo-randomness based on claim number itself for demo
        claim_hash = hash(claim_number)
        status_determinant = claim_hash % 10  # Get a value 0-9

        if status_determinant < 3:
            status = config.CLAIM_STATUS_REVIEW
            message = "Your claim is currently under review by our claims department."
        elif status_determinant < 6:
            status = config.CLAIM_STATUS_INFO_NEEDED
            message = "We need additional information to process your claim. Please check your email."
        elif status_determinant < 9:
            status = config.CLAIM_STATUS_APPROVED
            message = "Your claim has been approved. Payment will be processed within 5 business days."
        else:  # status_determinant == 9
            status = config.CLAIM_STATUS_COMPLETED
            message = "Your claim has been processed and payment has been issued."

    except Exception:  # Catch potential errors in the logic
        return utils.create_error_response("Could not determine claim status.")
    # --- End Claim Status Logic ---

    return {
        "status": config.STATUS_SUCCESS,
        "claim_status": {
            "claim_number": claim_number,
            "status": status,
            "message": message,
            "last_updated": utils.get_current_date(),
        },
    }
