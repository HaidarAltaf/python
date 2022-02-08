# var1 = 5
# var2 = int(input("Enter number: "))
# var3 = [1,2,3,4,5,6]

# Example 1
# if var1 == var2:
#     print("this is the true code path")
# else:
#     print("this is the false code path")

# print("this line isnt indented and will always run")
# Single = assigns values double = (==) is strict equals


# Example 2
# if var1 > var2:
#     print("this is the true code path")
# else:
#     print("this is the false code path")

# print("this line isnt indented and will always run")
# Greater than



# # Example 3
# if var1 >= var2:
#     print("this is the true code path")
# else:
#     print("this is the false code path")

# print("this line isnt indented and will always run")
# Greater than or Equal to



# # Example 4
# if var2 in var3:
#     print("this is the true code path")
# else:
#     print("this is the false code path")

# print("this line isnt indented and will always run")
# # If input number is in the table run true



# # Example 5
# if 10%2 != 0 or (var2 >= 5 and var2 in var3):
#     print("this is the true code path")
# else:
#     print("this is the false code path")

# print("this line isnt indented and will always run")
# # Boolean logic



# # Example 6
# if var2 > var1:
#     print (var2, "is bigger than 5")
# elif var2 > 0:
#     print(var2, "is positive")
# elif var2 < 0:
#     print(var2, "is negative")
# else:
#     print(var2, "is 0")
# print("end program")
# # Example using elif



# # Example 7
# var4 = input("type: ")

# if var4.isalnum(): 
#     print("is a number or letter")
# else: 
#     print("is a symbol")
# # Using isalnum which means is alpha numerical. 




# Work set exercise on QA
var5 = int(input("Mark: "))
var6 = 85
var7 = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]


if var5 > var6:
    print("Distinction")
elif var5 in var7:
    print("Pass")
else:
    print("Fail")


if var5 >= 65:
    if var5 > 85:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")