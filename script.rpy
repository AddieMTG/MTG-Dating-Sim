# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jace",who_color="#0000CC")
define m = Character("[playername]", color="#3399CC")

label start:
    python:
        playername = renpy.input("What's your name?")
        playername = playername.strip()

        if not playername:
            playername = "Addie"


    scene quad

    "It was a beautiful day at Planeswalker U, and you were watching the students out on the quad."

    "Most of the nervousness of coming to a new school had subsided, and you were finally enjoying yourself."

    "????" "Lookout!"

    scene black

    "Something hits you. Everything goes black for a bit, and you can feel yourself knocked forward on the soft, warm grass."

    "????" "Shit, are you alright?"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene quad
    show jace_sprite_neutral

    # These display lines of dialogue.

    "????" "..."

    show jace_sprite_neutral at left
    with move


    $ cute = False

    menu:

        "..."

        "Uh... yeah, I'm fine":

            jump fine

        "Wow, you're cute!":
            $ cute = True
            jump cute

        "Fuck! Can't you catch?":

            jump angry

label cute:

    scene quad
    show jace_sprite_blush

    "????" "Uh... thanks?"

    jump fine


label angry:

    scene quad
    show jace_sprite_annoyed

    "????" "Woah... I said I was sorry."

    show jace_sprite_annoyed at right
    with move

    menu:

        "..."

        "I'm sorry... you're right. I didn't mean to get upset.":

            jump fine

        "Look... just go away!":

            jump end

label fine:

    "????" "Anyway... I'm Jace. Nice to meet you, even if it had to hurt..."

    scene quad
    show jace_sprite_neutral

    "The boy reaches forward to help you up. You notice he has soft hands... and kind, striking eyes."

    "You look down for a second, checking your knees. Thank Heliod you avoided grass stains!"

    m "I'm [playername]."

    j "Hopefully I can make it up to you?"

    "You wonder what this Jace has in mind. It's only the first day..."

    m "Uhh..."

    j "There's this free concert for new students and all. We always do these at the beginning of the year."

    scene quad
    show jace_sprite_happy

    j "Would you believe it? This year they got MY IZZET ROMANCE!"

    show jace_sprite_happy at right
    with move
    
    menu:

        "..."

        "That sounds awesome!":

            jump concert_prep

        "No thanks, I don't really like music.":

            jump no_concert

label no_concert:

    scene quad
    show jace_sprite_confused

    j "Oh, that's cool. I guess I'll see you around then. Later!"

    jump end

label concert_prep:

    scene quad
    show jace_sprite_happy

    j "Awesome! Look, why don't you meet me at Rade Hall at 7. I'll get you some food and stuff before the show!"

    m "Thanks Jace! I'm looking forward to it!"

    jump concert

label concert:

    scene hall_outside
    with fade

    show jace_sprite_concert_neutral
    with dissolve

    "Was that... Jace? Wow, he's a big fan!"

    j "Hey there! You made it!"

    m "Love the outfit, Jace!"

    scene hall_outside
    show jace_sprite_concert_blush

    j "Heh... thanks. I'm a huge fan!"

    if cute == True:
        "You take a quick look up and down. You thought he was cute before... but wow."

    if cute == False:
        "It's kind of a fun look. Maybe you didn't think he was cute before, but now he's changing your mind."

    m "I don't think I know the band that much. But looking forward to having a great time."

    scene hall_outside
    show jace_sprite_concert_neutral

    j "Let's get inside!"
    jump end2

label end:

    scene black
    with dissolve

    "This sure was a lot for the first day. Maybe it's time to go back to your room, see what you can find on the MizziNet..."

    "{b}Bad Ending{/b}."

label end2:

    scene black
    with dissolve

    "The band rocked, even if it might not be what you normally listen to. You and Jace had a great time... and all it took was a frisbee!"

    "{b}Good Ending{/b}"

    # This ends the game.

    return
