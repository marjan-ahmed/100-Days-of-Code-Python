personAge = int(input("Enter you age: ")) # 18 or more 

if(personAge >= 18):
    personCountry = str(input("Enter your nationality: ")) # pakistani, bangladeshi 
    if(personCountry == "pakistani"):
        print("Now! You can enter")

    elif(personCountry == "bangladeshi"):
        print("Now! You can enter")

    else:
        print("These identities are not allowed")

else:
    print("You are currently",personAge,". Above 18 are only allowed")