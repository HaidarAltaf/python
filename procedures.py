# def Doom(inputvar):
#     Doom = words + 'is temporary, DOOM is eternal'
#     return Doom


# words = "everything "
# print(Doom(words))

# words = "she "
# print(Doom(words))

# words = input("singular phrase: ")
# print(Doom(words))

# print("===================")
# print("   RIP AND TEAR   ")
# print("===================")




# def add_calc(number1, number2):
#     answer = number1 * number2
#     return answer

# added_number = add_calc(5, 5)
# print(added_number + 20)


def grade(name, hw_score, assessment, f_exam):
    final = ((hw_score + assessment + f_exam) / 175) * 100
    return final

student = grade 
namevar = str((input("Name: "))) 
HWvar = 30
while HWvar > 25:
    HWvar = int(input("hw_score: ")) 
    if HWvar > 25:
        print("not accepted")
Avar = 55
while Avar > 50:
    Avar = int(input("assessment: ")) 
    if Avar > 50:
        print("not accepted")
Fvar = 105
while Fvar > 100:
    Fvar = int(input("f_exam: "))
    if Fvar > 100:
        print("not accepted")
End = grade(namevar, HWvar, Avar, Fvar)

print(namevar, End)

