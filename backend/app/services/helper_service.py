def parse_section_items(text: str, section_name: str):
    lines = text.splitlines()
    items = []
    in_section = False

    for line in lines:
        stripped = line.strip()

        if stripped.upper().startswith(section_name):
            in_section = True
            continue

        if in_section:
            if stripped.endswith(":") and not stripped.startswith("-"):
                break
            if stripped.startswith("-"):
                items.append(stripped[1:].strip())

    return items