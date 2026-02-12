karnataka_food = {
    "mysuru" : "Mysuru Pak",
    "Chikamanglur" : "Coffee",
    "Malenadu" : "Kadubu"
}
#Accessing
print(karnataka_food["Malenadu"])

#using get method
print(karnataka_food.get("Hassan","Not found"))
print(karnataka_food.get("mysuru","Not found"))

#updating and adding to the Dictionary
karnataka_food["Sakleshpura"]="Akki rotti"
print(karnataka_food)
karnataka_food["mysuru"]="sridevi hotel"
print(karnataka_food)

#removing an element 
del_food=karnataka_food.pop("mysuru")
print(del_food)

#del karnataka_food["Sakleshpura"]
#karnataka_food.clear()
print(karnataka_food)

#dictionary methods

print(karnataka_food.keys())
print(karnataka_food.values())
print(karnataka_food.items())

uttar_kannada={"ballari":"Egg rice"}
karnataka_food.update(uttar_kannada)
print(karnataka_food)


item1={
    "name": "Sugar",
    "Weight" : 2.8,
    "Brand" : "Madhur"
}

item2={
    "name" : "Coffe Powder",
    "Weight" : 5.56,
    "Brand" : "Bru"
}
print(f"Total weight is {item1['Weight']+item2['Weight']}kg")