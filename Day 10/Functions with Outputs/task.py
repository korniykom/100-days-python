def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    return f_name.title() + " " + l_name.title()

print(format_name("hello", "WORLD"))