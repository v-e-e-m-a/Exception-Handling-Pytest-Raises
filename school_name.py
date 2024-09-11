def claim_unreserved_code_school_name(name):
    if name == "Ada Developers Academy":
        raise ValueError("There's already an awesome school with that name!")

    return True