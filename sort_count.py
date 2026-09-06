
def sorting(x):
    sort_list = list(x)
    sort_list.sort()
    sort_str = "".join(sort_list)
    return sort_str

def counting(inp):

    counted = []
    for ch in inp:
        if ch not in counted:
            count = 0
            for curr_ch in inp:
                if curr_ch == ch:
                    count += 1

            counted.append(ch)
            print(ch + ":" + str(count))
    return ""

if __name__ == "__main__":
    inp = str(input("String to be sorted:  "))
    print("Sorted string:  " + sorting(inp))
    print("\nCharacter count:")
    print(counting(inp))

