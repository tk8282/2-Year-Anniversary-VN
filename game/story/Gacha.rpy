

label gacha_screen:
    jump gachapon_animation
    

label gachapon_animation:
    $ phone_acc = renpy.random.randint(1, 4)
    scene bg clubroom at fullyblurred with fade
    if pull_counter == 0:
        play sound "audio/sfx/success-bell.ogg" volume 0.2
        "You got a gift!"
    else:
        MC "Let's do this again!"
    # gacha pon appears
    show gachapon full onlayer layer5 at gacha_pon_center with dissolve
    pause 0.3
    play sound "audio/sfx/game-bonus.ogg" volume 0.3
    show gachapon full onlayer layer5 at shake2
    pause 0.8
    show gachapon back onlayer layer1 at gacha_pon_center
    show gachapon ball onlayer layer2 at gacha_pon_ball_up
    show gachapon front onlayer layer3 at gacha_pon_center
    show gachapon spin onlayer layer4 at gacha_pon_spin_center
    hide gachapon full onlayer layer5
    pause 0.5
    # gachapon animation start
    show gachapon spin onlayer layer4 at gacha_pon_spinning
    pause 1.7
    
    show gachapon ball onlayer layer2 at gacha_pon_ball_down with move
    play sound "audio/sfx/ball-thud.ogg" volume 0.3
    pause 0.5
    show gachapon full complete onlayer layer5 at gacha_pon_center
    # gachapon animation end
    # hide gachapon single parts
    hide gachapon back onlayer layer1
    hide gachapon ball onlayer layer2
    hide gachapon front onlayer layer3
    hide gachapon spin onlayer layer4
    
    MC "Let's see how lucky I am!"
    # hides full gachapon
    hide gachapon full complete onlayer layer5 with dissolve

    # gachaball animation start
    show gachaball full onlayer layer5 at gachaball_center with dissolve
    show gachaball top onlayer layer4 at gachaball_center
    show gachaball bottom front onlayer layer3 at gachaball_center
    show gacha reveal onlayer layer2 at gachaball_center
    show gachaball star onlayer layer1 at gachaball_center
    show gachaball bottom back onlayer layer0 at gachaball_center

    pause 0.5
    hide gachaball full onlayer layer5
    show gachaball top onlayer layer4 at gachaball_top_open
    show gachaball bottom back onlayer layer0 at gachaball_bottom_open
    show gachaball bottom front onlayer layer3 at gachaball_bottom_open

    hide gachaball top onlayer layer4 with dissolve

    hide gachaball bottom back onlayer layer0
    hide gachaball bottom front onlayer layer3 with dissolve
    play sound "audio/sfx/clear-combo.ogg" volume 0.3
    if phone_acc == 1:
        "It's Bibble!"
    elif phone_acc == 2:
        "It's Dingding!"
    elif phone_acc == 3:
        "It's Gobblycook!"
    elif phone_acc == 4:
        "It's Paddyraptor!"

    hide gacha reveal onlayer layer2 with dissolve
    hide gachaball star onlayer layer1 with dissolve
    $ pull_counter += 1
    jump gacha_open

label gacha_open:
    scene bg clubroom at fullyblurred with fade
    
    if pull_counter < 3:
        menu:
            "Would you like to keep this prize?"
            "Yes!": 
                jump prologue
            "No, I'd like to try again! (Try [pull_counter]/3)":
                jump gachapon_animation
    
    else:
        menu:
            "Would you like to keep this prize?"
            "Yes!": 
                jump prologue
            "Can I just pick my prize, please?":
                jump gacha_selection

label gacha_selection:
    scene bg clubroom at fullyblurred with fade
    call screen phone_acc_menu
    
    

screen phone_acc_menu:
    modal True
    zorder 1
    hbox:
        xalign 0.5
        yalign 0.3
        xoffset 0
        yoffset 0
        spacing 0

        imagebutton:
                idle "choice bibble gray"
                hover "choice bibble"
                focus_mask True
                action [SetVariable("phone_acc", 1), Jump("prologue")]
                at ib_fade
        
        imagebutton:
                idle "choice dingding gray"
                hover "choice dingding"
                focus_mask True
                action [SetVariable("phone_acc", 2), Jump("prologue")]
                at ib_fade

        imagebutton:
                idle "choice gobblycook gray"
                hover "choice gobblycook"
                focus_mask True
                action [SetVariable("phone_acc", 3), Jump("prologue")]
                at ib_fade

        imagebutton:
                idle "choice paddyraptor gray"
                hover "choice paddyraptor"
                focus_mask True
                action [SetVariable("phone_acc", 4), Jump("prologue")]
                at ib_fade
                
    add Image("gui/textbox.png", xalign=0.5, yalign=1.0)
    add Text("Choose your prize!",xalign=0.5, yalign=0.9, size=50)
    # New UI Tetsing
    #add im.Scale("gui/testing/story_text box (no flowers)_candy.png",1600, 392.93) xalign 0.5 yalign 0.9
    #add Text("Choose your prize!",xalign=0.5, yalign=0.82, size=50)           