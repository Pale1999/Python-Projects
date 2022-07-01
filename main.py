def employeeFiasco():

    #This is for user's input

    emp_name = input("What's your name?\nName: ")
    emp_age = input("How old are you?\nAge: ")
    emp_gender = input("Are you a male or a female?\nType 'M' for Male and 'F' for female.")
    emp_marital_status = input("Are you married?\n Type 'Y' for yes and 'N' for no.")


    #conditional statements here
    if emp_gender == 'F':
        print(emp_name + " can only work in an urban area.")
    elif emp_gender == 'M' and (int(emp_age) >= 20 or int(emp_age) <= 40):
        print(emp_name + " can work where ever his heart desires.")
    elif emp_gender == 'M' and (int(emp_age) >= 40 or int(emp_age) <= 60):
        print(emp_name + " can only work in an urban area.")
    elif emp_gender == 'M' and (int(emp_age) <= 20 or int(emp_age) >= 60):
        print("ERROR")

#Let's run our function

employeeFiasco()


