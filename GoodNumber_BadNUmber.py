def identifyGoodOrBadNumber(num: int):
    numStr = str(num)
    lenStr = len(numStr)
    str1 = ""
    str2 = ""
    res = 0
    list1 = ['1', '2', '3']

    if lenStr <= 1:
        if numStr[lenStr - 1] in list1:
            res = 1
    else:
        for i in range(lenStr - 1):
            if numStr[i] in list1:
                if numStr[i] == numStr[i + 1]:
                    res = 1
                    break
                str1 += numStr[i]
                str1 +=numStr[i+1]
                for j in range(i + 1, lenStr):
                    str2 += numStr[j]
                if str1 in str2:
                    res = 1
                    break
            else:
                res=1
    if res == 1:
        print("The given number is a Bad number")
    else:
        print("The given number is a good number")


num1 = int(input("Enter your number: "))
identifyGoodOrBadNumber(num1)
