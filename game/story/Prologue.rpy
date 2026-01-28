
# Start of prologue
label prologue:

    $ quick_menu = False
    scene black with fade
    show text "{color=#FFFFFF}{size=50}Prologue{/size}{/color}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve

    scene black with fade
    play music "audio/music/G1 - Cheerful (1).wav" fadein 1.0 loop
    scene bg clubroom
    with fade
    $ quick_menu = True

    show Gale angry at waist_up_left2 with dissolve
    show Gale angry at waist_up_left2, singlejump
    G "ARE YOU KIDDING ME-"
    hide Gale with dissolve

    show Lucien confused at waist_up_right4 with dissolve
    L "What are you talking about?"
    hide Lucien with dissolve

    "Laughter fills the room as chaos ensues. Gale curses as his turn in Ichi is skipped yet again."

    show Zander neutral at waist_up_left3 with dissolve
    Z "The cards just weren’t in your favor, darling."

    show Rosco neutral jacket at waist_up_right with dissolve
    R "Nah, skill issue."
    hide Rosco
    hide Zander
    with dissolve

    show Cassian hopeful at waist_up_center with dissolve
    show Cassian hopeful at waist_up_center, singlejump
    C "Ichi!!"

    show Cassian laughing at waist_up_center, singlejump 
    "You watch as Cass smiles, taking advantage of everyone’s confusion and proudly waving his final card in the air."
    hide Cassian with dissolve

    MC "Someone has to have a plus five, right?"

    show Rosco smug jacket at waist_up_center with dissolve
    R "Not me. Ichi."

    "You stare incredulously at Rosco next to you, rolling your eyes at the way he smirks in response."
    hide Rosco with dissolve

    show Gale angry at waist_up_left2 with dissolve
    show Gale angry at waist_up_left2, restless
    G "I swear this is RIGGED."

    show Lucien laughing at waist_up_right4 with dissolve
    L "Maybe you’re just bad."

    show Gale angry at waist_up_left2, singlejump
    G "You have more cards than me!"

    show Lucien laughing at waist_up_right4
    L "I dunno, man - your hand is pretty big."

    hide Gale
    hide Lucien
    with dissolve
    "A few of the boys snicker quietly."

    # Choice section

    menu:
        "Roll your eyes.": 
            $ choice = "eye_roll"
            MC "Yeah, right..."

        "Join in the laughter.":
            $ choice = "join_laugh"
            MC "Haha, okay, I’ll admit that was funny."

    # [Choice Ends]

    show Zander thinking at waist_up_right3 with dissolve
    Z "How about… "
    show Zander neutral
    extend "this?"

    show Zander smug
    "You watch Zanny lean forward and place down a skip card, grinning as Luci complains."

    show Gale laugh at waist_up_left2 with dissolve
    G "Zanny, I could KISS you right now!"

    show Gale neutral at waist_up_left2
    "Gale slams down a plus five, pointing at Cass."

    show Gale laugh at waist_up_left2, singlejump
    G "Blue!"

    show Zander shocked 
    "Everyone turns to look at Cass and watch as his lips purse in annoyance. Gale and Zanny cheer as he reaches forward to collect his cards."

    "You look down at your own cards."

    "…No blue."

    "You reach forward to draw your own card, making Rosco snort in laughter."

    "You look at your new card. A blue plus three."

    show Gale neutral
    show Zander neutral
    MC "You won’t be laughing for long!"

    show Gale laugh 
    hide Zander with dissolve
    "You place down your card and Gale’s cheering gets louder."

    show Gale at waist_up_left2, singlejump
    show Rosco shocked jacket at waist_up_right with dissolve
    G "Get his ass!"

    MC "Get top-decked, goofy."

    show Rosco annoyed jacket
    hide Gale with dissolve
    "Rosco curses and snatches up his cards, and everyone’s officially back in the game."

    show Lucien laughing at waist_up_left4 with dissolve
    L "Wow, you really talked big and got punished, Rosco."

    hide Rosco with dissolve
    show Zander neutral at waist_up_right3 with dissolve
    show Lucien laughing
    Z "Don’t you get cocky, now~"

    "Zanny places down yet another skip card, this time in blue."

    show Lucien angry
    L "What the frick!?"

    show Gale laugh at waist_up_center2 with dissolve
    G "Doesn’t feel so good now, does it??"

    show Gale laugh at waist_up_center2, singlejump
    show Zander laughing at waist_up_right3, singlejump


    "Gale and Zanny cackle and reach over the table to high-five."
    hide Gale
    hide Zander
    hide Lucien 
    with dissolve

    "You pass a few rounds in the same manner, everyone getting down to one card before the rest of the group works together to sabotage them."

    "It really is amazing to watch everyone pool together skips and plus cards to fill out hands and force the game to continue."

    show Gale neutral at waist_up_left2 with dissolve
    show Gale neutral at waist_up_left2, singlejump
    G "ICHI!"
    

    show Cassian panic at waist_up_right with dissolve
    C "Luci, PLEASE tell me you have another skip!"

    show Gale angry
    G "Don’t you dare-"

    show Gale shocked
    show Cassian neutral
    MC "Ichi~"

    "You sing out the word, feeling hopeful in your victory."

    show Gale angry at waist_up_left2, restless
    show Cassian laughing
    "Everything is in chaos as Zanny also reaches the final card in his hand. You can barely make out what anyone is saying as they all yell at each other."

    hide Gale
    hide Cassian
    with dissolve
    play sound "audio/sfx/door-knocking.ogg"
    "That’s when you realize you hear a sharp tapping at the door."

    "You thought you were imagining it at first, tilting your head at the sound."

    "You get distracted from the game, lifting your gaze to look at the door."

    show Zander neutral at waist_up_center3 with dissolve
    MC "Did you guys hear that?"

    show Zander confused at waist_up_center3
    Z "Hear what?"

    "He lifts his gaze to follow yours, looking back at the door."

    MC "I could’ve sworn I heard-"

    show Zander shocked
    N "Why is it so noisy?"

    hide Zander with dissolve
    "The familiar muffled voice makes everyone freeze. All of a sudden, everyone is speaking in hushed voices."

    show Cassian neutral at waist_up_left with dissolve
    show Cassian panic at waist_up_left, singlejump 
    C "The screens! Change the computer screens!"
    hide Cassian with dissolve

    show Lucien shocked at waist_up_right4 with dissolve
    L "Put the cards away!"
    hide Lucien with dissolve

    show Gale annoyed at waist_up_left2 with dissolve
    G "We were just getting to the best part!"

    show Rosco shocked jacket at waist_up_right with dissolve
    R "That’s not important right now!"

    hide Gale
    hide Rosco
    with dissolve

    play sound "audio/sfx/door-knocking.ogg"
    N "So… Are you guys going to open the door, or…?"

    show Zander neutral at waist_up_center3 with dissolve
    Z "Coming! Give us a moment~"

    hide Zander with dissolve
    "Zanny sounds so relaxed, even you almost believe there’s nothing wrong."

    "No wonder the boys tease him for yelling in lowercase font."

    MC "Go, go, go-"

    "You shove Rosco towards the PCs, glancing back to make sure that everyone looks like they’re working."

    "Then, with your best innocent smile, you open the door to greet the unamused person standing there."

    MC "Hey Nayu! What brings you to the club room?"

    N "Seriously? Have you guys forgotten?"

    "You glance back into the room, biting back a sound of laughter when you realize everyone looks as confused as you feel."

    "Probably not the best time to laugh when Nayu is giving you his “bruh” face."

    N "The school festival is in two weeks."

    # Choice start
    menu:
        "Of course! The school festival!":
            $ festival_choice = "remembered"
            MC "Of course! The school festival!"

        "What… festival…?":
            $ festival_choice = "forgot"
            MC "What… festival…?"

    if festival_choice == "remembered":
        N "We were making sure every club submitted what booth they’re running. Yours is the only one missing."

        "He pauses, giving you all a sweeping look. You all exchange glances, trying to keep your expressions neutral."

        N "So I came to ask what you guys were planning to do."

        show Zander neutral at waist_up_right3
        show Gale neutral at waist_up_left2
        with dissolve
        Z "Oh dear, I didn’t realize we forgot to submit our booth proposal."

        show Gale shocked
        G "Sorry, Nayu I think I might have accidentally thrown the paper away-"

        hide Zander 
        hide Gale 
        with dissolve
        "Why do they all think lying is the answer? Not that you’re doing any better."

    elif festival_choice == "forgot":
        N "I knew it."

        show Rosco neutral jacket at waist_up_center
        show Lucien neutral at waist_up_right4:
            xoffset 75
        show Cassian neutral at waist_up_left
        with dissolve
        "He glares at all of you."

        N "It’s in two WEEKS."

        show Rosco smug jacket
        R "Relaxxxx, we’ll have something ready in two weeks!"

        "Clearly, this was not the best thing to say. You take a step back as Nayu straightens up, his mouth opening."

        show Rosco neutral jacket 
        N "This festival is supposed to be a time to promote our school and fundraise money for your clubs and the campus."

        N "Please tell me how exactly you plan on having something presentable and profitable within the next two-"

        show Lucien laughing
        L "C’mon! You know us! We work best under pressure!"

        show Cassian neutral at waist_up_left, singlejump
        C "Exactly! We’ve done it before-"

        hide Cassian
        hide Lucien
        hide Rosco
        with dissolve
        N "That’s precisely the problem! Why do you guys do this everyti-"


    # [Choice Ends]
    show Lucien neutral at waist_up_right4 with dissolve:
        xoffset 75
    show Lucien neutral at waist_up_right4, singlejump:
        xoffset 75
    "Noting his temper flaring, Luci hurries over with a bag of gajacori, a snack that you’ve all come to realise works wonders in distracting him."

    hide Lucien with dissolve
    "Despite still glaring at all of you, he doesn’t reject the bag of snacks."

    "He starts munching on the potato sticks, his expression deadpanning."

    N "So? What are you guys going to do?"

    MC "Uhm…"

    "Nayu rolls his eyes, shrugging as he starts walking away."

    N "Whatever. Text me your decision when you have an answer."

    "You all stand still as you watch the door swing shut. After a moment of silence, everyone starts talking at once."

    show Rosco neutral jacket at waist_up_right with dissolve
    show Rosco annoyed jacket at waist_up_right, singlejump 
    R "Why the heck do we have so many school festivals?!"

    show Rosco angry jacket
    "(You don’t. There are only two each year. Spring and fall.)"

    show Gale neutral at waist_up_left2 with dissolve
    show Gale annoyed at waist_up_left2, singlejump
    G "Because the school HAAATES us!"

    hide Gale
    hide Rosco
    with dissolve

    show Cassian shocked at waist_up_left
    show Zander serious at waist_up_right3
    with dissolve

    show Cassian panic at waist_up_left, restless
    C "We’re so screwed. They’re going to disband our club-"

    show Zander vSerious pose2 at waist_up_right3
    Z "Maybe if we take out the student council president-"

    hide Cassian
    hide Zander
    with dissolve

    show Lucien confused at waist_up_left4
    show Rosco shocked jacket at waist_up_right 
    with dissolve

    show Lucien shocked at waist_up_left4, singlejump
    L "No, no we can’t just get rid of a guy!"

    show Rosco neutral jacket
    R "Okay, but what if-"

    hide Rosco
    hide Lucien
    with dissolve
    # [Choice Start]

    menu:
        "Panic with them.":
            $ player_choice = "panic"
        "Take the lead.":
            $ player_choice = "lead"

    if player_choice == "panic":

        show Lucien neutral at waist_up_center with dissolve
        L "Okay! Okay! Everyone calm— "
        show Lucien angry at waist_up_center, singlejump
        extend "EVERYONE SHUT UP!"

        "The overpowering shout quickly has everyone zipping their mouths, all eyes turning to Luci. He fixes a glare at everyone one by one, before sitting back down slowly."

        show Lucien neutral
        L "Okay, let’s talk about this calmly. First of all, what did Nayu say we have to do?"

        hide Lucien with dissolve
        "There’s a collective shift of gazes as people make eye contact with each other in the room."

        show Cassian thinking at waist_up_right
        show Lucien neutral at waist_up_left4
        with dissolve
        C "Uh. Preparations for our club’s stand for the festival that’s coming up."

        hide Cassian with dissolve
        L "Uh huh. And when is that?"

        show Zander thinking pose2 at waist_up_right3 with dissolve
        Z "In… two weeks?"

        MC "We… haven’t started anything yet."

        show Rosco shocked jacket at waist_up_center with dissolve 
        show Zander neutral pose2 
        R "Oh, we’re screwed."

        L "No we’re not. We just have to talk about it now then."

    elif player_choice == "lead":

        show bg clubroom at screenshake
        MC "We are NOT getting rid of someone!"

        show Rosco shocked jacket at waist_up_left
        show Zander shocked at waist_up_right3
        with dissolve 

        "They all stop at your sudden outburst, turning their gazes towards you."

        show Rosco neutral jacket
        show Zander neutral
        "You clear your throat, straightening up under their gazes."

        MC "We’ve done it before, we can do it again. We’re setting up a stand for the spring festival, right?"

        show Rosco concerned jacket
        R "Uh-huh."

        MC "And it’s in two weeks."

        show Zander thinking pose2
        Z "Correct."

        MC "Okay. It just means we have to speedrun this. It’s like a limited time quest that we ignored until 24 hours before it ends. We got this."

    # [Choice Ends]

    scene bg clubroom with dissolve
    "Now that logic had entered the chat, everyone was starting to nod along. Their suggestions became much more reasonable as the panic subsided."

    show Gale confused pose2 at waist_up_left2 with dissolve
    G "I mean, it’s just a stand. Surely we won’t need that much preparation."

    show Cassian thinking at waist_up_center with dissolve 
    C "That depends on what kind of stand we’re doing, I guess."

    show Lucien neutral at waist_up_right4 with dissolve:
        xoffset 75
    show Cassian neutral 
    L "A simple food stand is fine— nothing too crazy."

    hide Gale with dissolve

    show Zander at waist_up_left3 zorder 1.0:
        xoffset -100
    show Cassian neutral zorder 2.0
    with dissolve

    Z "That could work."

    show Cassian thinking at waist_up_center
    C "How would it relate to our club though?"

    show Cassian neutral
    MC "Oh! There’s that thing Rosco was making."

    hide Lucien with dissolve
    show Rosco confused jacket at waist_up_right with dissolve

    "Rosco blinks at you cluelessly."

    MC "The game?"
    
    show Rosco neutral jacket at waist_up_right, singlejump
    R "OHHH! B.I.T.E Protocol?"

    show Zander thinking pose2
    Z "Oh, you’re saying we should showcase that somehow?"

    hide Rosco
    hide Cassian
    with dissolve


    show Gale neutral at waist_up_center2 zorder 2.0
    show Lucien neutral at waist_up_right4:
        xoffset 75
    with dissolve

    MC "Maybe just the development and some of the beta gameplay?"

    show Zander neutral
    show Gale laugh
    G "That’s good!"

    show Lucien neutral smile
    L "Okay. We have that sorted out. Now, what about the food?"

    show Zander thinking
    show Gale neutral
    Z "Should it be a dessert? It would be easy to eat while parsing through the other stands."

    hide Gale with dissolve
    show Rosco confused jacket at waist_up_center zorder 2.0 with dissolve
    show Zander neutral
    R "Taiyaki? Or uhhh… Shaved ice, skewers, dango…"

    hide Rosco with dissolve
    "Rosco continues to spit out various names of desserts. Amidst his muttering, you can hear something about him ordering food for later."

    show Gale neutral pose2 at waist_up_center2 zorder 2.0 with dissolve
    G "…We can do a hotdog stand?"

    "There’s a few sounds of hesitation coming from those in the room."

    show Lucien neutral
    L "It should be something more flexible. So we can offer more variety."

    hide Gale with dissolve
    show Cassian at waist_up_center zorder 2.0 with dissolve
    C "Maybe we can do crepes?"

    show Zander excited
    Z "Ooh, that sounds nice."

    "The rest fill in with agreeable responses too."

    show Zander neutral
    "In the background, you see Gale repeating the word 'crepe' to himself in the same way Cass pronounced it— but harsher."

    show Cassian at waist_up_center, singlejump
    "You bite back a laugh when you see Cass smack Gale on the shoulder."

    show Lucien neutral smile
    L "That works. I can think of a few recipes already."

    Z "Then should we leave the cooking to you, our resident chef?"

    MC "We’re not leaving it to you, that’s for sure."

    show Zander angry
    hide Cassian with dissolve
    show Rosco neutral jacket at waist_up_center zorder 2.0 with dissolve
    "You turn to address Rosco, ignoring the look of protest on Zanny’s face. You wish you could forget about the protein powder cake sitting in the clubroom’s fridge right now."

    show Zander neutral 
    show Rosco shocked jacket
    MC "Rosco! You have a nice style. Wanna do outfits?"

    show Rosco neutral jacket at waist_up_center, singlejump
    R "Hell yeah. You trust me with them?"

    hide Lucien with dissolve
    show Cassian neutral at waist_up_right with dissolve
    C "Just don’t put us in like, cat-maid outfits or something."

    show Zander serious
    "You see Zanny visibly deflate in your peripheral vision."

    hide Rosco with dissolve
    show Gale at waist_up_center2 zorder 2.0 with dissolve
    G "And, in that case, I can help with the decorations!"

    show Zander neutral 
    Z "I’ll help buy the ingredients."

    hide Gale with dissolve
    show Cassian thinking at waist_up_right with dissolve
    C "Is there anything else that’s needed?"

    show Lucien neutral smile at waist_up_center4 zorder 2.0 with dissolve
    L "Can you buy the equipment? We might need some for the stand."

    show Cassian neutral 
    C "Sure! I’ll do that."

    scene bg clubroom with dissolve
    "You look around as each of the boys chat about their respective tasks. It doesn’t seem like there’s anything else you can be in charge of."

    "After mulling it over for a bit, you raise your hand to state your decision."

    MC "Then, I’ll help wherever I can!"

    "Cheering fills the room as you all hype each other up for the festival. There are satisfied looks on everyone’s faces as it seems that the initial planning of the stand is drawing to a close."

    show Gale confused at waist_up_left2 with dissolve
    G "Ah, but…"

    "He addresses you with an undertone of worry in his voice."

    G "We’ll most likely be working on these separately then. Wouldn’t you be dead on your feet running around trying to help all of us?"

    "That’s true. But you still want to help where you can."

    show Gale neutral
    show Rosco neutral jacket at waist_up_center with dissolve
    R "Don’t overwork yourself, goofy."

    "He gives you a knowing look, making you smile a bit sheepishly."

    show Lucien neutral smile at waist_up_right4 with dissolve:
        xoffset 75
    L "We can work on our own, and [player_subject] can come join us on different days throughout the next couple weeks."

    hide Rosco with dissolve
    show Cassian neutral at waist_up_center with dissolve
    C "Ah, yeah. We still have some time left before the festival anyway."
    
    hide Gale with dissolve
    show Zander neutral at waist_up_left3 zorder 1.0:
        xoffset -100
    show Cassian neutral at waist_up_center zorder 2.0
    with dissolve

    Z "In that case…"

    scene bg clubroom with dissolve
    #think about showing all sprites?
    "They all turn to look at you."

    show Zander at waist_up_center3 with dissolve
    Z "Who do you want to help first?"
    hide Zander with dissolve

    # [Route choices start]

    # Selecting Route
    jump choose_route   
