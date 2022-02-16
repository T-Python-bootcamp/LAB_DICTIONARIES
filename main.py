
# ----------------------------------------------
# Q1: Search user by number and return its name:
# ----------------------------------------------

PhoneBook = [
    {"Name":"Amal","Number":1111111111},
    {"Name":"Mohammed","Number":2222222222},
    {"Name":"Khadijah","Number":3333333333},
    {"Name":"Abdullah","Number":4444444444},
    {"Name":"Rawan","Number":5555555555},
    {"Name":"Faisal","Number":6666666666},
    {"Name":"Layla","Number":7777777777}
]

def checker (param):
    for i in range(len(PhoneBook)):
        if PhoneBook[i]["Number"]==int(param):
            return i
    return -1


while True:
    userInput = input("Please enter an input (type q to terminate):")
    if userInput == 'q' or userInput == 'Q':
        break
    if not (userInput.isnumeric()):
        print('This is invalid number (invalid data type)')
    elif len(userInput) != 10:
        print('This is invalid number (invalid length)')
    elif checker(userInput) != -1:
        print(f'{PhoneBook[checker(userInput)]["Name"]}')
    else:
        print('Sorry, the number is not found')


# ------------------------------------------------------
# Q2: Rearrange zeros to the end of the end of the list:
# ------------------------------------------------------

numbers = [0,22,-1,0,0,22,0]
for i in range(numbers.count(0)):
    numbers.remove(0)
    numbers.append(0)
print(numbers)