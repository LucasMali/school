t = [1,2,3]

split = len(t) //  3
a = t[split:]
b = t[split:split]
c = t[:split]

print(f"Original: {t}\nSplit: {split}\nfirst: {a}\nsecond: {b}\n third: {c}\n")

t = [1,2,3,4]

split = len(t) //  3
a = t[split:]
b = t[split:split]
c = t[:split]

print(f"Original: {t}\nSplit: {split}\nfirst: {a}\nsecond: {b}\n third: {c}\n")


t = [1,2]

split = len(t) //  3
a = t[split:]
b = t[split:split]
c = t[:split]

print(f"Original: {t}\nSplit: {split}\nfirst: {a}\nsecond: {b}\n third: {c}\n")

t = [1]

split = len(t) //  3
a = t[split:]
b = t[split:split]
c = t[:split]

print(f"Original: {t}\nSplit: {split}\nfirst: {a}\nsecond: {b}\n third: {c}\n")
