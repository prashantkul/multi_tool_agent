# policy_tools.py
"""Tools for handling insurance policy quotes and purchases."""

from typing import Dict, Any
from . import config
from . import utils


def get_insurance_quotes(
    coverage_type: str, coverage_amount: int, customer_info: Dict[str, Any]
) -> Dict[str, Any]:
    """Generates insurance quotes based on coverage type, amount, and customer information."""
    normalized_coverage_type = coverage_type.lower()

    if normalized_coverage_type not in config.SUPPORTED_INSURANCE_TYPES:
        return utils.create_error_response(
            f"Coverage type '{coverage_type}' is not supported. "
            f"Please choose from {', '.join(config.SUPPORTED_INSURANCE_TYPES)}."
        )

    if coverage_amount <= 0:
        return utils.create_error_response("Coverage amount must be greater than zero.")

    if not customer_info.get("age") or not customer_info.get("location"):
        return utils.create_error_response(
            "Customer information must include age and location."
        )

    # --- Premium Calculation Logic (Example) ---
    base_premium = coverage_amount * 0.05  # 5% of coverage amount as base
    premium = base_premium

    if normalized_coverage_type == "auto":
        age_factor = (
            1.5 if customer_info.get("age", 99) < 25 else 1.0
        )  # Added default for safety
        premium *= age_factor
    elif normalized_coverage_type == "home":
        location_factor = (
            1.2 if customer_info.get("location", "").lower() == "coastal" else 1.0
        )
        premium *= location_factor
    # Add more complex logic for other types if needed
    # --- End Premium Calculation ---

    return {
        "status": config.STATUS_SUCCESS,
        "quotes": [
            {
                "provider": "InsureCo Standard",
                "monthly_premium": round(premium / 12, 2),
                "annual_premium": round(premium, 2),
                "coverage_amount": coverage_amount,
                "deductible": round(coverage_amount * 0.01, 2),  # 1% deductible
            },
            {
                "provider": "InsureCo Premium",
                "monthly_premium": round((premium * 1.2) / 12, 2),  # 20% higher premium
                "annual_premium": round(premium * 1.2, 2),
                "coverage_amount": coverage_amount,
                "deductible": round(coverage_amount * 0.005, 2),  # 0.5% deductible
            },
        ],
    }


def purchase_policy(
    quote_id: str, payment_info: Dict[str, Any], customer_info: Dict[str, Any]
) -> Dict[str, Any]:
    """Processes the purchase of an insurance policy."""
    if not quote_id:
        return utils.create_error_response("Quote ID is required.")

    if not payment_info.get("method"):
        return utils.create_error_response("Payment method is required.")

    customer_name = customer_info.get("name")
    customer_email = customer_info.get("email")
    if not customer_name or not customer_email:
        return utils.create_error_response(
            "Customer information must include name and email."
        )

    policy_number = utils.generate_pseudo_unique_id(
        config.POLICY_PREFIX, quote_id, customer_name
    )

    return {
        "status": config.STATUS_SUCCESS,
        "policy": {
            "policy_number": policy_number,
            "status": "active",
            "start_date": utils.get_current_date(),
            "customer_name": customer_name,
            "payment_method": payment_info["method"],
            "confirmation_email": f"Confirmation sent to {customer_email}",
        },
    }
