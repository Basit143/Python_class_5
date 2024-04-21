print('hello ')
# List 
# * iteration operation with loop
# * apply any operation on element 

names : list[str] = ["Abdul Basit","Ali Zafar","Ali Anis", "Muhammad Ali"]

for name in names:
    print(name)





data_base : list[tuple[str,str]] = [("Abdul Basit","123"),
                                    ("Ali Anis","456"),
                                    ("Ali Zafar","789")
                                    ]
input_user : str   = input("Enter Username:")
input_password : str = input("Enter Password: ")

for row in data_base:
    user, password = row
    if input_user == user and  input_password == password:
        print("Valid User Login Welcome")
        break
else:
    print("Invalid User Login Please Try Again.")






