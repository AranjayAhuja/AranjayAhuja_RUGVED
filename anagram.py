from sort_count import sorting
st1 = input("Enter a string: ")
st2 = input("Enter another string: ")
a = sorting(st1).replace(" ","")
b = sorting(st2).replace(" ","")
if a == b:
    print("The strings are anagrams of each other")
else:
    print("The strings are not anagrams")
