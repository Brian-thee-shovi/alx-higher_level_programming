#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        _value = fct(*args)
        return _value
    except Exception as errinfo:
        print("Exception: {}".format(errinfo), file=sys.stderr)
        return None
