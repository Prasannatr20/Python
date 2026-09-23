dict = {
    "name" : "Prasanna",
    "age" : 22,
    "marks" : {
        "phy" : 98,
        "chem" : 99,
        "eng" : 98
    },
    "grade" : 'A'
}

# print(dict)
# print(type(dict))
# print(dict["marks"])
# print(dict["marks"]["chem"])
# print(dict["grade"])

# print(len(list(dict.keys())))
#print(dict.values())
# list = list(dict.items()) #Returned as types
# print(list[2])
# print(dict.get("name2"))
# print(dict["name2"])
# print("hi")

# dict = {"City" : "Chennai"}
dict.update({"City" : "Chennai"})
print(dict.get("City"))