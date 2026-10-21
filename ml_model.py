
"""
PackCheck AI-ML
Baseline label completeness checker.

This is a rule-based baseline, not a trained ML model.
It will help us build and test the pipeline first.
"""

REQUIRED_FIELDS = [
    "product_name",
    "manufacturer",
    "net_quantity",
    "mrp",
    "consumer_care",
]


def analyze_label(label_data):
    missing_fields = []

    for field in REQUIRED_FIELDS:
        value = label_data.get(field)

        if value is None or str(value).strip() == "":
            missing_fields.append(field)

    if missing_fields:
        status = "REVIEW"
    else:
        status = "READY_FOR_RULE_CHECK"

    return {
        "status": status,
        "missing_fields": missing_fields,
        "message": (
            "Some fields need review."
            if missing_fields
            else "All configured fields are present. "
                 "Further compliance checks are required."
        ),
    }
