# util.py
# used by run.py

import re

def has_senstive_word(line):
    result = (re.findall("\*[a-zA-Z][a-zA-Z0-9_]+\*", line))
    if len(result) == 0 :
        return None
    else:
        result = result[0].strip("*")
        if result == "":
            return None
        return result
def parse(s):
    # return a tuple of (key, value)
    value = ""
    sensitive_word = has_senstive_word(s)
    if sensitive_word is not None:
        try:
            value = re.findall("{.+}", s)
            if value == []:
                return None
            value = value[0].strip("}").strip("{")
            return (sensitive_word,value)
        except Exception as  e:
            raise  e
            return None

    return None

