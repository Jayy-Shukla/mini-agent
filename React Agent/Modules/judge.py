def judge_check(response: str, interpretation: str):
    red_flags = ["suicide", "kill", "hurt myself", "end my life"]
    flagged = any(flag in response.lower() for flag in red_flags)

    if flagged:
        return "⚠️ Red Flag — Escalate to clinician"
    
    if ("yes" in response.lower() and "negative" in interpretation.lower()) or \
       ("no" in response.lower() and "positive" in interpretation.lower()):
        return "⚠️ Discrepancy — Flag for review"
    
    return "✅ Aligned"
