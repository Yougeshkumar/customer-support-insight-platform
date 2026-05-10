import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

NUM_TICKETS = 10000

CATEGORIES = {
    "Delivery Delay": [
        "My order has not arrived yet.",
        "The package is delayed and there is no update.",
        "Delivery was supposed to be yesterday.",
        "Where is my order?"
    ],
    "Refund Request": [
        "I want a refund for this order.",
        "Please process my refund.",
        "I returned the item but haven't received my refund.",
        "Refund has not been credited."
    ],
    "Wrong Item": [
        "I received the wrong product.",
        "This is not what I ordered.",
        "Incorrect item delivered.",
        "The package contains another item."
    ],
    "Damaged Product": [
        "The item arrived broken.",
        "Product was damaged during shipping.",
        "Received a cracked product.",
        "Packaging was torn and product is damaged."
    ],
    "Payment Failure": [
        "Payment failed but money was deducted.",
        "Unable to complete payment.",
        "Card was charged twice.",
        "Transaction unsuccessful."
    ],
    "Login Issue": [
        "I cannot log into my account.",
        "Password reset link is not working.",
        "Account login failed.",
        "Unable to access dashboard."
    ],
    "Subscription Cancellation": [
        "Please cancel my subscription.",
        "I want to stop recurring billing.",
        "Cancel my membership immediately.",
        "Subscription is difficult to cancel."
    ],
    "Product Quality": [
        "The quality is very poor.",
        "Product does not match expectations.",
        "Material feels cheap.",
        "Very disappointed with the quality."
    ],
    "Missing Item": [
        "One item is missing from my order.",
        "Package did not contain all products.",
        "Missing accessories.",
        "Order incomplete."
    ],
    "Technical Bug": [
        "The app crashes when I open it.",
        "Website shows an error.",
        "Checkout page is broken.",
        "Found a bug in the application."
    ],
}

PRODUCTS = [
    "Wireless Earbuds",
    "Smart Watch",
    "Laptop Sleeve",
    "Gaming Mouse",
    "Bluetooth Speaker",
    "Phone Charger",
    "Keyboard",
    "Monitor",
]

COUNTRIES = [
    "India",
    "United States",
    "United Kingdom",
    "Germany",
    "Canada",
    "Australia",
]

CHANNELS = ["chat", "email", "web"]
RESOLUTION_STATUSES = ["Resolved", "Pending", "Escalated"]

AGENT_REPLIES = [
    "We're sorry for the inconvenience. Our team is looking into this issue.",
    "Thank you for reaching out. We will resolve this as soon as possible.",
    "We understand your frustration and appreciate your patience.",
    "Our support team has escalated this case.",
]

def random_timestamp():
    now = datetime.now()
    days_ago = random.randint(0, 180)
    minutes_ago = random.randint(0, 1440)
    return now - timedelta(days=days_ago, minutes=minutes_ago)

def generate_dataset():
    rows = []

    categories = list(CATEGORIES.keys())

    for i in range(1, NUM_TICKETS + 1):
        category = random.choice(categories)
        message = random.choice(CATEGORIES[category])

        row = {
            "ticket_id": f"TKT-{i:05d}",
            "timestamp": random_timestamp(),
            "customer_id": f"CUST-{random.randint(1000, 9999)}",
            "channel": random.choice(CHANNELS),
            "message": message,
            "agent_reply": random.choice(AGENT_REPLIES),
            "product": random.choice(PRODUCTS),
            "order_value": round(random.uniform(499, 50000), 2),
            "customer_country": random.choice(COUNTRIES),
            "resolution_status": random.choice(RESOLUTION_STATUSES),
            "true_category": category,
        }

        rows.append(row)

    df = pd.DataFrame(rows)

    Path("data").mkdir(exist_ok=True)
    output_path = Path("data/customer_support_tickets.csv")
    df.to_csv(output_path, index=False)

    print(f"Dataset generated successfully: {output_path}")
    print(f"Total tickets: {len(df)}")

if __name__ == "__main__":
    generate_dataset()