define MK_TIME = 5.0
define MK_BAR_WIDTH = 600
define MK_BAR_HEIGHT = 22
define MK_BAR_Y = 0.58


screen mk_timer():

    default t = MK_TIME
    default timed_out = False

    timer 0.05 repeat True action If(
        t > 0,
        SetScreenVariable("t", t - 0.05),
        If(
            not timed_out,
            [
                SetScreenVariable("timed_out", True),
                Hide("mk_timer"),
                Jump(timer_jump)
            ]
        )
    )

    $ ratio = t / MK_TIME

    if ratio > 0.2:
        $ bar_color = "#6fdc6f"
    else:
        $ bar_color = "#ff4d4d"

    frame:
        xalign 0.5
        yalign MK_BAR_Y
        background "#0008"
        padding (6, 6)

        bar:
            value t
            range MK_TIME
            xsize MK_BAR_WIDTH
            ysize MK_BAR_HEIGHT
            left_bar Solid(bar_color)
            right_bar Solid("#222")




label mk_timed_menu(menu_label, timeout_label, duration):

    $ mk_time_left = duration
    show screen mk_timer(mk_time_left, duration)

    while mk_time_left > 0:
        $ mk_time_left -= renpy.get_frame_time()
        $ renpy.pause(0.05, hard=True)

    hide screen mk_timer
    jump timeout_label

label MariaKart:

    # ---------------------------
    # STARTING BOOST
    # ---------------------------

    $ timer_jump = "mk_hold_3"
    show screen mk_timer

    menu:
        "Hold button down at 3":
            hide screen mk_timer
            jump mk_hold_3

        "Hold button down at 2":
            hide screen mk_timer
            jump mk_hold_2

label mk_hold_3:
    "You groan as the race starts, staring at the way your car wriggles on the screen."

    show Rosco smug jacket
    R "Hah! Rookie mistake."
    jump mk_chest_choice


label mk_hold_2:
    MC "Hah! Take that!"

    show Rosco smug jacket
    R "You're too slow!"
    jump mk_chest_choice

label mk_chest_choice:

    $ timer_jump = "mk_single_chest"
    show screen mk_timer

    menu:
        "Go for the double chest":
            hide screen mk_timer
            jump mk_double_chest

        "Go for the single chest":
            hide screen mk_timer
            jump mk_single_chest


label mk_double_chest:
    MC "Yes!"

    show Rosco annoyed jacket
    R "I was about to take that!"
    jump mk_coin_choice


label mk_single_chest:
    MC "That stupid NPC took the double chest!"

    show Rosco smug jacket
    R "Sucks to suck."
    jump mk_coin_choice

label mk_coin_choice:

    $ timer_jump = "mk_banana"
    show screen mk_timer

    menu:
        "Go towards the coin":
            hide screen mk_timer
            jump mk_coin

        "Go towards the banana":
            hide screen mk_timer
            jump mk_banana


label mk_coin:
    MC "What do coins do again?"

    show Rosco neutral jacket
    R "They help you go faster."

    MC "Wait, really?"
    jump mk_shell_choice


label mk_banana:
    MC "What—?! Who puts a banana THERE?!"

    show Rosco laugh jacket
    "Rosco laughs at your clear irritation, too focused on the race to say anything."
    jump mk_shell_choice

label mk_shell_choice:

    $ timer_jump = "mk_yellow_shell"
    show screen mk_timer

    menu:
        "Throw a yellow shell":
            hide screen mk_timer
            jump mk_yellow_shell

        "Throw a orange shell":
            hide screen mk_timer
            jump mk_orange_shell


label mk_yellow_shell:
    "You launch a shell in front of you, not even glancing at the other screens."

    show Rosco laugh jacket
    R "Nice try! You missed, goofy."

    MC "Careful, it’s still going~ You might jinx yourself!"
    R "Nope! It just broke."

    MC "Whatever."
    jump mk_final_choice


label mk_orange_shell:
    "You launch a shell ahead of you, and Rosco makes a strangled noise."

    show Rosco angry jacket
    R "What the fuck, [player_name]?!"

    MC "I didn't mean to."
    R "Nobody believes that!"
    jump mk_final_choice

label mk_final_choice:

    "Now at the last lap, you and Rosco occupy second and first place respectively."

    $ timer_jump = "mk_play_fair"
    show screen mk_timer

    menu:
        "Play fair and try to win":
            hide screen mk_timer
            jump mk_play_fair

        "Distract Rosco":
            hide screen mk_timer
            jump mk_distract


label mk_play_fair:
    $ rosco_won = True

    "You try your best on the final stretch of the game, pulling out all the little tricks you know from playing the game over the years."
    "Despite your best efforts, the gap between your two cars doesn't shrink."

    show Rosco smug jacket
    R "Hell yeah! Eat dust, [player_name]!"

    MC "What the hell?! It was half a second off!"
    R "You're too slow~"

    "You put the controller down, reaching over to pinch his cheek and giving it a sharp tug."
    MC "Oh, shut up already!"
    jump MariaKart_return

label mk_distract:
    $ rosco_won = False

    "Without hesitating, you stand in front of Rosco, blocking his view of the screen."

    show Rosco confused jacket
    R "Hey, what the heck—!"

    MC "All's fair in love and war!"

    "You smirk as a purple shell flies past you, hitting him just before he reaches the finish line."

    MC "Bless whatever NPC just threw that!"

    show Rosco annoyed jacket
    R "[player_name], get out of the way—!"

    MC "Nope!"

    "You move with every step he takes, making sure to block his view as you cross the finish line."

    MC "Let's go! First place!"

    "Rosco lets out a huff as you cheer."
    "He rolls his eyes, not missing the way you stick your tongue out at him."

    R "Yeah, yeah. Congratulations, goofy."
    jump MariaKart_return