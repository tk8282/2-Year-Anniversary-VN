# Start of Gale route
label gale_route:
    scene bg clubroom
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop
    show Gale at waist_up_center2 with dissolve
    MC "I'll help Gale."
    
label gale_route_day1:
    stop music fadeout 1.0
    scene black with fade
    show text "{size=50}Gale Route: Day 1{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve

    # Day 1
    play music "audio/music/C1 - Chill (1).wav" fadein 1.0 loop
    scene bg_gale_empty_stall with dissolve
    "You absently tap your foot against the concrete while you wait, enjoying the fresh spring breeze drifting through the open lawn."

    "You and Gale had agreed to meet where the stalls are being set up to check yours out and make a plan for how to go about decorating."

    "It’s a few minutes past the meeting time when you pull out your phone to text Gale, only to hear rushed footsteps coming around the bend."

    show Gale neutral at waist_up_center2 with dissolve
    G "[player_name], hi! Sorry I’m late, I wanted to stop and grab us some snacks, but it took longer than expected."

    "Gale lifts up a bag from the nearby convenience store that’s bulging with snacks and drinks with a triumphant grin."

    MC "Sweet! No worries - let’s get moving, though. I want as much time as possible to get the decorations made."

    G "Sure thing. Nayu sent you our table number?"

    MC "Yep! Should be a few rows in, near the middle."

    show Gale neutral at waist_up_center2, singlejump
    G "Lead on!"

    "As you lead Gale through the rows of empty stalls, you start pointing out some of the clubs that have already begun decorating."

    show Gale confused 
    G "Is that a fishing stall?"

    "He gestures to a stall a few rows down from where you are now, and you see the Marine Biology Club setting up what looks to be a kiddie pool and hanging some paper jellyfish."

    show Gale confused pose2
    G "I wonder what they’re going to use the pool for…"

    MC "We should check it out during the festival!"

    "The stall next to it catches your eye."
    "It’s also bustling with movement, the club decorating and lifting a banner to draw attention."
    "Home-Grown Organic Veggies Taste Test"

    show Gale neutral
    MC "Hey, Gale. We should also visit the one next to it."

    "You watch as Gale cranes his neck and squints to read the sign between the people moving in front of it, and laugh as his expression twists."

    show Gale shocked
    G "Do you want me dead? Is that it? Absolutely not."

    MC "Oh, come on! It’s a blind taste test to see if we can tell the difference between home-grown and store-bought veggies!"

    show Gale shocked
    G "I know how they’ll taste already!" 
    show Gale shocked at waist_up_center, singlejump
    extend " Bad!" 

    show Gale laugh 
    "You dissolve into laughter as you both move on, still making note of some stalls to visit during the festival."
    "After a minute or so more of walking, you stop at a stall bracketed by posts and check the number Nayu sent you in your messaging app, confirming it’s the correct table."

    scene bg_gale_day_stall with dissolve
    pause 3.0
    MC "Okay, this is ours!"

    show Gale neutral at waist_up_left2
    G "Hey, this is pretty nice! It’s close to the end but not so close that people will just walk past us."

    MC "Nayu really hooked us up with a great spot!"

    "Gale pulls a little notepad and a pen from his pocket, setting the bag of snacks on the stall for a moment as you both take a step back and assess the situation."

    MC "I think some string lights would be good to catch peoples’ attention - we could wrap them around these poles."

    "Gale makes a note, letting you circle the stall a few times as he also studies it."

    G "We obviously need a banner and some fliers."

    MC "Maybe we can do some pennants to hang between the poles as well?"

    "Gale writes everything down dutifully, both of you studying the stall again for final ideas."

    MC "That’s all I can think of for now."

    G "Great! Let’s get some measurements."

    "You work together to get measurements of the stall and the poles, Gale jotting down the numbers on a separate page of his notepad."

    MC "Alright! Let’s get going."

    "Gale nods and grabs the bag of snacks from the stall before catching up to you."

    scene bg_gale_empty_stall with dissolve
    show Gale neutral at waist_up_center2 with dissolve
    G "Which resource room did you book?"

    MC "Just the one on the same floor as our club room. It’s pretty well outfitted, even though it doesn’t have the newest gadgets that some of the ones on the first floor do."

    G "I haven’t used a resource room before. What do the first floor ones have?"

    MC "Last I heard, they were getting a new 3D printer and some fancy fabric printer."

    show Gale shocked
    G "What could any of the clubs possibly need a 3D printer for?!"

    "You shrug as you push open the doors to the club room building, holding it open for Gale to slip inside as well."

    scene black with fade
    scene bg gale clubroom with dissolve
    MC "I heard the Chess Club used it to print a few more boards and sets of pieces since their club has grown so much. I think they got someone in a 3D modeling course to design custom pieces, too."

    show Gale neutral at waist_up_center2 with dissolve
    G "That’s pretty cool. I wonder if we can find an excuse to use it at some point…"

    MC "Probably! Rosco probably has a hundred ideas for tabletop campaigns that could benefit from having some miniatures."

    "You arrive at the resource room and let yourselves in, propping the door open with the attached doorstop to get the air flowing."

    "The resource room itself is clean, if a little cramped."

    "The shelves are packed with buckets of every kind of art and creative supply one could imagine. Tubs of paint are separated by finish, and tubs of markers aren’t separated at all."

    "Gale sets down his bags on a chair near the door while you start looking through some of the drawers, pulling out a few things that could be useful. Scissors, paintbrushes, cardstock paper, and pencils all get put on the main working tables in the center of the room."

    "You work together to get an appropriately-sized piece of craft paper to use as a banner, making sure to leave plenty of room around the edges to fold over for durability’s sake."

    "With everything set out on the table, you put your hands on your hips and take a step back, blinking at the gathered supplies."

    show Gale confused
    G "So, uh… How confident are you?"

    menu:
        "Pretty confident. I do stuff like this a lot.":

            show Gale neutral
            G "Oh, good. I was a little worried there for a minute."

            "You chuckle and move towards the tubs of paint."

            MC "Do you have any colors that you really want to be a part of the design?"

            G "Should it match the pennants we were going to make? That’s what the paper is for, right?"

            "You nod."

            MC "Sure. That makes sense to me."

            "You dig out the appropriate colors from the bin, only to turn and grin at Gale where he stands next to the table."

            show Gale confused
            G "He tilts his head at you, reminiscent of a golden retriever, and yelps when you start tossing the paint tubes at him."

            show Gale shocked at waist_up_center2, restless
            G " He barely manages to catch them all, dumping them on the table while you peacefully walk back over with a larger bottle of black paint and a dish to put the paints on while you’re painting."

            show Gale angry at waist_up_center, shake
            G "Warn a guy next time!"

            MC "Where’s the fun in that?"

            show Gale laugh
            G "His irritation melts away as you both laugh and you pick up one of the pencils before squinting down at the paper."

            show Gale neutral
            MC "Can you look around in the cabinets for the string lights while I sketch out the banner design?"

            show Gale at waist_up_center2, singlejump
            G "You got it, boss."

            hide Gale with dissolve
            "He gives a mock salute before turning to rummage around in the cabinets, giving you the space to circle the blank canvas of your banner to get your bearings."

            "Using long, even strokes, you outline where the banner’s title will go, as well as a few small flourishes along the edges."

            "You’re backing up from the table just as you hear Gale’s triumphant shout behind you, so you turn to see him emerging from a low cabinet with two long strands of string lights. They’re tangled, but that’s a problem for later."

            G "Found 'em!"

            MC "Nice! Come over here and tell me if you like this. I’m thinking we could do the main lettering in gold or black and have the colors around the outside as little decorations."

            show Gale neutral at waist_up_center2 with dissolve
            G "Sounds good to me!"

            MC "Great! Because you’re going to be painting it."

            show Gale shocked
            MC "While you do that, I’ll be making a draft of the flyer... " 
            extend "unless you want to trade?"

            show Gale neutral 
            G "Nope, nevermind."

            "Gale picks up one of the paintbrushes and squeezes some black paint into the tray."

            MC "Make sure you work from the center of the canvas outwards so you aren’t dragging paint everywhere."

            G "You know, I never would have thought of that."

            MC "I saw the mess in my mind’s eye. Your mess."

            show Gale shocked at waist_up_center2, singlejump
            G "I resent that!"

            MC "Resent me all you want - I’ve seen what you do to the club room if you’re left unattended. I won’t even mention your dorm room."

            show Gale laugh
            G "Shh… let me work…"

            "You laugh with him and pull your laptop out of your bag, humming as you navigate to the school’s proprietary graphic design software."

            show Gale neutral
            G "Gale focuses on outlining the typography on the banner while you put together a basic flyer design, adding information about the game from what you remember Rosco telling you."

            "It’s only a few minutes of working in silence before Gale groans."

            G "Do you mind if I put on some music? I feel like a rat in a cage right now."

            MC "Go for it."

            show Gale neutral at waist_up_center2, singlejump
            "Gale jumps up and plugs his phone into the speaker system set up near the lounge area of the room, shuffling between songs for a moment before he’s satisfied with his playlist choice."

            "He rejoins you at the main working table with a grin and two thumbs up before picking his paintbrush back up, humming along to the songs as they play."

            "Just as you’re finishing up a draft of the flyer, Gale sets his paintbrush down and stretches."

            G "I think the lettering is done, at least."

            "You look up and stand to look at it, grinning back up at him."

            MC "Nice! It looks great."

            show Gale smug at waist_up_center2
            G "My artistic abilities know no bounds!"

            "You snort and look at a dark stain of paint on his cheek from where he must have accidentally swiped the bristles against his face."

            MC "Hey, you have a little bit of…"

            show Gale confused
            "You gesture towards your face, but when Gale reaches up, he only succeeds in smearing it across his cheek even more."

            MC "Oh my god, hold on."

            "After wetting a paper towel in the sink, you come back over to the table."

            menu:
                "Wipe the paint off his cheek.":
        
                    "You take hold of Gale’s chin with one hand and carefully wipe the paint off with the paper towel, eyebrows furrowed as you focus on getting every last bit of paint."

                    show Gale blush
                    G "Oh, uh.. Thanks."

                    "His cheeks are turning red, and you grin as you step back."

                    show Gale neutral
                    "Gale clears his throat and sets the paintbrush down, coming around the table."

                    G "Let’s see that flyer, huh?"

                "Hand him the towel to wipe the paint off himself.":
                    show Gale shocked
                    "You slap the wet paper towel into Gale’s hand and gesture towards his face."

                    show Gale smug
                    G "What, not going to clean it up for me?"

                    MC "Not a chance, princess."
                    show Gale laugh
                    "Gale barks out a surprised laugh and uses his phone’s front camera to get the paint off his cheek, smacking you with the cold, damp paper towel on his way to throw it away."

            show Gale neutral
            MC "Alright - I’ll do some of the designs around the edges if you want to start cutting out the pennants from that cardstock we found earlier."

            G "Do I have to use scissors?"

            MC "There should be a paper trimmer somewhere in this room."

            G "Is that one of those paper guillotines?"

            MC "Paper…guillotines?"

            G "You know, the things you cut paper on with the big blade that you bring down?"

            "He mimes the gesture, looking innocent as can be."

            MC "I… Yes, that’s a paper trimmer."

            "Gale nods and goes off to search in the cupboards while you shake your head and move to dispense the colored paints onto the makeshift palette."

            "You settle into a peaceful rhythm working next to each other again, Gale carefully measuring and cutting the cardstock into triangles while you add some flair to the otherwise-plain banner."

            G "Okay, I’ve gone through all the paper."

            "He holds up a stack of multicolored triangles that are remarkably even, and you give a thumbs up."

            MC "Maybe there’s some cord or twine somewhere in here that we can use to tie them together after punching some holes in the top?"

            G "Oh, great idea! But before we do that…"

            "You watch as he stands up, stretching briefly before going over to where you both dumped your bags."

            "He lifts the convenience store bag with a grin."

            G "Snacks."

            "You immediately put your paintbrush down, done with the banner, and go to sit in the lounge area, leaning forward as he unpacks the bag."

            G "Go ahead and grab whatever you want - I’m happy with anything left."

            menu:
                "Chips":

                    "You reach for the bag of chips and immediately pop it open, chowing down."

                    "Much like most bags of chips, this one is half empty… or half full, depending on how you choose to look at it."

                    "Gale reaches for the sour gummies, leaving the salt bread on the table between you."

                "Salt bread":

                    "You reach for the salt bread and immediately unwrap it, happily taking a bite."

                    "It’s still perfectly soft - he must have purchased one of the freshly-baked ones that morning."

                    "Gale reaches for the chips, leaving the sour gummies on the table between you."

                "Sour gummies":
                    
                    "You reach for the sour gummies and immediately tear the bag open, tossing a few into your mouth."
    
                    "The sour fruit flavors make your mouth water uncontrollably, but it’s a delicious kind of almost-pain."

                    "Gale reaches for the salt bread, leaving the chips on the table between you."

            "You eat your snacks while chatting back and forth for a few minutes, talking about upcoming club events and a game you’re both playing, easily bantering between bites."
            "After collecting and disposing of your trash, Gale swipes the remaining snacks into his bag."
            G "I’ll probably leave this in the club room for whoever wants it."
            "Energized once more, you both return to your respective tasks, humming along to Gale’s playlist as you work through the finishing touches on the banner while Gale punches holes into the pennants and strings them together."

            MC "Oh! I had an idea!"

            "Gale looks up from the pennants and cocks his head, curious."

            "You rummage around in the cabinets until, with a triumphant cry, you pull out a long bolt of white cloth."

            MC "I thought the stall itself might look a little boring, so what if I make a little table bunting to jazz it up? It shouldn’t take me too long - it’s just gathering the fabric and putting a few stitches into it."

            G "Why not? Crepes are supposed to be fancy, so anything to make it look cooler sounds great."

            "You grin and toss a thumbs up his way before digging around in the same cabinet to find a needle and some white thread."

            "It’s no issue at all for you to gather the fabric here and there, sewing in a few perfunctory stitches until it resembles the table bunting you would see at a wedding or fancy reception of some sort."

            "You carefully fold up the bunting and place it on the table while you go in search of something in which to transport all the decorations. You strike gold with a few empty cardboard boxes that you handily put together before placing the bunting inside of one."

            G "I think the pennants are done!"

            "He folds the strand of pennants and sets them in the box with the bunting, careful to not bend them."
            # Artistic Route complete

        "I mean, how hard can it be?":

            G "Okay, yeah. How hard can it be?"

            "You chuckle and move towards the tubs of paint."

            MC "What colors do we want to be part of the banner design?"

            G "Let’s make it match the pennants. That’s what the paper is for, right?"

            "You nod."

            MC "Sure. That makes sense to me."

            "You dig out the appropriate colors from the bin, only to turn and grin at Gale where he stands next to the table."

            show gale confused
            "He tilts his head at you, reminiscent of a golden retriever, and yelps when you start tossing the paint tubes at him."

            show gale shocked
            "He barely manages to catch them all, dumping them on the table while you peacefully walk back over with a larger bottle of black paint and a dish to put the paints on while you’re painting."

            show gale angry
            G "Warn a guy next time!"

            MC "Where’s the fun in that?"

            show gale laughing
            "His irritation melts away as you both laugh and you pick up one of the pencils before squinting down at the paper."

            show gale neutral

            MC "Can you look around in the cabinets for the string lights while I sketch out the banner design?"

            G "You got it, boss."

            "He gives a mock salute before turning to rummage around in the cabinets, giving you the space to circle the blank canvas of your banner to get your bearings."

            "Using short, uneven strokes, you outline where the banner’s title will go, as well as a few small doodles along the edges."

            "You’re backing up from the table just as you hear Gale’s triumphant shout behind you, so you turn to see him emerging from a low cabinet with two long strands of string lights. They’re tangled, but that’s a problem for later."

            G "Found ‘em!"

            MC "Nice! Come tell me if you like this. What if we do the main lettering in gold or black and have the colors around the outside as little decorations?"

            G "Sounds good to me!"

            MC "Great! You should paint the main part of it since I sketched it."

            show gale shocked

            MC "While you do that, I’ll be making a draft of the flyer since I have the design tools installed on my laptop."

            show gale neutral
            G "I really should get around to downloading those…."

            "Gale picks up one of the paintbrushes and squeezes some black paint into the tray."

            MC "I think you work from the center of the canvas outwards so you aren’t dragging paint everywhere."

            G "You know, I never would have thought of that."

            MC "I saw the mess in my mind’s eye. Your mess."

            show gale flustered
            G "I resent that!"

            MC "Resent me all you want - I’ve seen what you do to the club room if you’re left unattended. I won’t even mention your dorm room."

            show gale laughing
            G "You’re not that much better! You were part of the problem with the club room last time!"

            "You laugh with him and pull your laptop out of your bag, humming as you navigate to the school’s proprietary graphic design software."

            show gale neutral
            "Gale focuses on outlining the typography on the banner while you put together a basic flyer design, adding information about the game from what you remember Rosco telling you."

            "It’s only a few minutes of working in silence before Gale groans."

            G "Do you mind if I put on some music? I feel like a rat in a cage right now."

            MC "Go for it."

            "Gale jumps up and plugs his phone into the speaker system set up near the lounge area of the room, shuffling between songs for a moment before he’s satisfied with his playlist choice."

            "He rejoins you at the main working table with a grin and two thumbs up before picking his paintbrush back up, humming along to the songs as they play."

            "Just as you’re finishing up a draft of the flyer, Gale sets his paintbrush down and stretches."

            G "I think the lettering is done, at least."

            "You look up and stand to look at it, grinning back up at him."

            MC "Nice! It looks great."

            G "My artistic abilities know no bounds!"

            "You snort and look at a dark stain of paint on his cheek from where he must have accidentally swiped the bristles against his face."

            MC "Hey, you have a little bit of…"

            "You gesture towards your face, but when Gale reaches up, he only succeeds in smearing it across his cheek even more."

            MC "Oh my god, hold on."

            "After wetting a paper towel in the sink, you come back over to the table."

            menu:
                "Wipe the paint off his cheek.":
                    jump wipe_gale
                "Hand him the towel to wipe the paint off himself.":
                    jump hand_towel

            label wipe_gale:
                "You take hold of Gale’s chin with one hand and carefully wipe the paint off with the paper towel, eyebrows furrowed as you focus on getting every last bit of paint."

                show gale flustered
                G "Oh, uh.. Thanks."

                "His cheeks are turning red, and you grin as you step back."

                "Gale clears his throat and sets the paintbrush down, coming around the table."

                G "Let’s see that flyer, huh?"
                jump after_paint_choice

            label hand_towel:
                "You slap the wet paper towel into Gale’s hand and gesture towards his face."

                G "What, not going to clean it up for me?"

                MC "Not a chance, princess."

                "Gale barks out a surprised laugh and uses his phone’s front camera to get the paint off his cheek, smacking you with the cold, damp paper towel on his way to throw it away."
                jump after_paint_choice

            label after_paint_choice:
                MC "Alright - I can fill in some of the doodles around the edges if you want to start cutting out the pennants from that cardstock we found earlier."

                G "Do I have to use scissors?"

                MC "There should be a paper trimmer somewhere in this room."

                G "Is that one of those paper guillotines?"

                MC "Paper…guillotines?"

                G "You know, the things you cut paper on with the big blade that you bring down?"

                "He mimes the gesture, looking innocent as can be."

                MC "I… Yes, that’s a paper trimmer."

                "Gale nods and goes off to search in the cupboards while you shake your head and move to dispense the colored paints onto the makeshift palette."

                "You settle into a peaceful rhythm working next to each other again, Gale carefully measuring and cutting the cardstock into triangles while you add some color to the otherwise-plain banner."

                G "Okay, I’ve gone through all the paper."

                "He holds up a stack of multicolored triangles that are somewhat even, and you give a thumbs up."

                MC "How are we going to turn those into a decoration, though..?"

                G "Maybe there’s some string somewhere in here that I can use to tie them together after punching some holes in the top?"

                MC "Oh, great idea!"

                G "But before I do that…"

                "You watch as he stands up, stretching briefly before going over to where you both dumped your bags."

                "He lifts the convenience store bag with a grin."

                G "Snacks."
                #End of neutral choice
            
        "Uh… I was kind of hoping you knew what you were doing.":

            G "Okay, yeah, sure. How hard can it be? Let’s figure this out."

            "You grin and move towards the tubs of paint."

            MC "What colors should be on the banner?"

            G "Let’s make it match the pennants. That’s what the paper is for, right?"

            "You nod."

            MC "Sure. That makes sense to me."

            "You dig out the appropriate colors from the bin, only to turn and grin at Gale where he stands next to the table."

            show gale confused
            "He tilts his head at you, reminiscent of a golden retriever, and yelps when you start tossing the paint tubes at him."

            show gale shocked
            "He barely manages to catch them all, dumping them on the table while you peacefully walk back over with a larger bottle of black paint and a dish to put the paints on while you’re painting."

            show gale angry
            G "Warn a guy next time!"

            MC "Where’s the fun in that?"

            show gale laughing
            "His irritation melts away as you both laugh and you pick up one of the pencils before squinting down at the paper."

            show gale neutral

            MC "Can you look around in the cabinets for the string lights while I sketch out a banner design?"

            G "You got it, boss."

            "He gives a mock salute before turning to rummage around in the cabinets, giving you the space to circle the blank canvas of your banner to get your bearings."

            "Using long, shaky strokes, you outline where the banner’s title will go, as well as a few small doodles along the edges after a second glance."

            "You’re backing up from the table just as you hear Gale’s triumphant shout behind you, so you turn to see him emerging from a low cabinet with two long strands of string lights. They’re tangled, but that’s a problem for later."

            G "Found ‘em!"

            MC "Nice! What do you think of this for the banner? We could do the main lettering in gold or black and have the colors around the outside as little decorations?"

            G "Looks and sounds good to me!"

            MC "Cool. You should paint the main part of it since I sketched it."

            MC "And while you do that, I’ll be making a draft of the flyer since I have the design tools installed on my laptop."

            show gale neutral
            G "I really should get around to downloading those…."

            "Gale picks up one of the paintbrushes and squeezes some black paint into the tray."

            "You watch him for a minute before pulling your laptop out of your bag, humming as you navigate to the school’s proprietary graphic design software."

            show gale neutral
            "Gale focuses on outlining the typography on the banner while you put together a basic flyer design, adding information about the game from what you remember Rosco telling you."

            "It’s only a few minutes of working in silence before Gale groans."

            G "Do you mind if I put on some music? I feel like a rat in a cage right now."

            MC "Go for it."

            "Gale jumps up and plugs his phone into the speaker system set up near the lounge area of the room, shuffling between songs for a moment before he’s satisfied with his playlist choice."

            "He rejoins you at the main working table with a grin and two thumbs up before picking his paintbrush back up, humming along to the songs as they play."

            "Just as you’re finishing up a draft of the flyer, Gale sets his paintbrush down and stretches."

            G "I think the lettering is done, at least."

            "You look up and stand to look at it, grinning back up at him."

            MC "Nice! It looks great."

            G "My artistic abilities know no bounds!"

            "You grin and look at a dark stain of paint on his cheek from where he must have accidentally swiped the bristles against his face."

            MC "Hey, you have a little bit of…"

            "You gesture towards your face, but when Gale reaches up, he only succeeds in smearing it across his cheek even more."

            MC "Oh my god, hold on."

            "After wetting a paper towel in the sink, you come back over to the table."

            menu:
                "Wipe the paint off his cheek.":
                    jump gale_paint_wipe
                "Hand him the towel to wipe the paint off himself.":
                    jump gale_paint_towel

            label gale_paint_wipe:
                "You take hold of Gale’s chin with one hand and carefully wipe the paint off with the paper towel, eyebrows furrowed as you focus on getting every last bit of paint."

                show gale flustered
                G "Oh, uh.. Thanks."

                "His cheeks are turning red, and you grin as you step back."

                "Gale clears his throat and sets the paintbrush down, coming around the table."

                G "Let’s see that flyer, huh?"
                jump gale_after_paint

            label gale_paint_towel:
                "You slap the wet paper towel into Gale’s hand and gesture towards his face."

                G "What, not going to clean it up for me?"

                MC "Not a chance, princess."

                "Gale barks out a surprised laugh and uses his phone’s front camera to get the paint off his cheek, smacking you with the cold, damp paper towel on his way to throw it away."
                jump gale_after_paint

            label gale_after_paint:
                MC "Alright - I can fill in some of the doodles around the edges if you want to start cutting out the pennants from that cardstock we found earlier."

                G "Do I have to use scissors?"

                MC "What else would you use?"

                G "Fair enough."

                "Gale goes off to search in the cupboards for some scissors while you move to dispense the colored paints onto the makeshift palette."

                "You settle into a peaceful rhythm working next to each other again, Gale cutting the cardstock into triangles while you carefully add some color to the otherwise-plain banner."

                G "Okay, I’ve gone through all the paper."

                "He holds up a stack of multicolored “triangles” that are pretty uneven, but you give a thumbs up."

                MC "How are we going to turn those into a decoration, though..?"

                G "There should be some string somewhere in here that I can use to tie them together after punching some holes in the top."

                MC "Oh, great idea!"

                G "But before I do that…"

                "You watch as he stands up, stretching briefly before going over to where you both dumped your bags."

                "He lifts the convenience store bag with a grin."

                G "Snacks."

                "You immediately put your paintbrush down, done with your colorful, if messy, contributions to the banner, and go to sit in the lounge area, leaning forward excitedly as he unpacks the bag."

                G "Go ahead and grab whatever you want - I’m happy with anything left."

                "What do you choose?"

                menu:
                    "Chips":
                        jump gale_snack_chips
                    "Salt bread":
                        jump gale_snack_bread
                    "Sour gummies":
                        jump gale_snack_gummies

            label gale_snack_chips:
                "You reach for the bag of chips and immediately pop it open, chowing down."

                "Much like most bags of chips, this one is half empty…or half full, depending on how you choose to look at it."

                "Gale reaches for the sour gummies, leaving the salt bread on the table between you."
                jump gale_after_snacks

            label gale_snack_bread:
                "You reach for the salt bread and immediately unwrap it, happily taking a bite."

                "It’s still perfectly soft - he must have purchased one of the freshly-baked ones that morning."

                "Gale reaches for the chips, leaving the sour gummies on the table between you."
                jump gale_after_snacks

            label gale_snack_gummies:
                "You reach for the sour gummies and immediately tear the bag open, tossing a few into your mouth."

                "The sour fruit flavors make your mouth water uncontrollably, but it’s a delicious kind of almost-pain."

                "Gale reaches for the salt bread, leaving the chips on the table between you."
                jump gale_after_snacks

            label gale_after_snacks:
                "You eat your snacks while chatting back and forth for a few minutes, talking about upcoming club events and a game you’re both playing, easily bantering between bites."

                "After collecting and disposing of your trash, Gale swipes the remaining snacks into his bag."

                G "I’ll probably leave this in the club room for whoever wants it."

                "Energized once more, you both return to your respective tasks, humming along to Gale’s playlist as you work through the finishing touches on the banner while Gale punches holes into the pennants and strings them together."

                "You bring your laptop over to him to show him the flyer design, scrolling through while he squints at it."

                G "Looks good to me!"

                MC "Thanks. Graphic design is my passion."

                "Gale snickers as you put your computer down and go to rummage around the room to find something to transport the decorations in while Gale finishes his task."

                "There are a few empty cardboard boxes that you easily put together and set on a chair, just in time for Gale to cheer."

                G "I think the pennants are done!"

                "He folds the strand of pennants and sets them in one of the boxes you found, careful to not bend them."

            # END OF Option 3 (Non-Artistic Route)

    G "Should we untangle the lights while we wait for the banner to dry?"

    MC "Good idea."

    "You each take one strand of lights and work through untangling them, though not without a few muttered curses."

    "Gale gets his untangled first and heaves a sigh of relief, winding them into a neat coil around his arm."

    "You're not too far behind him, copying his method of coiling them up and handing them over for him to set in another box he found."

    "While Gale carefully checks on the banner and rolls it up once he's confirmed it's dry, you slip the mock flyer into your bag."

    MC "I'll make copies of the flyer either tonight or tomorrow morning before we meet up to decorate."

    G "Sounds great! Let’s get these back to the club room for safekeeping."

    "He goes to pick up one of the boxes, but you dash past him and into the hallway."

    "On your way up to the club room, you remember seeing… aha!"

    "There's a rolling cart just a few doors down, empty and up for grabs."

    "You wheel it back to the resource room and present it with a flourish."

    G "Oh hell yeah."

    "Gale loads the box he was holding onto the cart while you grab the other one, carefully balancing the rolled banner between them."

    G "Let’s get this bad boy to the club room. I’m starving."

    MC "But… the snacks?"

    G "I’m a growing boy! I need more than just a snack to get me through!"

    "You laugh and follow him out of the resource room after picking up your bags, making sure to close the door behind you."

    "Rosco is in the club room when you both get there, and you call out to him."

    MC "Hey, can you check to make sure the information in this flyer is right?"

    R "Yeah, no prob."

    "You hand over the flyer and he skims it, making a vague sound of appreciation before handing it back."

    R "Looks good. How did the decorations go?"

    G "We’re gonna be the belle of the ball… stall? The stall of the ball? Wait…"

    MC "Gale…"

    "Rosco winces."

    R "Maybe stick to the decorations instead of the jokes."

    "Gale pouts while you and Rosco chuckle."

    MC "Alright. I have to go, but I’ll see you in the morning, Gale."

    G "Bright and early!"

    "Rosco turns back to his computer and waves as you both leave after tucking the cart with the decorations safely out of the way."

    "You and Gale part in the hallway, going your separate ways for the evening with the promise of meeting the following day."


    

label gale_route_day2:

    scene black with fade
    show text "{size=50}Gale Route: Day 2{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve

    label day2:

    "Gale runs into the club room where you agreed to meet yesterday, fifteen minutes late."

    "His shirt is partially unbuttoned and his bag is half opened, his hastily shoved lunch box sticking out from between the zippers."

    "His wallet’s shoved into his pocket while he's still attempting to tie a messy ponytail with his hair, a few rubber bands wrapped around his wrist."

    G "[player_name]! I’m really sorry for being late! I overslept, which caused me to miss my usual bus and-"

    MC "It’s fine Gale, chill. Here, take a croissant."

    G "[player_name], I could kiss you right now! I haven’t eaten breakfast, and you got me a croissant, from my favourite bakery no less!"

    MC "Less talking, more eating, Gale~"

    G "Right away boss!"

    "You watch Gale scarf down the croissants as you start gathering materials you need to take outside."

    "Once he finishes, he comes over to help you move the remaining boxes onto the cart."

    G "And that's the last of them."

    G "Are we missing anything?"

    MC "I don't think so, but at most we can run back and get it from the clubroom."

    G "Alright, let's go!"

    scene bg stalls_undecorated

    MC "Phew, we finally finished moving all the decorations outside."

    MC "What do you think would be something good to start with?"

    G "Maybe the pennants and the string lights first?"

    G "They seem the most simple to do, I guess."

    MC "Okay, lemme get them out of the box."

    MC "..."

    MC "Eh? Why are the string lights so badly tangled up??"

    MC "I swear I just untangled them the last time, oh my god."

    G "Maybe it's just your bad luck."

    MC "Gale, you just had to jinx it. Alright, you’re gonna untangle the string lights while I put up the main banner and pennants."

    G "Huh? What? Hey, you can’t just do that!"

    MC "Yes, I can and will do that. Now bring the ladder over here before I kick your ass for real."

    G "Right away, boss!"

    G "I guess I kinda deserved that."

    MC "Gale, stop talking. I need the ladder here now."

    "Gale brings the ladder over for you and then starts work on detangling the string lights while you take the pennants out of their box and carefully hang them up."

    "Just as Gale’s almost done detangling the string lights—he spent another 10 minutes detangling the last particularly annoying knot in the cord and actually cheers when it’s done—and you’re just about finished with hanging the main banner and the last of the pennants, disaster strikes."

    "First, a pipsqueak flying by decides that the banner your masterpiece would make a great toilet."

    G "Oi! What d’you think you’re doing, defacing our masterpiece!"

    "The pipsqueak simply chirps at him before flying away."

    G "*sigh* I must have done something bad in my past life to get this kind of bad luck"

    MC "Maybe you were a bird who pooped on someone else's artwork, Gale."

    G "Yeah, that does make sense."

    "He takes a wet wipe from the packet in his pocket and walks over to the ladder, easily climbing up and quickly wiping it off."

    MC "Whew! We’re okay for now, let’s hope that nothing else happens."

    "The wind starts to pick up, prompting you and Gale to look at each other."

    G "I think you just jinxed it."

    MC "Definitely."

    G "We should make sure the decorations don’t fly off before the wind becomes worse."

    MC "Yeah, let’s do it now."

    "As you hurry to secure the decorations, the wind becomes extremely strong all of a sudden, causing the already hung decorations to flap around wildly."

    "As if that’s not enough, the next gust of wind causes Gale’s bandana to fly off."

    G "Hey, I was using that! Come back here!"

    "Gale hops off the ladder and runs off after his bandana."

    MC "Well, he’s gonna take a while. I guess I’ll start with the string lights first, since the wind seems to have died down all of a sudden."

    G "Oh, come on! Are you kidding me? God of the wind or whoever, why do you hate me so much? Why does the wind only stop now?"

    "Once Gale comes back, thankfully with his bandana wrapped safely around his hair this time, he insists on helping you with the second set of fairy lights, complaining that you didn’t wait for him to help with the first set."

    G "Hey, you didn’t wait for me to start with the lights that I so painstakingly untangled over half an hour!"

    MC "Eh, at least you can help me with the next set of lights."

    G "I guess. Come on, we gotta hurry or the boys are gonna be on our asses for not finishing on time."

    MC "Yeah, we should start."

    "You carefully climb onto the ladder with one end of the fairy lights in hand, securing it around the top of the pole with a tight knot."

    "You’re starting to carefully climb down the ladder when a freak gust of wind hits, and you see your life flash before my eyes."

    menu:
        "Scream loudly":
            MC "AHHHH!!"
            MC "GALE!!!!"
            MC "SAVE ME!!! I'M GONNA DIE!!!"
            MC "AHHH I'M TOO YOUNG FOR THIS!!!"

        "Softly whimper":
            MC "G.. Gale! Help!!"
            MC "Please… I don't want to die…"
            MC "I'm too young for this…"

    # CG hook: Gale stabilizes ladder
    G "Don’t worry, I’ve got you."

    MC "Thank you so much Gale, you saved my life!"

    G "No worries! Like I said, I've got your back!"

    MC "Thanks, Gale. I really owe you one."

    G "You know… there's that one Dario Mart game I've been eyeing recently that you promised to play with me, [player_name]."

    "Gale slings his arm over your shoulders as he says this, eyeing you suggestively. Not like you don't already know what he means."

    MC "*snorts* All right, Gale. I do"

    MC "All right! I think we’re almost done?"

    MC "What else are we missing…"

    G "The flyers!"

    MC "I think they're in the club room, do you wanna go back and get them?"

    G "Yeah, sure."

    scene bg club_room

    MC "Gale, they should be on the table."

    MC "You go grab them while I hold the door open for you."

    G "On it!"

    G "Hold on, I swear there were only like two of them yesterday?"

    G "How'd they multiply so fast?"

    MC "I made copies of them this morning while I was waiting for you."

    G "That was a good idea."

    G "Here, I got them, let's go and quickly put them up."

    MC "Aight, I'm letting go of the door now, better hurry~"

    "Gale lunges at the door and makes it past just as the door slams shut."

    G "I'm alive!"

    MC "Damn, I half hoped you'd get trapped in there. /j"

    G "Hey, that's so mean!"

    MC "Come on, let's get down to business."

    G "Yes boss!"

    scene bg stall

    MC "Hey, Gale, do you know where the fasteners are?"

    MC "I swear they were in this box yesterday."

    "You frantically rummage through one of the boxes, moving to another one when your first search proves fruitless."

    G "Wait. I'll check the boxes over here, and you check the ones over there."

    "The two of you continue the search for the fasteners in silence, but another five minutes pass to no avail."

    MC "Gale, do you just wanna go and buy them instead?"

    MC "It would probably save more time, and we could get lunch at the same time, since it's almost one already."

    G "That's a good idea, why not?"

    G "Do you know any place we can go?"

    MC "If I remember correctly, there's a small shop selling stationery and party supplies near campus, and the onigiri cart that you like is nearby."

    G "Let's go right now!"

    G "I can't wait to get the onigiri!"

    MC "Of course it's the food that attracts you."

    G "Haven't you heard the saying, food is a man's best friend?"

    MC "Isn't it dog is a man's best friend?"

    G "Well, technically both aren't wrong so…"

    MC "Fair enough."

    MC "Come on, enough talking, let's go."

    G "Right behind ya!"

    scene bg store

    G "We're here!!!"

    G "Is that…"

    G "A Digimon pencil case?"

    G "[player_name], can I get that please?"

    MC "Gale, you don't even use pencil cases anymore."

    MC "Come on, let's go find the fasteners."

    "Gale pretends to look dejected for three seconds before he realises it's not gonna work on you."

    G "I guess you're right."

    MC "The stationery section is over there."

    MC "Do you wanna walk together, or should we split up and conquer?"

    G "Let's just go together, it'll probably be better."

    MC "Okay ~"

    "You and Gale walk through the aisle, oohing and aahing at the variety of stationery."

    G "Look, there's Dario and Muiji shaped pencil toppers!"

    MC "Is that a snowflake pencil topper there?"

    G "Oh oh oh!!!"

    G "Those bird sticky notes look just like a pipsqueak!"

    MC "Wait no, Gale, remember our goal."

    MC "We cannot be distracted."

    G "But they're so cute…"

    MC "I know, but today, we need to lock in and get the fasteners so we can finish setting up the stall."

    G "Okay, let's do it."

    "The two of you continue walking along the aisle, carefully scanning each row for the fasteners."

    G "There!"

    "You look over to where he's pointing, the bottom corner of the last row of the shelf you're standing next to."

    "You crouch down, taking a closer look at the fasteners."

    MC "Gale, there's only zipties left."

    MC "We should be able to get everything down with that, right?"

    G "I think so?"

    "Gale squats down next to you, picking up a random box of zipties."

    G "Hey, these are rainbow zipties!"

    G "I didn't know these existed."

    MC "I think there's also a neon yellow box over there."

    MC "Ooh, is that pink I see?"

    "You pick up the boxes of neon yellow and pink zipties, weighing them in each hand as you scan the rest of the boxes."

    G "We are not getting pink. The stall's gonna look like Darbie decorated it or something."

    MC "Hmm."

    MC "Then how about we just get the rainbow ones?"

    MC "I don't see any regular zipties, and the rest are all either neon or pink."

    G "Alright then, rainbow it is."

    "You put the two boxes you're holding in your hands back onto the shelf, while Gale picks up another box of rainbow zipties."

    "You side-eye him, but he simply shrugs."

    G "You never know."

    G "Just get extra to be safe."

    MC "Okay then. Let's go to the cashier."

    "You and Gale take the short walk over to the cashier in silence, admiring the things all around you."

    "Gale places the two boxes of zipties onto the counter, pulling out his wallet to pay as the cashier scans the items."

    MC "Alright let's go!!"

    G "Eh? But I haven't paid for the stuff yet?"

    MC "I paid for it while you were busy pulling your wallet out."

    G "Hey, I was supposed to pay!"

    MC "Technically you didn't say anything so…"

    MC "But if you insist, you can pay me back by buying onigiri for me later."

    G "Yes! Onigiri!"

    G "Come on, let's go already!"

    G "I can't wait to eat!"

    "Gale picks up the two boxes of zipties and speed walks out the store while you follow closely behind."

    scene bg street

    "You follow Gale down the street, the familiar smell of freshly-cooked rice and seaweed growing stronger with every step."

    "The onigiri cart comes into view, the vendor already busy serving a small line of customers."

    G "We're here!"

    G "I know exactly what I want."

    MC "Of course you do."

    "You wait patiently while Gale places his order, bouncing slightly on his heels as he watches the vendor work."

    G "Two salmon onigiri, one tuna mayo, and…"

    G "Oh, and one extra plum."

    G "For [player_name]."

    MC "Hey, you remembered."

    G "I'm not heartless."

    "The vendor hands over the wrapped onigiri, and Gale quickly pays before ushering you out of the way."

    "You find an empty bench nearby and sit down together."

    G "Okay, eat it while it's warm."

    MC "You act like these disappear if they cool down."

    G "They disappear because I eat them."

    "You unwrap your onigiri and take a bite, the rice still warm and perfectly seasoned."

    MC "Yeah… this was a good idea."

    G "See? I always have good ideas."

    "You eat in comfortable silence for a moment, watching people pass by."

    MC "So… are you excited for tomorrow?"

    G "Yeah."

    G "A little nervous, but excited."

    G "I really want the stall to turn out well."

    MC "It will."

    MC "We've put a lot of work into it."

    G "True."

    G "And even if something goes wrong…"

    G "At least we'll be dealing with it together."

    "You glance over at him, surprised, but Gale is focused on his food, seemingly unaware of what he just said."

    MC "Yeah."

    "You finish the last bite of your onigiri and crumple up the wrapper."

    G "Done already?"

    MC "Unlike you, I don't inhale my food."

    G "Skill issue."

    "You both toss your trash into a nearby bin and stand up."

    MC "Alright, back to the stall?"

    G "Back to the stall."

    scene bg stall

    "You return to the stall area, the decorations waiting patiently where you left them."

    G "Okay, let's get these zipties put to use."

    "You both get to work, carefully fastening the banner and pennants in place."

    "The rainbow zipties blend surprisingly well with the decorations."

    MC "I hate to admit it, but…"

    MC "The rainbow ones were a good call."

    G "I know."

    G "You doubted me."

    MC "Only a little."

    "You step back once everything is secured, taking in your handiwork."

    MC "It actually looks really good."

    G "Right?"

    G "We're basically professionals."

    MC "Let's not get ahead of ourselves."

    "You make a few small adjustments, straightening fabric and fixing minor tilts."

    "Once satisfied, you let out a small sigh of relief."

    MC "I think we're done."

    G "Finally."

    G "My arms are dead."

    MC "You say that like you didn't spend half the time hyping yourself up."

    G "That takes energy too."

    "You laugh."

    MC "Let's pack up and head back to the club room."

    G "Yeah."

    scene bg club_room

    "You return the remaining supplies to the club room, carefully stacking the empty boxes out of the way."

    G "Mission accomplished."

    MC "For now."

    G "Hey, that's future us's problem."

    MC "You're not wrong."

    "You sling your bag over your shoulder and glance at the clock."

    MC "I should probably head out."

    G "Same."

    G "Big day tomorrow."

    MC "Yeah."

    MC "See you in the morning, Gale."

    G "Bright and early."

    "You leave the club room together before parting ways in the hallway."

    "You head home feeling tired, but satisfied, already thinking about how tomorrow will turn out."
    #End of Day 2
