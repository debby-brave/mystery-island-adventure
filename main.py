print("====================")
print(" MYSTERY ISLAND: THE LOST LIGHTHOUSE")
print("====================")

player_name = input("Enter your name:")

player = {
    "name": player_name,
    "energy": 5,
    "location": "Beach",
    "inventory": []
}


print("You are standing on the Beach.")
print("You see a rope on the ground.")

print("\n=====   BEACH =====")
print("1. Collect rope")    
print("3. Leave the Beach")

choice = input("Choose an option (1-3): ")

if choice == "1": 
    player["inventory"].append("rope")
    print("You collected a rope!")

elif choice == "2":
    print("Your inventory:", player["inventory"])
    
elif choice == "3":
    print("You are leaving the Beach.")

else:
    print("Invalid choice. Please choose 1, 2,  or 3.")




   