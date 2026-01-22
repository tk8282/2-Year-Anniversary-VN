# Haori Selection File

# Image Choice Screen
screen haori_choice():

    modal True

    frame:
        align (0.5, 0.5)
        background None

        vbox:
            spacing 40
            xalign 0.5

            hbox:
                spacing 80 
                xalign 0.5

                vbox:
                    spacing 10
                    xalign 0.5

                    frame:
                        background Solid("#000000c0")
                        padding (6, 6)

                        imagebutton:
                            idle "haori_gale_idle"
                            hover "haori_gale"
                            action Jump("left_haori")
                    frame:
                        xalign 0.5
                        background Solid("#000000c0")
                        padding (6,4)
                        text "Take the haori on the left" 

                vbox:
                    spacing 10
                    xalign 0.5

                    frame:
                        background Solid("#000000c0")
                        padding (6, 6)

                        imagebutton:
                            idle "haori_luci_idle"
                            hover "haori_luci"
                            action Jump("mid_haori")
                    frame:
                        xalign 0.5
                        background Solid("#000000c0")
                        padding (6,4)
                        text "Take the haori in the middle"

                vbox:
                    spacing 10
                    xalign 0.5

                    frame:
                        background Solid("#000000c0")
                        padding (6, 6)

                        imagebutton:
                            idle "haori_zander_idle"
                            hover "haori_zander"
                            action Jump("right_haori")
                    frame:
                        xalign 0.5
                        background Solid("#000000c0")
                        padding (6,4)
                        text "Take the haori on the right"



# Haori Choice Label
label haori_selection:
    call screen haori_choice

    return

label left_haori:

    "You reach out and grab the leftmost hanger, holding it up."

    MC "Look! This one gives me Gale vibes!"

    "You wave the yellow haori from side to side. Rosco looks over, his eyes lighting up instantly."

    show Rosco smug jacket at waist_up_center with dissolve
    R "Yeah, it matches his shoes really well—and that stupid Hawaiian shirt he always wears, I guess. It's like that colour but less harmful to my eyes."

    R "Plus, his favourite colour is gold, so he wouldn't have any complaints about wearing it!"

    "Approaching the rack, Rosco pulls out the other two haoris, holding one in either hand."

    show Rosco laugh jacket
    R "Oh, perfect! This purple one is so Zanny, just from looking at it… and most of Luci's wardrobe are paler red shades, right? He'll like this!"
    jump dialogue_continued

label mid_haori:

    "You reach out and grab the haori in the middle, holding it up."

    MC "Look! Doesn't this one remind you of Luci?"

    "You wave the red haori from side to side. Rosco looks over, his eyes lighting up instantly."

    show Rosco smug jacket at waist_up_center with dissolve
    R "Yeah, he likes to wear a lot of deep hues and red shades—or a combination of both, really. He'd definitely wear this kind of style, too."

    R "Now that I think about it, it'll also match that ring he always wears!"

    "Approaching the rack, Rosco pulls out the other two haoris, holding one in either hand."

    show Rosco laugh jacket
    R "Oh, perfect! This purple one is so Zanny, just from looking at it… and Gale really likes the colour gold, so he'll definitely like this, too."
    jump dialogue_continued

label right_haori:

    "You reach out and grab the rightmost haori, holding it up."

    MC "Look! This is {i}totally{/i} something Zanny would wear."

    "You wave the purple haori from side to side. Rosco looks over, his eyes lighting up instantly."

    show Rosco smug jacket at waist_up_center with dissolve
    R "Wait, you're right! It's practically the same colour as the lilac-y sweater he wears to school every day!"

    R "I already know he'd love to wear this kind of outfit."

    "Approaching the rack, Rosco pulls out the other two haoris, holding one in either hand."

    show Rosco laugh jacket
    R "Oh, perfect! Gale's favourite colour is gold, and this yellow is just like a diluted version of it… and most of Luci's wardrobe are paler red shades, right? He'll like this!"
    jump dialogue_continued


    label dialogue_continued:
        MC "Yeah! Knowing them, I think they'd agree with these choices."

        show Rosco neutral jacket at waist_up_center
        "Rosco nods cheerfully, moving both haoris to one hand."

        R "Great! I also saw a lime coloured one over there, and I think it'd complement Cass really well… It's not emerald, yeah, but it's the closest we'll get."

        R "So that's four down… oh, then all we have left is ours!"

        MC "What colour do you plan on getting?"

        show Rosco smug jacket
        R "Pink, obviously!"

        R "It'll go well with my hair if I can get it in the same range of magenta, but I'll take anything close to it at this point."

        R "As long as I can personalize it, I'll make it look like it was made for me!"

        # show Rosco neutral
        R "Now that we're talking about it, what kind of haori have {i}you{/i} been eyeing?"
        jump haori_choice_mc
    
    label haori_choice_mc:
        menu:
            "A warmer color":
                jump warm_haori
            "A cooler color":
                jump cool_haori
            "Something neutral":
                jump neutral_haori

    # Haori Choice
    label warm_haori:

        MC "I think I'd prefer a warmer color…"

        "Rosco thinks about it for a moment before taking a hanger from the rack to his right."

        show haori_warm with dissolve:
            pos (1100, 100)
        R "What about this one? I think it goes with your skin tone…?"

        MC "I didn't know you knew about matching skin tone to colors."

        R "… I don't. It sounds right, though."

        hide haori_warm with dissolve
        "You laugh at his admission, taking the haori from his hands."
        jump haori_selection_return

    label cool_haori:

        MC "I usually like wearing cool tones…"

        "Rosco glances around before pulling out a haori of a deeper, less striking hue."

        show haori_cool with dissolve:
            pos (1100, 100)
        R "Hey, look at this one! It looks like a good match for your wardrobe."

        MC "You're right! I love that color."

        hide haori_cool with dissolve
        R "Then it's settled."
        jump haori_selection_return

    label neutral_haori:

        MC "Hmm… Maybe something neutral? You guys are all wearing pretty distinct colors…"

        hide Rosco with dissolve
        "Rosco walks away as you mull over your options. You look through the bright colors, not feeling very inspired by any of them."

        show Rosco neutral jacket at waist_up_center with dissolve
        show haori_neutral with dissolve:
            pos (1100, 100)

        R "Something like this?"

        "He reappears beside you, holding out a haori that seems to have come out of thin air."

        show haori_neutral with dissolve
        MC "Where did you find this?"

        hide haori_neutral with dissolve
        R "Over there."
        jump haori_selection_return