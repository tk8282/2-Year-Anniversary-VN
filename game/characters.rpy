init -1:
    # Ensure player_name is defined here before defining characters
    $ player_name = player_name if "player_name" in globals() else "You"  # Default to "You" if not set


# --- Character Definitions ----------------------------------------------------

define Z = Character("Zanny", who_outlines=[(3,"#9932cc",0,0)], window_background=Image("gui/textbox_f.png", xpos=13, yalign=1.0))        
define L = Character("Luci", who_outlines=[(3,"#bb0f28",0,0)], window_background=Image("gui/textbox_f.png", xpos=13, yalign=1.0))         
define R = Character("Rosco", who_outlines=[(3,"#fa1c9a",0,0)], window_background=Image("gui/textbox_f.png", xpos=13, yalign=1.0))        
define C = Character("Cass", who_outlines=[(3,"#50c878",0,0)], window_background=Image("gui/textbox_f.png", xpos=13, yalign=1.0))         
define G = Character("Gale", who_outlines=[(3,"#ffc124",0,0)], window_background=Image("gui/textbox_f.png", xpos=13, yalign=1.0))         
define N = Character("Nayu", who_outlines=[(3,"#1520A6",0,0)], window_background=Image("gui/textbox_f.png", xpos=13, yalign=1.0))
define MC = Character(player_name,who_outlines=[(3,"#1520A6",0,0)], window_background=Image("gui/textbox_f.png", xpos=13, yalign=1.0))   

define duo = Character(
    "{size=26}{color=#fa1c9a}{b}Rosco{/b}{/color} & "
    "{color=#1520A6}{b}[player_name]{/b}{/color}{/size}",
    window_background=Image("gui/textbox_f.png", xpos=13, yalign=1.0)
)

# NPCs
define Hostess = Character("Hostess",who_outlines=[(3,"#b290ab",0,0)], window_background=Image("gui/textbox_r.png", xpos=13, yalign=1.0))
define Waiter = Character("Waiter",who_outlines=[(3,"#b290ab",0,0)], window_background=Image("gui/textbox_r.png", xpos=13, yalign=1.0))
define Staff = Character("Staff Member",who_outlines=[(3,"#b290ab",0,0)], window_background=Image("gui/textbox_r.png", xpos=13, yalign=1.0))
define Cashier = Character("Cashier",who_outlines=[(3,"#b290ab",0,0)], window_background=Image("gui/textbox_r.png", xpos=13, yalign=1.0))
define anon = Character("???",who_outlines=[(3,"#b290ab",0,0)], window_background=Image("gui/textbox_r.png", xpos=13, yalign=1.0))
define ClassmateA = Character("Clingy Classmate",who_outlines=[(3,"#b290ab",0,0)], window_background=Image("gui/textbox_r.png", xpos=13, yalign=1.0))



# define name for mc for phone
define mc_nvl = Character("MC", kind=nvl, callback=Phone_SendSound)
define r_nvl = Character("Rosco", kind=nvl, callback=Phone_ReceiveSound)


define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# TO DO: 1. Ask for specific colors for characters 2. Use of first person character colors/name