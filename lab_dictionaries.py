phones = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}

entry = ""#input("Type a phone number to get the owner\n")

if(not entry.isdigit()):
    print("This is invalid number")
elif len(entry) != 10:
    print("This is invalid number")
elif phones[entry]:
    print(phones[entry])
else:
    print("Sorry, the number is not found")

def func(nums: list):
    lst = []
    if(type(nums) == list):
        for num in nums:
            if num == 0 :
                lst.append(num)
            else:
                lst.insert(0, num)
        return lst
    else:
        print("Please enter a list of numbers")
