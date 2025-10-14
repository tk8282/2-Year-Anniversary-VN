init -1:
    # -- Player Name --
    default player_name = "You"          # Default name
    default player_pronouns = "they/them"   # Default pronouns

    # Pronoun forms (subject, object, possessive, reflexive)
    default player_subject = "they"
    default player_object = "them"
    default player_possessive = "their"
    default player_possessive_obj = "theirs"
    default player_reflexive = "themself"

    # -- Choices --

    # -- Progress Flags --
    default chapter1_complete = False  
    default chapter2_complete = False  

# custom code

# transforms.rpy
transform waist_up_center:
    xalign 0.5
    yoffset 100

transform waist_up_left:
    xalign -0.25
    yoffset 100

transform waist_up_right:
    xalign 1.25
    yoffset 100

#shake effect
transform shake:
        ease .06 yoffset 24
        ease .06 yoffset -24
        ease .05 yoffset 20
        ease .05 yoffset -20
        ease .04 yoffset 16
        ease .04 yoffset -16
        ease .03 yoffset 12
        ease .03 yoffset -12
        ease .02 yoffset 8
        ease .02 yoffset -8
        ease .01 yoffset 4
        ease .01 yoffset -4
        ease .01 yoffset 0

transform shake2:
    xanchor 0.5
    yoffset 0  # Lock the y position
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0

