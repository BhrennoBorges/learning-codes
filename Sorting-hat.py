gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")
answer = int(input())

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

print("\nQ2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
answer = int(input())

if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Wrong input.")

print("\nQ3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
answer = int(input())

if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print("Wrong input.")

print("\nCalculating your house...")
house_points = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff,
    "Slytherin": slytherin
}

sorted_houses = sorted(house_points.items(), key=lambda x: x[1], reverse=True)
winner = sorted_houses[0][0]

print(f"You belong to {winner}!")
