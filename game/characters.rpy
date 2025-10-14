init -1:
    # Ensure player_name is defined here before defining characters
    $ player_name = player_name if "player_name" in globals() else "You"  # Default to "You" if not set

define Z = Character("Zanny", color="#e67e22")          # Orange
define L = Character("Luci", color="#9b59b6")           # Purple
define R = Character("Rosco", color="#3498db")          # Blue
define C = Character("Cass", color="#2ecc71")           # Green
define G = Character("Gale", color="#e74c3c")           # Red
define N = Character("Nayu")
define MC = Character(player_name, color= "#FFFF00")     # Yellow

# TO DO: 1. Ask for specific colors for characters 2. Use of first person character colors/name
#
