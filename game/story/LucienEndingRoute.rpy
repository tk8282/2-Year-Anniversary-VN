label luci_ending_route:
    scene bg stalls
    play music "audio/music/G1 - Cheerful (2).wav" fadein 1.0 loop
    "Time passes quickly, and before you know it, it is your turn to go on break."

    MC "Whew! I’m glad that our stand is so successful, but it’s really a lot of work..."

    show Lucien neutral smile at waist_up_center4 with dissolve
    L "We finally caught a break, huh?"

    MC "Yeah, and there’s so much to do here!"
    hide Lucien with dissolve

    # [Choice Start]
    menu:
        "The other clubs…":
            $ player_choice = "opt-1"
        "The delicious smell…":
            $ player_choice = "opt-2"
    show Lucien neutral smile at waist_up_center4 with dissolve
    if player_choice == "opt-1":
        MC "The other clubs prepared their booths really nicely. It’s actually fun to see what everyone came up with."

        L "It is! Have you been to any stalls yet?"

        "Earlier, you had stopped by a confectionery for a quick breakfast and then a stationery stall ran by the book club. Between setting up and running your club’s crepe stand, you hadn’t had the time for much else."

        MC "Just a few, though I’ve been meaning to visit some others during downtime..."

        L "We should go, then. Which ones?"

        "He’s already turning to look, scanning the colorful booths that line the walkway with interest."

        MC "Are you sure? Don’t you have anything else you want to do?"

        show Lucien laughing at waist_up_center4, pop
        L "What’s the point of a festival if you’re not spending time with your friends?"

        "He smiles at you, and you can feel yourself grinning back as the festival buzzes with energy around you."

        MC "Alright, then! First..."
    elif player_choice == "opt-2":
        MC "Everything smells so great, it’s making me hungry..."

        "The two of you are surrounded by various scents wafting from different stalls. Some students who walk by are munching on fresh food. From where you’re standing, you can see a takoyaki stand, kebabs, and other small eats that make your stomach grumble."

        L "Hm? Have you eaten yet? You’ve been working so hard."

        "You’d had breakfast earlier in the morning, but between helping with your stall and taking a quick trip to a stationery stand, you hadn’t done much of anything else."

        MC "No, not yet. Running a crepe stand is honestly harder than I’d thought! It’s good that we have so many hands on deck; otherwise, we’d be swamped by customers."

        L "You’re right. But I’m sure the others will be fine without us, so why don’t we go and grab a snack?"

        MC "I know just the place!"
    
    # [Choice End]
    show Lucien neutral smile at waist_up_center4
    "You push through the crowd, keeping a tight grip on Luci’s hand to not lose him in the rush of people. Luckily, the stall you’re looking for is easy to spot."

    MC "I’ve been wanting to try this for a {i}long{/i}, long time."

    show Lucien confused at waist_up_center4
    "Luci eyes the display at the front of the stand with a look of confusion on his face."

    L "You’ve been wanting to try fruit kebabs? Have you never had these before?"

    MC "These aren’t {i}just{/i} fruit kebabs. They’re actually sugared fruit kebabs, called tanghulu–the outside is like a crystallized shell, but the inside is all fresh fruit!"

    "You think you hear him mutter something like \"What the frick is a tanghulu\" but it must be just a passing whisper from the crowd because he’s nodding the next instant."
    show Lucien neutral at waist_up_center4
    L "Oh, I see... I think I’ve seen something similar before, but I’ve never had them."

    MC "We can each have our first taste then! Should we order two, or just get one that has different fruits?"

    show Lucien neutral smile at waist_up_center4
    L "I don’t mind either option."

    "It’s almost your turn to order. You decide to..."

    hide Lucien with dissolve
    
    # [Choice Start]
    menu:
        "Each order one separately!":
            $ player_choice = "separate"
        "Get one to share!":
            $ player_choice = "share"
    show Lucien neutral smile at waist_up_center4 with dissolve
    if player_choice == "separate":
        MC "Why don’t we pick out a stick of our favorite fruits? We’re likely to enjoy them more that way, right? Especially since it’s both of our first times..."

        L "That sounds good to me."

        MC "It’s unlucky that there’s no option for tomato tanghulu."

        "You laugh as his excited smile turns into a disgusted deadpan"

        show Lucien deadpan at waist_up_center4
        L "Right... {i}Un{/i}lucky."

    elif player_choice == "share":
        MC "Lets share and save room for other things later. If we end up not liking it, we won’t waste food, and if we do like it we could always order another."

        L "Oh, that’s smart. There’s more variety in the fruits we can try as well."

        MC "It’s just so unfortunate that there aren’t any cherry tomatoes..."

        show Lucien angry at waist_up_center4, pop
        "Luci makes a disgusted face, making you laugh."

    show Lucien neutral smile at waist_up_center4

    "In front of you a couple receives their snack, peeling away from the stand with delighted smiles, and then it’s time for you to order."
    "The two of you pay for the tanghulu and continue to walk down the street, taking note of each festival stall. You decide to try it first, lifting the first fruit–a grape–to your lips."
    "Sweetness explodes in your mouth as you take a bite. The candied shell breaks easily, practically melting in your mouth as your teeth puncture the skin of the small skewered grape."

    MC "It's..."
    MC "It’s pretty good!"

    hide Lucien with dissolve
    show screentint with dissolve
    "You continue to walk through the crowded festival together, enjoying the sugary snack. Soon, the number of booths around you dwindles, and in no time, you’ve wandered further into the school, ending up at the on-campus pond."
    play sound "audio/sfx/quack.ogg" volume 0.2
    "You both are heavily invested in conversation until the quack of a distant duck breaks through the shared words. Looking around, Lucien’s gaze lingers on the pond nearby, your own eyes follow his just in time to see a frog jump into the water."
    
    stop music fadeout 1.0
    scene bg luci pond with fade
    play music "audio/music/G5 - Romatic.wav" fadein 1.0 loop 

    show Lucien shocked at waist_up_right4, pop with dissolve
    L "Wow, I didn’t even realize we’d wandered so far from the main grounds."

    MC "I didn’t either, but they do say that time flies when you’re having fun... And I, for one, am having a great time."

    "You give Luci a thumbs-up paired with a smile, moving over to the lake’s edge, squatting down to get a closer look at a small turtle resting within the grass along the edge. Lucien follows after, taking a closer look as well."

    MC "It's nice having some downtime after all that hard work. Everyone did amazing, despite us completely forgetting about it at first."

    show Lucien deadpan pose2 at waist_up_right4
    L "Nayu would have never let us live if we didn’t finish in time."

    show Lucien laughing at waist_up_right4, pop
    "The two of you share a look before laughing at the thought of their diligent president. That’s when you remember something. Reaching into the messenger bag on your shoulder, you pull out a journal. The cover is decorated with intricate shapes resembling the sun and moon."

    show Lucien shocked at waist_up_right4
    L "Wait, is that for me?"

    MC "Mhm, I was wandering around and saw this journal earlier."
    MC "I figured that it might come in handy for you, considering you have a hard time remembering things. You can write down memories you want to keep; that way, you can always come back to them."
    hide Lucien with dissolve
    stop music fadeout 1.0
    
    play music "audio/music/E2 - Luci.wav" fadein 1.0 loop
    window hide
    $ quick_menu = False
    scene CG Luci 2 with fade
    pause 2.0
    $ quick_menu = True
    "You hand the journal to him, watching as he looks it over, his fingers seeming to lightly run against the cover."

    MC "Also, I wanted to get you a thank-you gift for everything. I meant it when I said that I had fun these past few days."

    scene bg luci pond with fade
    show Lucien deadpan at waist_up_right4 with dissolve
    L "Maybe a bit too much fun with the tomatoes?"

    "You laugh at his joke."

    MC "Never. That was the best part. I hope you like it, Lucien."

    "You tease, tone switching to a more genuine one. At that moment, he looks up from the journal."

    show Lucien neutral smile at waist_up_right4 with dissolve
    L "It's perfect; I love it. Thank you for the gift. I’ll make sure to treasure it each day. I think I know just the perfect first entry for it too."

    MC "Yeah?"
    
    L "Well, before that... you have something you want to say to me, don't you?"

    MC "Uh..."

    "Luci gently bonks you on the forehead with his new notebook."

    L "Come on, spit it out already! I can tell it's making you nervous."

    hide Lucien with dissolve

    # [Choice Start]
    menu:
        "Affirm friendship":
            $ luciRomantic = False
        "Confess feelings":
            $ luciRomantic = True
    
    show Lucien neutral smile at waist_up_right4 with dissolve
    if luciRomantic == False:
        MC "This is probably going to sound kind of strange, since we've been friends for... what, two years at this point?"
        MC "But I just wanted you to know that I really appreciate being able to plan part of this whole festival thing with you."
        MC "Kind of cheesy, I know, but sometimes I feel like I never really tell my friends how much they mean to me."

        "Luci remains silent for a few seconds before a smug grin spreads across his face. You immediately start to regret talking about your feelings."
        
        show Lucien smug at waist_up_right4
        L "Aww, you {i}like{/i} hanging out with me."

        MC "Never mind, I take it back. You suck and I hate you."

        "Your regret only intensifies as you see Luci try to mold his facial expression into a human depiction of the pien emoji."

        show Lucien crying at waist_up_right4
        L "Noooo, don't say that..."

        MC "Oh my god, please stop making that face."
        MC "Yes, you're my friend, and I care about you! Wasn't I sappy enough earlier?"
        MC "I'm still not letting you beat me in {i}Bario Racing{/i}, though."

        show Lucien annoyed at waist_up_right4
        L "Okay, we can't be friends anymore. I don't know you."

        MC "Your turn to deny your feelings today, huh?"

        "You burst out laughing at his sudden bout of childishness, poking his arm teasingly as he pouts and refuses to look at you."

        MC "You don't mean that."

        L "Maybe I do. Hmph."

        MC "Come on, you never do."

        "Perhaps it's because of your touching declaration of friendship earlier, but he cracks surprisingly quickly."
        
        show Lucien neutral smile at waist_up_right4
        L "Yeah. You're right."
        L "Just like you didn't mean it earlier when you said I sucked."
        L "Well, I could suck–"

        MC "If you make another vampire joke I will push you into the pond."

        L "Fiiiine."
    
    elif luciRomantic == True:
        MC "Well, I was just thinking..."
        MC "After all of this festival stuff, maybe we could go back to that crepe place?"
        MC "Not for research purposes, but just as... a date?"

        show Lucien shocked at waist_up_right4, pop
        L "?!"

        MC "{i}Please don't say no, please don't say no... Or at least be nice about saying no...{/i}"

        show Lucien neutral smile at waist_up_right4
        L "Damn, you really beat me to it, didn't you."

        MC "Huh??"

        L "I was going to ask you the same thing after the festival."
        show Lucien annoyed at waist_up_right4
        L "Man, now I'm kind of upset I didn't get to do it!"

        MC "And how {i}were{/i} you going to do it?"

        L "Well, I was gonna offer to walk you home after the fireworks, and then I was gonna ask if you wanted to get coffee sometime, and then I–"
        L "Why are you looking at me like that?"

        "You can't help but burst out laughing at the kicked puppy look on his face."

        MC "Hahahahaha!"

        L "Stop laughing at me! I already agreed to your date, didn't I?"

        MC "Did you? I don't remember you actually answering my question."
        show Lucien neutral at waist_up_center4 with move
        L "You're right, I didn't."
        
        show Lucien neutral smile at waist_up_center4, zoomin3
        "Before you can react, he grabs your wrist with his free hand and tugs you forward."
        "You make a very undignified noise as you desperately try to avoid face planting directly into his chest, only to almost smack your nose into his jaw."
        "He smiles mischievously down at you, but there's something nervous in his gaze."

        L "Maybe it's because I wanted you to answer mine instead."

        MC "You–"

        show Lucien laughing at waist_up_center4
        "Luci bursts out laughing as he holds you against his chest. Your face is probably comparable to a tomato with how hot your cheeks feel."
        L "So, what's your answer?"

        "You cover your face with your hands"

        MC "This is unfair. Cruel and unusual punishment."

        show Lucien neutral smile at waist_up_center4
        L "Yes or no, [player_name]. It's not a hard question."

        MC "Ugh, fine."
        MC "Yes, I'll go to the stupid crepe cafe with you because you're cute and I like you."
        MC "Happy now?"

        show Lucien annoyed at waist_up_center4
        L "... Wait, I'm not cute."
        
        "You look up in surprise only to see him looking away, cheeks puffed out like a little kid."

        MC "You're just proving my point, you know."

        L "Well, {i}you're{/i} supposed to think I'm cool and handsome! Not cute!"

        MC "Well, {i}YOU'RE{/i} stuck with me now, so you have to accept my assessment of your cuteness. Too bad."

        L "Hmph."

        hide Lucien with dissolve
        "He buries his nose in your hair and grumbles something about how he's a grown man and shouldn't be called cute."
        "Your sassy response dies on your tongue at the show of affection. You'll get him some other time."
        show Lucien neutral at waist_up_right4 with dissolve
    
    # [Choice End]

    "Both of you eventually fall into a comfortable silence. A family of ducks waddles towards the edge of the pond and hops in, the ducklings quacking happily."
    show Lucien neutral smile at waist_up_right4
    L "I won't forget this moment for a long time."

    MC "Even if you don't write it down?"

    "You gesture to the notebook in his hand. Luci looks thoughtful for a second, but you can see a mischievous grin tugging at the corners of his mouth."
    show Lucien neutral smile at waist_up_right4
    L "Well, this was a really fun festival, and I did like getting to spend time with you alone, but you know how my memory is..."

    MC "Come on. Really?"

    "You make a show of patting your pockets"

    MC "I think I have a pen here somewhere. Actually, maybe we should write it on your forehead instead–"

    L "I was kidding! You don't have to do that! Of course, I won't forget what happened today."
    L "But you're right. I'll make it the first entry in my notebook, just to be safe."

    "End of Luci Ending"
    stop music fadeout 1.0
    # jump back to general end