txt = input("Enter the text:")
lc = 0

sc = 0
for ch in txt:
    if ch.isalpha():
        lc += 1
    if ch =="." or ch == "!" or ch == "?":
        sc += 1
words = txt.split()
wc = len(words)
if wc == 0:
    print("Below Grade 1")
else:
    if sc == 0:
        sc = 1
    L = (lc/wc)*100
    S = (sc/wc)*100
    index = 0.0588*L - 0.296*S - 15.8
    grade = round(index)
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Below Grade 1")
    else:
        print("Grade " ,grade)