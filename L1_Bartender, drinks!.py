def get_drink_by_profession(param):
    table = {"jabroni": "Patron Tequila", "school counselor": "Anything with Alcohol",  
        "programmer": "Hipster Craft Beer",  "bike gang member": "Moonshine", 
        "politician": "Your tax dollars", "rapper": "Cristal"}
    for i in table:
        if param.lower() == i:
            return table[i]
        if i == "rapper" and param.lower != i:
            return "Beer"