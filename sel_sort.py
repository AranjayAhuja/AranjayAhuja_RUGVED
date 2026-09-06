def sel_sort(inp):
    ch = list(inp)
    length = len(ch)
    for i in range(length):
        min = i
        for j in range(i+1,length):
            if ch[j]<ch[min]:
                min = j
        x = ch[i]
        ch[i] = ch[min]
        ch[min] = x
    return "".join(ch)
inp = str(input("Enter string: "))
print(sel_sort(inp))