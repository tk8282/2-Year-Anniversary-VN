# Defaults

default mascots_remaining = 5

default seen_pipsqueak = False
default seen_dewdrop = False
default seen_lunarist = False
default seen_netherling = False
default seen_roscal = False



# DEPENDENT COMMENTS
label mascot_dependent:

    if mascots_remaining == 4:
        MC "There are five characters so far, right? I'll have a look at all of them before making my pick."
    elif mascots_remaining == 3:
        MC "That one's interesting, but there are still three more to decide on."
    elif mascots_remaining == 2:
        MC "Two more to go, then I'll pick!"
    elif mascots_remaining == 1:
        MC "Okay, I'll look at the last one then choose, promise!"
    else:
        MC "That's all of them, isn't it?"

    return


# ENTRY POINT
label mascot_selection:

    # default values 
    $ mascots_remaining = 5
    $ seen_pipsqueak = False
    $ seen_dewdrop = False
    $ seen_lunarist = False
    $ seen_netherling = False
    $ seen_roscal = False

    jump mascot_loop


# mascot loop
label mascot_loop:

    hide screen portrait
    if mascots_remaining <= 0:
        jump mascot_end

    call screen mascot_select_screen
    return



# ROUTES 
label mascot_pipsqueak:
    show screen portrait(
    "Rosco neutral jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )

    MC "Is that a… pirate bird…?"
    R "Yeah! Don't even ask me about the design. Gale thought of this one… He's got a weird obsession with pirates. And swords."
    R "Anyway, yes, that's Pipsqueak! They're a ranged DPS; that is to say, they do a lot of damage from afar!"
    R "The downside is that they're squishy—meaning to say that their health isn't as high as the other characters."
    MC "Ooh, okay!"

    call mascot_dependent from _call_mascot_dependent
    jump mascot_loop

label mascot_dewdrop:
    show screen portrait(
    "Rosco neutral jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )

    MC "Is this one made of water?"
    show screen portrait(
    "Rosco laugh jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )
    R "Yep, that's how Cass designed it!"
    show screen portrait(
    "Rosco neutral jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )
    R "This is a Dewdrop! They're more of a support character than the others, so their kit is focused around healing."
    R "Dewdrops are kind of squishy, though, but they have some self-healing effects that can be used to prevent getting instantly cooked."
    MC "I get it!"

    call mascot_dependent from _call_mascot_dependent_1
    jump mascot_loop

label mascot_lunarist:
    MC "What is this even meant to be?"

    show screen portrait(
    "Rosco confused jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )

    R "Honestly, I don't really know either, but Luci said that the concept is meant to be a soul?"

    show screen portrait(
    "Rosco neutral jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )
    
    R "This is a Lunarist! They're pretty strong, but they have a longer cooldown for skills and run out of MP kind of quickly early game."
    MC "I… think I get it? Kind of hard to visualise, but I'll probably pick it up."

    call mascot_dependent from _call_mascot_dependent_2
    jump mascot_loop

label mascot_netherling:
    MC "Is this a one-winged demon… jelly… thing?"
    show screen portrait(
    "Rosco shocked jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )
    R "How'd you get that on your first try? That's exactly what Zander wanted it to be."
    show screen portrait(
    "Rosco neutral jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )
    R "This is a Netherling! Their role is to be a tank."
    R "They absorb attacks and turn it into health."
    R "Out of all the characters, I'm pretty sure Netherling has the most base HP."
    MC "That's so cool!"

    call mascot_dependent from _call_mascot_dependent_3
    jump mascot_loop

label mascot_roscal:
    MC "Is that… a rat?"
    show screen portrait(
    "Rosco smug jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign= 1.05,
    yalign=0.95
    )
    R "That's a Roscal! I came up with this one."
    MC "It has such a cute smile and a color combination I never would have imagined."
    show screen portrait(
    "Rosco neutral jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign= 1.05,
    yalign=0.95
    )
    R "We actually took inspiration from a jacket I wear pretty often."
    MC "Inspiration really can come from anywhere, huh?"
    R "Definitely."
    MC "So what role does this one have?"
    R "The Roscal is a melee DPS. Tanky, mobile, great for roaming."
    MC "Cool! Roaming sounds stressful—but fun."

    call mascot_dependent from _call_mascot_dependent_4
    jump mascot_loop


# END POINT
label mascot_end:

    MC "Wah, all these characters are so well-designed and thought out…"
    MC "Damn, do I really have to pick one?"
    
    show screen portrait(
    "Rosco annoyed jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )
    R "It's not like you'll be stuck with one for life!"
    show screen portrait(
    "Rosco neutral jacket",
    crop_x=450,
    crop_y=0,
    crop_w=360,
    crop_h=360,
    xalign=0.95,
    yalign=0.95
    )
    R "After release, you can play as many characters as you want. This is just for testing!"

    MC "Uuuugh. Okay, fine…"


    jump mascot_info_return


# SCREEN
screen mascot_select_screen:

    tag menu

    frame:
        align (0.5, 0.5)
        background None
        
        vbox:
            spacing 20
            text "Choose a character to learn about:" align (0.5, 0.5)

            # Top row
            hbox:
                spacing 20
                align (0.5, 0.5)

                if not seen_pipsqueak:
                    imagebutton:
                        idle "pipsqueak_idle"
                        hover "pipsqueak_hover"
                        xysize (350, 350)
                        action [
                            SetVariable("seen_pipsqueak", True),
                            SetVariable("mascots_remaining", mascots_remaining - 1),
                            Jump("mascot_pipsqueak")
                        ]
                else:
                    null

                if not seen_dewdrop:
                    imagebutton:
                        idle "dewdrop_idle"
                        hover "dewdrop_hover"
                        xysize (350, 350)
                        action [
                            SetVariable("seen_dewdrop", True),
                            SetVariable("mascots_remaining", mascots_remaining - 1),
                            Jump("mascot_dewdrop")
                        ]
                else:
                    null

                if not seen_lunarist:
                    imagebutton:
                        idle "lunarist_idle"
                        hover "lunarist_hover"
                        xysize (350, 350)
                        action [
                            SetVariable("seen_lunarist", True),
                            SetVariable("mascots_remaining", mascots_remaining - 1),
                            Jump("mascot_lunarist")
                        ]
                else:
                    null

            # Bot row
            hbox:
                spacing 20
                align (0.5, 0.5)

                if not seen_netherling:
                    imagebutton:
                        idle "netherling_idle"
                        hover "netherling_hover"
                        xysize (350, 350)
                        action [
                            SetVariable("seen_netherling", True),
                            SetVariable("mascots_remaining", mascots_remaining - 1),
                            Jump("mascot_netherling")
                        ]
                else:
                    null

                if not seen_roscal:
                    imagebutton:
                        idle "roscal_idle"
                        hover "roscal_hover"
                        xysize (350, 350)
                        action [
                            SetVariable("seen_roscal", True),
                            SetVariable("mascots_remaining", mascots_remaining - 1),
                            Jump("mascot_roscal")
                        ]
                else:
                    null
