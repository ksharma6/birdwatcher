def txt_reader(path_to_txt):
    """Reads txt file and returns a list of lines with index removed

    Args:
        path_to_txt (str): path to txt file

    Returns:
        list: list of cleaned strings
    """
    f = open(path_to_txt)
    content = f.read()
    temp = content.splitlines()

    cleaned_content = []
    for s in temp:
        parts = s.split(' ', 1)

        if len(parts) > 1:
            new_string = parts[1]
        else:
            new_string = ''  # In case there is no space, return an empty string
        cleaned_content.append(new_string)

    return cleaned_content