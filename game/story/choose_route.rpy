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
            
    add "gui/textbox_n.png" xpos 13 yalign 1.0 at ib_fade
    if len(collected_routes) == 0:
        add Text("Who do you want to help?",xalign=0.5, yalign=0.81, size=50, outlines = [(3,"#b290ab",0,0)], outline_scaling = "linear")
    else:
        add Text("Who do you want to help next?",xalign=0.5, yalign=0.81, size=50, outlines = [(3,"#b290ab",0,0)], outline_scaling = "linear")



label choose_route:

    scene bg clubroom with fade  
    call screen choice_menu
    
    

