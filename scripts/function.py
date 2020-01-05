def say_hi(name, age):
    print("Hello " + name + "! Your age: " + str(age))


say_hi("User", 33)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation += "g"
        else:
            translation += letter
    return translation

print(translate(input("Enter a phrase: ")))