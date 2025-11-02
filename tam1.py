import random
rooms = {
    1: {"right": 2, "down": 3},
    2: {"left": 1, "down": 4},
    3: {"up": 1, "right": 4, "down": 5},
    4: {"up": 2, "down": 6},
    5: {"up": 3, "right": 6},
    6: {"up": 4, "left": 5}
}

def clean_room():
    choose_room = int(input("Please pick a room number from 1 to 6: "))
    cleaned_rooms = []

    while len(cleaned_rooms) < 6:
        if choose_room not in cleaned_rooms:
            cleaned_rooms.append(choose_room)
            print(f"Room {choose_room} is clear now!")

        neighbors = list(rooms[choose_room].values())
        available_neighbors = [room for room in neighbors if room not in cleaned_rooms]

        if available_neighbors:
            choose_room = random.choice(available_neighbors)
        else:
            other_rooms = [room for room in rooms if room not in cleaned_rooms]
            if other_rooms:
                choose_room = random.choice(other_rooms)
            else:
                break

    print("All the rooms are cleared!")
    print("I want to change something in here, just for test")
    print("course: Az Mohandesi ")
    
    

clean_room()