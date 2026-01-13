# Start of Cass Route
label cass_route:
    
    scene bg clubroom
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop
    MC "I'll go with Cass!"

    # change Cass Expression to neutral
    show Cassian neutral pose2 at waist_up_center with dissolve
    C "Alright!"
    C "Do you mind meeting somewhere else first, though? I have some stuff to take care of before we can actually begin."

    MC "Sure! Just text me the location and I'll be there."

    C "Good. Make sure of that."
    hide Cassian with dissolve
    stop music fadeout 1.0
    jump cass_route_day1

label cass_route_day1:
    # [Start of Cass Day 1]
    #Fade out into next Scene
    scene black with fade
    show text "{size=50}Cassian Route: Day 1{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    
    "Despite having been a student at the university for quite a while already, you’re still constantly amazed by just how vast the entire campus is."   
    "You're helping Cass today, and he gave you exact directions towards a place you’ve never even thought to visit before."
    "When you finally arrive, you are struck speechless."

    MC "Holy shit..."
    # Start music: G2 Chill
    # Change scene with Garden without flower
    scene bg cass garden without flowers with fade
    hide black
    play music "audio/music/G2 - Chill.wav" loop
    "In front of you lies a garden, green covering every inch of the place. The shrubs are trimmed to perfection, highlighting the stone fountain sitting beautifully in the center."
    "The water rushes with vigour. It almost seems like it sensed a new visitor and got excited."
    "The garden is far enough away from everything else to appear peacefully silent, free of the chatter of people or rushing footsteps."
    "There are birds that fly past, some even landing for a visit. Though there are no flowers, the buds that are yet to bloom perfectly dot each and every bush, pointing towards the fountain."
    "Of course, standing next to the fountain is the man you were meeting for today."
    "He looks up at the sound of you entering, giving you a casual smile and a wave."

    # Change Cass Expression to neutral
    # switch Cass asset fullbody center
    # show Cassian neutral at waist_up_right with moveinright/fade?
    show Cassian fullbody pose2 at fullbody_center with dissolve
    C "You came."

    "The tranquil feeling abruptly leaves your body as you raise your hands in the stop motion."

    MC "Woah. Maybe we should rephrase that."
    show Cassian fullbody at fullbody_center
    "He rolls his eyes at you, but you can see him holding back laughter."

    # Change Cass Expression to C_Bruh
    show Cassian fullbody bruh at fullbody_center
    C "You’ve {i}arrived{/i}. You’re {i}approaching{/i} me."

    MC "I {i}am{/i} approaching you!"

    

    play sound "audio/sfx/running.ogg" volume 0.5
    show Cassian bruh fullbody at fullbody_center, zoomin2
    show black at truecenter onlayer zero
    show bg cass garden without flowers at screenshake
    pause 1
    #hide Cassian
    #show Cassian at waist_up_center
    "You grin at him as you skip over, managing to dodge his attempt of bonking you on the head."
    
    # Change Cass Expression to C_Laughing
    show Cassian laughing fullbody at fullbody_center2, pop
    C "Shut the fuck up."
    # Change Cass Expression to C_Neutral
    show Cassian fullbody at fullbody_center2
    C "Anyways, do you like the garden?"


    "He lifts his arms up to point around, spinning a little as well in an act of showmanship."
    "And it’s truly a beautiful garden. But do you really wanna give him that satisfaction right now? Or should you look him in the eyes and properly praise him for his hard work?"
    
    hide Cassian with dissolve

    # [Choice Start]

    menu:
        "Tease him.":
            $ player_choice = "tease"
        "Praise him.":
            $ player_choice = "praise"

    if player_choice == "tease":
        show Cassian at waist_up_center with dissolve
        MC "It’s alright, I guess."

        # Change Cass Expression to C_Shocked
        show Cassian shocked at waist_up_center, pop
        C "{i}Alright?!{/i}"
        C "What do you mean \"{i}alright{/i}!?\""


        MC "Hey, it’s pretty, okay? I just expected more flowers."

        "You shrug, snickering at the look on his face."

        #Change Expression to C_Smug
        show Cassian smug pose2 at waist_up_center

        C "Alright then. Next time they bloom, you’ll be the first to see."


        MC "{i}Awww{/i}—"
        scene bg cass garden without flowers at vpunch
        show Cassian at waist_up_center
        "He shuts down your teasing tone immediately by successfully bonking you on the head this time."
        "You laugh as you rub the top of your head. Man. He really didn’t spare any strength at all, huh?"

        #Change Expression to C_Bruh
        show Cassian bruh at waist_up_center
        C "Shut up. Do you want to spend the entire day arguing here?"

        MC "Wait, yeah... We do that enough in the clubroom already."

        C "Right. Sure. You’re sooo right."


        "As he throws you a deadpan glare and a bucket of sarcasm, he pulls out a piece of paper from his pocket."

    elif player_choice == "praise":
        show Cassian at waist_up_center with dissolve
        MC "It's very pretty! You did such a good job with it."

        "You take another moment to look around the entire place. The green surroundings really compliment the man in front of you, fitting right in with his green top."

        MC "It suits you too~"

        #Change Expression to C_Sus
        show Cassian suspicious at waist_up_center
        C "What do you mean by that?"


        MC "Look at you! You're green. And this place doesn't need flowers to look pretty, you're pretty enough to make up for it."

        #Change Expression to C_Laughing
        show Cassian laughing pose2 at waist_up_center, pop
        C "Aww, thank you!"


        "He lets out a little \"teehee,\" making the both of you laugh at his rather cute reaction."

        #Change Expression to C_Neutral
        show Cassian neutral at waist_up_center
        C "You're right, though. It would be prettier with flowers."
        # change Cass Expression to C_Hopeful
        show Cassian hopeful at waist_up_center
        C "Hey, how about I take you back here when they {i}do{/i} bloom? Then you'll see the extent of my hard work."


        MC "I’ll look forward to it! Better keep your word~"

        #Change Expression to C_Laughing
        show Cassian laughing at waist_up_center, pop
        C "Of course I will!"

        "He pulls out a piece of paper from his pocket with a bright smile on his face."

    # [Choice Ends]

    MC "What’s that?"

    #change Expression to C_Smug
    show Cassian smug at waist_up_center
    C "{i}This{/i} is a full list of everything we need for the stand on the day of the festival. I made sure to ask the others about what they think we'd need and did a little research on any other equipment that might be required."


    MC "You're prepared, huh?"

    #change Expression to C_Neutral
    show Cassian neutral at waist_up_center
    C "Of course I am!"
    C "Now, since we're setting up a crepe stand—"

    "You cut him off with the sound of your giggling."

    #change Expression to C_Bruh
    show Cassian bruh at waist_up_center
    C "Now what's that about?"


    MC "Nothing... You have a unique way of pronouncing the word \"crepe.\""


    C "I pronounce it the right way."


    MC "Uh huh. That's cute."

    #change Expression to C_Shocked
    show Cassian shocked at waist_up_center

    C "...{w=0.5} What?"
    show bg cass garden without flowers at camerapanleft
    hide Cassian shocked with easeoutleft #maybe just hide without effect
    #MC move head away from Cass /scene move maybe?
    "You turn away from him purposefully to look at the ripples of water in the fountain. How pretty! Some of the water splatters onto the stone base, a little on the ground. You wonder just how fast the water is moving."
    show bg cass garden without flowers at camerapanright
    show Cassian shocked at waist_up_center with easeinleft
    #MC moves head back towards Cass /scene move maybe?
    "Your eyes return to his still stunned gaze when you realize he hasn't continued talking."
    "{i}Don't laugh, don't laugh.{/i}"

    MC "The stand?"

    #change Expression to C_Soft
    show Cassian soft at waist_up_center
    C "Right...{w=0.5} Anyway, since we're setting up a {i}crepe{/i} stand—"
    #change Expression to C_Neutral
    show Cassian neutral pose2 at waist_up_center
    C "Here's everything that needs to be bought. We'll be heading to the appliance store later today to make sure we have everything we don't already have. On that note, mind double-checking the list?"


    MC "Sure! Let me see that..."

    show Cassian neutral at waist_up_center
    "He turns the paper over to you and you start reading off the top of the list."

    MC "Hm... round griddle greaser... wooden spreader..."
    stop music fadeout 1.0
    # Wind blows
    play sound "audio/sfx/wind-gust.ogg" volume 0.6
    pause 0.3
    show Cassian neutral at waist_up_center, trembling
    pause 0.5
    show Cassian panic pose2 at waist_up_center, pop
    "As you reach out to grab the paper—your fingertips barely grazing the side—the breeze gets stronger and blows the paper out of his hands."
    
    #change Expression to C_Panic
    show Cassian panic pose2 at waist_up_center, shake2
    C "NO!"
    

    "You both watch with horror as the piece of paper flies away. With the most miserable stroke of luck ever, it lands straight into the fountain and they lose sight of it the moment it sinks deeper into the water."

    MC "That did not just happen."

    
    "Cass rushes towards the fountain, having to push aside and even kneeling in the bushes that surround it."
    # Add Sound effect Water splashing
    show Cassian panic at waist_up_center, bounce
    pause 0.5
    show Cassian panic at waist_up_center
    pause 0.3
    play sound "audio/sfx/watersplash.ogg" volume 0.05

    
    "He dips his arms into the water and tries to find where the paper could have traveled to. His efforts spark you to move as well, doing the same on the other side of the fountain."
    
    show Cassian panic at waist_up_center, restless
    C "Where is it?! Where could it have gone???"

    MC "We'll find it! We'll find it for sure!"
    MC "... Or at least pieces of it..."

    # Change Expression to C_Angry
    show Cassian angry pose2 at waist_up_center, pop
    C "Don't say that!"

    show Cassian angry at waist_up_center
    "The two of you splash around more, but to no avail. There seems to be no trace of the list anywhere."
    "Cass raises his wet arms out of the water, shaking the droplets off with an edge of frustration."

    
    C "This is so stupid..."

    # Change Expression to C_Upset
    show Cassian upset at waist_up_center
    "His expression shifts. The sharpness of his irritated look warps into one of dejection."

    
    C "How will we be able to buy what we need now? We have to do it today, and time is moving faster by the minute..."


    "You walk over to him, also shaking off the water from your arms. You hesitate to react to his words after seeing his disappointment laid out so clearly in front of you."
    
    C "The other guys are all doing their best to help and then..."


    "No way! There's no way you can hesitate now."

    MC "It's okay!! I still remember some of what I read, and you wrote it. Between the two of us, I think we can cover everything and get what we need by today if we leave now!"

    # Change Cass Expression to C_Hopeful
    show Cassian hopeful at waist_up_center
    C "You think so?"

    "He still looks pretty pensive. You give him as bright a smile as you can muster and nod your head with enthusiasm."

    MC "Yeah! Wouldn't you say your memory is good?"

    # Change Cass Expression to C_Thinking
    show Cassian thinking pose2 at waist_up_center
    C "I mean... If you ask me anything about Mythic Eleven, I'll be able to answer it."
    
    "You can't help but let out a sincere laugh. Of course he would mention one of his favorite games in this situation."
    "{i}Of course{/i} it would help cheer him up."

    MC "See? We got this!"
    MC "We gotta get there soon so we can browse through what we'll need."
    MC "I got your back if you got mine?"

    # Change Cass Expression to C_Neutral
    show Cassian neutral at waist_up_center
    C "Sure. Let's do our best, then."

    # fade out to Background Appliance Store
    scene bg cass appliance store with fade
    # Start music C1 (2)
    play music "audio/music/C1 - Chill (2).wav"

    MC "...{w=0.5} I should go shopping more."

    "You try to ignore the mocking snicker behind you. It takes you a little more time than the average person to find the kitchen appliances section in this huge store."
    "How were you supposed to know it would be on the opposite side of the store from the entrance?!"
    "Besides, it's not like your {i}trusty{/i} companion is of any help!"

    MC "Shut up! You literally didn't even help. Don't talk!"

    # Change Cass Expression to C_Laughing
    show Cassian laughing pose2 at waist_up_center, pop with dissolve
    
    C "What do you mean?? I held your hand and guided you through the store!"


    MC "AFTER watching me fumble through different aisles???"

    # Change Cass Expression to C_Smirking
    show Cassian smirking at waist_up_center
    C "That seems like a you problem."

    #Turning Head away from Cass n switch background to tools and equipment
    show bg cass appliance store at camerapanleft
    hide Cassian smirking with easeoutleft
    
    "You turn away from him, looking at the display of tools and equipment in front of you."
    "Right. Now all you have to do is look for the things you need, which are all written down on the list..."

    MC ".{w=0.3}.{w=0.3}.{w=0.3} Uh...{w=0.3} We needed a girdle greaser or something...{w=0.3} right?"

    # Change Cass Expression to C_Bruh
    show bg cass appliance store at camerapanright
    show Cassian at waist_up_center with easeinleft
    show Cassian bruh at waist_up_center
    C "...{w=0.3} I thought {i}I{/i} was the ESL in this club."


    MC "I DON'T KNOW! What was it then, huh?"


    C "{w=0.3}.{w=0.3}.{w=0.3}."
    # Change Cass Expression to C_Neutral
    show Cassian neutral at waist_up_center
    C "Let's just look around for now! We'll remember it when we see it."
    hide Cassian with dissolve

    pause 0.5
    #Maybe add headshake animation
    show bg cass appliance store at headshake
    "You shake your head in exasperation. How long are you two gonna be in this store?"
    "As you look around, though, seeing all the cool equipment is actually more fun than you thought it would be. Hell, there are some you haven't even heard of before. With really unique designs too!"
    "But maybe you should stay professional and point out the equipment the club would {i}actually{/i} need..."

    # [Choice Start]
    menu:
        "Point out the fun appliances.":
            $ appliance_choice = "fun-appliances"
        "Point out the normal appliances.":
            $ appliance_choice = "normal-appliances"

    if appliance_choice == "fun-appliances":
        "To hell with being normal! You're sure Cass is also seeing all these designs and wanting to comment on them anyway. Might as well take the first step."

        MC "That is a crazy design for a stand mixer."

        "Cass looks over to where you're pointing, laughing at the cartoon face printed on the sides of the bowl and the mixer itself."
        
        # Change Cass Expression to C_Laughing
        show Cassian laughing pose2 at waist_up_center, pop with dissolve
        C "What the hell? Is it sticking its tongue out?"

        MC "It's feeling a little silly today, Cass."

        "His responding laugh is cut off by your gasp as you grab his arm and spin him towards a shelf. He reacts before you could even point out what you saw."
        
        
        #Asset "Crepe maker Dingding" appears
        show Cassian at waist_up_right_for_asset with move
        pause 0.5
        show Crepe maker Dingding at asset_center with dissolve
        pause 0.5
        C "Holy shit, {i}Pipmon{/i}."

        MC "That's a {i}Pipmon{/i} crepe maker... We need that for the stand."
        # Change Cass Expression to C_Thinking
        show Cassian thinking pose2 at waist_up_right_for_asset
        C "...{w=0.5} It's cool and all, but for the stand? Really?"
        show Cassian thinking at waist_up_right_for_asset
        MC "Yes! We're buying it. It has the Gen 1 starters! It has Dingding on it! I'm enabling you."

        # Change Cass Expression to C_Neutral
        show Cassian neutral at waist_up_right_for_asset
        C "What the hell. Sure."
        # Asset "Crepe maker with Dingding" dissapears
        hide Crepe maker Dingding with dissolve
        show Cassian at waist_up_center with move
        # Change Cass Expression to C_Laughing
        show Cassian laughing at waist_up_center, pop
        "You both giggle as you take pictures of the crepe maker. You absolutely have to show them to the rest of the guys! They'll want to buy it too, surely."

        C "You know, I bought a booster pack for myself after finishing some important projects."

        MC "Damn! Nice~ Did you get lucky or was it a bust?"

        # Change Cass Expression to C_Hopeful
        show Cassian hopeful at waist_up_center
        C "Well...{w=0.5} I got the Gobblycook holo that was said to be really rare!"

        MC "Nice one! That was deserved, if you bought it to reward yourself for the projects. You'll have to show me the card sometime."

        # Change Cass Expression to C_Winking
        show Cassian winking at waist_up_center
        C "I'll bring it over to the club when I can."

        MC "Sure thing! And then I'll steal it~"

        #Change Cass Expression to C_Angry
        show Cassian angry at waist_up_center, pop
        C "Nuh uh. Don't you fucking dare—"

        MC "Cass, wait, don't look behind you but there's a starter Pipmon kettle right behind you and it's a water type."

        # Change Cass Expression to C_Sus
        show Cassian suspicious pose2 at waist_up_center
        C "... Is it Bibble?"
        
        "You break down into giggles while looking back at the Bibble kettle that's staring into your soul. This is {i}way{/i} better than collecting cards."
        show Cassian suspicious at waist_up_right_for_asset with move
        #hide Cassian with dissolve
        # Asset "Bibble kettle" appears and dissapears
        pause 0.5
        show Bibble kettle at asset_center with dissolve
        pause 2
        hide Bibble kettle with dissolve
        show Cassian suspicious at waist_up_center with move
        # Change Cass Expression to C_Hopeful
        show Cassian hopeful at waist_up_center
        C "Wait, isn't that the Pipmon that Ryzar really likes? From the new gen?"
        
        "Turning back, you spot a rice cooker. A green rice cooker in the design of a dinosaur with wheat tails."
        show Cassian hopeful at waist_up_right_for_asset with move
        pause 0.5
        # Asset "Paddyraptor rice cooker" appears
        show Paddyraptor rice cooker at asset_center with dissolve
        pause 0.5
        MC "Wait, we need that."

        # Change Cass Expression to C_Bruh
        show Cassian bruh pose2 at waist_up_right_for_asset
        C "The—The Paddyraptor rice cooker? No, no, we don't need that."
        # Asset "Paddyraptor rice cooker" dissapears
        hide Paddyraptor rice cooker with dissolve
        show Cassian bruh at waist_up_center with move
        MC "But!"

        C "We have a perfectly fine rice cooker in the club room already! And literally only Rosco and Luci use it!"

        MC "It will get us more likeability points from Ryzar and maybe the festival organization committee will forgive us for procrastinating—"
        
        C "Nuh uh. You might be able to bribe Ryzar, but the rest of the committee won't forgive us so easily. Drop the rice cooker, now!"

        MC "Ehh, so bossy. What are you? The military?"

        # Change Cass Expression to C_Smirking
        show Cassian smirking pose2 at waist_up_center
        C "Funny you mention that..."

        MC "???"

        hide Cassian with dissolve

        "The both of you continue to argue and joke around. Half the time is spent pointing out the funny designs and debating on whether or not you guys need these things in the club."

        "(You absolutely do need them, and you will continue insisting on it. Cass is a little more reluctant, but he'll give into almost anything if you bribe him with gacha.)"

        "The other half is spent picking out the things you {i}actually{/i} need based on what you remembered. Despite being distracted, you're 98.7\% sure you got everything you needed."

        "And though the loud laughter from you two gets the staff to quickly process your purchases and promptly kick you both out of the store—there was some good progress made and many boxes to carry back to campus!"

        "Mission success!"

    elif appliance_choice == "normal-appliances":
        "Yes, you should probably stay normal and stick to what you actually need."

        "You turn away from the colorful items and focus on the sleek, monochrome appliances. They all look shiny and cool—wonderful additions to the stand on the day of the festival!"

        MC "I think this was on the list you wrote... right?"

        # Change Cass Expression to C_Confused
        show Cassian confused at waist_up_center with dissolve
        C "What is that? Wait, read the name—"

        "You two browse through the selection of items, discussing and debating over which ones to buy."

        MC "That one's cool... But maybe too expensive?"

        # Change Cass Expression to C_Thinking
        show Cassian thinking pose2 at waist_up_center
        C "Hard to find good ones that aren't a little over our budget."
        show Cassian thinking at waist_up_center
        "You shrug. Not much you two can do about that. Maybe the festival organization committee will forgive you for how much you spend if you make your stand extra awesome!"

        MC "If we buy something good, we can keep it in the dorm and it will last until the end of time!"

        "You approach a random small appliance, not bothering to read the name. Surely something of this size and shape can be used for crepes?"

        MC "Like this!"

        #Asset "Strawberry stem remover" appears
        show Cassian at waist_up_right with move
        pause 0.5
        show Strawberry stem remover at asset_center with dissolve
        pause 0.5
        # Change Cass Expression to C_Bruh
        show Cassian bruh at waist_up_right
        C "{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3} We do not need a strawberry stem remover in the clubroom."
        
        "...{w=0.3} Oh."
        "Wait, on second thought—"
        # Asset "Strawberry stem remover" dissappears
        hide Strawberry stem remover with dissolve
        show Cassian bruh at waist_up_center with move

        MC "But look at it... I didn't know these things existed. We could use it!"

        "Surely it can be used somewhere. At this point, you're a little too stubborn to pull back."

        C "Where will we use—We don't even have a basket of strawberries in the clubroom!"

        MC "Well, what if we happen to collect {i}one singular strawberry{/i}?"

        C "{w=0.5}.{w=0.5}.{w=0.5}."
        hide Cassian with dissolve

        "You end up buying the stuff you need that's only a little over budget. No big loss! Success!"
        "(You'll sneak in that strawberry stem remover somehow.)"
    stop music fadeout 1.0
    # [Choice Ends]

    # Fade out into Clubroom
    scene bg clubroom with fade
    
    play music "audio/music/C1 - Chill (1).wav" fadein 1.0 loop

    "You both return to the clubroom, boxes full of appliances ready to unload."
    "You set to work, giggling about the occurrences and jokes from earlier. You open up some of the boxes and pull out..."
    show screentint with dissolve
    show Measuring cups at asset_pos1 with dissolve   
    show Ladles at asset_pos2 with dissolve
    show Crepe maker at asset_pos3 with dissolve
    show Wooden spreaders at asset_pos4 with dissolve
    

    if appliance_choice == "fun-appliances":
        "A Pipmon crepe maker, Pipmon measuring cups, and some wooden spreaders."
        #Assets "Crepe maker with Dingding", "Gobblycook measuring cups", and "Wooden spreaders/ladles" appears and dissapears

    elif appliance_choice == "normal-appliances":
        "A crepe maker, measuring cups, and some wooden spreaders."
        #Assets "Normal crepe maker", "Normal measuring cups", and "Wooden spreaders/ladles" appears and dissapears
    
    hide Wooden spreaders with dissolve
    hide Crepe maker with dissolve
    hide Ladles with dissolve    
    hide Measuring cups with dissolve
    hide screentint with dissolve
    # [Options End]

    "As you are working, though, you notice Cass abruptly pause in the middle of unboxing one of the equipment."

    
    MC "Yo, Cass? What's up?"

    "The mood switches, and you see Cass' neutral expression shift into one of irritation."

    show Cassian at waist_up_center with dissolve
    # Change Cass expression to C_Upset
    show Cassian upset at waist_up_center
    C "...{w=0.5} We bought an electric crepe maker."

    MC "...{w=0.5} Oh?"

    "You make a noise of confusion, not quite getting the gist of what he's saying."
    "So? It's a crepe machine. You don't quite understand what the problem is here."
    "But you want to understand him."

    C "... We were meant to buy a gas crepe maker."
    stop music fadeout 1.0
    MC ".{w=0.3}.{w=0.3}.{w=0.3} Oh."
    
    "From what you know, gas crepe makers are better for faster and more efficient ways of making crepes. It would make Luci's job so much easier on the day of the festival!"
    "And neither of you were able to get one, apparently..."

    MC "Well, we couldn't have known—"

    #Change Cass Expression to C_Thinking
    show Cassian thinking pose2 at waist_up_center
    C "We {i}could{/i} have. If we kept the list safe."
    show Cassian thinking at waist_up_center
    play music "audio/music/G4 - Sad.wav" fadein 1.0 loop
    "The sigh of frustration he lets out silences any other words you want to say. It seems the series of inconveniences throughout the day added a lot of weight on Cass' shoulders."
    
    MC "I'm sorry, Cass, I—"

    # Change Cass Expression to C_Upset
    show Cassian upset pose2 at waist_up_center
    C "No, it's my fault. I should have prepared an extra just in case things don't go perfectly—"
    show Cassian upset at waist_up_center
    MC "You couldn't have predicted that. And surely, an electric crepe maker won't make that much of a difference."

    C "But what if—"
    hide Cassian with dissolve

    menu:
        "Call his name.":
            $ player_choice = "call"
        "Hug him.":
            $ player_choice = "hug"

    show Cassian upset at waist_up_center with dissolve

    if player_choice == "call":

        MC "Cassian."

        "Your serious tone cuts him off and catches his attention immediately. Suddenly, in the silence and solitude of the clubroom, you only see each other."

        MC "Luci won't blame you; neither will any of the other guys. The list getting lost was not your fault. This is just one tiny slip up."

        "You walk closer to him and lightly place your hand on his, giving him a gentle smile."

        MC "You did your best today and you put in so much effort already."
        MC "You always make sure that the rest of the boys and I are happy. For that, we can't be more grateful."
        MC "We are very, {i}very{/i} proud of you."

    elif player_choice == "hug":
        "His words get cut off when you suddenly close the distance and wrap him in an embrace."

        "You're not quite sure what expression he's making at the moment, but you feel his arms slowly place themselves on your back as well, reciprocating the hug."

        "For a long time after, neither of you say anything more. You simply remain hugging, his arms growing tighter around you."

        "The first one to speak up is you."

        MC "None of this is your fault, okay? Not everything has to end up perfect all the time."

        "You move away from his warmth, looking him in the eyes and giving him a small grin."

        MC "Haven't we gone with the flow of things so far? Our club isn't full of level 1 players, you know."

    # [Choice Ends]

    C "I know... I just didn't want to cause any more trouble for the rest of you."
    
    MC "So what if you do? We cause trouble every moment of our lives, whether we intend to or not."

    MC "What's important is we're all there to hold each other back and cheer each other on when we need to."

    MC "Cass, I'll {i}always{/i} have your back."

    MC "Just like you always have mine."

    "There's a round of silence as you gaze into his eyes, almost like breaking eye contact would make you look any less sincere."

    "You watch as his expression shifts, and the tension leaves his shoulders. There's lingering warmth in the air now, your smile growing alongside his."

    # Change Cass Expression to C_Relieved
    show Cassian relieved at waist_up_center
    C "I think... Nothing I say can truly express how much you mean to me."

    MC "That's fine. I get what you mean."

    C "No. You need to hear it."

    #Change Cass Expression to C_Soft
    show Cassian soft at waist_up_center
    C "Thank you."
    C "So much."
    C "For being a part of my life."

    #Change Cass Expression to C_Relieved
    show Cassian relieved at waist_up_center
    C "Even if time does its damage and we can't be present in each other's lives anymore..."
    C "I'll always cherish the memories we've made so far, and they shall be woven into gold for eternity."

    "The words of appreciation catch you slightly off guard. It's not like Cass is particularly stingy about compliments and reassurances, but..."
    "You kinda wanna cry a little."
    "Just a little."

    # Change Cass Expression to C_Soft
    show Cassian soft at waist_up_center
    C "I hope... We're able to make many more memories together."

    MC "Many many more memories?"

    # Change Expression to C_Relieved
    show Cassian relieved at waist_up_center
    C "Pfft. Many many more memories."
    show Cassian laughing at waist_up_center
    "You both share a laugh, the atmosphere much lighter and cheerier than earlier."
    stop music fadeout 1.0
    # switch to C1???
    pause 1.0
    play music "audio/music/C1 - Chill (1).wav" fadein 1.0 loop

    show Cassian relieved at waist_up_center
    "You're glad. It's definitely better to see Cass being happy and comfortable than being troubled and uncomfortable."
    MC "Well then, let's continue unpacking for now and setting the equipment aside for the day of the festival. Hm... We can discuss the stuff needed for the game showcase tomorrow."

    "Cass nods, but you see a teasing smile slowly growing on his face."

    # Change Cass Expression to C_Smirking
    show Cassian smirking pose2 at waist_up_center
    C "You're moving fast now. Are you getting shy all of a sudden?"

    "There we go. He's back to being annoying, just like the Cass you know and love."
    "You can't help but roll your eyes."

    MC "{i}Maybe{/i} I just need to get home early tonight so I can wake up early tomorrow."

    # Change Cass Expression to C_Confused
    show Cassian confused at waist_up_center
    C "Eh? Do you have an agenda before meeting me?"

    MC "Yeah. I'm going on a date."

    "You snort at your own joke. Really. With this crunch time for the festival? None of you have any time to go out and meet anyone new."
    "You set aside the now empty box and turn to Cass to help with his, only to pause at the strange look on his face."

    # Change Cass Expression to C_Sus
    show Cassian suspicious at waist_up_center
    C "You're going on a {i}what{/i}."

    "You're taken aback by the darker tone in his voice, letting out an awkward laugh."

    MC "It was a joke... Do you think I can't pull or something?"

    # Change Cass expression to C_Soft
    show Cassian soft at waist_up_center
    C "No...{w=0.3} Just..."

    "He turns away from you and you hear him let out a sigh."
    "A sigh of what? You're not quite sure. He might just be mocking you for having no game."

    MC "Okay, joke's over. Are you done with that?"

    "He looks back at you, composed with not a single mischievous emotion on his face."
    "In fact, he looks rather satisfied."

    #Change Cass expression to C_Smug
    show Cassian smug pose2 at waist_up_center
    C "Yes. Can you take the box and put it there with yours, please?"
    show Cassian smug at waist_up_center
    MC "Sure."

    "As you go to take the box, the placement of your hands overlap each other's, and you feel his fingers touching yours."
    "The feeling lingers even as you take the box from his hold and he pulls away to set aside the equipment."
    "Huh. It's warm."

    MC "Alright, I think I'll head home for now."

    # Change Cass Expression to C_Neutral
    show Cassian neutral at waist_up_center
    C "Sure. I'll lock up here. Same time tomorrow in the clubroom, okay?"

    MC "You got it."

    "You take your stuff and step through the clubroom door. As you're leaving, you look over your shoulder and give Cass a small wave."
    hide Cassian with dissolve
    scene black with fade
    stop music fadeout 1.0
    "The door slowly closes, but before it could fully shut, you hear a small whisper from him."

    C "...{w=0.5} Do I have to be more straightforward?"

    "The clubroom door shuts. You can't go back in to ask."
    "What was that about...?"
    "Well."
    "You trust him. It should be nothing important."
    "Right?"



    # [End Day 1]
    jump cass_route_day2

label cass_route_day2:
    # [Start of Cass Day 2]
    scene black with fade
    show screentint
    show text "{size=50}Day 2{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    hide screentint
    scene bg clubroom with fade
    # start of music c1 (2)
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop
    "You arrive in front of the clubroom, refreshed and ready for another day. If you remember correctly, you'll be gathering supplies for the game showcase."

    MC "Alright! Let's do this!"

    "Entering the room, you're surprised to see Cass already there, facing away from you. Hoping to scare him a bit, you slowly tip toe closer, but small mutterings stop you in place."

    show Cassian thinking pose2 at waist_up_right with dissolve
    # Change Cass EXpression to C_Thinking
    C "Are you...{w=0.5} ten I see,{w=0.5} what? {w=0.5}.{w=0.5}.{w=0.5}.{w=0.5} Ohhh."

    "What is bro talking about? Curious, you try to listen in. After all, patience is a virtue..."

    C "...{w=0.5} U {w=0.5}R {w=0.5}A {w=0.5}Q {w=0.5}T—{w=0.5}wait, that one's kinda good!"

    "Yeah, yeah, virtue your ass. There's no way you're waiting here longer!"
    show Cassian thinking at waist_up_center with easeinright
    MC "Hey, Cass, what are you doing?"
    
    # Change Cass expression to C_Panic
    show Cassian panic at waist_up_center, shake2
    C "UWAHAHH—"

    "Ah yes, the signature Cass scream."

    # Cass sprite sudden movement of surprise
    show Cassian panic at waist_up_center, singlejump
    "Spooked, he quickly turns toward you, eyes wide. You notice a stack of cards in his hands, must've been what he was focusing on."

    MC "Uh, you alright there, dude?"

    "Cass stares at you like a deer in headlights."

    C "...{w=0.3} D."

    MC "Dee?"

    C "D...{w=0.3} you..."

    "Did you break him??"
    "A few more moments pass without a single word from Cass; it's quite concerning."

    MC "Umm, Cass? You there?"

    C "O-{w=0.5}oh ummm, yeah.{w=0.3} Right here.{w=0.3} Uh, hold on—"

    show Cassian panic at waist_up_center, restless
    "Coming out of his stupor, Cass starts to shuffle through his note cards until he finds the right one. All of a sudden, the once lost and confused air around him turns confident and playful."

    # Change Cass Expression to C_Smirking
    show Cassian smirking pose2 at waist_up_center
    C "But enough about me, how you doing, cutie~?"

    "What{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5} Did you hear that right?"

    MC "Uh...{w=0.5} I'm good?{w=0.5} Anyway, what the HELL did you just say to me?!"

    C "What do you mean? You're just so cute I can't help myself."
    # Change Cass Expression to C_Winking ### Finger Gun Winking Sprite
    show Cassian winking fingergun at waist_up_center, pop
    C "In fact, if you were a vegetable, you'd be a cute-cumber!"
   
    "Pointing finger guns your way, he waits for your response; but all you can give is a look of pure disgust."
    # Change cass Expression to C_Neutral ### normal sprite
    show Cassian neutral at waist_up_center
    "Realizing your poor reaction, Cass sadly puts down his hands and starts to leaf through his cards once more."

    # Change Cass Expression to C_Thinking
    show Cassian thinking at waist_up_center
    C "Okay, okay so no on that one,{w=0.3} uhhh{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    show Cassian hopeful at waist_up_center, pop
    extend " AHAH!"

    # Change Cass Expression to C_Smirking
    show Cassian smirking at waist_up_center
    C "I mean, cute like a dog because you're so fetching~"

    "{w=0.5}.{w=0.5}.{w=0.5}."
    "You slowly walk to face your smirking friend, moving to grip his shoulders and holding on as if it's your last strand of sanity... Maybe in this case, it is."

    MC "... Cassian."

    # Change Cassian expression to C_Hopeful
    show Cassian hopeful at waist_up_center
    C "Did you like that one? Was that one good?!"

    "You tilt your head upward, making complete eye contact with his bright eyes."

    MC "... I need you to listen to me... {w=0.3}word{w=0.3} for{w=0.3} word."
    MC "{i}Never{/i}.{w=0.5} Never say that again."
    MC "Never to me or anyone else."

    # Change Cassian Expression to C_Confused
    show Cassian confused at waist_up_center
    C "Wha-{w=0.5}what?"
    
    "The once smug and confident Cass reverts back to his stunned and confused state at your words."

    C "Was that line no good too? W-well, I have other ones, just give me a sec!"

    "Just as the panicked male rushes back to his cards, you tighten your grip to bring attention back."

    MC "{i}{b}No.{/b}{/i}"
    show Cassian disappointed at waist_up_center
    C "B-but{nw}"
    show Cassian thinking at waist_up_center
    extend " I have a few more, like this one!{w=0.3}{nw}"
    show Cassian smirking at waist_up_center
    extend " Hey, did you fall from hea—"

    MC "No more, Cassian. No more."
    # Change Cassian Expression to C_Dissapointed
    show Cassian disappointed at waist_up_center
    "You watch as your words finally sink into Cass, his face falling like a kicked puppy."
    "You'd feel bad; but {i}goddamn{/i}, he was horrible at... whatever he was doing"

    MC "You good now? Got it all out of your system?"

    "All you receive is a small nod from your companion in response. Good enough."

    MC "As much as I'd love to ask what all that was about, we should start getting the equipment. Don't wanna stay too late and get locked in school, y'know?"

    
    C "Right...{w=0.3} all we need for today is in the storage room across the way."

    MC "Alright! Lead the way, Cass!"
    stop music fadeout 1.0

    hide Cassian with dissolve
    show screentint with dissolve
    "Moving aside, you let Cass lead you out of the clubroom to your next task."
    "At the door frame, he suddenly stops to look back at you."
    show Cassian disappointed at waist_up_center with dissolve
    C "[player_name], were they really that horrible?"

    MC "Just keep walking, Cass."
    hide Cassian with dissolve
    "And walk he does."
    "Further down the hallway, Cass stops before a dimly lit room."

    # Background: Dark Storage Room
    scene bg cass storage door pov with fade
    # play music g1
    play music "audio/music/G2 - Chill.wav" fadein 1.0 loop
    "Peering in, you can see the outline of shelves full of miscellaneous objects and stacks of boxes. A line of five plushes catches your eye, staring into your soul. The plushes range from a colorful parrot to a... wait." 
    "What {i}is{/i} that? A taxidermy rat? Um, cool, to each their own, you guess?"
    "At the entrance, you spot all kinds of familiar items decorating the space."
    "You move into the room to get a closer look, keeping in mind to avoid the boxes in your path. The right shelf catches your eye and by just looking over its miscellanea, waves of memories come crashing into you."

    # Background: Storage Room Right Shelf
    scene bg cass storage with fade
    "On the wall is a faint mural of illustrations, giving color to the gloomy room."
    "Along the floor, a sad little box catches your eye titled \"BANNED\" in a large, messy scrawl. Looking in, you see hints of red and green."
    "You realize it was probably those tomato decor you bought that one time... They were on sale and really cute, what were you supposed to do?"
    "As you wrap yourself in old memories, Cass also walks into the room, heading toward the left side for his own exploration."
    "The two of you fall into concentrated silence as you both survey the disorganized shelves. On your shelves, nothing stands out as useful for the festival which is definitely not a good sign... Let's hope Cass is doing better than you at this point."

    # Change Cassian Expression to C_Hopeful
    show Cassian hopeful at waist_up_center with dissolve
    C "Hey, [player_name]! Check it out!"

    "Huh, talk about coincidence!"
    "You turn to Cass, confused, only to see him wearing a hair accessory. Intricate carvings depict the ornament as a pair of wings, wrapping around the head like a crown."
    "Cass looks...{w=0.3} surprisingly nice with it."

    # Change Cassian Expression to C_Smug
    show Cassian smug pose2 at waist_up_center
    C "Sooooo, what do you think? Don't you agree it just fits my {i}elegance{/i}?"

    "There is something about how the headdress frames Cass' face, bringing out features you didn't realize he had. Despite being in such a dark room, you swear Cass' usually brown eyes are sparkling gold."
    "You can't help but admire the {i}strange{/i} man in front of you, completely forgetting the unanswered question sitting in the air."

    C "Wow, it must really suit me?"

    "The playful tone in Cass' voice takes you out of your viewing."

    MC "What?"
    
    C "See, you're even left speechless by my utter beauty, just admit it!"
    show Cassian smug at waist_up_center
    "Cass continues to look at you with a smug yet anticipating stare. Man, he's really begging for a compliment."
    "You try to avoid his awaiting gaze. One part of you just wants to relent, but then there's another side of you that would rather keel over than compliment this idiot in front of you."
    "Looking back at Cass, you're still met his wide and waiting eyes. He's really not gonna let this go, huh."
    "Sighing to yourself, you weigh your current options."
    hide Cassian with dissolve

    menu:
        "Be honest, what's the worst that could happen?":
            $ player_choice = "honesty"
        "Over your dead body, lie to that man!!":
            $ player_choice = "lie"

    if player_choice == "honesty":
        show Cassian at waist_up_center with dissolve
        "Just {i}one{/i} compliment, then it's back to your usual insults."

        MC "Don't let this get to your head but yeah, the hairband suits you really well. Call me crazy or whatever, but your eyes become a pretty gold with it on."

        "Man, that was cheesy."
        "But hey, you're just appreciating your friend's appearance, nothing too weird. Just a buddy being a good buddy. Yep, exactly that and nothing else."

        # Change Cassian Expression to C_Soft
        show Cassian soft at waist_up_center
        C "Oh, um, thank you..."

        "Cass quietly whispers a reply as you turn back to your shelf, hoping to leave the conversation at that—definitely not because you're embarrassed."
        "Unconsciously, Cass raises his hands up to cup at the winged accessory. Did it really look nice on him? Did you really think he was pretty? Cass could feel his ears beginning to burn the longer he thought about what you said."
        "Checking on your companion, you move back to see Cass stuck in the same position, obviously thinking about something else. About what, you'll never know."
        "You call out to him, trying to get his attention 'cause, well, it just hits you that you don't really know what you're trying to find right now."

        MC "Cass? Casssss... HELLLO??"

        # Change Cassian Expressuin to C_Panic
        show Cassian panic at waist_up_center, singlejump
        C "YES!{w=0.5} Sorry, uh, what's up?"

    elif player_choice == "lie":
        show Cassian at waist_up_center with dissolve
        "You are going to be Cass' number one hater to the end, no pretty hair accessory will change your mind."

        MC "If you mean your cockiness, sure. I can feel it all the way over here."

        "Grinning right at Cass, you sarcastically roll your eyes at his antics."
        "Cass jolts back, his hand raising to his chest, an appalled look written all over his face."

        # Change Cassian Expression  to C_Angry
        show Cassian angry at waist_up_center, shake2

        C "HAH?"

        "You can't help but burst out laughing at Cass' reaction. Gosh, he's looking at you as if you insulted his whole bloodline or something."
        show Cassian bruh at waist_up_center
        C "I'll have you know \"Humble\" happens to be my middle name."

        "Cass turns away from you, arms crossed. You really can never be civil to him, can you?"

        MC "Yeah, yeah, whatever you say, Cass."

        "You wave off what he says. After all, Cass has said that so many times that the whole damn dictionary is his middle name."

        # Change Cassian Expression to C_Upset
        show Cassian upset at waist_up_center
        C "W-whatever! Just get to work already. We don't have all day, y'know."
        hide Cassian with dissolve
        "Cass turns away, signaling the end of the conversation. Point to you, zero to Cass."

        MC "Alright, let's find our equipment!"

        "Invigorated to find the equipment, you look over your side of the storage room only to realize you have no idea what you're looking for... Shit."
        "Stumped and a little lost, you look back to Cass, knowing he most likely knew."
        show Cassian upset at waist_up_center with dissolve

    # [Choice End]

    MC "So Cass, what {i}exactly{/i} are we looking for?"

    # Change Cassian Expression to C_Thinking
    show Cassian thinking at waist_up_center
    C "Hm, another PC probably, a few screens and controllers, I guess?"

    MC "Ohhh~ You guess? Did the Great Cassian Floros not come prepared this time?"

    "With a teasing edge to your words, you egg on your friend, hoping for his usual silly and defensive retorts."

    C "Well, I didn't feel like I needed to today. Plus, a certain someone said not everything needs to be by the book, or something like that."

    hide Cassian with dissolve
    "Wowwww, would you look at that? He actually listened to you and your yapping! Hm, maybe you are wise beyond your years."
    "Haha, take that. Who cares if you can't do math, you're THE Enlightened one for real, for real."
    "If you weren't so wrapped up in your head, you might've noticed the blush crawling up Cass' ears. But no, you didn't... because you suck."
    "Enjoying your little taste of victory a while longer, you pass over the many items in front of you."
    "Hm... a mannequin with a pirate hat, a purple crystal in a bowl of fake fruit, random vinyl records, and framed butterflies... Damn, there's really anything and everything in here except for what you need!"
    "If you were anything, though, you are pure, unadulterated stubbornness. You're finding that gaming equipment, even if it's the last thing you do! High and low, you glare into every nook and cranny of the shelf."
    "Your eyes suddenly land on a long wire poking out from the top of the shelf. Ahaha, a wired controller, bingo!"
    "Approaching the bookshelf, you realize how tall it is, the controller just out of your reach."

    MC "Man, you just {i}hate{/i} me, huh? Fine. Be that way."

    "Even on your tip toes, your hand can only brush over the hanging wire, unable to grasp it."
    
    MC "What.{w=0.5} The.{w=0.5} FUCK."

    "Who makes shelves this tall anyway? They're horrible. They don't deserve the cold sides of pillows. May their ankles randomly give out."
    "You mutter a curse under your breath and glare at the wire as if you're waiting for it to magically float down to you."
    "Peering behind himself, Cass looks your way, a little worried."

    show Cassian at waist_up_center with dissolve

    C "Need some help there, [player_name]?"

    "Taking in Cass' words, you begin to wonder yourself. Do you need a hand with this? The shelf is a little too tall for you and you don't want to risk hurting yourself, especially with the festival on the horizon..."
    "But are you really going to let yourself be bested by this skyscraper monstrosity of a shelf? Like, come on, you gotta save {i}some{/i} face."
    hide Cassian with dissolve

    menu: 
        "Accept your fate and ask for help.":
            $ player_choice = "accept-help"
        "Hell no! You got it!!":
            $ player_choice = "deny-help"

    if player_choice == "accept-help":

        show Cassian at waist_up_center with dissolve
        "Better safe than sorry! The last thing you need is to explain to the rest of the boys about how you almost died via a shelf."

        MC "Actually, yeah, I do. Can you grab that for me, Cass?"

        "Pointing upward, Cass follows your hand to the controller wire and without missing a beat, he moves toward you."

        # Change Cassian Expression to C_Smirking
        show Cassian smirking pose2 at waist_up_center
        C "Make way, make way, your knight in shining armour is here to save you!"

        "The witty spirit in Cass' words make you laugh. What a weirdo."

        MC "Call yourself whatever you want, just put your convenient height to use."

        show Cassian laughing at waist_up_center, pop
        "At your words, Cass lets out a soft chuckle."

    elif player_choice == "deny-help":

        show Cassian at waist_up_center with dissolve
        "Vertically challenged or not, you're getting that controller. If the shelf has to come down, it's going down."

        MC "Naw, I got this, Cass! Watch this!"
        hide Cassian with dissolve
        "You search for a steady foothold on the lowest shelf. Once you find it, you hold onto the sides of the shelf and push yourself upward, setting your plan into motion."
        "With the boost, you're nearly there. You can see it! The wire is right within your grasp! You quickly move both hands towards it, ensuring you get the wire this time."
        "Almost, almost{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3} GOT I—wait a minute... WAIT A MINUTE! YOU'RE FALLING!"
        stop music fadeout 1.0
        MC "OH SHI—"

        "Great thinking there, [player_name]! You let go of the shelf and just as that apple guy foretold in physics, GRAVITY HATES EVERYONE!"
        "Out of fear, you let go of the controller that you so stupidly risked your whole life for."
        "You should've written your will; who knows what'll happen to all your treasures now?" 
        "Man, your digital Pipmons will be so lonely. Your Bibble is going to starve without its daily meals, and don't even think about your Paddyraptor—it was so close to evolving!"
        "Welp, you'll die now. There goes it. Goodbye, cruel world."
        "Resigned, you cross your arms over your chest, closing your eyes and letting gravity take you."
        
        # Falling down shake
        show black at truecenter onlayer zero
        play sound "audio/sfx/body-fall.ogg" volume 0.1
        with vpunch

        # Change Cassian Expression to C_Panic
        show Cassian panic at waist_up_center, pop
        C "Woah, I got you."
        play music "audio/music/G2 - Chill.wav" fadein 1.0 loop
        "You let the warm embrace of death take you...{w=0.3} Waitwaitwait, warm?"
        "Confused, you tilt your head upwards, opening your eyes to see familiar hazel staring back at you."

        # Change Cassian Expression to C_Neutral
        show Cassian neutral at waist_up_center
        C "Are you okay, [player_name]?"

        MC "Uhhm, the Grim Reaper's lookin' a little different."

        # Change Cassian Expression to C_Confused
        show Cassian confused at waist_up_center
        C "I—What are you even talking about?"

        "Cass isn't sure if he should take you to the nurse to check your head or something because what the actual fuck are you on right now?"
        "But you both got things to do, so he does the next best thing: making sure you don't fall again by placing you securely on the ground."
        "You give out a small thanks as you get back on your feet. Maybe it's your nerves getting to you or you're crashing out, but you couldn't help but feel a tingle under your skin as Cass' warm arms unwrap around you."
        "It was definitely the nerves, yes. Absolutely."

        # Change Cassian Expression to C_Smug
        show Cassian smug pose2 at waist_up_center
        C "That could've {i}all{/i} been avoided if you just let me do it."
        show Cassian smug at waist_up_center
        MC "Yeah, yeah, whatever. Just get the dumb thing already."

        "As if you'd give Cass the satisfaction of being right. The embarrassment from the whole ordeal makes your cheeks hot and eyes flighty. To protect the last of your pride, you tilt your face down, away from Cass' gaze."
        show Cassian laughing at waist_up_center, pop
        "Cass lets out a small snicker at your actions while moving behind you"
    # [End of Choice]

    # Change Cassian Expression to C_Neutral
    show Cassian neutral at waist_up_center
    C "Hold on, I got it."

    "Suddenly, you are {i}very{/i} self-aware of your surroundings."
    "Was the room always this small? Walls closing in on you, stuck between a shelf that tried to kill you and a hard place—the hard place being a whole human being."
    "You aren't sure if you should move or not. While being crushed in your school's storage room isn't how you wanted to go, a shuddering pit in your stomach sticks you in place... Damn, these nerves are working in overdrive."
    "Unaware of your current dilemma, Cass moves to grab the controller, placing one hand on a lower shelf while the other rises to reach the item."
    "An arm comes into your peripheral, muscles contracting under pale skin. Oh, bare forearm—{i}how scandalous.{/i}"
    "Following Cass' arm down to his fingers, you take note of the gold jewelry. It really complimented him. The dainty bracelet clasps around his wrist, flattering its soft curve while the ring accentuates his slim and elegant fingers."
    "How... {w=0.3}{i}pretty.{/i}"
    "...{w=0.5} Dawg, are you seriously losing it over a forearm? What are you, an old Victorian??"
    "Averting your eyes (like an outraged Victorian), you try to focus on something else, anything else, ignoring the wild thoughts in your head."

    show Cassian at waist_up_right_for_asset with move
    # Controller Asset appears on screen
    show controller at asset_center with dissolve
    C "Hey, [player_name], I got the controller! It seems to be in good shape, so it should work for the showcase!"
    hide controller with dissolve
    show Cassian at waist_up_center with move

    "You can feel Cass looking down at you, waiting for a response; but all you can focus on is your close proximity to each other. The hairs on your neck stand still as his breath tickles the area and his words jingle in your ears."

    # Change Cassian Expression to C_Confused
    show Cassian confused at waist_up_center
    C "Um, [player_name], you there?"

    "His chest is solid and firm against your back, rising up and down with each breath he takes... Is it getting hot in here?"

    MC "Ahahaa, yes, you did. Now that you finished up, can you move? I think you're going to crush me to death."

    "You quickly learn it's very hard to play it cool when all you feel is the warmth of a man's chest crushing you."

    # Change Cassian Expression to C_Soft
    show Cassian soft at waist_up_center
    C "OH, SORRY—Ehem, sorry, I'm sorry."

    "Realizing his position, Cass swiftly jumps away from you, nearly tripping over the boxes littering the floor in the process."
    "Thinking back to his actions and his closeness to you, Cass can't help but feel his face heat up again, a pink flush coloring his ears and cheeks once more."
    "There's this weird air left between the two of you, nearly just as suffocating as your past position.You want out, out of this awkward moment, out of this dusty room. Your social battery is done."

    MC "Well, uh, look at that! We got the controller, great! Thank you, let me just go put this in the clubroom, y'know?"

    "Seeing a way out, you take the controller out of Cass' hand and begin to walk backward."

    MC "How about you wait here, look around more while I'm out!"
    
    "Cass watches your frantic movements, lost. While seeing you lose it is always a breath of fresh air, why are you tweaking when Cass hasn't done anything??"

    # Change Cassian Expression to C_Confused
    show Cassian confused at waist_up_center
    C "Uh, [player_name]—"

    MC "Like over there, in the corner! I'm sure there's like, a screen in that mess. How about you go look over there while I just, uh, leave."

    C "Wait, hold on, [player_name]. Be careful—"

    "As Cass takes one step towards you, you take two back, not paying attention to your surroundings."
    "The controller wire wraps around your feet, tripping you backward. In a panic, you reach out to the objects in your peripheral— but wow, would you look at that?"
    show Cassian panic at waist_up_center
    "It's just a stack of boxes... A stack of boxes you tipped over that are about to crash land onto you."
    
    # [Start of choice dependent dialog]
    if player_choice == "accept-help":
        MC "OH SHI—"

    elif player_choice == "deny-help":
        MC "AGAIN?? FUCK THI—"

        "Damn, not once but TWICE! There you go, falling to your death once again because of some dusty-ass controller."

    # [End of Choicedependent dialog]
    stop music fadeout 1.0
    "Instinctively, you close your eyes and curl into yourself."
    scene black with fade

    # Change Cassian Expression to C_Panic
    show Cassian panic at waist_up_center, pop with dissolve
    
    C "[player_name]!"
    hide Cassian with dissolve
    "A familiar warmth envelops you once more, but this time a fresh scent follows it, blinding your senses."
    "The ocean. Sea waves and salt take over you as you brace yourself for the fall."
    play sound "audio/sfx/box-of-stuff-falls.ogg" volume 0.03
    "You feel yourself hit the concrete floor with the sound of falling boxes around you. You wait for some sort of pain to hit you, but nothing happens."

    scene bg cass storage at partlyblurred with dissolve
    pause 0.2
    scene bg cass storage at unblur with dissolve

    "Opening your eyes, you take in your surroundings only to see Cass over you, his head tucked into your neck. So that's where the sea breeze came from. It suits him."
    "Your other senses slowly catch up, relaying you the feeling of Cass' hand cupping the back of your head as his arm is tight around your waist, pulling you into him."
    "You're too stunned to react as Cass moves his head up and above you while his hands move from their positions to lay near your ears."

    # Change Cassian Expression to C_Panic
    show Cassian panic at waist_up_center with dissolve
    "{w=0.5}Cass scans over you, looking for any tell you're hurt."

    C "[player_name], are you okay?"

    "Cass tilts his head to the side, causing loose hair to fall down his shoulder and his earring to slightly shimmer."
    play music "audio/music/G5 - Romantic.wav" fadein 1.0 loop
    # Show CG 1
    scene CG Cass 1 with fade
    pause 1.0
    "There is only so much light in the storage room, but what is there highlights Cass' face, reflecting off eyes that only stare at you and his ivory fly-aways."
    "Shadows settle over his face, accentuating his slender nose and long lashes as their silhouettes lay on his skin."
    
    
    MC "{w=0.5}Um, yeah...{w=0.5} All good down here."

    "You whisper out your response, too caught up looking at Cass above you."
    # Back to storage room
    # Change Cassian Expression to C_Smug
    scene bg cass storage with fade
    show Cassian smug at waist_up_center with dissolve

    C "Geez, what's with you today? When you said you'd help me out, I didn't think I'd have to babysit you like this."

    "You have half a mind to give your own sarcastic retort, but you can't bring yourself to, especially not in your current predicament."

    MC "Just...{w=0.3} just shut up already."

    "Heat begins to crawl up your neck the longer you think about it. None of this is normal. You can't kid yourself anymore."
    "That heavy feeling you've had ever since the bookshelf was never from nerves, and the lingering glances were never for innocent admiration."
    "Gosh, you've gone and done it now..."
    "Your sudden revelation leaves you winded and embarrassed." 
    scene black with fade
    "Unable to look Cass without bursting into flames, you opt to turn away from him and cover your eyes. You don't have to confront anything if you can't see it!"
    scene bg cass storage with fade
    show Cassian smug at waist_up_center with dissolve
    "Cass starts to carry on his teasing, but looking back at you stops him in his tracks."
    "The light shines on your face, bringing his attention to your flushed cheeks. An unfamiliar expression of aversion and timidness is drawn on your face."
    "In all his years of knowing you, not once has Cass ever seen you like this. Off your game and off your feet, literally and figuratively." 
    "A sense of recognition passes over him as he continues to stare at you. A warm feeling pierces his chest, pushing him to say everything he's been holding back."

    # Change Cassian Expression to C_Hopeful
    show Cassian hopeful at waist_up_center
    C "Hey, [player_name], there's something I have to tell yo—"

    "A sudden voice reaches your ears."
    stop music fadeout 1.0
    G "Oh shit, guess we didn't close this up, huh. Well—there we go! Time to head out!"

    queue sound ["audio/sfx/shoe-shuffling.ogg", "audio/sfx/door-locking.ogg"] volume 0.3
    "Shoe shuffling follows with a soft click at the door and complete darkness."

    # Change Cassian Expression to C_Panic
    show Cassian panic at waist_up_center, pop
    C "Did he just..."

    MC "Um, I think so."

    # Change Cassian Expression to C_Upset
    show Cassian upset at waist_up_center
    C "...{w=0.3} You have got to be kidding me."

    # add music?

    "Gale fucking Galleon just locked you in the dark storage room with Cassian Floros right on top of you... What in the shoujo manga is this shit? Y'know, just what is your life at this point?"
    "The two of you stay in silence, trying to process your new situation along with the awkward tension from before still simmering."

    MC "Sooooo, uh, what were you about to say, Cass?"

    # Change Cassian Expression to C_Panic
    show Cassian panic at waist_up_center, pop
    C "Oh, uh, nothing. Don't worry about it."

    "You catch the weird twinge to Cass' words. The vulnerable and tender expression he wore doesn't leave your mind."
    "Whatever Cass was about to say seemed important to him, but if you learned anything from being around all the boys, it's that all men do is LIE."
    "In your current situation, Cass' strange reaction should be the last of your worries—but like, where's the fun in that? To poke or not to poke, that is the question. Oughh, the curiosity is eating away at you."

    hide Cassian with dissolve
    # [Start of Choice]
    menu:
        "Bug Cass more about it.":
            $ player_choice = "ask-more"
        "Leave it alone.":
            $ player_choice = "leave-it-alone"

    if player_choice == "ask-more":
        show Cassian panic at waist_up_center with dissolve
        "As if you'd believe him, you know these games. You can even say you've played them before."
        "You try to ask Cass again, but he quickly stands up to walk around the room."

        # Change Cassian Expression to C_Thinking
        show Cassian thinking at waist_up_center
        C "I'm sure there's something in this room that we can use to unlock the door."
        
        "You watch him pace around the tiny room like a cockroach, ready to flap its wings and fly into your direction to jumpscare you and make its escape."

        MC "Cass—"

        # Change Cassian Expression to C_Upset
        show Cassian upset at waist_up_center
        C "Once we get out of here, Gale is {i}so{/i} dead to me."

        "He tries for the doorknob, huffing and stomping away when the dumb thing still remains locked."
        "His eyes dart around the space in search of something to help open the door. Despite this, his gaze firmly stays away from your general direction."

        MC "Cass, you're just a chill guy."

        # Change Cassian Expression to C_Confused
        show Cassian confused at waist_up_center
        C "What?"

        "He jumps at the direct call out, looking over to you with alarm."

        C "Oh, uh, yeah. I'm just a chill...{w=0.3} Have you been hanging out with Luci lately??"

        MC "Nuh uh. I ask the questions. What were you gonna say earlier? It seemed really important?"

        # Change Cassian Expression to C_Panic
        show Cassian panic at waist_up_center, pop
        C "D-don't worry about it—"

        MC "Oh my god, shut up and tell me already!!"

        C "There's nothing to talk about!! Haha!!"

        MC "Fine! Don't tell me then."

        "You lift yourself off the floor and take your phone into your hand. You quickly and furiously type in Rosco's number in and press the dial button."
        "As the phone rings, the tapping of your foot is the only other sound that can be heard in the room. There's occasional shuffling behind you like Cass is moving, but you hear and feel nothing from him."

        C "Hey, uh...{w=0.3} What are you doing?"

        MC "I thought you didn't wanna talk to me?"

        "You fire back with sass. The sharp bite doesn't get a response from the man, so you roll your eyes and show your phone screen over your shoulder."

    elif player_choice == "leave-it-alone":
        show Cassian panic at waist_up_center with dissolve

        MC "Whatever you say, Cass."

        "You nod in compliance, accepting Cass' diversion."
        "If it was truly important, Cass would've said something. There's no point in obsessing about it when you're stuck in your school's storage room... Right?"
        "Doubt creeps in you, worrying over what is left unsaid between the two of you."
        show Cassian disappointed at waist_up_center,pop, zoom_away
        "Suddenly, Cass stands up, leaving you lost in your thoughts."
        
        show Cassian disappointed at waist_up_left with slow_move
        show Cassian disappointed at waist_up_center with slow_move2
        show Cassian disappointed at waist_up_right with slow_move
        show Cassian disappointed at waist_up_center with slow_move2
        "You watch as Cass walks aimlessly around the room, avoiding you entirely."
        
        "Damn, what's up with him?"
        "You prop yourself up, moving towards Cass. At his side, you lift a hand to his shoulder in comfort."
        show Cassian disappointed at waist_up_center, singlejump
        show Cassian disappointed at waist_up_center, zoom_back
        show bg cass storage at screenshake2
        pause 1
        MC "{w=1.0}Cass, are you alright?"

        "Your presence startles him, the sting of held-back words still heavy on his tongue. Not now, it wasn't good enough yet. Irritation at his own fearful silence begins to bubble under his skin."

        # Change Cassian Expression to C_Upset
        show Cassian upset at waist_up_center
        C "Of course I'm fine, why would there be something wrong?"

        "You watch as Cass remains focused on everything except you, pretending like you aren't there."

        MC "Well, it's like you're avoiding me so I was just wondering—"

        C "Just leave it, [player_name], okay! I already told you, just let it go."

        "The sharp edge of Cass' words surprise you. You step away from him, half-annoyed at his audacity and a drizzle of hurt in your chest."
        "You search Cass' face for something, anything that could help you understand, anything that could tell you what was wrong—but there was nothing."

        MC "Fine...{w=0.3} Do whatever you want, see if I care."

        # Change Cassian Expression to C_Dissapointed
        show Cassian disappointed at waist_up_center
        C "{w=0.3}.{w=0.3}.{w=0.3}."

        "To hear such a cold response from you is unnerving, wrong. Cass realizes how badly he messed up the moment your company disappears, leaving him with just his deprecating thoughts to cycle through his head."
        "You stride to the opposite side of the storage room, placing your feelings in order. Your heart has simmered, the hurt fading. And terrible for Cass, all that's left is pure spite. Pigs will fly first before you let that stupid man make you feel bad."
        "Feeling around in your pocket, you find the object you're looking for, reminding you there's a much {i}simpler{/i} way to get out of the locked room."

        MC "So fucking obvious, can't believe we didn't do this first."

        "You mutter to yourself as you take out your phone and navigate to the call list."
        "As you push the familiar contact, Cass peeks over from his corner of shame, hoping to see you less upset; but of course you weren't... if anything, it looks like you are about to tear apart anyone who gets in your personal bubble."
        
        show Cassian confused at waist_up_center
        C "Um, what are you doing, [player_name]?"

        MC "I'm getting us out of here."

        # Change Cassian Expression to C_Hopeful
        show Cassian hopeful at waist_up_center
        C "Oh! You found one, what is it?"

        "You wave the phone in Cass' direction as the call rings out."
    play sound "audio/sfx/cell-phone-dial.ogg"
    # [End of Choice]
    MC "I'm calling Rosco."

    # Change Cassian Expression to C_Dissapointed
    show Cassian disappointed at waist_up_center
    C "Oh..."
    hide Cassian with dissolve
    
    "His voice takes on a tone of dejectedness, sounding like the human embodiment of \"kicking rocks all alone.\""
    "You would feel bad if he wasn't such a stubborn prick."
    "Just as you start getting impatient, Rosco picks up the call, sounding slightly annoyed and almost like he just crawled out of bed."
    stop sound
    # Add music comedic?
    R "{i}Yo? What's up.{/i}"

    "You put the phone on speaker as Cass physically whips his head over to the new voice."

    # Change Cassian Expression to C_Confused
    show Cassian confused at waist_up_right with dissolve
    C "Did he just wake up?"
    hide Cassian with dissolve

    MC "Did you just wake up?"

    R "{i}.{w=0.3}.{w=0.3}.{w=0.3} So? Doesn't matter if I did. What d'ya need?{/i}"

    MC "Don't laugh at us, but—"

    R "{i}Oh, I'm already laughing, dude.{/i}"

    MC "Shut up! My god. Pink-haired brat."

    "Lovely, leave it up to Rosco to poke and prod you until you explode."
    "You continue spouting every profanity you can conjure up in your mind, getting more and more riled up as the guy on the other line keeps giggling harder and harder."

    R "{i}Holy brap, you're so pissed. What happened??{/i}"

    MC "Cass is being stupid, Gale locked us in the damn storage room, and {i}now{/i} I have to call your dumb ass as our last option!!"

    # Change Cassian Expression to C_Upset
    show Cassian upset at waist_up_right,pop with dissolve
    C "Hey—"
    hide Cassian with dissolve

    "You try to take deep breaths to calm yourself as laughter roars from the speaker of your phone."
    "That evil, pink twink will pay."

    R "{i}No way, bro! How'd you get yourselves locked in there?? Was it Cass' fault???{/i}"

    # Change Cassian Expression to C_Angry
    show Cassian angry at waist_up_right, pop with dissolve
    C "It was not my fault!"
    hide Cassian with dissolve

    R "{i}Whatever. I think [player_name]'s about to blow up. I can hear [player_possessive] fuse running.{/i}"

    MC "If you can hear it, then hurry {i}the fuck{/i} up and help us."

    R "{i}Sure. Let me go get food first.{/i}"
    play sound "audio/sfx/mobile_phone_hanging_up.ogg" volume 0.1
    "You could say nothing more as he hangs up on you, leaving you stunned as if you just got stood up on your first date."
    "Which...{w=0.3} kind of doesn't feel far off with the guy you're currently locked in a room with."

    MC "Stupid Rosco...{w=0.3} Always eating."

    "A huge sigh leaves your lips as you take your seat once more on the floor. Might as well get comfy. This'll take quite a while, huh?"
    # Change Cassian Expression to C_Neutral???
    show Cassian neutral at waist_up_right with dissolve
    "You stare off at a random spot on the wall, trying not to give too much attention to the guy still awkwardly standing in the corner. Eventually, he also lets out a sigh and moves closer to you."
    show Cassian at waist_up_center with move
    "He takes the spot next to you, close enough that you could touch hands if he moved just a space closer. From your peripheral vision, you see him take a few glances before he directs his gaze forward like you are doing."
    "The two of you are quiet for a bit, both for opposite reasons. The silence remains until Cass heaves a deep exhale and trains his eyes ahead nervously."

    # Change Cassian Expression to C_Dissapointed
    show Cassian disappointed at waist_up_center
    C "Um, [player_name]—"

    "At his voice, you whip your head to glare at Cass, stopping him from continuing his sentence."
    play music "audio/music/G4 - Sad.wav" fadein 1.0
    "Cass averts his eyes down, choosing to watch his twiddling thumbs. Gaining his courage again, Cass lets out an exhale."

    C "I'm sorry, [player_name]. I shouldn't have acted like that towards you."
    C "There's no good excuse for it, really, but I... just know it's nothing you did. Just me being stupid, I guess."

    "You watch as Cass scrunches up his face in guilt. This man is literally the embodiment of a kicked puppy, insultingly."

    MC "Geez, Cass, you make it so hard to be mad at you."
    MC "I was planning to stay upset until you started begging for forgiveness and get myself a free meal, but you're making me feel bad."

    "You let yourself slide down from your sitting position, putting you flat on the floor."
    "You look over to Cass, biting words turning soft."

    MC "...{w=0.3} And you're not stupid. Just—a weirdo with feelings, big and impulsive ones."
    MC "Next time, let me in on them or something. We're friends, yeah?"

    # Change Cassian Expression to C_Neutral
    show Cassian neutral at waist_up_center
    C "Yeah, friends."

    "Cass would have internally crawled into a hole and cried after being called just your friend, but the way you said it made it... different, a good different."

    MC "Good, good. I'm not sure I'll have the self-control not to punch you in the face if you pull that shit again."

    # Change Cassian Expression to C_Panic
    show Cassian panic at waist_up_center, pop
    C "You WHAT?"

    MC "Hey, I was {i}thinking{/i} about it, not like it happened or anything..."

    # Change Cassian Expression to C_Bruh
    show Cassian bruh at waist_up_center
    C "{w=0.5}.{w=0.5}.{w=0.5}."
    stop music fadeout 1.0
    pause 1.0
    play music "audio/music/G2 - Chill.wav" fadein 1.0 loop
    "The two of you look at each other for a moment but instead of the tense and awkward air from before, it's lighter, clearer."
    "Before you know it, you let out a small laugh, followed by Cass' louder, unfiltered fit."

    # Change Cassian Expression to C_Laughing
    show Cassian laughing at waist_up_center, pop
    C "Always so mean to me, huh, [player_name]?"
    hide Cassian with dissolve
    "The storage room echoes with your laughter. The happy sounds bounce on the walls, shattering the previous memories of your little argument. At the end of the day, Cass is someone important to you, small arguments like those be damned."
    play sound "audio/sfx/door-knocking.ogg"
    "An abrupt knock outside stops your laughter, bringing you back to your current locked-in-a-room problem."

    R "Helloooo, are you dumbasses still alive in there?"

    "This bitch."

    MC "Shut up, Rosco, just unlock the door already!"

    R "Man, hold your horses. I got it."

    play sound "audio/sfx/keys-door-opening.ogg" volume 0.5
    pause 0.8
    "You hear sounds of keys and latches—{w=1.0}then suddenly, light."

    MC "AHHHHH, MY EYES!"

    # Change Cassian Expression to C_Panic
    show Cassian panic at waist_up_right, pop with dissolve
    C "UGH—I forgot how dark it is in there, geez. Give us a little warning, Rosco."

    # Change Rosco expression to R_Laughing
    show Rosco laugh jacket at waist_up_left, pop with dissolve
    MC "I-I think you just caused permanent damage to my retinas...{w=0.5} STOP LAUGHING, YOU PINK SHIT!"

    "If you had working eyes, you'd shut his dumb ass up; but you don't, so you'll just beg for nature to smite him off the planet."
    hide Rosco with dissolve
    hide Cassian with dissolve
    show screentint with dissolve
    "Your walk back to the clubroom consisted of Cass leading you back (blind leading the blind... you can guess how great that went) as giggles and various profanities that would have even Zanny staring at you in stunned and impressed silence leave your lips."
    "Somehow, though, you make it to the clubroom with all people alive and limbs attached."
    stop music fadeout 1.0
    # Change scene to Clubroom
    scene bg clubroom with fade
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop

    MC "Woo! Glad that's over."

    # Change Cassian Expression to C_Neutral
    show Cassian neutral at waist_up_right with dissolve
    C "Thanks for coming, Rosco."

    # Change Rosco Expression to R_Neutral
    show Rosco neutral jacket at waist_up_left with dissolve
    R "Yeah, yeah, whatever. What were y'all doing in there anyway?"

    C "We were gathering equipment we'll need for your game showcase at our stall."

    R "Oh, cool, what did you guys find?"

    MC "So, um, about that...{w=0.3} We found a controller."
    show Rosco confused jacket at waist_up_left
    R "One controller?"

    # Change Cassian Expression to C_Dissapointed
    show Cassian disappointed at waist_up_right
    C "...{w=0.3} One controller."

    R "...{w=0.3} Brother."

    # Change Cassian Expression to C_Winking
    show Cassian winking pose2 at waist_up_right
    
    C "I'm sure it's fineeee."

    MC "If we need more, we can look again!"
    show Rosco neutral jacket at waist_up_left
    R "No yeah, it's fine, but like... What else were you two doing in there to find just one singular controller?"

    "At the question, the whole shoujo manga situation barrels into you like a freight train. Ahahah rightttt, that indeed happened."
    "You feel your cheeks flush at the recollection, your heart shaking in your ribcage."

    MC "It was...{w=0.3} a bit more crowded than we thought."

    # Change Cassian Expression to C_Soft
    show Cassian soft at waist_up_right
    C "Y-yeah, what [player_name] said..."

    "You slowly look over to make eye contact with Cass, seeing a similar reaction of red embarrassment color his face... Hey, wait a minu—"
    "Nopenopenope. You are not opening that can of worms right now. Operation Get the Fuck Out of There Now is a go."

    MC "Anyway! It's pretty late now, I'm gonna head back to my dorm. UH— see you guys."

    "Confrontation being your biggest fear, you say your quick good-byes to your friends and bolt back to the comfort of your dorm."

    #Change cassian and Rosco Expression to C/R_Confused
    show Cassian confused at waist_up_right
    show Rosco confused jacket at waist_up_left
    "Rosco and Cass stare at you in confusion as you swiftly leave the room..."

    R "Bro, what did you do?"
    # Change Cassian Expression to C_Panic
    show Cassian panic at waist_up_right, pop
    C "HAH—WHAT?! NOTHING??"

    hide Cassian with dissolve
    hide Rosco with dissolve
    stop music fadeout 1.0
    # Change scene to MC Dorm
    scene bg mc bedroom cass with fade
    play music "audio/music/C1 - Chill (1).wav" fadein 1.0 loop
    "You let out a large sigh once you enter your room and belly flop on your bed. Everything that happened today comes crashing down on you. And by everything, it's {i}everything{/i}."
    "Your brain does that horrible memory slideshow, but instead of it showing that one public presentation you did where your nervousness was visibly through the roof or when you tripped over yourself in a crowded street, it was Cass... which is arguably worse."
    "Eyes like gleaming copper, an embrace warm and inviting as a winter hearth, that salty sea breeze lingering in his hair... what the shit."
    "It is all too sudden, new, uncomfortable sometimes—This view of Cass you never thought of before taking over your whole mind. What do you even do with them? Are you supposed to know? Do you just go for it, like what does someone even do—"

    MC "Just...{w=0.3} one day. One day at a time, I'll get there."

    "Worrying and stressing about it won't get you anywhere. You need time, as much as you can get before you put anything in motion."

    MC "Hmmm, now that's done, what's next?"
    if "C" not in collected_routes:
        
        $ collected_routes.append("C")

    if len(collected_routes) == 5:
        scene black with fade
        stop music fadeout 1.0
        "Thinking back, you realize you helped out all the boys with their parts of the stall. Must mean the festival is soon, huh. How time flies."
        "Laying down in bed, you can't help but feel excited as you think about the event. What kind of fun awaits you at this spring festival!"
        
        #jump ending_route
        "Onto Ending Routes"

    else:
        scene black with fade
        stop music fadeout 1.0
        "You check your phone messages. Since you pretty much finished Cass' part of the stall, guess you'll start helping out one of the other boys." 
        "Your thumb dangles over the countless chats. Hmm, who's next?" 
        
        jump choose_route