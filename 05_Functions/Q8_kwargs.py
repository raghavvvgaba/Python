#function with *kwargs
# accept any number of arguments and prints them in the format of key: value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}, {value}")

print_kwargs(name = "Raghav", city = "Agra")
print_kwargs(name = "Priyansh")
print_kwargs(name = "Aaryan,", city = "Faridabad", type = "Gendu")