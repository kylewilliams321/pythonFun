import random

print("Hello reader")

readerName= input("What is your name?")

print("Hello " + readerName)


names = ["Zara", "Ben", "Dorothy", "Lucy", "Andrew", "Boris"]
places = ["Chicago", "Austin", "London", "New York City", "Canada"]
quests = ["seek the holy grail", "return the ring", "slay the dragon", "pick up sticks", "eat a sandwich"]
roles = ["knight", "queen", "king", "jester", "ogre" "witch"]
otherRoles = ["wise man", "prince", "princess", "builder", "sailor"]

randomName = random.choice (names)
randomPlace = random.choice (places)
randomQuest = random.choice (quests)
randomRole =random.choice (roles)
randomRole2 = random.choice (otherRoles)

story = "Once upon a time there was a " + randomRole + " called " + randomName + ". " + randomName + " needed to " + randomQuest +". One day " + randomName + " made a trip to " + randomPlace +" to visit the " + randomRole2 + ". " + readerName + " is the real hero. The End."

print(story)