
# Start of prologue
label prologue:

    scene bg clubroom
    with fade

    show Gale at waist_up_center, shake2
    G "ARE YOU KIDDING ME-"
    hide Gale

    show Lucien at waist_up_center
    L "What are you talking about?"
    hide Lucien

    "Laughter fills the room as chaos ensues. Gale curses as his turn in Ichi is skipped yet again."

    show Zander at waist_up_center
    Z "The cards just weren’t in your favor, darling."
    hide Zander

    show Rosco at waist_up_center
    R "Nah, skill issue."
    hide Rosco

    show Cassian at waist_up_center, shake
    C "Ichi!!"

    "You watch as Cass smiles, taking advantage of everyone’s confusion and proudly waving his final card in the air."
    hide Cassian

    MC "Someone has to have a plus five, right?"

    show Rosco at waist_up_center
    R "Not me. Ichi."

    "You stare incredulously at Rosco next to you, rolling your eyes at the way he smirks in response."
    hide Rosco

    show Gale at waist_up_left, shake2
    G "I swear this is RIGGED."
    hide Gale

    show Lucien at waist_up_right
    L "Maybe you’re just bad."
    hide Lucien

    show Gale at waist_up_left
    G "You have more cards than me!"
    hide Gale

    show Lucien at waist_up_right
    L "I dunno, man - your hand is pretty big."
    hide Lucien

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

    show Zander at waist_up_center
    Z "How about…this?"

    "You watch Zanny lean forward and place down a skip card, grinning as Luci complains."
    hide Zander

    show Gale at waist_up_center
    G "Zanny, I could KISS you right now!"

    "Gale slams down a plus five, pointing at Cass."

    show Gale at waist_up_center, shake2
    G "Blue!"
    hide Gale

    "Everyone turns to look at Cass and watch as his lips purse in annoyance. Gale and Zanny cheer as he reaches forward to collect his cards."

    "You look down at your own cards."

    "…No blue."

    "You reach forward to draw your own card, making Rosco snort in laughter."

    "You look at your new card. A blue plus three."

    MC "You won’t be laughing for long!"

    "You place down your card and Gale’s cheering gets louder."

    show Gale at waist_up_center, shake2
    G "Get his ass!"
    hide Gale

    MC "Get top-decked, goofy."

    "Rosco curses and snatches up his cards, and everyone’s officially back in the game."

    show Lucien at waist_up_center
    L "Wow, you really talked big and got punished, Rosco."
    hide Lucien

    show Zander at waist_up_center
    Z "Don’t you get cocky, now~"

    "Zanny places down yet another skip card, this time in blue."
    hide Zander

    show Lucien at waist_up_center
    L "What the frick!?"
    hide Lucien

    show Gale at waist_up_left
    G "Doesn’t feel so good now, does it??"

    show Zander at waist_up_right
    "Gale and Zanny cackle and reach over the table to high-five."
    hide Gale
    hide Zander

    "You pass a few rounds in the same manner, everyone getting down to one card before the rest of the group works together to sabotage them."

    "It really is amazing to watch everyone pool together skips and plus cards to fill out hands and force the game to continue."

    show Gale at waist_up_center, shake2
    G "ICHI!"
    hide Gale

    show Cassian at waist_up_center
    C "Luci, PLEASE tell me you have another skip!"
    hide Cassian

    show Gale at waist_up_center
    G "Don’t you dare-"
    hide Gale

    MC "Ichi~"

    "You sing out the word, feeling hopeful in your victory."

    "Everything is in chaos as Zanny also reaches the final card in his hand. You can barely make out what anyone is saying as they all yell at each other."

    "That’s when you realize you hear a sharp tapping at the door."

    "You thought you were imagining it at first, tilting your head at the sound."

    "You get distracted from the game, lifting your gaze to look at the door."

    MC "Did you guys hear that?"

    show Zander at waist_up_center
    Z "Hear what?"

    "He lifts his gaze to follow yours, looking back at the door."
    hide Zander

    MC "I could’ve sworn I heard-"

    N "Why is it so noisy?"

    "The familiar muffled voice makes everyone freeze. All of a sudden, everyone is speaking in hushed voices."

    show Cassian at waist_up_center, shake
    C "The screens! Change the computer screens!"
    hide Cassian

    show Lucien at waist_up_center
    L "Put the cards away!"
    hide Lucien

    show Gale at waist_up_center
    G "We were just getting to the best part!"
    hide Gale

    show Rosco at waist_up_center
    R "That’s not important right now!"
    hide Rosco

    N "So… Are you guys going to open the door, or…?"

    show Zander at waist_up_center
    Z "Coming! Give us a moment~"

    "Zanny sounds so relaxed, even you almost believe there’s nothing wrong."
    hide Zander

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

        Z "Oh dear, I didn’t realize we forgot to submit our booth proposal."

        G "Sorry, Nayu I think I might have accidentally thrown the paper away-"

        "Why do they all think lying is the answer? Not that you’re doing any better."

    elif festival_choice == "forgot":
        N "I knew it."

        "He glares at all of you."

        N "It’s in two WEEKS."

        R "Relaxxxx, we’ll have something ready in two weeks!"

        "Clearly, this was not the best thing to say. You take a step back as Nayu straightens up, his mouth opening."

        N "This festival is supposed to be a time to promote our school and fundraise money for your clubs and the campus."

        N "Please tell me how exactly you plan on having something presentable and profitable within the next two-"

        L "C’mon! You know us! We work best under pressure!"

        C "Exactly! We’ve done it before-"

        N "That’s precisely the problem! Why do you guys do this everyti-"

    # [Choice Ends]

    "Noting his temper flaring, Luci hurries over with a bag of gajacori, a snack that you’ve all come to realise works wonders in distracting him."

    "Despite still glaring at all of you, he doesn’t reject the bag of snacks."

    "He starts munching on the potato sticks, his expression deadpanning."

    N "So? What are you guys going to do?"

    MC "Uhm…"

    "Nayu rolls his eyes, shrugging as he starts walking away."

    N "Whatever. Text me your decision when you have an answer."

    "You all stand still as you watch the door swing shut. After a moment of silence, everyone starts talking at once."

    show Rosco at waist_up_center
    R "Why the heck do we have so many school festivals?!"

    "(You don’t. There are only two each year. Spring and fall.)"
    hide Rosco

    show Gale at waist_up_center
    G "Because the school HAAATES us!"
    hide Gale

    show Cassian at waist_up_center
    C "We’re so screwed. They’re going to disband our club-"
    hide Cassian

    show Zander at waist_up_center
    Z "Maybe if we take out the student council president-"
    hide Zander

    show Lucien at waist_up_center
    L "No, no we can’t just get rid of a guy!"
    hide Lucien

    show Rosco at waist_up_center
    R "Okay, but what if-"
    hide Rosco

    # [Choice Start]

    menu:
        "Panic with them.":
            $ player_choice = "panic"
        "Take the lead.":
            $ player_choice = "lead"

    if player_choice == "panic":

        show Lucien at waist_up_left, shake
        L "Okay! Okay! Everyone calm— EVERYONE SHUT UP!"

        "The overpowering shout quickly has everyone zipping their mouths, all eyes turning to Luci. He fixes a glare at everyone one by one, before sitting back down slowly."

        L "Okay, let’s talk about this calmly. First of all, what did Nayu say we have to do?"
        hide Lucien

        "There’s a collective shift of gazes as people make eye contact with each other in the room."

        show Cassian at waist_up_right
        C "Uh. Preparations for our club’s stand for the festival that’s coming up."
        hide Cassian

        show Lucien at waist_up_left
        L "Uh huh. And when is that?"
        hide Lucien

        show Zander at waist_up_center
        Z "In… two weeks?"
        hide Zander

        MC "We… haven’t started anything yet."

        show Rosco at waist_up_center
        R "Oh, we’re screwed."
        hide Rosco

        show Lucien at waist_up_left
        L "No we’re not. We just have to talk about it now then."
        hide Lucien

    elif player_choice == "lead":

        show bg communal_room at shake2
        MC "We are NOT getting rid of someone!"

        "They all stop at your sudden outburst, turning their gazes towards you."

        "You clear your throat, straightening up under their gazes."

        MC "We’ve done it before, we can do it again. We’re setting up a stand for the spring festival, right?"

        show Rosco at waist_up_center
        R "Uh-huh."
        hide Rosco

        MC "And it’s in two weeks."

        show Zander at waist_up_center
        Z "Correct."
        hide Zander

        MC "Okay. It just means we have to speedrun this. It’s like a limited time quest that we ignored until 24 hours before it ends. We got this."

    # [Choice Ends]

    "Now that logic had entered the chat, everyone was starting to nod along. Their suggestions became much more reasonable as the panic subsided."

    show Gale at waist_up_center
    G "I mean, it’s just a stand. Surely we won’t need that much preparation."
    hide Gale

    show Cassian at waist_up_center
    C "That depends on what kind of stand we’re doing, I guess."
    hide Cassian

    show Lucien at waist_up_center
    L "A simple food stand is fine— nothing too crazy."
    hide Lucien

    show Zander at waist_up_center
    Z "That could work."
    hide Zander

    show Cassian at waist_up_center
    C "How would it relate to our club though?"
    hide Cassian

    MC "Oh! There’s that thing Rosco was making."

    show Rosco at waist_up_center
    "Rosco blinks at you cluelessly."

    MC "The game?"
    
    show Rosco at waist_up_center, shake
    R "OHHH! B.I.T.E Protocol?"
    hide Rosco

    show Zander at waist_up_center
    Z "Oh, you’re saying we should showcase that somehow?"
    hide Zander

    MC "Maybe just the development and some of the beta gameplay?"

    show Gale at waist_up_center
    G "That’s good!"
    hide Gale

    show Lucien at waist_up_center
    L "Okay. We have that sorted out. Now, what about the food?"
    hide Lucien

    show Zander at waist_up_center
    Z "Should it be a dessert? It would be easy to eat while parsing through the other stands."
    hide Zander

    show Rosco at waist_up_center
    R "Taiyaki? Or uhhh… Shaved ice, skewers, dango…"

    "Rosco continues to spit out various names of desserts. Amidst his muttering, you can hear something about him ordering food for later."
    hide Rosco

    show Gale at waist_up_center
    G "…We can do a hotdog stand?"
    hide Gale

    "There’s a few sounds of hesitation coming from those in the room."

    show Lucien at waist_up_center
    L "It should be something more flexible. So we can offer more variety."
    hide Lucien

    show Cassian at waist_up_center
    C "Maybe we can do crepes?"
    hide Cassian

    show Zander at waist_up_center
    Z "Ooh, that sounds nice."
    hide Zander

    "The rest fill in with agreeable responses too."

    show Gale at waist_up_center 
    "In the background, you see Gale repeating the word 'crepe' to himself in the same way Cass pronounced it— but harsher."
    hide Gale

    "You bite back a laugh when you see Cass smack Gale on the shoulder."

    show Lucien at waist_up_center
    L "That works. I can think of a few recipes already."
    hide Lucien

    show Zander at waist_up_center
    Z "Then should we leave the cooking to you, our resident chef?"
    hide Zander

    MC "We’re not leaving it to you, that’s for sure."

    show Rosco at waist_up_center
    "You turn to address Rosco, ignoring the look of protest on Zanny’s face. You wish you could forget about the protein powder cake sitting in the clubroom’s fridge right now."

    MC "Rosco! You have a nice style. Wanna do outfits?"

    show Rosco at waist_up_center, shake
    R "Hell yeah. You trust me with them?"
    hide Rosco

    show Cassian at waist_up_center
    C "Just don’t put us in like, cat-maid outfits or something."
    hide Cassian

    "You see Zanny visibly deflate in your peripheral vision."

    show Gale at waist_up_center
    G "And, in that case, I can help with the decorations!"
    hide Gale

    show Zander at waist_up_center
    Z "I’ll help buy the ingredients."
    hide Zander

    show Cassian at waist_up_left
    C "Is there anything else that’s needed?"

    show Lucien at waist_up_right
    L "Can you buy the equipment? We might need some for the stand."

    C "Sure! I’ll do that."
    hide Cassian
    hide Lucien

    "You look around as each of the boys chat about their respective tasks. It doesn’t seem like there’s anything else you can be in charge of."

    "After mulling it over for a bit, you raise your hand to state your decision."

    MC "Then, I’ll help wherever I can!"

    "Cheering fills the room as you all hype each other up for the festival. There are satisfied looks on everyone’s faces as it seems that the initial planning of the stand is drawing to a close."

    show Gale at waist_up_center
    G "Ah, but…"

    "He addresses you with an undertone of worry in his voice."

    G "We’ll most likely be working on these separately then. Wouldn’t you be dead on your feet running around trying to help all of us?"
    hide Gale

    "That’s true. But you still want to help where you can."

    show Rosco at waist_up_center
    R "Don’t overwork yourself, goofy."

    "He gives you a knowing look, making you smile a bit sheepishly."
    hide Rosco

    show Lucien at waist_up_left
    L "We can work on our own, and [player_subject] can come join us on different days throughout the next couple weeks."
    hide Lucien

    show Cassian at waist_up_right
    C "Ah, yeah. We still have some time left before the festival anyway."
    hide Cassian

    show Zander at waist_up_center
    Z "In that case…"
    hide Zander

    #think about showing all sprites?
    "They all turn to look at you."

    show Zander at waist_up_center
    Z "Who do you want to help first?"
    hide Zander

    # [Route choices start]
    "End of prologue"

    return
