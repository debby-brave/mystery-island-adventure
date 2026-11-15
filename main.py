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

print("Welcom to Mtstery island,", player["name"])
print("You are standing on the Beach.")
print("You see a rope on the ground.") 

playing = True

while playing:
   print("\n=====", player["location"].upper(), "=====")


   if player["location"] == "Beach":
      print("1. Collect rope")
      print("2. Check inventory")    
      print("3. Go to Jungle")

   elif player["location"] == "Jungle":
      print("1. Explore the Jungle")
      print("2. Chack inventiry")
      print("3. Return to Beach")
       
      choice = input("Choose an option (1-3): ")

      if choice == "1": 
        if "rope" not in player["inventory"]:
            player["inventory"].append("rope")
            print("You collected a rope!")
        else:
            print("You already collected the rope!")


   elif choice == "2":
        print("Your inventory:", player["inventory"])
    
   elif choice == "3":
        player["location"] = "Jungle"
        print("you are moving to the Jungle!")
        print("Current location",player["location"])

   else:
        print("Invalid choice. Please choose 1, 2,  or 3.")




   