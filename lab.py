## Q1:Build a phone book program that receives the phone number, and returns the name of the owner. 
dict1 = {
    "Amal": 1111111111,
    "Mohammed": 2222222222,
    "Khadijah": 3333333333,
    "Abdullah": 4444444444,
    "Rawan": 5555555555,
    "Faisal": 6666666666,
    "Layla": 7777777777,
}

num = 333333*3333

def phoneName(num):
    if len(str(num)) < 10 or len(str(num)) > 10 or type(num) != int:
        print("This is invalid number")
    elif num not in dict1.values():
        print("Sorry, the number is not found")
    else:
        for k in dict1.items():
            if k[1] == num:
                print("This phone number belongs to: ", k[0])

phoneName(num)
#-----------------------------------------#
## Q2:Write a function that receives a list containing different numbers, 
# rearranges the list so that the zeros are the end of the list, 
# and finally returns the arranged list.
lst1 = [-1, 0, 8, 1.3, 3,0, 2, 11, 0, -30]
def arrangeZeros(lst:list):
    arrangedList = [item for item in lst if item == 0]
    for i in lst:
        if i == 0:
            lst.remove(i)
    for x in arrangedList:
        lst.append(x)
    print(lst)
    return lst

arrangeZeros(lst1)
