from distutils.util import strtobool


def safe_bool(str):
    if not str:
        return False
    elif str.isdigit():
        return bool(int((str)))
    elif str.lower() in ['true', 'false']:
        return bool(strtobool(str))
    else:
        return False
