# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = nvl_narrator
define c = Character("Cassy", kind=nvl)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    c "god I fucking hate this office."

    "That's what I say outwardly, atleast."

    "I just don't want to get close to them."

    "fuuuuuck"

    nvl clear

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    "You've created a new Ren'Py game."

    "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
