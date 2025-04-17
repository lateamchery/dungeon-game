print("Welcome to the ultimate dungeon game")
player_name = input("Enter your name brave fellow!")

 
#initializing_player
#hghghg
player_health = 100
player_score = 0
inventory = []

print(f"Hello, {player_name} your goal is to escape the dungeon safely!")
print("good luck")

dungeon_rooms = {
    "room1":{
        "description": " Room1, A dark, musty room with cobwebs in every corner.",
        "items": ["Torch"],
        "exits":{"north":"room2","east":"room3"}
    },
    "room2":{
        "description": "Room 2, A small, dusty library with ancient books.",
        "items": ["key"],
        "exits": { "south": "room1", "east": "room4" }
    },
    "room3":{
          "description": "Room 3, A dimly lit armory filled with old weapons.",
          "items": ["sword"],
          "exits": { "west": "room1" }
    },
    "room4":{
          "description": "Room 4 A locked exit door stands here. You need a key to leave.",
          "items": [],
          "exits": { "west": "room2" }
    }
}
current_room = "room1"
def player_location(current_room):
    print("You are in ", dungeon_rooms[current_room]["description"])

game_is_active = True
while game_is_active is True:
    player_location(current_room)
    for items in dungeon_rooms[current_room]["items"]:
        print(f"There is a {items} in this room")
    
    def item_pickup_function():
        user_item_pickup = input("would you like to pick up one of these items (yes/no)")
        if user_item_pickup == "yes":
            chosen_item = input("enter the item name\n")
            if chosen_item in dungeon_rooms[current_room]["items"]:
                inventory.append(chosen_item)
                dungeon_rooms[current_room]["items"].remove(chosen_item)
                print("chosen items have been added to inventory")

            else:
                print("That item does not exist in this room")

    item_pickup_function()
    print("Exits available: ")
    for direction in dungeon_rooms[current_room]["exits"]:
        print(direction)

    command_input = input("Enter a command (e.g., 'go north', 'check inventory', 'quit'):\n")

    # command processing
    if command_input.startswith("go"):
        direction = command_input.replace("go", "").strip()
        print(f"moving on {direction}")
        if direction in dungeon_rooms[current_room]["exits"]:
            current_room = dungeon_rooms[current_room]["exits"][direction]
            print(f"You move to {current_room}!")
        else:
            print("You can't go that way.")
    elif command_input == "check inventory":
        print("Your inventory:", inventory)
    elif command_input == "quit":
        print("Thank you for playing! Goodbye!")
        game_is_active = False
    else:
        print("Unknown command. Please try again!")
    if current_room == "room4" and "key" in inventory:
        print("congradulations you've successfully escaped")
        game_is_active = False



