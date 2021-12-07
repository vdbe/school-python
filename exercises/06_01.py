def delChar(s: str, idx: int):
    if len(s) < idx:
        print("String not long enough")
        return

    print(s[:idx] + s[idx + 1 :])


delChar("Python", 0)
delChar("Python", 2)
delChar("Python", 127)
