def generate_response(category: str, message: str) -> str:
    templates = {
        "Delivery Delay": (
            "We apologize for the delay. Our logistics team is tracking your shipment and "
            "we will update you shortly."
        ),
        "Refund Request": (
            "We understand your concern. Your refund request has been initiated and "
            "will be processed soon."
        ),
        "Damaged Product": (
            "We're sorry the product arrived damaged. We can arrange a replacement or refund."
        ),
        "Payment Failure": (
            "We regret the payment issue. Our billing team is reviewing the transaction."
        ),
        "Login Issue": (
            "Please try resetting your password. If the issue persists, we'll investigate."
        ),
    }

    return templates.get(
        category,
        "Thank you for contacting support. Our team is reviewing your issue and will respond shortly.",
    )