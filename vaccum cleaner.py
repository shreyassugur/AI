rooms = {"A": "DIRTY", "B": "CLEAN"}

room = "A"
count = 4

while count > 0:
    print("Room:", room)
    print("Status:", rooms[room])

    if rooms[room] == "DIRTY":
        print("Clean the room")
        rooms[room] = "CLEAN"

    else:
        print("Move to other room")

        if room == "A":
            room = "B"
        else:
            room = "A"

    count = count - 1

print("A =", rooms["A"])
print("B =", rooms["B"])
