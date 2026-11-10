print("====================")
print(" MYSTERY ISLAND: THE LOST LIGHTHOUSE")
print("====================")

player_name = input("Enter your name: ")

player = {
    "name": player_name,
    "energy": 5,
    "location": "Beach",
    "inventory": []
}

print("Welcome to Mystery Island,", player["name"])
print("Your energy:", player["energy"])
print("Your location:", player["location"])
print("Your inventory:", player["inventory"])
print("You are standing on the Beach.")
print("You found a rope!")

player["inventory"].append("rope")

print("Your inventory:", player["inventory"])