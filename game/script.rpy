# The script of the game goes in this file.

# The game starts here.

label start:

    # Ask for player name at the start of the game
    $ player_name = renpy.input("What is your name?", default="")
    $ player_name = player_name.strip()  # Remove any extra spaces

    # If the player doesn't input anything, default to "You"
    if player_name == "":
        $ player_name = "You"

# Pronoun selection
label choose_pronouns:
    menu:
            "He/Him":
                $ player_pronouns = "he/him"
                $ player_subject = "he"
                $ player_object = "him"
                $ player_possessive = "his"
                $ player_possessive_obj = "his"
                $ player_reflexive = "himself"
                jump after_pronouns  # Jump to the next section

            "She/Her":
                $ player_pronouns = "she/her"
                $ player_subject = "she"
                $ player_object = "her"
                $ player_possessive = "her"
                $ player_possessive_obj = "hers"
                $ player_reflexive = "herself"
                jump after_pronouns  # Jump to the next section

            "They/Them":
                $ player_pronouns = "they/them"
                $ player_subject = "they"
                $ player_object = "them"
                $ player_possessive = "their"
                $ player_possessive_obj = "theirs"
                $ player_reflexive = "themself"
                jump after_pronouns  # Jump to the next section
    
    label after_pronouns:
    # After pronouns have been selected, show confirmation
    "Hello, [player_name]! You have chosen [player_pronouns] as your pronouns."

    # Proceed to prologue
    jump prologue

    # This ends the game.

    return
