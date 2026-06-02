import re

COMPLEX_KEYWORDS = {
    "performance", "bug", "crash", "segfault", "leak", "fuite", 
    "optimiser", "optimisation", "vitesse", "lent", "lenteur",
    "error", "erreur", "fail", "échoue", "bloqué", "deadlock"
}

def choose_agent(prompt: str) -> str:
    if not prompt:
        return "claude-3-5-haiku"
    prompt_lower = prompt.lower()
    words = set(re.findall(r'\b\w+\b', prompt_lower))
    if words.intersection(COMPLEX_KEYWORDS):
        return "claude-3-5-sonnet"
    return "claude-3-5-haiku"