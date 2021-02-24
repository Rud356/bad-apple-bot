def validate_prefix(s: str):
    if not isinstance(s, str):
        raise ValueError(f"Invalid prefix type, got {type(str)}")

    if len(s) > 3:
        raise ValueError("Too long prefix (must be from 1 to 3 chars)")

    return True
