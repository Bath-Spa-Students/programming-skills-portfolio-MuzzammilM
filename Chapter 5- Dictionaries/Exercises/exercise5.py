#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet

# Empty list to store the pets in.
pets = []

# Individual pets, and store each one in the list.
pet = {
    'animal type': 'cat',
    'name': 'lucy',
    'owner': 'ahmed',
    'weight': 3,
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'rabbit',
    'name': 'tuffy',
    'owner': 'omer',
    'weight': 6,
    'eats': 'carrot',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'oscar',
    'owner': 'ali',
    'weight': 37,
    'eats': 'meat',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))