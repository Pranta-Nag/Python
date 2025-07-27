# Dictionary are used to store data values in key:value pairs
# They are unordered, mutable & do not allow duplicate keys

info = {
    "Name" : "Pranta Nag",      # string type
    "Is_adult" : True,          # bollen type
    "Age" : 25,                 # int type
    "District" : "Chittagong",
    "Mobile No" : "01785868771",
    "Family members" : ["Father", "Mother", "Brother"],     # list
    "Address": ("Foradpur", "Sitakund"),        # tuple
}

info["Name"] = "Shuvo"         # replace the name = override

print(info)
print(info["Name"])         # print specific item into dictionary

null_info = {}          # create a null dictionary
null_info["Name"] = "Pranta"
null_info["Sub name"] = "Nag"
print(null_info)

null_info.update({"Id" : 44})
print(null_info)

null_info.pop("Name")               # remove name pair
print(null_info)



