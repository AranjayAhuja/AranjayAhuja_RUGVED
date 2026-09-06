def credit_card(num):
    num = num[::-1]
    digits = list(num)


    length = len(digits)
    doubled = []
    other = []
    for i in range(1,length,2):
        doubled.append(int(digits[i])*2)
    dlen = len(doubled)
    for i in range(0,length,2):
        other.append(int(digits[i]))
    for i in range(0,dlen):

         if doubled[i]>9:
             x = doubled[i]
             add = 0
             while x>0:
                rem = x%10
                add = add + rem
                x = x//10
             doubled[i] = add
    total = sum(doubled) + sum(other)
    if total%10 == 0:
        print("The number belongs to a valid credit card")
    else:
        print("The number does not belong to a valid credit card")



number = input("Enter a number: ")
credit_card(number)

