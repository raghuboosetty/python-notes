is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are not a tall male")
elif is_male or is_tall:
    print("You are male or tall or both!")
else:
    print("You are neither a male nor tall!")
