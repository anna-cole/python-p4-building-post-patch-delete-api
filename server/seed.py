#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Game, Review, User

genres = [
    "Platformer",
    "Shooter",
    "Fighting",
    "Stealth",
    "Survival",
    "Rhythm",
    "Survival Horror",
    "Metroidvania",
    "Text-Based",
    "Visual Novel",
    "Tile-Matching",
    "Puzzle",
    "Action RPG",
    "MMORPG",
    "Tactical RPG",
    "JRPG",
    "Life Simulator",
    "Vehicle Simulator",
    "Tower Defense",
    "Turn-Based Strategy",
    "Racing",
    "Sports",
    "Party",
    "Trivia",
    "Sandbox"
]

platforms = [
    "NES",
    "SNES",
    "Nintendo 64",
    "GameCube",
    "Wii",
    "Wii U",
    "Nintendo Switch",
    "GameBoy",
    "GameBoy Advance",
    "Nintendo DS",
    "Nintendo 3DS",
    "XBox",
    "XBox 360",
    "XBox One",
    "XBox Series X/S",
    "PlayStation",
    "PlayStation 2",
    "PlayStation 3",
    "PlayStation 4",
    "PlayStation 5",
    "PSP",
    "PS Vita",
    "Genesis",
    "DreamCast",
    "PC",
]

fake = Faker()

with app.app_context():

    Review.query.delete()
    User.query.delete()
    Game.query.delete()

    users = []
    for i in range(100):
        u = User(name=fake.name(),)
        users.append(u)

    db.session.add_all(users)

    games = []
    for i in range(100):
        g = Game(
            title=fake.sentence(),
            genre=rc(genres),
            platform=rc(platforms),
            price=randint(5, 60),
        )
        games.append(g)

    db.session.add_all(games)

    reviews = []
    for u in users:
        for i in range(randint(1, 10)): # explanation below
            r = Review(
                score=randint(0, 10),
                comment=fake.sentence(),
                user=u,
                game=rc(games))
            reviews.append(r)

    db.session.add_all(reviews)

    for g in games: # explanation below
        r = rc(reviews)
        g.review = r
        reviews.remove(r)

    db.session.commit()

# The line for i in range(randint(1, 10)): is a loop that will iterate a random number of times between 1 and 10 (inclusive).

# In Python, the range() function is used to generate a sequence of numbers. The range() function takes three parameters: start, stop, and step. In this case, we are only providing the stop parameter, which is randint(1, 10).

# The randint(1, 10) function call generates a random integer between 1 and 10 (both inclusive). This random number will determine the number of iterations for the loop.

# For example, if randint(1, 10) returns 5, then the loop will iterate 5 times. On each iteration, it will create a new Review object with random score, comment, user, and game, and append it to the reviews list. 

#------------------------------
           
# for g in games: This portion of your code seems to be assigning a random review to each game. The loop iterates through each game, and for each game, it selects a random review from the reviews list using the rc() function. Then, it assigns that review to the review attribute of the game object.

# After assigning the review to the game, it removes the selected review from the reviews list using the remove() method. This ensures that each review is assigned to only one game.

# Finally, the db.session.commit() statement saves the changes made to the database, which includes the assignment of reviews to games.