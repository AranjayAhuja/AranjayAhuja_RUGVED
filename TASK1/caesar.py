

def caesar(inp , key):
    ua = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    la = "abcdefghijklmnopqrstuvwxyz"
    enc_str = ""
    for ch in inp:
        if ch in la:
            i = la.index(ch)
            i_new = (i+key)%26
            enc_str = enc_str + la[i_new]
        elif ch in ua:
            i = ua.index(ch)
            i_new = (i+key)%26
            enc_str = enc_str + ua[i_new]
        else:
            enc_str = enc_str + ch
    return enc_str


txt = input("Enter message to be encrypted: ")
k = int(input("Enter key for encryption: "))

print(caesar(txt,k))






