import random 

# break in for loop
for i in range(1,101,1):
    print(i, end=" ")
    if(i==50):
        break
        print("Hey ! Iam break. I exited the loop")

print("\n")

# continue in for loop
for i in range(1,11):
    print("\n 5 x",i,"=",5 * i)
    print(i,"line")
    continue
