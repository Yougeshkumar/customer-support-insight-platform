def summarize_ticket(message: str) -> str:
    words = message.split()
    if len(words) <= 12:
        return message
    return " ".join(words[:12]) + "..."