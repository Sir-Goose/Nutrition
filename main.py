fruit = input("Item: ")
fruit = fruit.lower()

fruitydict = {
    "apple": 130,
    "avocado": 50,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100

}

if fruit in fruitydict:
    print("Calories: " + str(fruitydict[fruit]))
