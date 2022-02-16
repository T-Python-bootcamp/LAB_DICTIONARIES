#A1
phone=[{"number":1111111111,"name":"Amal"},{"number":2222222222,"name":"Mohammed"},{"number":3333333333,"name":"Khadijah"},{"number":4444444444,"name":"Abdullah"},{"number":5555555555,"name":"Rawan"},{"number":6666666666,"name":"Faisal"},{"number":7777777777,"name":"Layla"}]

def searchByNumber(num:int):
    x=len(str(num))
    if x==10 and type(num)==int:
        for n in phone:
            if num==n["number"]:
                print(n["name"])
                return
        print("Sorry, the number is not found ")
        return
    else:
        print("This is invalid number")

def searchByName(name:str):
    for n in phone:
        if name==n["name"]:
            print(n["number"])
            return
    print("Sorry, the name "+name+" is not found ")
    return

def addPhone():
    addNumber=int(input("please inter the phone number..."))
    addName=input("please inter the name...")
    phone.append({"number":addNumber,"name":addName})

   
searchByNumber(9999999999)
searchByNumber("njjgj")
searchByNumber(2222222222)
searchByName("saleh")
searchByName("Khadijah")
addPhone()
print(phone)

#A2
def rearrang(lis):
    x=lis.count(0)
    while x>0:
        lis.remove(0)
        lis.append(0)
        x-=1
    print(lis)
rearrang([1,4,7,5,0,6,2,0,1])

            