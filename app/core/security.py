BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "bypass security"
]

def detect_prompt_injection(question: str):
    question_lower = question.lower()
    for pattern in BLOCKED_PATTERNS:
        if pattern in question_lower:
            return True
    return False
