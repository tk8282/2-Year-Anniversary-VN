# The script of the game goes in this file.

# The game starts here.



label splashscreen:
        
    $ _preferences.volumes['music'] *= .75
    scene black
    with Pause(0.3)
    play music "audio/music/G1 - Cheerful (1).wav"
    scene starting_screen_bg
    with fade
    show starting_screen_frame with dissolve
    show starting_screen_gale with dissolve
    show starting_screen_luci with dissolve
    show starting_screen_cass with dissolve
    show starting_screen_zanny with dissolve
    show starting_screen_rosco with dissolve
    show starting_screen_frame with dissolve
    with Pause(0.3)

    return

label start:
    stop music fadeout 1.0
    scene black with fade

    # Ask for player name at the start of the game
    $ player_name = renpy.input("What is your name?", default="")
    $ player_name = player_name.strip()  # Remove any extra spaces

    # If the player doesn't input anything, default to "You"
    if player_name == "":
        $ player_name = "You"

# Pronoun selection
label choose_pronouns:
    menu:
            "He/Him":
                $ player_pronouns = "he/him"
                $ player_subject = "he"
                $ player_object = "him"
                $ player_possessive = "his"
                $ player_possessive_obj = "his"
                $ player_reflexive = "himself"
                $ player_romterm = "boyfriend"
                jump after_pronouns  # Jump to the next section

            "She/Her":
                $ player_pronouns = "she/her"
                $ player_subject = "she"
                $ player_object = "her"
                $ player_possessive = "her"
                $ player_possessive_obj = "hers"
                $ player_reflexive = "herself"
                $ player_romterm = "girlfriend"
                jump after_pronouns  # Jump to the next section

            "They/Them":
                $ player_pronouns = "they/them"
                $ player_subject = "they"
                $ player_object = "them"
                $ player_possessive = "their"
                $ player_possessive_obj = "theirs"
                $ player_reflexive = "themself"
                $ player_romterm = "partner"
                jump after_pronouns  # Jump to the next section

    label after_pronouns:
    # After pronouns have been selected, show confirmation
    "Hello, [player_name]! You have chosen [player_pronouns] as your pronouns."

    # Proceed to prologue
    #jump prologue

    # Proceed to gacha screen
    jump gacha_screen

    # This ends the game.

    return

#use "call credits"
label credits:
    $ quick_menu = False
    $ credits_speed = 100 #scrolling speed in seconds
    play music "audio/music/G1 - Cheerful (1).wav" fadein 1.0
    scene starting_screen_full
    with dissolve
    show screentint
    with dissolve
    show tbc:
        yanchor 0.5 ypos 0.45
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide tbc with dissolve
    pause(1.0)
    show part2:
        yanchor 0.5 ypos 0.45
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide part2 with dissolve
    pause(1.0)
    show cred at Move((0.5, 7.5), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom") with dissolve
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.45
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    stop music fadeout 1.0
    return

init python:
    credits = ('Mods',' ', 'Arin @light_arin'),('Mods',' ', 'Eve @Ebaelynn'),('Mods',' ', 'Aly @_Alycarus'),('Mods',' ', 'Angie @_kaokaos'),('Mods',' ', 'Ann @ann_teasocial'),('Mods',' ', 'TK @TkFlash2'),('Gale Route', 'Writers', 'Shelby @shoobilled'), ('Gale Route', 'Writers', 'Chia @chiaseed_lol'), ('Gale Route', 'Sprite', 'Zoo @Mawfische'),('Gale Route', 'CG', 'Cas @casterseer'),('Gale Route', 'Backgrounds', 'Jae @chromaticdawn') ,('Cass Route', 'Writers', 'Lala @oopsiesloops'), ('Cass Route', 'Writers', 'Sel @moiselvie'), ('Cass Route', 'Sprite', 'Jeanne @smolmouche'),('Cass Route', 'CG', 'Lafiska @Lafa_or_Life'),('Cass Route', 'Backgrounds', 'Karasu @karasu_draws'),('Luci Route', 'Writers', 'Lykos @Moonlit_Lykos'), ('Luci Route', 'Writers', 'Focks @starfocks_'), ('Luci Route', 'Writers', 'Anon'), ('Luci Route', 'Sprite', 'Ann'),('Luci Route', 'CG', 'Ken @kenwnyan'),('Luci Route', 'Backgrounds', 'Angie'),('Zanny Route', 'Writers', 'Samatokiiis @samatokiiis'), ('Zanny Route', 'Writers', 'Axel @CheesyGabite'), ('Zanny Route', 'Sprite', 'Moka @mocha2ru'),('Zanny Route', 'CG', 'Miky San @MikySan29'),('Zanny Route', 'Backgrounds', 'Rain @rain__ghost'),('Rosco Route', 'Writers', 'Arin'), ('Rosco Route', 'Writers', 'Bayqus @bayquswrites'), ('Rosco Route', 'Sprite', 'Chowwy @DogChow101'),('Rosco Route', 'CG', 'Hoshka @lohoska'),('Rosco Route', 'Backgrounds', 'Cris @crisosstomo_'),('General', 'Homescreen', 'Zivvi @zivvikal'),('General', 'UI/UX', 'Candy @_amurta'),('General', 'Coding', 'TK'),('General', 'Coding', 'Hanxi @Hanxiowo'),('General', 'Editing', 'Hannah B. @Beenana0_0'), ('General', 'Editing', 'Nyx @chamanthus '),('General', 'Editing', 'Eve'),('General', 'Music', 'Yena @sheepshxt'),('General', 'Music', 'Han Hyo Mi @Han_Hyomi_'),('General', 'Assets', 'Aly'),('General', 'Assets', 'Zomboba  @Zomboba / @zomboblab'),('General', 'Assets', 'Destinie @Dezk_is_crying '),('General', 'Assets', 'Anon'),('General', 'Backgrounds', 'Ikin @akiramonsta'),('General', 'Backgrounds', 'Aly'),
    credits_s = "{size=80}Credits"
    c1 = ''
    c2 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n\n\n\n{size=70}" + c[0] + "\n"
        if not c2==c[1]:
            if not c[1]== " ":
                credits_s += "\n{size=50}" + c[1] + "\n"
            else:
                credits_s += "\n{size=50}"
        credits_s += "{size=40}" + c[2] + "\n"
        c1=c[0]
        c2=c[1]
    credits_s += "\n{size=50}Engine\n{size=40}Ren'py\n8.3.7" #Don't forget to set this to your Ren'py version
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5, color = "#ffff")
    image tbc = Text("{size=80}To be continued...", text_align=0.5, color = "#ffff")
    image part2 = Text("{size=80}Part 2 Coming soon!", text_align=0.5, color = "#ffff")
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5, color = "#ffff")
