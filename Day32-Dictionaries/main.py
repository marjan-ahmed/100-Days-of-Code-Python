infoDict = {
    "name": "Marjan",
    "age": 15,
    "eligiblity": True 
}
print(type(infoDict))

# print(infoDict.get('eligibility1')) # It will print None
# print(infoDict["eligibility1"]) # It will pass the error 

rollNumber = {
    1: "Salih",
    2: "Abrar",
    3: "Hassan",
    4: "Shaid",
    5: "Halima",
    "absent": False
}

# print(rollNumber[1])
# print(rollNumber[2])
# print(rollNumber[3])
# print(rollNumber[4])
# print(rollNumber[5])
# print(rollNumber['absent'])

# Acesssing multiple values

print(infoDict.keys())

for key in infoDict.keys():
    print(infoDict[key])

dictItems = infoDict.items()
print(type(dictItems))

