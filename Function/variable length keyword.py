def show_details(**details): #dictionary is passed
    for key, value in details.items():
        print(f"{key}: {value}")

show_details(name="Reet", age=25, country="India")