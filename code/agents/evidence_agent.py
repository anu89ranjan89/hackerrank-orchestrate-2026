def check_evidence_standard(
        claim_info,
        vision_info
):

    if not vision_info.get("issue_type") == "unknown":
        

        return (True,"uncertain vision but claim still evaluated")

    if vision_info.get(
        "damage_visible",
        False
    ):

        return (
            True,
            "damage visible"
        )

    return (
        False,
        "damage not visible"
    )