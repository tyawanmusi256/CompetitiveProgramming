s = input()
t = ""
for i in s:
    if i != "A":
        t += "."
    else:
        t += i
print(t)