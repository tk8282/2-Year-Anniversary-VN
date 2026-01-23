# MascotPlayTest.rpy

# defaults
default chosen_mascot = None

screen ability_wait(correct_key, ability_name):

    modal True
    zorder 100

    frame:
        align (0.25, 0.35)
        padding (40, 30)

        vbox:
            spacing 15
            text "Press" size 38 xalign 0.5
            text correct_key.upper() size 48 bold True xalign 0.5

    # handle for all keys
    key "q" action Return("success" if correct_key == "q" else "fail")
    key "w" action Return("success" if correct_key == "w" else "fail")
    key "e" action Return("success" if correct_key == "e" else "fail")
    key "r" action Return("success" if correct_key == "r" else "fail")

    # handle for extra possible keys
    key "a" action Return("fail")
    key "s" action Return("fail")
    key "d" action Return("fail")
    key "f" action Return("fail")
    key "z" action Return("fail")
    key "x" action Return("fail")
    key "c" action Return("fail")
    key "v" action Return("fail")
    key "K_SPACE" action Return("fail")
    key "K_RETURN" action Return("fail")
    key "K_ESCAPE" action Return("fail")

    # block mouse clicking
    key "mouseup_1" action NullAction()



#check for fails
label ability_check(correct_key, display_key):
    $ ability_failures = 0

    while True:
        $ result = renpy.call_screen("ability_wait", correct_key, display_key)

        if result == "success":
            return
        else:
            $ ability_failures += 1

            if ability_failures >= 3:
                show Rosco shocked at waist_up_center
                R "Wow you really don't game, do you?"
            else:
                show Rosco neutral at waist_up_center
                R "Wrong button goofy"


# ENTRY POINT
label mascot_playtest:
    call screen mascot_PlayTest_Screen
    jump mascot_choice


# ROUTES
label mascot_choice:

    if chosen_mascot == "pipsqueak":
        jump pipsqueak_route
    elif chosen_mascot == "dewdrop":
        jump dewdrop_route
    elif chosen_mascot == "lunarist":
        jump lunarist_route
    elif chosen_mascot == "netherling":
        jump netherling_route
    elif chosen_mascot == "roscal":
        jump roscal_route
    else:
        return


# SELECTION SCREEN
screen mascot_PlayTest_Screen:
    tag menu

    frame:
        align (0.5, 0.5)
        background None

        vbox:
            spacing 30
            text "Pick your final character:" xalign 0.5 size 32

            # Top row
            hbox:
                spacing 30
                xalign 0.5

                imagebutton:
                    idle "pipsqueak_idle"
                    hover "pipsqueak_hover"
                    xysize (350, 350)
                    action [SetVariable("chosen_mascot", "pipsqueak"), Return()]

                imagebutton:
                    idle "dewdrop_idle"
                    hover "dewdrop_hover"
                    xysize (350, 350)
                    action [SetVariable("chosen_mascot", "dewdrop"), Return()]

                imagebutton:
                    idle "lunarist_idle"
                    hover "lunarist_hover"
                    xysize (350, 350)
                    action [SetVariable("chosen_mascot", "lunarist"), Return()]

            # Bot row
            hbox:
                spacing 30
                xalign 0.5

                imagebutton:
                    idle "netherling_idle"
                    hover "netherling_hover"
                    xysize (350, 350)
                    action [SetVariable("chosen_mascot", "netherling"), Return()]

                imagebutton:
                    idle "roscal_idle"
                    hover "roscal_hover"
                    xysize (350, 350)
                    action [SetVariable("chosen_mascot", "roscal"), Return()]


# ROUTES
label pipsqueak_route:

    MC "I'll go with Pipsqueak. I'm really curious about the ranged DPS thing!"

    R "Good choice! Gale would be happy to hear that you picked his design."

    "When you click the Pipsqueak, the character shows as selected. You load up into a proper game in no time."

    MC "Woah. These graphics are insane! Did you do this yourself?"

    show Rosco smug at waist_up_center
    R "Hell yeah! We all planned the design together, but I modelled the actual thing on my own."

    MC "This is so sick… It's a real game!"
    MC "Everything runs so smoothly, and it's got no lag for a demo."
    MC "You really put a lot of time and care into this, huh? It shows!"

    show Rosco shocked at waist_up_center
    R "…"

    show Rosco embarrassed at waist_up_center
    R "Thank you…"

    R "Okay, okay, enough fawning about it. Let's get to the controls."

    "You grin at the sight of him, as unable to take a compliment as ever."

    MC "If you say so…"

    show Rosco neutral at waist_up_center
    R "So Pipsqueak has abilities that are easy to learn, okay?"
    R "Let's walk up to that bot in the middle so I can show you them in action."

    "He guides you to maneuver your character up and towards the bot."

    R "Look, press Q."

    #wait for q
    call ability_check("q", "Q")

    show Rosco neutral at waist_up_center
    "When you press it, a wave of smaller Pipsqueaks dive down from above, all assaulting the motionless bot standing in the middle of the lane."

    MC "Woah! Gale made this cute bird terrifying!"

    R "Yep… So that's one… Ah, press W and run around!"

    #wait for w
    call ability_check("w", "W")

    show Rosco neutral at waist_up_center
    "Following Rosco's instructions, you move as you click around, suddenly speeding up as you click."

    MC "So this one's a speed buff?"

    R "Exactly! It helps Pipsqueak get out of bad situations quickly, since they're a squishy unit."

    MC "Got it!"

    R "Now, E!"

    #wait for e
    call ability_check("e", "E")

    show Rosco neutral at waist_up_center
    "Pipsqueak begins to flap their wings, and a giant whirlwind manifests from it, heading straight for the bot. When it hits the other character, it takes a few points of health off and stuns it."

    MC "That's absolutely insane! This little bird can make a tornado!?"

    R "Isn't it crazy? Pipsqueak canonically has to be a wind whisperer or something."

    R "Okay, last ability: press R for the ultimate!"

    #wait for r
    call ability_check("r", "R")

    show Rosco neutral at waist_up_center
    "A huge wall of wind rushes forward, reaching beyond where the tornado had stopped. It's also a lot wider, and the hit points of the enemy go down significantly more."

    MC "That is so awesome."

    R "Yep, Pipsqueak does crazy damage."
    R "Okay, let's go test it out in a proper match!"

    MC "Wh—I haven't gotten the hang of anything yet!"

    show Rosco smug at waist_up_center
    R "Ehh… You'll be fine!"

    "Without missing a beat, Rosco exits the practice mode and puts you in a proper game, one with five AI opponents and four AI teammates."

    MC "This is insane. This is insane!! I got no practice time!"

    R "It's the kind of game that you learn from playing."

    MC "!?"

    MC "YOU'RE JUST SAYING THAT!"

    "Trying to ignore the smugness on Rosco's face, you follow the game's tutorial suggestion and head to the bottom lane, noticing a Dewdrop AI following you."

    MC "There's two of us here?"

    R "That Dewdrop will give you support since your health's at risk."

    MC "Ah, gotcha."

    "You're locked in battle once more players appear, circling around each other and being extra cautious."

    "Once the last bird is thrown, you leave the encounter victorious."

    MC "Holy crap! I did it!"
    #show Rosco laugh
    R "See! It's really a learning game!"

    # END OF SUB-ROUTE, JUMP TO MAIN
    jump mascot_playtest_return

label dewdrop_route:

    MC "I'll go with the Dewdrop. I'm more suited for healers. I like this kind of playstyle!"

    R "Ooh, don't tell Cass but… I think this one is at risk for the most bugs. This'll be good for testing."

    "When you click the Dewdrop, the character shows as selected, and you load up into a proper game in no time."

    MC "Woah. These graphics are insane! Did you do this yourself?"

    show Rosco smug at waist_up_center
    R "Hell yeah! We all planned the design together, but I modelled the actual thing on my own."

    MC "This is so sick… It's a real game!"
    MC "Everything runs so smoothly, and it's got no lag for a demo."
    MC "You really put a lot of time and care into this, huh? It shows!"

    show Rosco shocked at waist_up_center
    R "…"

    show Rosco embarrassed at waist_up_center
    R "Thank you…"

    R "Okay, okay, enough fawning about it. Let's get to the controls."

    "You grin at the sight of him, as unable to take a compliment as ever."

    MC "If you say so…"

    show Rosco neutral at waist_up_center
    R "A-anyway, Dewdrop's abilities are very easy to understand."
    R "Let's walk up to that bot in the middle so I can show you them in action."

    "He guides you to maneuver your character up and towards the bot."

    R "Look, press Q."

    call ability_check("q", "Q")
    show Rosco neutral at waist_up_center
    "A flurry of leaves, all seemingly spawning from the top of Dewdrop's head, propel towards the bot in the middle."

    MC "What on earth? The drop of water can spawn leaves?"

    R "… I'm sure Cass will integrate that into the lore somewhere."

    R "Okay, I'm gonna need a second bot for this bit."

    "Taking control of the keyboard, Rosco presses a few buttons which creates a low-health Pipsqueak next to you."

    MC "Oh, is this a healing thing?"

    R "Yeah, exactly. Click W!"

    call ability_check("w", "W")
    show Rosco neutral at waist_up_center
    "Suddenly, Dewdrop lunges sideways towards Pipsqueak, and Pipsqueak is immediately smothered in Dewdrop's gooey casing."

    MC "What the hell?! Did I just attach on to Pipsqueak?"

    R "Yep! I'm… actually surprised that it didn't break the game. I thought the modelling for that was gonna crash."

    R "Anyway, yeah, this grants an ally a shield and healing! But on the flip side, you're stuck on them."

    MC "Can I… do anything?"

    R "…"

    "Dewdrop slides off Pipsqueak, returning to their original position."

    R "Why don't you go ahead and press—"

    MC "Aren't you gonna answer my question!?"

    R "Press E!"

    call ability_check("e", "E")
    show Rosco neutral at waist_up_center
    "Dewdrop turns to Pipsqueak, and a squirt of water hits Pipsqueak square in the beak. Despite the weird display, Pipsqueak's health rises again."

    MC "Did I just… piss on them?"

    R "Well, I don't know if that's what Cass was trying to make it seem like, but you basically just squirted some purified water onto Pipsqueak and healed them."

    MC "This is… very Cass of him."

    R "… I know."

    R "You can also heal yourself, and the animation for that is less… graphic."

    "You press E again and Dewdrop jumps, their watery form rebuilding itself and swelling, before dropping back down onto the ground."

    MC "That was so much cooler."

    R "Right?!"

    R "Okay, last ability: R for the ultimate!"

    call ability_check("r", "R")
    show Rosco neutral at waist_up_center
    "Dewdrop turns again and lunges to surround Pipsqueak, and the healing skyrockets."

    MC "Wait, isn't this just a better version of the W ability?"

    R "Hold on, hold on!"

    "Rosco clicks something to draw Pipsqueak closer to the opponent bot. Dewdrop suddenly starts spitting leaves everywhere, damaging the enemy."

    MC "Oh! So it's the W, but I can actually do things!"

    R "Exactly!"

    MC "This is a perfect healer-support. I like it!"

    R "Okay, let's go test it out in a proper match!"

    MC "Wh—I haven't gotten the hang of anything yet!"

    show Rosco smug at waist_up_center
    R "Ehh… You'll be fine!"

    "Without missing a beat, Rosco exits the practice mode and puts you in a proper game, one with five AI opponents and four AI teammates."

    MC "This is insane. This is insane!! I got no practice time!"

    R "It's the kind of game that you learn from playing."

    MC "!?"

    MC "YOU'RE JUST SAYING THAT!"

    "Trying to ignore the smugness on Rosco's face, you follow the game's tutorial suggestion and head to the bottom lane, noticing a Pipsqueak AI following you."

    MC "There's two of us here? It's just like training."

    R "Since you're a support, it's better for you to go with the ADC and keep them from instantly dying."

    R "Especially Pipsqueak, since that health… leaves things to be desired."

    MC "Ah, gotcha."

    "You're locked in battle once more players appear, circling around each other and being extra cautious."

    "Once the last bird is thrown, you leave the encounter victorious."

    MC "Holy crap! I did it! I kept Pipsqueak alive!"

    R "See! It's really a learning game!"

    # END OF SUB-ROUTE, JUMP TO MAIN
    jump mascot_playtest_return

label lunarist_route:
    MC "I'll go with Lunarist. I'm a sucker for some mage action."

    R "I had a feeling you'd pick this one… Luci had this one put out a lot of effects, so I'm looking forward to seeing how it holds up!"

    "When you click the Lunarist, the character shows as selected. You load up into a proper game in no time."

    MC "Woah. These graphics are insane! Did you do this yourself?"

    show Rosco smug at waist_up_center
    R "Hell yeah! We all planned the design together, but I modelled the actual thing on my own."

    MC "This is so sick… It's a real game!"
    MC "Everything runs so smoothly, and it's got no lag for a demo."
    MC "You really put a lot of time and care into this, huh? It shows!"

    show Rosco shocked at waist_up_center
    R "…"

    show Rosco embarrassed at waist_up_center
    R "Thank you…"

    R "Okay, okay, enough fawning about it. Let's get to the controls."

    "You grin at the sight of him, as unable to take a compliment as ever."

    MC "If you say so…"

    show Rosco neutral at waist_up_center
    R "Okay, Lunarist's abilities are all related to crowd control in some way."
    R "Let's walk up to that bot in the middle so I can show you them in action."

    "He guides you to maneuver your character up and towards the bot."

    R "Let's start with pressing Q."

    call ability_check("q", "Q")

    show Rosco neutral at waist_up_center
    "Lunarist opens their cloak and a music note floats out. It gravitates towards the bot and absorbs into it forcefully, knocking off some health."

    MC "Ooh, so Lunarist has music as the character motif?"

    R "Yeah! Luci had a lot of fun making it, and he plans to add some of his own melodies in when it's done."

    R "Now press W!"

    call ability_check("w", "W")

    show Rosco neutral at waist_up_center
    "A barrage of music notes fly out of Lunarist's cloak, and they encircle the bot as though performing a ritual at its feet. The bot tries to escape, but the music notes bar it from leaving the circle."

    MC "Eh? So I just trapped them in a circle?"

    R "Mhm! That way, they won't be able to move out of it. It's really good for team fights!"

    R "Okay, E now!"

    call ability_check("e", "E")

    show Rosco neutral at waist_up_center
    "A music staff with notes on it flows out this time, wrapping the bot in a layer of music. The staff circles the bot and it starts walking towards you, as if trapped under a spell."

    MC "Wait, I can just force it to walk towards me?!"

    MC "That's so cool… If it happens to a real player, does the same thing happen?"

    R "Yeah! They won't be able to avoid the movement when you cast it, and it'll pull them in the same way."

    MC "That's frustrating for anyone playing against Lunarist."

    R "Can confirm… Luci made sure of that when crafting this skillset."

    R "Okay, last ability: press R for the ultimate!"

    call ability_check("r", "R")

    show Rosco neutral at waist_up_center
    "Suddenly, a blast of music floods out of Lunarist as they float high into the air. The bot, unfortunately in radius, is stunned by the time Lunarist floats back down and is nearly dead."

    MC "That almost killed the bot! This is broken!"

    R "Well, there's also a difference in levels, so it's not actually that bad… But, yeah."

    R "Lunarist's damage is crazy, but you have to be mindful of the mana. You can't go around casting all these spells all at once."

    MC "Is that the bar under my health?"

    R "Mhm! Be careful not to run out, or you'll be totally defenseless."

    R "Okay, let's go test it out in a proper match!"

    MC "Wh—I haven't gotten the hang of anything yet!"

    show Rosco smug at waist_up_center
    R "Ehh… You'll be fine!"

    "Without missing a beat, Rosco exits the practice mode and puts you in a proper game, one with five AI opponents and four AI teammates."

    MC "This is insane. This is insane!! I got no practice time!"

    R "It's the kind of game that you learn from playing."

    MC "!?"

    MC "YOU'RE JUST SAYING THAT!"

    "Trying to ignore the smugness on Rosco's face, you follow the game's tutorial suggestion and head to the middle lane."

    MC "Wait, there's just another Lunarist here! Is it a one-on-one duel?"

    R "Yep, unless the jungling Roscal comes and helps either side."

    MC "Got it…"

    "You're locked in battle once the enemy Lunarist plays the first skill, and you click the buttons in whichever order seems fit to combo."

    "Once the last note is thrown, you leave the encounter victorious."

    MC "Holy crap! I did it!"

    R "See! It's really a learning game!"

    #End of sub-route
    jump mascot_playtest_return

label route_netherling:

    MC "I'll go with Netherling. The more health, the less likely it is for me to die, right?"

    R "… Not exactly, but I think that's what Zanny had in mind too. Great minds think alike, I guess?"

    "When you click the Netherling, the character shows as selected. You load up into a proper game in no time."

    MC "Woah. These graphics are insane! Did you do this yourself?"

    show Rosco smug at waist_up_center
    R "Hell yeah! We all planned the design together, but I modelled the actual thing on my own."

    MC "This is so sick… It's a real game!"
    MC "Everything runs so smoothly, and its got no lag for a demo."
    MC "You really put a lot of time and care into this, huh? It shows!"

    show Rosco shocked at waist_up_center
    R "…"

    show Rosco embarrassed at waist_up_center
    R "Thank you…"

    R "Okay, okay, enough fawning about it. Let's get to the controls."

    "You grin at the sight of him, as unable to take a compliment as ever."

    MC "If you say so…"

    show Rosco neutral at waist_up_center
    R "Okay, Netherling's skills aren't too hard to wrap your head around."
    R "Let's walk up to that bot in the middle so I can show you them in action."

    "He guides you to maneuver your character up and towards the bot."

    R "Here, press Q."

    call ability_check("q", "Q")

    show Rosco neutral at waist_up_center
    "Netherling takes a half step back before jabbing forward with its pointy tail, slashing through the ribs of the bot."

    MC "Woah, this one's a fighter! That tail looks really dangerous…"

    R "Zanny definitely made this one quite physical, and they have the most normal skillset in my opinion."

    R "This one's a bit different, though—hit W."

    call ability_check("w", "W")

    show Rosco neutral at waist_up_center
    "Nothing seems to happen other than a green aura hovering over Netherling."

    "Rosco maneuvers the bot to hit you, and you see it happen. The attack doesn't affect your health negatively—it actually goes up."

    MC "What?! Did I just absorb the attack?"

    R "Yep, any attacks while you're in this state will convert to health instead."

    R "Okay, wait, move back a bit… then E!"

    call ability_check("e", "E")

    show Rosco neutral at waist_up_center
    "Netherling uses their wing to dash in, ramming into the bot with their horns while inducing a slight knockback effect."

    "The bot is dazed, stunned in place. Netherling stands upright again as if nothing happened."

    MC "That is badass."

    R "Right! I know that if that happened to me mid-game, I'd flip my shit… It's such an annoying attack, especially in teamfights."

    R "Okay, last ability: press R for the ultimate!"

    call ability_check("r", "R")

    show Rosco neutral at waist_up_center
    "Suddenly, Netherling pounces onto the enemy, absorbing them into their jelly-like being. Even encased in the Netherling, the enemy's health ticks down by the second."

    "A few moments later, Netherling spits the enemy out, leaving them with half the HP they had when they went in."

    MC "That's… That's insane?! What the hell?!"

    R "It's probably the most annoying ability of all, since the player can't do anything while inside Netherling."

    MC "This is broken!"

    R "Don't worry, there are a few counters to this, like Dewdrop's healing effects."

    R "It's not too broken yet, since the damage isn't substantial—at least compared to some of the other characters."

    R "Okay, let's go test it out in a proper match!"

    MC "Wh—I haven't gotten the hang of anything yet!"

    show Rosco smug at waist_up_center
    R "Ehh… You'll be fine!"

    "Without missing a beat, Rosco exits the practice mode and puts you in a proper game, one with five AI opponents and four AI teammates."

    MC "This is insane. This is insane!!  I got no practice time!"

    R "It's the kind of game that you learn from playing."

    MC "!?"

    MC "YOU'RE JUST SAYING THAT!"

    "Trying to ignore the smugness on Rosco's face, you follow the game's tutorial suggestion and head to the top lane."

    MC "Wait, there's just another Netherling here! Is it a one-on-one duel?"

    R "Yep, unless the jungling Roscal comes and helps either side."

    MC "Got it…"

    "You're locked in battle once the enemy Netherling plays the first skill, and you click the buttons in whichever order seems fit to combo."

    "Once the last punch is thrown, you leave the encounter victorious."

    MC "Holy crap! I did it!"

    R "See! It's really a learning game!"

    #end of sub-route
    jump mascot_playtest_return

label roscal_route:

    MC "I'll go with Roscal. I wanna see just how broken you made your own character…"

    show Rosco shocked at waist_up_center
    R "What!? What do you mean!? I'm a fair man! I'd never do that!"

    show Rosco laugh at waist_up_center
    MC "Mhm…"

    "When you click the Roscal, the character shows as selected. You load up into a proper game in no time."

    MC "Woah. These graphics are insane! Did you do this yourself?"

    show Rosco smug at waist_up_center
    R "Hell yeah! We all planned the design together, but I modelled the actual thing on my own."

    MC "This is so sick… It's a real game!"
    MC "Everything runs so smoothly, and it's got no lag for a demo."
    MC "You really put a lot of time and care into this, huh? It shows!"

    show Rosco shocked at waist_up_center
    R "…"

    show Rosco embarrassed at waist_up_center
    R "Thank you…"

    R "Okay, okay, enough fawning about it! Let's get to the controls."

    "You grin at the sight of him, as unable to take a compliment as ever."

    MC "If you say so…"

    show Rosco neutral at waist_up_center
    R "Roscal’s abilities are actually a little difficult, but it shouldn’t be too hard."

    "He watches you click around on the practice map, letting you get used to the movement before continuing."

    R "Okay, go into the forest there."

    "You follow his directions, ignoring the pathways and going into an area that was filled with bushes. At some point, you come across a group of foxes."

    R "Now, press Q."

    call ability_check("q", "Q")

    show Rosco neutral at waist_up_center
    "Once you click Q, your character leaps straight towards the foxes, biting at one of them."

    MC "Oh shoot—Oh lord—Rosco, they're attacking me—"

    show Rosco laugh at waist_up_center
    R "Chill! You won't die from that. Click W."

    call ability_check("w", "W")

    show Rosco neutral at waist_up_center
    "The Roscal sticks its sewing needle into the ground, creating a ring of pink around it."

    MC "Woah, I'm not taking damage anymore?"

    show Rosco neutral at waist_up_center
    R "Yup! It's like a shield. Now try E."

    call ability_check("e", "E")

    show Rosco neutral at waist_up_center
    "The safety pin in Roscal's ear flicks out, flying around and hitting the foxes surrounding you before flying back into place."

    R "A boomerang. Pretty cool, huh? When you're around other players, it'll hit every enemy character before coming back to you."

    MC "… And this isn't OP because…?"

    "He ignores your comment, continuing his explanation."

    R "And lastly, click R! This is your ult."

    call ability_check("r", "R")

    show Rosco neutral at waist_up_center
    MC "Ohemgee. I'm so big now!"

    "You watch Roscal smile on your screen, towering over the foxes."

    R "You also heal and gain attack damage. Notice your needle is bigger now? Even your basic attack will do decent damage."

    "You click around the map, attacking the different creatures you come across in the bushes, growing accustomed to the different moves."

    MC "How'd you come up with all of this anyways?"

    R "Well, the game actually has a lot of lore behind it. You know, world building and all of that."

    MC "So… are you going to explain any of it?"

    R "Explaining the whole thing will take a lot of time… but Roscal actually comes from a lab. They were created by a scientist that ended up setting them free since they developed a full consciousness and a soul."

    MC "The scientist set them free? Isn't that a successful experiment?"

    R "Yeah, but he feels as if it's inhumane to keep them contained like an experiment."

    MC "Aww, the scientist sounds really sweet."

    R "Well, to be fair, he also has a lot of other experiments that he keeps. They'll be added as characters later on."

    MC "You have more characters planned already?"

    R "Yup. Slime, Worg, Gargoyle, Chimera, Hydra, and Minotaur."

    R "There was supposed to be one more called Mimic, but the others vetoed it."

    MC "Why?"

    R "… It was too broken."

    MC "Are you going to tell me how?"

    R "Nah."

    R "Okay, let's go test it out in a proper match!"

    MC "Wh—I haven't gotten the hang of anything yet!"

    show Rosco smug at waist_up_center
    R "Ehh… You'll be fine!"

    "Without missing a beat, Rosco exits the practice mode and puts you in a proper game, one with five AI opponents and four AI teammates."

    MC "This is insane. This is insane!!  I got no practice time!"

    R "It's the kind of game that you learn from playing."

    MC "!?"

    MC "YOU'RE JUST SAYING THAT!"

    "Trying to ignore the smugness on Rosco's face, you follow the game's tutorial suggestion and head to the little fox creatures once more."

    MC "Wait, why are there two mascots in the top lane?"

    R "Because we're going against bots. They won't have a real roamer, so you're technically safe!"

    MC "So I just keep killing these creatures?"

    "You move around the map and get jumpscared by a giant wolf spider. You click on it without thinking, triggering a fight."

    MC "WHAT THE HECK DO YOU MEAN SAFE? THIS ISN'T SAFE AT ALL!"

    R "Chill, chill! Just use your skills!"

    "You try to do as he said, torn between running away and trying to do damage."

    MC "Oh, it started walking away…"

    R "Then that means you took too long. You can try attacking it again later. Look, just go to the middle and kill the bot there. The character has low HP."

    MC "Is that why it's a roamer? Literally roaming around the map?"

    R "Yep. Nice and simple."

    "You follow his instructions, approaching the character at low health."

    MC "Uuuh… I'm supposed to kill him, right?"

    "You click E before he responds. The safety pin flies out, and you watch the health bar drop even lower. You're trying to decide how to attack next when Rosco speaks up."

    R "Q!"

    call ability_check("q", "Q")

    "You listen to him without thinking, nearly screeching as Roscal dashes in to bite the opposing Lunarist."

    MC "It's going to kill me—Woah! I actually got a kill!"

    "Your panic subsides as you realize that the fight was already won. You walk back into the forest, a bit stunned."

    R "See! It's not too hard to get the hang of, right?"

    #End of sub-route
    jump mascot_playtest_return