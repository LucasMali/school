t = [1,2,3]

split = len(t) //  2
a = t[split:]
b = t[:split]

print(f"Original: {t}\nSplit: {split}\nfirst: {a}\nsecond: {b}\n")

t = [1,2,3,4]

split = len(t) //  2
a = t[split:]
b = t[:split]

print(f"Original: {t}\nSplit: {split}\nfirst: {a}\nsecond: {b}\n")


t = [1,2]

split = len(t) //  2
a = t[split:]
b = t[:split]

print(f"Original: {t}\nSplit: {split}\nfirst: {a}\nsecond: {b}\n")

t = [1]

split = len(t) //  2
a = t[split:]
b = t[:split]

print(f"Original: {t}\nSplit: {split}\nfirst: {a}\nsecond: {b}")
