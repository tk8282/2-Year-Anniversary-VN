label zanny_route:
    scene bg clubroom
    MC "I'll help Zanny!"

    # Zanny Expression neutral
    show Zander neutral at waist_up_center3 with dissolve
    Z "Splendid, darling!"
    # Change Zanny Expression to Smug
    show Zander smug at waist_up_center3
    Z "I’ll see you soon."

    MC "Can’t wait!"

    hide Zander with dissolve
    jump zanny_route_day2

label zanny_route_day2:
    scene black with fade 
    show text "{size=50}Zander Route: Day 1{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve

    # Change BG to MC's Bedroom
    scene bg mc bedroom zanny with fade
    # [Common Track Starts]
    MC "Classes are over for the day... but I’m supposed to help Zanny this afternoon!"

    "You check your calendar as you’re getting ready, only to find out that you still have another day until you help out with him."

    MC "... Oh, oops. Well, checking in on him wouldn’t hurt, would it?"

    # [Choice Start]
    menu:
        "Let's go touch base with Zanny!":
            $ player_choice = "go-base"
        "I'm so tired. I need to rest.":
            $ player_choice = "go-rest"

    if player_choice == "go-rest":
        MC "No, I shouldn't...{w=0.3} let's go meet up with Zanny! Rest can wait!"
    
    # [Choice End]

    "You rub your eyes and get ready to head out. Time to pop by Zanny's dorm."

    scene black with fade

    "You finally reach a familiar door, raising your hand to knock."

    play audio "audio/sfx/door-knocking.ogg"
    pause 0.5

    "A muffled \"one second\" sounds from behind the door. After a few seconds, it opens, revealing his excited face."

    # Change Zanny Expression to SHocked
    show Zander shocked at waist_up_center3, pop with dissolve
    Z "Oh? What a lovely surprise, [player_name]! Please, come on in!"
    hide Zander with dissolve

    scene bg zanny bedroom morning with fade

    "You walk through the door and enter his personal dorm. Even though you've been here before, you're still shocked at how cozy it is. It's almost as if you're back at home."
    show Zander neutral at waist_up_center3 with dissolve
    # Neutral
    Z "Feel free to get comfortable. Is there a particular reason for this early visit? I was under the impression that the shopping trip is tomorrow. Not that I mind, of course—it's always a pleasure seeing your face."

    "You have to fight back a blush as he goes to take a seat by his desk. Always such a tease, that one. It takes a while for you to come up with an actual reply."
    show Zander neutral at waist_up_right3 with move
    MC "Oh, y'know. Just wanted to check in. Do we even know what ingredients to buy yet?"

    Z "That is a very good question. I don't think we do. Would you like to sit down and make a list?"

    MC "If that's ok with you."

    # Excited
    show Zander excited pose2 at waist_up_right3, pop
    Z "Darling, why wouldn't it be? Go on. Have a seat. Make yourself at home."

    "You tentatively glance around his room before finally sitting at the edge of his bed across from his desk."
    show Zander neutral at waist_up_right3 with move
    "Zanny begins to start up his computer, causing you to awkwardly scan around in the uncomfortable silence. While you've been here before, you've never stayed that long on your own. It's an unknown, but not unwelcome feeling."

    # Neutral
    show Zander neutral at waist_up_right3
    Z "No need to be so shy, [player_name]. I promise I don't bite."
    hide Zander with dissolve
    # [Choice Start]
    menu:
        "Yeah? I'll hold you to that promise.":
            $ player_choice = "yeah"
        "You don't? Bummer...":
            $ player_choice = "bummer"

    if player_choice == "yeah":
        # Smug
        show Zander smug pose2 at waist_up_right3 with dissolve
        Z "I'll try my best, but... no guarantee."

    elif player_choice == "bummer":
        # Flustered/Blushing
        show Zander flustered at waist_up_right3 with dissolve
        Z "Well I'll be damned. Didn't know you had it in you to tease me back like that. I'll have to up my game."

    # [Choice End]
    hide Zander with dissolve
    "You laugh as he begins to type away on his computer. In the meantime, you continue to look around his dorm, on the lookout for any details you missed before."
    "There's a lot of personalization that adds to the warm feeling of the room, details you haven’t taken the time to fully observe."
    "That's when you notice the other various additions to his dorm since you last visited. Added displays that fit neatly into his unique aesthetic. It's nice. Cozy. You want to know more."
    
    # [Major Choice Start]
    menu:
        "Ask about figure.":
            $ major_choice = "ask-figure"
        "Ask about A&R dice.":
            $ major_choice = "ask-dice"
        "Ask about the mysterious box in the corner.":
            $ major_choice = "ask-box"
        "Ask about the giant Netherling plushie on the chair.":
            $ major_choice = "ask-plushie"

    if major_choice == "ask-figure":
        "You approach one of the top shelves, your eyes glued to a particular figure of a pale humanoid with white hair and sharp fangs."
        show ballers gate box at asset_center with dissolve

        MC "Zanny... is that who I think it is?"

        show Zander neutral pose2 at waist_up_right_for_asset3 with dissolve
        Z "Oh, this guy?"
        # Excited
        show Zander excited at waist_up_right_for_asset3, pop
        Z "That’s my husband, the love of my life, the light to my darkness, from the game Baller’s Gate 3! He is such a well-written character, so complex yet so lovable, you can’t help but want to root for him!"
        Z "It just instantly clicked, y'know? And I've been obsessed ever since. After saving up, I bought the figure as soon as it got released."
        Z "Which, by the way, was a really smart impulsive decision. The figure sold out almost as quickly as it went on sale! Not surprising at all, given how wonderful his character is."
        
        show Zander excited at waist_up_right_for_asset3
        
        MC "So they're all gone now?"

        # Neutral
        show Zander neutral pose2 at waist_up_right_for_asset3
        Z "It's been a while since the game's release, so it should be restocked. But before I get too carried away, I have to ask; \"Did you play the game?\""

        hide Zander with dissolve

        # [Choice A Start]
        menu:
            "I’ve played it!":
                $ player_choice_a = "yes"
            "I haven’t played it, but I know a bit about it!":
                $ player_choice_a = "no"
        
        if player_choice_a == "yes":
            MC "Of course I’ve played it! I couldn’t put it down once I started!"

            show Zander excited at waist_up_right_for_asset3, pop with dissolve
            Z "You too?! Then you understand how good a character he is and why he’s my in-game husband, right?!"

            MC "He’s honestly one of my favorite party members in the game. I couldn’t help but try to romance him on my first playthrough because he was so hilarious and charismatic!"

            show Zander neutral pose2 at waist_up_right_for_asset3
            Z "Did you succeed in romancing him?"

            MC "No...{w=0.3} I was too much of a goody-two-shoes for him. But once this semester’s over, I’m gonna commit all of the evil stuff to win his heart!"

            show Zander laughing pose2 at waist_up_right_for_asset3
            Z "That’s the spirit!"
            show Zander neutral pose2 at waist_up_right_for_asset3

            MC "Though, you have to tell me where you got that figurine from because now, I really want it in my dorm."
            
            # Smug
            show Zander smug at waist_up_right_for_asset3
            Z "That’s a secret, darling."

            MC "Aw, come on! Not even just a hint, Zanny?"

            show Zander smug pose2 at waist_up_right_for_asset3
            Z "Nope!"

            "You sigh and pout in front of him, which makes him let out a chuckle."

            # Neutral
            show Zander neutral at waist_up_right_for_asset3
            Z "Anyways, you get the gist. What I like most about him—beyond his handsome surface-level persona—is that deep, complicated motivation that drives him to do what he does."
            Z "I love that sort of complexity in a character. It adds layers, much like an onion. I don't take him out of the case in fear that I’ll accidentally damage it—"
            show Zander neutral pose2 at waist_up_right_for_asset3
            Z "Ah, I'm rambling, aren't I? Apologies for that, my dear."
            hide Zander with dissolve

            # [Choice B Start]
            menu:
                "Don't apologize! There's nothing wrong with a little rambling.":
                    $ player_choice_b = "1-B"
                "Oh, please. I could listen to you talk all day. It's part of your charm!":
                    $ player_choice_b = "2-B"

            if player_choice_b == "1-B":
                # Excited
                show Zander excited at waist_up_right_for_asset3, pop with dissolve
                Z "Well, that's reassuring! I can't help but yap whenever I talk about something I love and enjoy. It’s an essential part of who I am."

            elif player_choice_b == "2-B":
                # Blushing/Flustered
                show Zander flustered at waist_up_right_for_asset3 with dissolve
                Z "How sweet of you to say. I appreciate the reassurance, darling. And for the record? I could say the same for you as well."

                "Your face heats up a bit at his words. There's something new sparking in the air between you two—something you're beginning to crave."
            # [Choice B End]

        elif player_choice_a == "no":
            MC "Ooooh, I haven’t gotten around to playing that yet! But maybe once this semester’s over, I can start it."

            # Neutral
            show Zander neutral at waist_up_right_for_asset3 with dissolve
            Z "Ah, then I can’t say much more."

            # Smug
            show Zander smug at waist_up_right_for_asset3
            Z "You’ll just have to play it and see. You’ll love him a lot, I promise. Besides that, the world and characters alone are enough to get you hooked, romance aside. Romancing a pathetic man is a plus."

            MC "Sounds like a good time. I’ll be sure to keep you updated on everything that happens in my playthrough, deal?"

            Z "You better!"
        
        # [Choice A End]
        hide ballers gate box with dissolve
        # Neutral
        
        show Zander neutral pose2 at waist_up_right3 with move
        Z "Goodness, I sure do talk a lot. Anything else you’d like to ask about?"

        # [End Major Choice #1]

    elif major_choice == "ask-dice":
        "Your eyes are drawn to the tray with two sole dice abandoned in the middle. It’s not a full set, but they drew your attention anyway."
        show d20 and d6 at asset_center with dissolve

        MC "Oooooh, those are some pretty dice you got there, Zanny!"

        # Blushing/ flustered
        show Zander flustered pose2 at waist_up_right_for_asset3 with dissolve
        Z "You think so too? I’m glad!"

        MC "I always see you and your group roll these kinds of dice around in the club room sometimes. What exactly do they do?"

        # Neutral
        show Zander neutral pose2 at waist_up_right_for_asset3
        Z "What do the dice do?"

        # Smug
        show Zander smug at waist_up_right_for_asset3
        Z "Oh, darling, are you sure you want to go down this rabbit hole?"

        MC "Of course I do! I’ve always been kind of curious."

        # Excited
        show Zander excited pose2 at waist_up_right_for_asset3, pop
        Z "Well, in that case, let me enlighten you. What you see here is a D20 and a D6. The bigger one is for most actions in A&R. Y'know, you roll and the number determines if you're able to perform a certain action or not."
        show Zander excited at waist_up_right_for_asset3
        Z "The six-sided one is typically for stuff like weapons, attacks, spells, and so on."
        Z "There are so many other types of dice out there, but I only have these two displayed on my little trinket shelf, because... well... I may or may not have misplaced the rest."
        Z "They’re from an old set anyway. Now I use a better, custom-made one. A {i}special{/i} one."

        # Neutral
        show Zander neutral at waist_up_right_for_asset3
        Z "Ah, there I go again, yapping on and on."

        MC "Don’t say it like that! I’m the one who asked."

        show Zander neutral pose2 at waist_up_right_for_asset3
        Z "And are you satisfied with your answer?"
        hide Zander with dissolve
        # [Choice A Start]
        menu:
            "Of course I am!":
                $ player_choice_a = "1-A"
            "Are you kidding me? I could listen to you talk forever.":
                $ player_choice_a = "2-A"

        if player_choice_a == "1-A":
            # Neutral
            show Zander neutral at waist_up_right_for_asset3 with dissolve
            Z "That’s great to hear. Because I definitely won’t be stopping anytime soon."
        
        elif player_choice_a == "2-A":
            #Blushing/Flustered
            show Zander flustered at waist_up_right_for_asset3 with dissolve
            Z "You flatter me. I’ll make sure to hold you to that then. So you better be prepared."
        # [Choice A End]
        hide d20 and d6 with dissolve
        # Neutral
        show Zander neutral at waist_up_right3 with move
        Z "Notice anything else? I’ve added quite a lot since the last time you’ve visited."
    
    # [End of Major Choice #2]

    elif major_choice == "ask-box":
        "Your eyes flicker over to the corner where a mysterious box sits, unopened. Curious, you get up and walk over it, hovering over the cardboard curiously."

        MC "Uh...{w=0.3} Zanny? What’s inside this box?"

        show Zander neutral at waist_up_right3 with dissolve
        Z "That’s just my new supply of protein powder. Came in yesterday, too. It’s pretty neat, actually. Why don’t you take a look!"

        "Heeding his words, you finally open the flaps and pull out a large jar of protein powder. Except, it’s not like the others you’ve seen at the supermarkets. This one is more...{w=0.3} {i}unique{/i}"
    
        show Zander neutral at waist_up_right_for_asset3 with move
        show protein powder at asset_center with dissolve

        MC "Woah. This is pretty neat!"

        # Excited
        show Zander excited at waist_up_right_for_asset3, pop
        Z "Right?! I got it custom ordered from a small business to cater to my interests. Haven’t used it yet, though. I wanted to save it for a special occasion."

        MC "It’s pretty big, though. I didn’t know you were a gym rat as well..."

        # Neutral
        show Zander neutral pose2 at waist_up_right_for_asset3
        Z "I know I don’t look the part, but I assure you I take fitness very seriously. Getting your daily protein intake is important, let me tell you."

        "A thought suddenly occurred in your mind—maybe you could use some of those protein powders for making crepes."

        MC "Hey, what if we use this as an ingredient for the club’s festival booth? I say that’s a pretty special occasion."

        # Confused
        show Zander confused pose2 at waist_up_right_for_asset3
        Z "Protein powder...{w=0.3} for crepes?"

        MC "Yeah!"

        # Neutral
        show Zander neutral at waist_up_right_for_asset3
        Z "Huh. That sounds like something I need to try out, actually. I use it to make pancakes all the time. Might as well experiment with crepes too!"

        "Laughing, you put it back in the box and move to sit back down on the bed."

        hide protein powder with dissolve
        # Neutral
        show Zander neutral at waist_up_right3 with move

        MC "It’s a fun idea, but the rest of the boys would probably kill us if we did that."

        # Laughing
        show Zander laughing at waist_up_right3
        Z "Unfortunately, you’re correct. Maybe we can save it for a feast for just the two of us, yeah? I genuinely do want to try it out. For the funny."

        hide Zander with dissolve
        # [Choice A Start]

        menu:
            "Sounds like a lot of fun.":
                $ player_choice_a = "1-A"
            "Like a date? Count me in.":
                $ player_choice_a = "2-A"

        if player_choice_a == "1-A":
            # laughing
            show Zander laughing pose2 at waist_up_right3 with dissolve
            Z "You get me. I knew I could trust you."
        elif player_choice_a == "2-A":
            # Blushing/ Flustered
            show Zander flustered pose2 at waist_up_right3 with dissolve
            Z "You’re quite the bold one, aren’t you? Not that I mind though. You’re quite the charmer."

            "Despite it initially being a light tease, his response warms your heart. If anyone here is the charmer, it’d be him. You keep his words in the back of your mind for later. Maybe there’s a chance after all..."
        # [Choice A End]
        # Neutral
        show Zander neutral at waist_up_right3
        Z "Anything else you’d like to chat about? I can answer questions all day."

        # [End of Major Choice #3]

    elif major_choice == "ask-plushie":
        "Next to the bed on the couch, a large stuffed animal catches your attention. You’ve noticed it there before, but never had the time to take a good look at it. When you do, your heart swells in excitement."
        
        show giant netherling plushie at asset_center with dissolve
        MC "Hey, that’s the rare limited edition Netherling plushie! How did you get it?! I’ve been wanting this one for ages, but it sold out in half an hour!"

        # Smug
        show Zander smug at waist_up_right_for_asset3 with dissolve
        Z "Well...{w=0.3} let’s just say that I have my ways."

        MC "What?! You’re gonna have to tell me your ways once this is all done. I wanted one so badly."

        "His expression dwindles down into something more endearing. He looks at the plushie in earnest, his gaze drowning in visible adoration."

        # Blsuhing/ Flustered
        show Zander flustered pose2 at waist_up_right_for_asset3
        Z "Let’s just say, I would’ve murdered someone to get my hands on that thing. I’m not sure how much you know about the history of the character, but I have a very deep connection to it. A connection no one else in the universe could ever understand."

        MC "Wow. Sounds like you love Netherlings a lot."

        show Zander flustered at waist_up_right_for_asset3
        Z "Of course I do! They’re my entire world. And I can say for certain that they feel the same way. We have a sort of relationship that outsiders struggle to understand. There’s a lot of love and trust involved, and I wouldn’t have it any other way."

        MC "\"We?\" \"They?\" Isn’t it just a character?"

        # Smug
        show Zander smug at waist_up_right_for_asset3
        Z "Darling, it’s {i}so{/i} much more than that. It’s one of those things where if you know, you know."

        MC "Oh? May I know more, then?"
        
        Z "Considering how you’re here, I’d say you already do. Nevertheless, the club is always open to welcoming newcomers. Say the word, and I’ll give you the whole spiel."

        "Unsure exactly what he means, you nod excitedly, curious as to what ‘club’ he’s talking about. Not wanting to get too carried away, you mentally note to ask more later when the time is right."
        "From how he talks about it, it appears to be something very much worth investing in."

        hide giant netherling plushie with dissolve
        # Neutral
        show Zander neutral pose2 at waist_up_right3 with move
        Z "Oh my days, I really went on-and-on there, didn’t I! Would you like to ask more?"
    
    # [End of Major Choice #4]
    # [Major Choice End]

    show Zander neutral at waist_up_right3
    MC "I think I’m finished. Plus, if we went on any longer, we probably wouldn’t have been able to get anything productive done."
    MC "Oh! Right! Speaking of, I almost forgot... {w=0.3} I came here to check in about the festival."
    
    # Neutral
    Z "We're going shopping tomorrow, right? What is there to do again?"

    MC "Make a list? To be more organized? That way we actually know what we’re doing."

    # Smug
    show Zander smug at waist_up_right3
    Z "You just couldn't wait to see me then, huh? We could’ve made a list over text, y’know?"

    hide Zander with dissolve
    # [Choice Start]
    menu:
        "Roll your eyes.":
            $ player_choice = "eye-roll"
        "Tease back.":
            $ player_choice = "tease-back"
    
    if player_choice == "eye-roll":
        MC "Oh, hush."
        
        show Zander neutral pose2 at waist_up_right3 with dissolve
        Z "Please, it's just a little teasing!"

    elif player_choice == "tease-back":
        MC "And what if I did?"
        
        # Blushing
        show Zander flustered at waist_up_right3 with dissolve
        Z "Oh? Then I’d be more than happy to oblige your visit. It’s quite nice just talking, isn’t it?"

        "You clear your throat and try to get back on track, trying to ignore the rising heat across your cheeks."

    # [Choice End]

    show Zander neutral at waist_up_right3
    MC "Should we make a list of ingredients to buy, then? Before we go on another tangent?"

    "Zanny turns to face his computer, typing away as you scoot closer across the bed to see."

    # Neutral
    show Zander neutral pose2 at waist_up_right3
    Z "It shouldn’t be too hard, since we already know what sort of crepes we’re buying. Come, sit closer. Let’s get to work."
    hide Zander with dissolve
    "The two of you spend some time researching ingredients that go in the different crepes based on the ones the club is planning on selling at the festival."
    "Most of them have the same base ingredients, so it’s more a question of which special additions are there to buy."
    "According to the list, there are all sorts of types, both sweet and savory. Each ingredient is separated into produce, dairy, condiments, and meat products."
    "Your mouth waters just planning out the shopping trip for tomorrow. You can’t wait for the actual festival!"
    "When you finish the list, you feel a bit disappointed. It didn’t take long at all, and a large part of you isn’t ready to stop hanging out with Zanny."

    MC "Wow. That was quick. Man, I can’t believe we got that sidetracked!"

    # Laughing
    show Zander laughing at waist_up_center3 with dissolve
    Z "Oh goodness, you’re right! Nothing wrong with that, though. I had a blast just yapping."

    MC "For sure, for sure. It was so interesting learning about all the new decorations and trinkets you have in your room."
    MC "That’s the whole reason I joined the game development club in the first place. The nerd in me loves the creative process behind developing, but I love learning more about the games already out there."

    "You spot a glint in Zanny’s eyes, one that tells you he’s about to get sidetracked again."

    show Zander neutral at waist_up_center3
    Z "Y'know, there are more trinkets like these in the club room if you wanna see. Typically, Rosco and I are the ones involved with TTRPG, so the stuff rarely sees the light of day."
    Z "Especially since we spend more time developing than gaming in the first place. I bought something new recently, if you'd like to have a look? Trust me, if you liked what I put in my room, you’ll {i}love{/i} the little collectibles I added to the club’s shelf."

    MC "Sounds like a lot of fun!"

    show Zander neutral at waist_up_right3 with move
    "Zanny wastes no time getting up and walks over to the door, casting an exciting glance over his shoulder."

    #Excited
    show Zander excited at waist_up_right3, pop
    Z "Well, what are you waiting for? Let's go!"
    hide Zander with dissolve

    # Change Scene to BG Clubroom
    scene bg clubroom with fade

    # Play common club room Track
    "After walking across campus, the two of you finally enter the clubroom. Usually, you work on projects or procrastinate by playing games with the other boys here."
    "This is your first time hanging out in the club room with him one-on-one. You're a bit nervous."
    "As soon as you two enter, Zanny walks over to the shelves with all the members' personal belongings. There are a few laminated pipmon cards, bags, and other various trinkets."
    "He pulls out a small box that had been sitting next to one of the boys' Gobbledygook figurine."

    # Excited
    show Zander excited at waist_up_right3, pop with dissolve
    Z "This is the newest merchandise I bought. I had been showing it to Rosco previously, which is why it's still here."

    "When he opens the box, a treasure chest-looking container is pulled out. Near the lock in the front are long, sharp teeth. It almost appears to be some sort of creature."

    show Zander excited at waist_up_right_for_asset3 with move
    show mimic closed at asset_center with dissolve
    Z "It's a mimic dice holder!"

    MC "Woah...{w=0.3} aren't those the creepy shapeshifting chests?"

    Z "Correct! I try to get my hands on any A&R merch I can. Not only does it help me keep everything organized."

    MC "A&R? That’s the TTRPG, right? Avallum and Ravanis?"

    Z "Yes. Literally my favorite game ever. Remember how you were asking about dice earlier? Well, this is the holder I put my {i}actual{/i} dice set in. Here. Take a look."

    "He opens the dice holder to reveal another set of purple dice inside."

    hide mimic closed with dissolve
    show mimic open at asset_center with dissolve

    "Unlike the ones in his room, these ones have a more luminescent look to them. They shine under the light, sparkling under the right angle. They're gorgeous."

    # Blushing/ Flustered
    show Zander flustered pose2 at waist_up_right_for_asset3
    Z "I got these custom-made based on something near and dear to my heart. I almost don't want to use them because of how precious they are to me. Whenever we do play A&R, it’s always a different, more normal dice set that’s used."

    "The purple almost seems to glow brighter at that. He gently closes the dice holder and puts it back in the box where it's shielded from dust."

    hide mimic open with dissolve
    # Neutral
    show Zander neutral at waist_up_center3 with move
    Z "While we're here, is there anything else you'd like to know about TTRPGs? Maybe we can even do a short little one shot if you'd like? Or a short scene, rather, since it is getting kind of late."

    MC "I'd love to do a quick scene! I’m a better hands-on learner after all."

    # Excited
    show Zander excited at waist_up_center3, pop
    Z "Wonderful!"

    "He grabs a few items and leads you to the TTRPG table tucked away in the corner. He stands still for a moment, glancing over at the shelf hesitantly. After a few seconds, he turns back and grabs the special purple dice out of the box."
    show Zander excited at waist_up_right_for_asset3 with move
    show custom dice at asset_center with dissolve

    MC "Those are absolutely gorgeous..."

    "You take some time to look over them, captivated by the purple shine they radiate under the club room’s overhead light. And there, right where the number 20 is supposed to be, is an engraved Netherling instead."

    MC "No wonder you said they’re so special. I’m honored to play with them for the very first time."

    show Zander excited pose2 at waist_up_right_for_asset3, pop
    Z "Can’t keep ‘em cooped up forever. Plus, you’re special to me as well.  I’d love to use them in your presence."

    "The honor causes your heart to swell, and the tease incites a faint blush across your face."
    hide Zander with dissolve
    # [Choice Start]
    menu:
        "You flirt too much. Let’s just get started!":
            $ player_choice = "choice-1"
        "You’re special to me as well.":
            $ player_choice = "choice-2"
    
    if player_choice == "choice-2":
        # Blushing/Flustered
        show Zander flustered pose2 at waist_up_right_for_asset3 with dissolve
        Z "You’re playing a dangerous game here, darling. Indulge my advances too much, and I might be under the impression that you like it."

        MC "Of course I do. If I didn’t, I wouldn’t be flirting back."

        show Zander flustered at waist_up_right_for_asset3
        Z "It’s rare I meet someone as bold as I am. Let’s start this whole thing before we get too carried away."

        "A laugh escapes you, something you’ve done a lot in Zanny’s presence lately. There’s just something about that man that keeps drawing you in."

        MC "You’re right, we should focus!"
    elif player_choice == "choice-1":
        show Zander neutral at waist_up_right_for_asset3 with dissolve
    # [Choice End]

    # Neutral
    show Zander neutral at waist_up_right_for_asset3
    "Let’s get this damn party started then!"

    hide custom dice with dissolve
    hide Zander with dissolve

    # [CG 1 Start]
    scene CG Zanny 1 with fade
    # [Fantasy Ambiance Track Start]
    pause 1.0
    Z "First order of business is character creation. Here is a printed sheet to get you started. You can either base the character on you or go crazy with it! It's all about the roleplay."

    MC "Sweet!"

    "On the table in front of you is a neatly organized beginner's character customization sheet. You skim through the contents, eager to get started."

    MC "{i}Hmm...{w=0.3} what should my character's name be?{/i}"

    # [Choice Start]
    menu:
        "[player_name]":
            $ player_choice = "mc-name"
        "John Avallum":
            $ player_choice = "john-avallum"
        "Randy Ravanis":
            $ player_choice = "randy-ravanis"
        "Zandra Netherbrand":
            $ player_choice = "zandra-netherbrand"
    
    # [Choice End]

    MC "{i}Perfect. Now what about race?{/i}"
    
    # [Choice Start]
    menu:
        "Human":
            $ player_choice = "human"
        "Elf":
            $ player_choice = "elf"
        "Drow":
            $ player_choice = "drow"
        "Tiefling":
            $ player_choice = "tiefling"
        "Other…":
            $ player_choice = "other"

    if player_choice == "other":
        # [Choice A Start]
        menu:
            "Githyanki":
                $ player_choice = "githyanki"
            "Gnome":
                $ player_choice = "gnome"
            "Dwarf":
                $ player_choice = "dwarf"
            "Halfling":
                $ player_choice = "halfling"
            "Dragonborn":
                $ player_choice = "dragonborn"
        # [Choice A Ends]
    # [Choice End]

    MC "{i}Great! Now what class should I be...{/i}"

    # [Choice Start]
    menu:
        "Barbarian":
            $ player_choice = "barbarian"
        "Bard":
            $ player_choice = "bard"
        "Cleric":
            $ player_choice = "cleric"
        "Druid":
            $ player_choice = "druid"
        "Fighter":
            $ player_choice = "fighter"
        "Other":
            $ player_choice = "other"

    if player_choice == "other":
        # [Choice A Start]
        menu:
            "Monk":
                $ player_choice = "monk"
            "Paladin":
                $ player_choice = "paladin"
            "Ranger":
                $ player_choice = "ranger"
            "Rogue":
                $ player_choice = "rogue"
            "Sorcerer":
                $ player_choice = "sorcerer"
            "Warlock":
                $ player_choice = "warlock"
        # [Choice A Ends]
    # [Choice End]

    "You continue finalizing your choices until you're satisfied. Zanny helps you out with all the numbers and logistics of your character and is very enthusiastic about the whole ordeal. The two of you work together until you get to the final parts."

    scene CG Zanny 1 BG with fade
    show Zander excited at waist_up_left3, pop with dissolve

    Z "Now the fun part—your lore! This is your background and the meat of the role-playing experience, essentially. Who would you like to be?"

    MC "{i}Hmm...{w=0.3} what should my lore be?{/i}"

    hide Zander with dissolve
    # [Choice Start]
    menu:
        "A wish-granter cursed to a lamp":
            $ player_choice = "genie"
        "Someone who used to be trapped for thousands of years.":
            $ player_choice = "oni"
        "An old fossil that became conscious after millions of years.":
            $ player_choice = "dino"
        "Someone who's originally from space":
            $ player_choice = "alien"

    #[Choice End]
    show Zander neutral at waist_up_left3 with dissolve
    Z "All done?"

    MC "Yeup!"
    show Zander excited at waist_up_left3, pop
    Z "Perfect! Let's get started. This is going to be more freestyle based on what Rosco and I have been cooking up in our free time. Don't worry about the logistics of the rolls or anything—I'll handle that. Just play along and have fun!"

    "You nod, completely swept up in his excitement. With your confirmation, the short journey begins."

    show Zander serious at waist_up_left3
    Z "The two travelers sit huddled by one another on the cart that bumps and jumps on the rocky, gravelly road."
    Z "The carriage driver brings them into a small town after traversing far and long across Shamai. They've been on many journeys after registering with the adventurer's guild of Primatera."
    Z "After being on the road so long, this is the first time in a long time they've got some downtime. With no particular goal ahead, they've been looking around for possible new adventures."
    Z "It's been a long while, so they decided to stop to rest. In the dead of the night, silence greets them."

    show Zander neutral pose2 at waist_up_left3
    Z "Looks like we're here... we should stop by the inn first. I'm tired."

    MC "Cinder Inn? Sure, let's go. I’m in desperate need of a hot bath after all that travelling."

    show Zander serious at waist_up_left3
    Z "The young travelers hop out of the cart and walk up to the brick building. It's oddly quiet, but you're both too tired to notice. When you enter the place, the crisp scent of peaches overwhelms you. It's fairly empty, save for a few stragglers."
    Z "Behind the wooden desk across the entrance is a chirpy red-haired man. He greets them upon arrival with a cheery voice and wide smile."

    show Zander laughing at waist_up_left3
    Z "\"Greetings! I'm Malim Cendari, the humble innkeeper of this establishment. Would you folks like a room with one bed or two?\""
    hide Zander with dissolve

    # [Choice Start]
    menu:
        "One is fine!":
            $ player_choice = "one"
        "Two separate ones, please.":
            $ player_choice = "two"

    if player_choice == "one":
        show Zander flustered at waist_up_left3 with dissolve
        Z "Well, I’ll be damned! Bold as always, I see. You'd better not regret that decision."

    elif player_choice == "two":
        show Zander neutral at waist_up_left3 with dissolve
        Z "What [player_subject] said."

    # [Choice End]

    show Zander neutral pose2 at waist_up_left3
    Z "The innkeeper disappears behind the desk and pulls out a keyring."

    show Zander laughing at waist_up_left3
    Z "\"Last door on your right down that hallway! Enjoy your stay.\""

    show Zander neutral pose2 at waist_up_left3
    Z "The two travelers walk down the hallway toward their humble room where they're staying for the night. Upon entering, they set all their stuff down and throw themselves onto the comforting blankets."
    Z "We should get some rest before tomorrow. Shamai is jam-packed with possibilities."

    MC "You're right."

    show Zander serious pose2 at waist_up_left3
    Z "They both get settled in for the night, washing up and flicking off the switches. Once tucked under the covers, their breaths slowly even out. You both find yourselves relaxing in the silence, the weight of the journey sinking you into the mattress."
    Z "But something isn't quite right. You begin to hear a low creaking sound outside the door. It could be someone walking to their room. It could be something else."
    Z "The incubus seems to still be asleep, not noticing the sudden noise. Go ahead and roll a perception check for me."

    MC "Is this where I start rolling the dice?"

    "He breaks character and starts to excitedly explain the process."

    show Zander excited pose2 at waist_up_left3, pop
    Z "Yeup! For checks, you're mostly going to use the 20-sided dice. Go ahead and roll it—I'll add the modifiers for you."

    
    "You pick up the designated dice and give them a good shake."
    hide Zander with dissolve
    # [Choice Start]
    menu:
        "Give it a rough throw.":
            $ player_choice = "throw"
        "Toss it gently.":
            $ player_choice = "toss"

    if player_choice == "throw":
        play sound "audio/sfx/d20-roll.ogg"
        "After a nice and thorough shake, you put a bit of force into the toss, causing the dice to skid across the table. Once it stops, you see the number one staring back at you, taunting your failure. Zanny chuckles a bit out of his character. You just rolled a Nat 1."

        show Zander smug at waist_up_left3 with dissolve
        Z "Unfortunately, you fail the perception check. Not thinking anything of the noise, you decide to fall back into the pillows. After a few minutes of trying to fall back asleep, the doors of the room suddenly blast open!"

        "Both you and Zanny are startled, completely caught off guard. They charge in, faces obscured, and neither of you gets an action on your first turn."
        "He explains some basic attacks as they strike first, forcing you to start combat at slightly-depleted levels of health."

    elif player_choice == "toss":
        play sound "audio/sfx/d20-roll.ogg"
        "With gentle hands, you lightly toss out the dice onto the table. It briefly rolls in front of you before stopping. There, on the table, a luminescent Netherling glows right back at you."
        
        show Zander shocked at waist_up_left3, pop with dissolve
        Z "A Nat 20 first try?! My goodness..."

        show Zander serious pose2 at waist_up_left3
        Z "You succeed the perception check. Using your personal capabilities, you strain your hearing, tensing your body for a fight. There, outside the door, you barely pick up on a whispered countdown. Something isn't right."

        MC "Hmm...{w=0.3} I decide to wake up Zanny immediately, shaking him until he’s conscious. ‘Wake up!’ I whisper. ‘I think we’re about to be ambushed!"

        show Zander confused pose2 at waist_up_left3
        Z "\"H-Huh?\" I grab my knife from the bedside table as a reflex. \"What do you mean?\""

        show Zander serious at waist_up_left3
        Z "A group of bandits suddenly breaks through the door and charges through with daggers in hand! Since you two are alert, you’ve already prepared your weapons—there is no need to use an action to equip them."

        # [Choice End]
        # [Fantasy Battle Track Start]
    
    show Zander neutral at waist_up_left3
    Z "We've entered combat now! Go ahead and roll for initiative."

    MC "D20?"

    Z "Yeup!"
    
    "You roll the dice and get started on the fight.{nw}"
    play sound "audio/sfx/d20-roll.ogg"
    extend " Zanny goes through all the logistics with you, carefully explaining the different dice and how they determine your attacks."
    "It's fun going through the motions with him, learning a lot about the game and how it works. You're incredibly immersed, feeling as if you're actually fighting a group of bandits."
    
    show Zander serious pose2 at waist_up_left3
    Z "After they all flitter into the room, I take my turn to sort of back away and take a more defensive stance."
    Z "Since they seem to all be targeting you, I cast Shield of Faith on you to help boost your AC. As I’m back here, I’m observing the faces of the bandits, searching for anything that can help us determine who they are."

    MC "They’re all wearing masks, correct?"

    Z "Indeed, they are. No identifiable marks on their clothing or tattoos that stand out either. What would you like to do?"

    MC "Let’s see...{w=0.3} Noticing the magic user in the back, I maneuver slightly so that they’re in my direct line of sight. Do we know what their weakness is?"

    Z "At the moment, we do not. You could roll an arcana check, but that would be an action. The only fact we know for certain is that they are resistant to fire, as exhibited by my previous attack. Go ahead and make a decision."
    hide Zander with dissolve

    # [Choice Start]
    menu:
        "Use a cantrip.":
            $ player_choice = "c-1"
        "Cast a spell.":
            $ player_choice = "c-2"
        "Do a close strike.":
            $ player_choice = "c-3"
        "Attack from a distance.":
            $ player_choice = "c-4"

    show Zander neutral pose2 at waist_up_left3 with dissolve

    if player_choice == "c-1":
        MC "I decide to cast acid splash! Conjuring up a bubble of bursting acid in my grasp, I hurl it back at the wizard bandit, watching as it sears the wooden floorboards beneath it and poisons the man standing within its range."

    elif player_choice == "c-2":
        MC "I use my level 1 spell slot to cast magic missile! Glowing darts shoot forward and pierce the bandit in the back! They dramatically grab their shoulders at the impact, and I smile in triumph at the successful hit."

    elif player_choice == "c-3":
        MC "I walk across the room to get up close to the magic user. With my weapon, I swipe at their feet, knocking them to the ground. They grovel on the floor, and I look down at them with a victorious grin."

    elif player_choice == "c-4":
        MC "I whip out my bow to shoot an arrow across the room right toward the bandit who uses magic. It whirrs by and pierces their shoulder, causing them to fall to a knee and clutch the wound with agony."
    
    play sound "audio/sfx/d20-roll.ogg"
    "You roll the die to decide the amount of damage. Zanny does all the math for you with an excited smile, acting along with the sudden, close-knit combat."
    "The two of you take turns strategizing and attacking. It’s exciting to improvise the different descriptions that come with fighting in a fantasy world. This is way more fun than you thought."
   
    #[Choice End]

    "At the climax of it all, it’s their turn to attack again. Zanny narrates in great detail how they continue to target you, working together to deplete your health. The first one walks up and slashes by your feet, cackling as the attack hits."
    "A second one aims a flaming arrow right in your direction, applying a status effect of burn."
    "And finally, the third wizard in the back does a fancy twirl with his staff before casting Ice Knife in your direction. The ice stings at your skin, and you fail a saving throw, effectively getting knocked prone off your feet."
    "You really start to get into the zone. These bandits need to go down."

    MC "Goddamn! What do they have against me?"

    show Zander confused pose2 at waist_up_left3
    Z "I have no idea! We’ll have to defeat them to find out. As you're hunched over and sort of clenching your side, I walk up within melee range and cast Cure Wounds on you, healing seeping from my fingertips upon touching your arm."

    show Zander neutral pose2 at waist_up_left3
    Z "Roll a D8 and add my spell casting modifier...{w=0.3} I heal you for about 6 hit points. I can’t back away without provoking an opportunity attack, so my turn effectively ends."

    MC "My body feels stronger, and I stand back up on two feet. I turn and smile graciously, sending a playful wink amidst the chaos. \"Thanks, Zanny.\""

    show Zander neutral at waist_up_left3
    Z "Any time, darling. Now go ahead and kick their asses for me."

    "You look down at the exploded ice all beneath your feet. Is the gamble worth it?"

    # [Choice Start]
    menu: 
        "Use an action to melt the ice.":
            $ player_choice = "action"
        "Risk walking to make a melee attack.":
            $ player_choice = "walk"

    show Zander neutral at waist_up_left3 with dissolve

    if player_choice == "action":
        MC "It’s a bit too slippery here for my liking. I don’t want any of them getting an advantage, so I reach over to my left and pick up a still-lit lantern that got knocked over in the heat of the battle."
        MC "I throw it to the ground and watch the fire explode, melting the ice and allowing me to move freely next turn."

        Z "The action turns the ice into a slight pile of fire, causing you to take a bit of fire damage instead. Would you like to end your turn?"

        MC "I use the rest of my movement to back up since I’m barely out of range for an opportunity attack. I stand near the foot of the bed, leaning against it on my left side, sort of out of breath."

    elif player_choice == "walk":
        Z "You’re gonna roll a D20 and add your acrobatics bonus if you have any."
        
        "You pick up the shining dice and give them a light toss.{nw}"
        play sound "audio/sfx/d20-roll.ogg"
        extend " It spins around on the table, eventually landing on a 17 right by your wrist."

        Z "Congratulations! You passed the check! Instead of slipping and falling on your ass, you’re able to move freely. What do you do?"

        MC "Let’s see...{w=0.3} I back up so that I’m not within the ice’s range anymore, standing right at the foot of my bed. In my traveler’s sack underneath it, I dig my hand inside and pull out a vile of chemical flames."
        MC "I aim it to where it hits all of the bandits to the left of you. The fire spreads and hits the discarded lantern right next to the ice pile, effectively melting that as well."

        show Zander shocked pose2 at waist_up_left3, pop with dissolve
        Z "My days! That almost hit me!"

        MC "But it didn’t! We need to take risks if we’re going to defeat these guys once and for all. I end my turn."
        
        show Zander neutral at waist_up_left3
        Z "{w=0.2}.{w=0.2}.{w=0.2}."

    # [Choice End]
    "The battle continues onward. Even at level 1, your heart pounds at the adrenaline rush. You didn’t expect this level of excitement at all. It feels as though you’re actually in that inn room with how descriptive and immersed you feel with Zanny."
    "He allows the scene to flow smoothly, taking on the burden of details. This enables you to act out to your heart’s desire."
    "Whether it’s playful banter or in-depth depictions of wounds, you’re having a blast creating this fantasy world. It practically makes you forget about all your real-life priorities in the moment."
    "After a few more minutes, the battle reaches its end. Only one bandit remains, standing alone between you and Zanny."

    MC "My turn right?"

    play sound "audio/sfx/d20-roll.ogg"
    "You roll the die."
    "It lands on the cute creature drawn onto the purple luminescent material."

    show Zander excited at waist_up_left3, pop
    Z "Well, I’ll be damned! A Nat 20! Go ahead and describe a critical hit for me."

    MC "Hmm..."
    hide Zander with dissolve

    # [Choice Start]
    menu:
        "Dramatic":
            $ player_choice = "dramatic"
        "Calm":
            $ player_choice = "calm"

    
    if player_choice == "dramatic":
        MC "Without any hesitation, I deliver the final blow. They beg for mercy, but I have none if it! These bandits came into our room, tried to steal our belongings, and interrupted our peace!"
        MC "I laugh as the bandit crumples to the ground, weapon triumphantly raised in the air."
        show Zander shocked at waist_up_left3, pop with dissolve
        Z "My days..."

    elif player_choice == "calm":
        MC "I am exhausted. We still have to get up early tomorrow morning. I put the bandit out of their misery with a quick and clean blow. They collapse, and the battle is finally over."
        show Zander neutral at waist_up_left3 with dissolve
    # [Choice End]

    # [End Fantasy Battle Track]
    # [Fantasy Ambiance Track Start]
    show Zander neutral pose2 at waist_up_left3
    Z "Your final attack depletes their HP, and they fall to the ground. One of the attackers is still conscious off to the side, groaning on the floor with their hand clutching their shoulder. What would you like to do?"

    MC "Well...{w=0.3} we should probably ask for information, right?"

    Z "Smart thinking—I like it. And how would you like to do that?"

    # [Choice Start]
    hide Zander with dissolve
    menu:
        "Threaten with force.":
            $ player_choice = "force"
        "Have a calm conversation.":
            $ player_choice = "calm"

    if player_choice == "force":
        MC "I walk up to the bandit and point my weapon right at their neck. It barely touches the skin, but puts enough force to add a sense of danger. \"Tell me right now or else this dagger will be the last thing you see.\""

        show Zander shocked at waist_up_left3, pop with dissolve
        Z "\"F-Fine! Fine! My group was sent to kill you!\""

    elif player_choice == "calm":
        MC "I walk up to the bandit and kneel beside him with a smile, knowing that they’re too weak to fight now. \"So now that we've got the introductions out of the way, I need you to answer this. What was your goal in trying to kill us while we were sleeping?\""

        show Zander neutral pose2 at waist_up_left3 with dissolve
        Z "{w=0.2}.{w=0.2}.{w=0.2}."

        MC "\"Silence, huh? Did this previous battle mean nothing to you?\""

        Z "The bandit grits his teeth, internally contemplating his next course of action. After a few seconds of awkward silence, he dramatically sighs, tears starting to form at the corners of his eyes."

        show Zander shocked at waist_up_left3, pop
        Z "\"P-Please don’t hurt me again! My group... We were sent to kill you!\""
    # [Choice End]

    MC "Elaborate."

    show Zander shocked at waist_up_left3, pop
    Z "T-There's a famous Port City called Sanwyn! I heard a lot about that area... I swear that's all I know! We were told to stake out inns and take out all the other people searching for Avallum! That's all! P-Please don't kill me!"

    MC "Thank you for your compliance. I won't kill you…for now. So go ahead and get out of here."

    show Zander neutral pose2 at waist_up_left3
    Z "The remaining bandit hastily begins dragging his buddies out of the bedroom. After the battle, an eerie silence settles over the travelers."
    Z "Looks like your journey has only barely gotten started. We gather our bearings and sit back down, going over what just took place."

    MC "The bandit mentioned something called \"Avallum.\""

    show Zander neutral at waist_up_left3
    Z "Avallum? Like the legendary place?"

    MC "You know what that is?"

    Z "I've only heard about it in passing...{w=0.3} It's supposedly a place capable of granting wishes. I hear that only crystals are capable of guiding you there."

    MC "Crystals? Legends? Sounds like there’s something brewing in this continent that’s bigger than we thought. I don’t think we should get involved..."

    show Zander excited pose2 at waist_up_left3, pop
    Z "Why not? Sounds like a fun adventure to me!"

    MC "I mean, I guess we can look into it. It’s not like we have any other concrete leads. Let’s do it!"

    show Zander neutral at waist_up_left3
    Z "Looks like we're headed to Sanwyn next, then, to search for better clues. But we can look into it more tomorrow morning. Let's get some rest."

    MC "Sounds good."

    Z "You both finally traverse into a stable slumber. After wandering aimlessly for a bit, there's now a clear goal in mind. The journey to find this so-called \"Avallum\" starts early tomorrow morning. Until then, let's end it on a nice night of sleep."

    # [CG End]
    # [Fantasy Ambiance Track End]
    hide Zander with dissolve

    # [BACKGROUND—Club Room]
    scene bg clubroom with fade

    MC "That's it? We're finished?"

    show Zander neutral at waist_up_center3 with dissolve
    Z "This is unnaturally short, more like a scene rather than a story. Even one-shots go for a few hours. For the sake of time, I whipped this up just to show you the basics. We should definitely do it properly one day."

    MC "I would love that! Seems like you and Rosco put a lot of thought into this campaign."

    Z "That we did. A&R is a lot of fun, I’m telling you."

    MC "So? Will I be able to join you in finding Avallum one day?"

    show Zander neutral pose2 at waist_up_center3
    Z "Of course, darling. I'll let you know when we plan on running it in full. You did great for your first time playing. Color me impressed."

    "He smiles, and the two of you stand in silence for a moment. The fatigue of the day finally kicks in full force, and you sadly realize it's time for you to head back. You got {i}way{/i} too carried away."

    MC "I'm feeling a little tired. I think I’m gonna head back."

    Z "Well, what are you waiting for? Go on and get some rest, darling. Don't worry about the mess, I'll clean it up."

    show Zander laughing at waist_up_center3
    "Sorry for getting too carried away there. I'm very prone to distractions, especially when I'm having so much fun."

    MC "It's ok! I love spending time with you, and I was just as immersed as you. In fact, I’m sad it was so short! Thankfully, we already made the ingredients list, so we'll go out and shop for it tomorrow. It'll be quick and easy."

    show Zander neutral at waist_up_center3
    Z "Sounds like a solid plan. Now go on and get some rest."
    hide Zander with dissolve
    "You turn to exit the clubroom. Right before you rest your hand on the door handle, you glance back."

    
    # [Choice Start]

    menu: 
        "Wave him goodbye.":
            $ player_choice = "wave"
        "Give him a hug.":
            $ player_choice = "hug"

    # fullbody
    show Zander fullbody at fullbody_center with dissolve
    if player_choice == "wave":
        "You lift your arm and wave back with a smile."

        MC "Thanks for the fun time. See you tomorrow, Zanny!"

    elif player_choice == "hug":
        "As you glance back, you contemplate for a moment.{nw}"
        # zoom in/walk towards
        show Zander fullbody at fullbody_center, zoomin3
        
        extend " Before you can second-guess yourself, you walk forward and move to envelop him in a brief hug. He indulges in it after a few seconds, securely embracing you back."

        MC "Thanks so much for the fun time. I really enjoyed it."

        "The two of you pull away."
        show Zander flustered fullbody at fullbody_center,zoom_back
        #show Zander flustered at waist_up_center3
        Z "Anytime, darling. I had a lot of fun as well. And we’ll have even more fun tomorrow."

        MC "I'll hold you to that. See you tomorrow!"
        
        Z "Likewise."

        # [Choice End]
        hide Zander with dissolve
        "Reluctantly, you turn back around, set on passing out as soon as you hit your bed. Tomorrow is going to be a long day of preparation."

        # [Day 1 End]