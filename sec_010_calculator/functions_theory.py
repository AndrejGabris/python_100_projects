def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version."""
    if f_name == "" or l_name == "":
        return "No valid inputs."
    formated_f_name = f_name.title()
    fomrated_l_name = l_name.title()

    return f"{formated_f_name} {fomrated_l_name}"


formated_string = format_name(l_name="gabris", f_name="ANDREJ")
print(formated_string)

print(len("ANDREJ"))
