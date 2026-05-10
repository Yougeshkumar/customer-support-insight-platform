from typing import Tuple

CATEGORY_KEYWORDS = {
    "Delivery Delay": ["delay", "late", "not arrived", "where is my order"],
    "Refund Request": ["refund", "money back", "returned"],
    "Wrong Item": ["wrong item", "incorrect item", "not what i ordered"],
    "Damaged Product": ["damaged", "broken", "cracked"],
    "Payment Failure": ["payment failed", "charged twice", "transaction unsuccessful"],
    "Login Issue": ["cannot log in", "login failed", "password reset"],
    "Subscription Cancellation": ["cancel my subscription", "stop recurring billing"],
    "Product Quality": ["poor quality", "cheap", "disappointed with the quality"],
    "Missing Item": ["missing item", "order incomplete"],
    "Technical Bug": ["app crashes", "website error", "bug"],
}


def categorize_ticket(message: str) -> Tuple[str, float]:
    text = message.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return category, 0.95

    return "General Inquiry", 0.50