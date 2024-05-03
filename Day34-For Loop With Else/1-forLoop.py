for i in range(6):
    print(i)
    if i == 4:
        break

else:
    print("Invalid, No i\n")

# for i in []:
#     print(i)

# else:
#     print("Invalid, No i")

for x in range(5):
    print("iteration number {} in for loop".format(x+1))
else:
    print("else block in loop.")
print("Out of loop")