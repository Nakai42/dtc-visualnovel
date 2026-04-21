# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = nvl_narrator
define c = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#005eda")
define d = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#f07400")
define s = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#aa0202")
define e = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#ff0000")
define w = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#56356b")

# The game starts here.

label start:

    "You ever just stare at yourself in the mirror?"

    "Get lost in a mental spiral of every life choice, until you've been standing there minutes, completely out of it."

    "I still think about where I worked before Hypogean."

    "Hard not to when just two months prior you were standing in their blood, surrounded by their corpses."

    "I'm sorry, Lachlan."

    nvl clear

    "I sigh, pushing off the sink. Got places to be, people to... kill. 
    Something like that, anyways. Maybe Dominic has a contract for us that doesn't involve gutting some random group of guys."

    "Hypogean Office. Odd name for a merc office, in all honesty. 
    Maybe it's some commentary on how all our morals are in the dirt because of contract killing, or something."

    "Wouldn't put it past Dom, anyways. Eccentric wierdo."

    "I briefly meander through my apartment, before sitting in front of my door to change out my prosthetic legs. I would absolutely scratch the fuck out of the floor if I wore my taloned ones in here."

    "Out the door, onto the overcast streets of District 12."
    

    

    

    # This ends the game.

    return
