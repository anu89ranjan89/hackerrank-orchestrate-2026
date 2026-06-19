from agents.semantic_matcher import semantic_match

def decide(claim_info, vision_info, claim_object):

    claim_issue = claim_info.get("issue_type")
    vision_issue = vision_info.get("issue_type")

    # unknown handling (VERY IMPORTANT for hackathons)
    if vision_issue == "unknown":
        return {
            "claim_status": "supported",
            "reason": "vision uncertain → fallback to claim"
        }

    matched, family = semantic_match(claim_issue, vision_issue)

    if matched:
        return {
            "claim_status": "supported",
            "reason": f"semantic match in {family}"
        }

    return {
        "claim_status": "contradicted",
        "reason": f"{claim_issue} not consistent with {vision_issue}"
    }