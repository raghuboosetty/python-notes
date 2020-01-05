# r - read
# w - write
# r+ - read/write
# a - append

employee_file = open("employees.txt", "r")
# print(employee_file.readable())
# print("---")
# print((employee_file.readline()))
# print((employee_file.readline()))
# print("---")
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

employee_file = open("employees.txt", "a")
employee_file.write("\nDog")
employee_file.close()