#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for names_m in sorted(dir(hidden_4)):
        if not names_m.startswith('__'):
            print(names_m)
