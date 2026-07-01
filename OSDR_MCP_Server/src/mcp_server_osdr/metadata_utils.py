def format_mission_name(value: object) -> str:
    """Return an OSDR mission name consistently for scalar and sequence values."""
    if value is None or value == "":
        return "N/A"
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)):
        return ", ".join(str(item) for item in value) or "N/A"
    return str(value)
