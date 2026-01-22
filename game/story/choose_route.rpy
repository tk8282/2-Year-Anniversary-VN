screen choice_menu:

    
    $ cassBG = "#50c878"
    $ galeBG = "#ffc124"
    $ luciBG = "#bb0f28"
    $ roscoBG = "#fa1c9a"
    $ zannyBG = "#9932cc"

    if "C" in collected_routes:
        $ cassBG = "#111111"
    if "G" in collected_routes:
        $ galeBG = "#111111"
    if "L" in collected_routes:
        $ luciBG = "#111111"
    if "R" in collected_routes:
        $ roscoBG = "#111111"
    if "Z" in collected_routes:
        $ zannyBG = "#111111"
    
    modal True
    zorder 1
    hbox:
        xalign 0.5
        yalign 0.04
        xoffset 0
        yoffset 0
        spacing 20
      
        imagebutton:
            background cassBG
            idle "CassianGray"
            hover "CassianChoice"
            focus_mask True
            action Jump("cass_route")
                #ysize 0.58
                #xsize 350
            # imagebutton will be enabled if Route wasn't already played
            sensitive "C" not in collected_routes
            at ib_fade    

        imagebutton:
            background galeBG
            idle "GaleGray" 
            hover "GaleChoice"
            focus_mask True
            action Jump("gale_route")
            # imagebutton will be enabled if Route wasn't already played
            sensitive "G" not in collected_routes
            at ib_fade    

        imagebutton:
            background luciBG
            idle "LucienGray" 
            hover "LucienChoice"
            focus_mask True
            action Jump("luci_route")
            # imagebutton will be enabled if Route wasn't already played
            sensitive "L" not in collected_routes
            at ib_fade

        imagebutton:
            background roscoBG
            idle "RoscoGray" 
            hover "RoscoChoice"
            focus_mask True
            action Jump("rosco_route")
            # imagebutton will be enabled if Route wasn't already played
            sensitive "R" not in collected_routes
            at ib_fade
            
        imagebutton:
            background zannyBG
            idle "ZanderGray" 
            hover "ZanderChoice"
            focus_mask True
            action Jump("zanny_route")
            # imagebutton will be enabled if Route wasn't already played
            sensitive "Z" not in collected_routes
            at ib_fade
            
    add "gui/textbox.png" xalign 0.5 yalign 1.0
    if len(collected_routes) == 0:
        add Text("Who do you want to help?",xalign=0.5, yalign=0.9, size=50)
    else:
        add Text("Who do you want to help next?",xalign=0.5, yalign=0.9, size=50)
    # New UI Tetsing
    #add im.Scale("gui/testing/story_text box (no flowers)_candy.png",1600, 392.93) xalign 0.5 yalign 0.9
    #add Text("Who do you want to help?",xalign=0.5, yalign=0.82, size=50)
    


label choose_route:

    scene bg clubroom with fade  
    call screen choice_menu
    
    

