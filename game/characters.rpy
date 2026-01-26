init -1:
    # Ensure player_name is defined here before defining characters
    $ player_name = player_name if "player_name" in globals() else "You"  # Default to "You" if not set


# --- Character Definitions ----------------------------------------------------

define Z = Character("Zanny", color="#ffc124")        
define L = Character("Luci", color="#9932cc")         
define R = Character("Rosco", color="#fa1c9a")        
define C = Character("Cass", color="#50c878")         
define G = Character("Gale", color="#bb0f28")         
define N = Character("Nayu")
define MC = Character(player_name, color="#1520A6")   


# NPCs
define Hostess = Character("Hostess")
define Waiter = Character("Waiter")
define Staff = Character("Staff Member")
define Cashier = Character("Cashier")
define anon = Character("???")
define ClassmateA = Character("Clingy Classmate")



# define name for mc for phone
define mc_nvl = Character("MC", kind=nvl, callback=Phone_SendSound)
define r_nvl = Character("Rosco", kind=nvl, callback=Phone_ReceiveSound)


define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# TO DO: 1. Ask for specific colors for characters 2. Use of first person character colors/name