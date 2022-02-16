#Q1:
name1 = {"Name":"Amal", "Number":1111111111}
name2 = {"Name":"Mohammed", "Number":2222222222}
name3 = {"Name":"Khadijah", "Number":3333333333}
name4 = {"Name":"Abdullah", "Number":4444444444}
name5 = {"Name":"Rawan", "Number":5555555555}
name6 = {"Name":"Faisal", "Number":6666666666}
name7 = {"Name":"Layla", "Number":7777777777}

dict1 = {
    "name1": name1,
    "name2": name2,
    "name3": name3,
    "name4": name4,
    "name5": name5,
    "name6": name6,
    "name7": name7,
}

def checkPhone():
    phoneNumber = input("Enter Phone Number: ")
    if type(int(phoneNumber)) == int:
        if not int(len(phoneNumber)) == 10:
            print("This is invalid number")
            return
        else:
            for dic in dict1:
                if int(phoneNumber) == dict1[dic]["Number"]:
                    print(dict1[dic]["Name"])
                    return
            print("Sorry, the number is not found")
            return
    else:
        print("This is invalid number")
        return

checkPhone()


# Q2:

def orderList(lst):
    for num in lst:
        if num == 0 :
            lst.remove(num)
            lst.append(0)
    print(lst)

orderList([1,0,3,6,7,0])