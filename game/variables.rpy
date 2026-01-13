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
    default player_romterm = "partner"

    # -- Choices --
    default collected_routes = []

    # -- Gacha System --
    default pull_counter = 0
    default phone_acc = 1 # 1=bibble, 2=dingding, 3=gobblycook, 4=paddyraptor

    # -- Choices for Lucien Route --
    default luciRomantic = False # affects ending
    default flowerPoppy = False # affects ending
    default flowerDaisy = False # affects ending

    # -- Choices for Cassian Route --
    default appliance_choice = "normal-appliances"
    default cassRomantic = False # affects ending

    # -- Choices for Zanny Route ---
    default ask_figure = False
    default ask_dice = False
    default ask_box = False
    default ask_plushie = False
    default convo_festival = False
    default convo_school = False
    default zanny_orchid = False # affects ending
    default zanny_scare = False # affects ending

    # -- Progress Flags --
    default chapter1_complete = False  
    default chapter2_complete = False  

# custom code
# slower move transitions
define slow_move = MoveTransition(1.5)

define slow_move2 = MoveTransition(2.0)

transform ib_fade:
    alpha 0.0
    easein 1.0 alpha 1.0

# asset appears from bottom (used for e.g. phone asset)
transform move_up:
    yoffset 800
    alpha 0.0
    ease 1 yoffset -40 alpha 1.0
    ease 0.5 yoffset 0 alpha 1.0
    on hide:
        ease 1 yoffset 600 alpha 0.0

# blurres image fully
transform fullyblurred:
    blur 10

# blurres image partially
transform partlyblurred:
    blur 5

# unblurs image
transform unblur:
    linear 1 blur 0

# bounce animation
transform bounce:
    yoffset 0
    easein .175 yoffset -10
    easein .175 yoffset 0
    easeout .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat 1

# zoom transitions might have bugs! might have to be tweaked
#zoom 2 for fullbody (MC running towards character scene)
transform zoomin2:
    linear 1 zoom 1.3 yoffset 100

#zoom 3 for waist_up (character stand up, comes in closer scene)
transform zoomin3:
    ease 0.5 yoffset 0
    linear 1 zoom 1.3 yoffset 0

#zoom out for both zoomin 2 + 3
transform zoomout2:
    linear 1 zoom 1.0 yoffset 0

#zoom out for zoomin 2+3 with jump
transform zoomout_jump:
    linear 1 zoom 0.77 yoffset 0

transform zoom_back:
    linear 1 zoom 1.0 yoffset 0
transform zoom_away:
    linear 1 zoom 0.7 yoffset 0

#immediately removes Zoom 2 + 3
transform removezoom:
    zoom 1.0 yoffset 0

# trembling animation no auto stop!
# ex. 
# show Character at waist_up_center, trembling -> activate
# pause 1.0 -> pauses actions while charcter keeps trembling for chosen time frame
# show Character at wasit_up_center -> to stop trembling after pause
transform trembling:
    yoffset 0
    parallel:
        linear .05 xoffset -5
        linear .05 xoffset 5
        repeat
    parallel:
        linear .1 yoffset 10
        linear .1 yoffset 0.0
        repeat

transform pop:
    yoffset 0
    easein 0.1 yoffset -10
    easeout 0.1 yoffset 0

# single jump followed by smaller bounce
transform singlejump:
    yoffset 0
    easein 0.1 yoffset -50
    easeout 0.1 yoffset 0
    easein 0.1 yoffset -10
    easeout 0.1 yoffset 0

transform jumping:
    yoffset 0
    easein 0.2 yoffset -100
    easeout 0.2 yoffset 0
    easein 0.175 yoffset -30
    easeout 0.175 yoffset 0
    easein 0.15 yoffset -10
    easeout 0.15 yoffset 0
    easein 0.1 yoffset -4
    easeout 0.1 yoffset 0

# restless movement
transform restless:
    yoffset 0
    parallel:
        linear .05 yoffset -5
        linear .05 yoffset 0
        linear .2 xoffset 10
        linear .1 xoffset 0.0
        linear .2 xoffset -10
        linear .1 xoffset 0.0
        repeat 3

# used for BG
transform screenshake:
    ypos 0.5
    xpos 0.5
    xanchor 0.5
    yanchor 0.5
    parallel:
        linear 0.2 yanchor 0.503 
        linear 0.2 yanchor 0.497
        repeat 2
    parallel:
        linear 0.22 xanchor 0.503 
        linear 0.22 xanchor 0.497 
        repeat 2
    ypos 0.5
    xpos 0.5
    xanchor 0.5
    yanchor 0.5

transform screenshake2:
    ypos 0.5
    xpos 0.5
    xanchor 0.5
    yanchor 0.5
    parallel:
        linear 0.3 yanchor 0.503 
        linear 0.3 yanchor 0.497
        repeat 2
    parallel:
        linear 0.32 xanchor 0.503 
        linear 0.32 xanchor 0.497 
        repeat 2
    ypos 0.5
    xpos 0.5
    xanchor 0.5
    yanchor 0.5
    
# used for BG
transform headshake:
    easein .3 xoffset -20
    easeout .3 xoffset 0
    easein .3 xoffset 20
    easeout .3 xoffset 0
    repeat 3

# used for BG
transform nod:
    easein .3 yoffset -20
    easeout .3 yoffset 0
    easein .3 yoffset 20
    easeout .3 yoffset 0
    repeat 2

transform camerapanright:
    ease .2 xoffset 20
    ease .2 xoffset 0

transform camerapanleft:
    ease .2 xoffset -20
    ease .2 xoffset 0

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

#---------specifically for gale----------
transform waist_up_center2:
    xalign 0.5
    yoffset 80

transform waist_up_left2:
    xalign 0
    yoffset 80

transform waist_up_right2:
    xalign 0.95
    yoffset 80
#----------------------------------------

#-------specifically for zanny-----------
transform waist_up_center3:
    xalign 0.5
    yoffset -80

transform waist_up_left3:
    xalign -0.5
    yoffset -80

transform waist_up_right3:
    xalign 1.7
    yoffset -80
#------------------------------------------

# character position for showing assets
transform waist_up_right_for_asset:
    xalign 1.4
    yoffset 100

# character position for showing assets / Gale
transform waist_up_right_for_asset2:
    xalign 1.04
    yoffset 80

# character position for showing assets / Zanny
transform waist_up_right_for_asset3:
    xalign 2.15
    yoffset -80

# ----fullbody versions/zoomed out character positions----
transform fullbody_center:
    xalign 0.5
    yoffset 0

transform fullbody_center2:
    xalign 0.5
    yoffset 100

transform fullbody_right:
    xalign 1.05
    yoffset 0

transform fullbody_left:
    xalign -0.05
    yoffset 0
#------------------------------------------------------------
#----------------asset positioning---------------
transform asset_center:
    xalign 0.5
    yoffset 0

transform asset_pos1:
    xalign 0
    yoffset 100

transform asset_pos2:
    xalign 0.3
    yoffset 0

transform asset_pos3:
    xalign 0.62
    yoffset 150

transform asset_pos4:
    xalign 1.06
    yoffset 0
#----------------------------------------------------------------
#--------gacha position and animations---------
transform gacha_pon_center:
    xalign 0.5
    yoffset 0.5

transform gacha_pon_ball_up:
    xalign 0.5
    yoffset -300

transform gacha_pon_ball_down:
    xalign 0.5
    yoffset 0.5

transform  gacha_pon_spin_center:
    xalign 0.4605
    yoffset 541

transform gachaball_center:
    xalign 0.5
    yoffset 100

transform gachaball_top_open:
    easeout 1 yoffset -100
    xoffset 0

transform gachaball_bottom_open:
    easeout 0.5 yoffset 150
    xoffset 0

# gacha effects
transform  gacha_pon_spinning:
    rotate 0
    subpixel True
    yoffset 520
    xoffset -3
    linear 1 rotate 180
    pause 0.3
    linear 1 rotate 360
#-------------------------------------------------------------
# shake effect
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