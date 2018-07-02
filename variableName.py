import re

def variableName(name):
    regex = re.compile(r'^[a-zA-Z_]+[0-9a-zA-Z_]*$')
    if regex.match(name):
        return True
    else:
        return False