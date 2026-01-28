label luci_route:
    scene bg clubroom 
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop
    MC "I'll help Luci."
    # Change Luci Expression to Shocked
    show Lucien shocked at waist_up_center, pop with dissolve
    # show Lucien shocked at waist_up_center
    L "{w=0.5}.{w=0.5}.{w=0.5}."
    # Change Luci Expression to L_Smug
    show Lucien smug at waist_up_center
    L "It'll help to have your opinion. Should we plan a time to meet?"
    
    MC "Sure thing!"
    hide Lucien with dissolve
    stop music fadeout 1.0
    jump luci_route_day1

label luci_route_day1:
    window hide
    $ quick_menu = False
    scene black with fade 
    show text "{size=50}{color=#ffff}Lucien Route: Day 1{/size}{/color}" at truecenter
    with dissolve
    pause 1.0
    hide text
    with dissolve
    $ quick_menu = True
    # Change Background to MC's Home
    scene bg mc bedroom luci at fullyblurred with dissolve
    pause 0.3
    scene black with fade
    scene bg mc bedroom luci at fullyblurred with dissolve
    pause 0.2
    scene black with fade
    scene bg mc bedroom luci at partlyblurred with dissolve
    pause 0.2
    scene bg mc bedroom luci at unblur with dissolve
    play music "audio/music/C1 - Chill (1).wav" fadein 1.0 loop
    MC "Eugh, waking up early sucks."
    MC "So much for finding inspiration."

    "Your attempted research got interrupted as your {b}{i}BinstaVibe{/i}{/b} feed filled with pet videos and DIYs."
    "Lamenting your lack of preparation, you set off to meet Luci."
    stop music fadeout 1.0
    # Clubroom Couch POV?
    pause 1.0
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop
    scene bg clubroom with fade
    "You arrived at the clubroom a while ago. The two of you are lazing on the couch, scrolling on your phones for inspiration."
    show Lucien annoyed at waist_up_center4 with dissolve
    # Change Luci Expression to L_Annoyed
    L "{w=0.5}Why is this so hard? I didn’t know there were so many flavors..."

    MC "We can always pick the classics— sweet ones like chocolate and cherry or savory ones like spinach and mushroom."

    L "Yeah, but then we have to consider what batter we want as well..."

    MC "I didn’t think of that. I’ve heard of the basic batter, matcha, and chocolate."

    L "Those can work for the sweet ones. Any ideas of what to pick for the savory ones?"

    MC "Hmm..."
    window hide
    show Lucien neutral at waist_up_right_for_asset4 with move
    # Phone asset booble search appears
    show crepe booble search at asset_center, move_up
    pause 0.5
    window show
    "You fiddle with your phone, looking up a few possibilities for savory batters."
    # Phone asset booble search dissapears
    hide crepe booble search
    pause 1.0
    show Lucien at waist_up_center4 with move
    "Meanwhile, Luci casually slings an arm over the back of the couch, leaning closer to look at your screen."
    
    show Lucien at waist_up_center4, zoomin3
    pause 2

    MC "So there is{w=0.2}.{w=0.2}.{w=0.2}.{w=0.5} garlic butter batter?"
    
    # Change Luci Expression to L_Shocked screenshake?
    show Lucien shocked at waist_up_center4, zoomout_jump, singlejump
    pause 1.0
    hide Lucien
    show Lucien shocked at waist_up_center4
    L "Garlic?!"
    MC "Beer batter..."

    L "Scallion batter..."

    # Change Luci Expression to L_Confused
    show Lucien confused at waist_up_center4,pop
    L "People will put anything on a crepe."
    # Change Luci Expression to L_Neutral
    show Lucien neutral smile pose2 at waist_up_center4
    L "We should make a tuna and wasabi one."
    show Lucien neutral smile at waist_up_center4
    MC "Sushi crepes? You're losing me on this one."
    
    L "Then what about...{w=0.2} pineapple and cheese?"

    MC "I know pineapple on pizza is a thing, but that just sounds gross."
    MC "It'd get weirdly soggy."
    MC "What the world {i}really{/i} needs is pickle crepes."

    # Change Luci Expression to L_Neutral
    show Lucien neutral at waist_up_center4
    L "Coming from someone who doesn't appreciate pineapple like I do? Come on."
    # Change Luci Expression to L_Smug
    show Lucien smug at waist_up_center4
    L "In my opinion, the humble powdered sugar and ketchup crepe is being severely overlooked in the current crepe economy."
    L "So I'm investing early."

    MC "I mean, I wasn't gonna say it, but now that you've mentioned ketchup..."
    MC "We should totally make some tomato and egg crepes–"

    #Knock sfx
    "Someone knocks on the clubroom door,{nw}"
    play sound "audio/sfx/door-knocking.ogg"
    extend " but you both are too wrapped up in the conversation to notice."

    # Change Luci Expression to L_Angry, shake
    show Lucien angry at waist_up_center4, shake2
    L "TOMATO crepes?! You want me dead."

    MC "They're not so bad. If you put enough stuff in the crepe you can barely taste them!"

    # Change Luci Expression to L_Annoyed
    show Lucien annoyed at waist_up_center4, pop
    L "That doesn't change the fact that they're still there!"
    L "And I can {i}still{/i} taste them, by the way."

    MC "At least it’s not a lukewarm gummy worm crepe. Or a squid crepe."

    # Change Luci Expression to L_Neutral
    show Lucien neutral pose2 at waist_up_center4
    L "Or an orange peel crepe. Just the peels."
    # Change Luci Expression to L_Shocked
    show Lucien shocked at waist_up_center4, pop
    L "Wait, that last one actually sounds pretty good-"

    MC "How about a whole live squid? Covered in whipped cream?"

    # Change Luci Expression to L_Neutral
    show Lucien neutral smile at waist_up_center4
    L "Never mind."
    "Someone cleared their throat very loudly and pointedly behind you. It seems your contest for \"Worst Crepe in Existence\" has been interrupted."
    
    N "What the hell did I just overhear?"
    hide Lucien 
    show Lucien at waist_up_center4
    "You both turn around guiltily to see Nayu giving you a thoroughly unimpressed look."
    show Lucien at waist_up_right4 with move
    MC "Oh. Um. Hi?"

    N "You will not be serving live squid crepes on the menu. We're trying to feed the attendees, not poison them."
    show Lucien neutral smile at waist_up_right4, pop
    L "Yeah, we did get a little carried away now that you mention it..."

    N "If you're looking for inspiration, why not just go to a café? There's a crepe place about 10 minutes south of campus."

    # Change Luci Expression to L_Shocked
    show Lucien shocked at waist_up_right4, pop
    L "Oh, good point. Why didn't we think of that?"
    show Lucien neutral smile at waist_up_right4,
    "Nayu doesn't respond, instead choosing to raise a {i}very{/i} pointed eyebrow in your direction."
    "You get the sneaking suspicion that your common sense is being judged. Just a little."
    "While you were busy pondering the source of his (well-deserved) judging, Nayu seems to have given up on the subtle approach."

    N "Bruh. Go outside and touch some grass instead of inventing new cruel and unusual punishment methods."

    MC "Damn. There go my weekend plans."

    "Nayu sighs heavily, leaving the clubroom without another word. Luci turns to face you after the door thuds shut."
    
    show Lucien neutral smile at waist_up_center4 with move
    # Change Luci Expression to L_Neutral
    L "Well, you heard him. Shall we?"
    hide Lucien with dissolve
    stop music fadeout 1.0
    # Change Background to Café
    scene bg luci cafe with fade
    show screentint with dissolve
    "You push the door open,{nw}"
    play sound "audio/sfx/entrance-bell-chime.ogg"
    extend " the bell chiming with your entrance."
    "The hum of conversation and clinking of cups fills the air. The cozy crepe cafe exudes a warm vibe, with plum-colored cushions and old-fashioned booths."
    play music "audio/music/C1 - Chill (1).wav" fadein 1.0 loop
    Hostess "Welcome in."

    MC "Hey there! Is there a table for two available?"

    Hostess "Right this way."
    hide screentint with dissolve
    "The hostess leads you to a cozy table by the window. Sunlight pours in, casting a soft glow over the table."
    "You sit down and open up the menu."

    MC "Any ideas on what to order first?"

    show Lucien neutral smile at waist_up_center4 with dissolve
    # Change Luci Expression to L_Neutral
    L "Not really, but something sweet sounds good."
    # Change Luci Expression to L_Laugh
    show Lucien laughing at waist_up_center4
    L "You can pick though. I trust your taste."
    hide Lucien with dissolve

    "You look over the menu, taking note of a few crepes Luci would probably enjoy, then wave down a waiter who's passing by your table."

    Waiter "Hello! What can I get you?"

    MC "Can I get a tiramisu crepe and a..."

    menu:
        "Spinach, tomato, and cheese crepe.":
            $ crepe_choice = "tomato-crepe"
        "Egg, onion, and corn crepe.":
            $ crepe_choice = "egg-crepe"

    if crepe_choice == "tomato-crepe":
        MC "A spinach, tomato, and cheese crepe... And two ice waters, please."

        "The waiter notes down your order, repeating it back to confirm, then leaves with a nod."

        
        # Change Luci Expression to Laugh
        show Lucien laughing at waist_up_center4, pop with dissolve
        L "A TOMATO crepe? You’re crazy for that."

        MC "It’s tomato, spinach, {i}and{/i} cheese, not just a plain tomato crepe."
        MC "Besides, I got you a tiramisu crepe."

        "You watch his teasing smile soften."

        # Change Luci Expression to L_Blushing
        show Lucien blushing at waist_up_center4
        L "You know me so well."
    
    elif crepe_choice == "egg-crepe":
        MC "The egg, onion, and corn crepe... and two ice waters, please."

        "The waiter repeats your order, writing it down in a notepad, then leaves."
        "You feel a nudge on your shoulder."

        show Lucien neutral smile at waist_up_center4 with dissolve
        L "Egg, onion, and corn? Sounds interesting."

        MC "I was feeling adventurous. I knew you’d like the tiramisu one."
        
        # Change Luci Expression to L_Blushing
        show Lucien blushing at waist_up_center4
        L "You know me well, huh."

    # [Choice Ends]
    hide Lucien with dissolve
    "You chat animatedly while waiting for the waiter."
    "You don't have to wait long as they return with your food in less than ten minutes."

    MC "These look amazing! We should take notes on their presentation."

    #Change Luci Expression to L_Neutral
    show Lucien neutral smile at waist_up_center4 with dissolve
    # show Lucien neutral at waist_up_center
    L "Let’s eat!"

    "You both dig in. Seeing Luci thoroughly enjoy his tiramisu crepe, you..."
    hide Lucien with dissolve

    menu: 
        "Steal a bite.":
            $ player_choice = "steal"
        "Ask to try a piece.":
            $ player_choice = "ask"

    if player_choice == "steal":

        "You take advantage of his distraction and quickly take a piece off Luci’s crepe."
        
        # Change Luci Expression to L_Angry
        show Lucien angry at waist_up_center4, pop with dissolve
        L "Hey! That was mine!"

        MC "Sorry. Couldn't resist."

        "You smirk at him, taking a big bite of your ill-gotten goods."

        MC "Wow... it’s really good!"

        "His fake anger melts into a teasing smile."

        # Change Luci Expression to L_Laugh
        show Lucien laughing at waist_up_center4, pop
        L "You should start sleeping with one eye open."

        MC "Oh, come on! I was the one who got you the tiramisu crepe."

    elif player_choice == "ask":

        MC "Hey, do you mind if I try a bite of yours?"

        # Change Luci Expression to L_Smug
        show Lucien smug at waist_up_center4 with dissolve
        L "Hmm... you chose yours and now want to steal a piece of mine?"

        MC "Just one small bite. Please?"

        "You make your best puppy eyes at Luci, trying to convince him."

        # Change Luci Expression to L_Laughing
        show Lucien laughing at waist_up_center4, pop
        L "Sure you can have a bit. Don’t go stealing the whole thing though."

        MC "Hehe. You're the best."

        "You reach over to take a piece of his crepe and stuff it into your mouth."

        MC "Wow... this tastes amazing!"

    # [Choice Ends]


    MC "Do you want to try a piece of mine? That way we're even."

    # [Start of Crepe Choice dependent dialog]
    if crepe_choice == "tomato-crepe":
        "Luci eyes the crepe suspiciously."
        
        # Change Luci Expression to L_Shocked
        show Lucien shocked at waist_up_center4, pop
        L "As long as you take out those tomatoes."

        MC "No tomatoes, I promise. Just spinach and cheese for you."

    elif crepe_choice == "egg-crepe":
        "Luci eyes the crepe curiously."
        
        # Change Luci Expression to L_Neutral
        show Lucien neutral at waist_up_center4
        L "That's an interesting combination..."

        MC "It’s really good, promise."

    # [End of Crepe Choice dependent dialog]
    show Lucien neutral at waist_up_center4
    "Luci reaches over your plate with his fork, cutting a piece for himself."
    "He hums thoughtfully as he savors the piece before nodding."

    # Change Luci Expression to L_Neutral
    show Lucien neutral smile at waist_up_center4
    L "Wow, it's surprisingly good. A bold decision, but I guess it paid off."

    "You both continue eating, sharing your thoughts on the flavors and taking a few notes."
    "After finishing, you pick the menu back up."

    MC "Since we're already here, do you want to try out another one?"
    MC "I probably can’t finish the whole thing, but we can split it."

    L "Yeah, we can share. Did you have anything in mind?"

    "You lean forward, angling the menu towards Luci so he can also have a look."

    MC "There are still so many options. I can’t decide."

    L "Me either, but I also don’t want to try too many. We’ll just end up back at square one."

    "You nod in agreement, knowing it’d only make it harder to decide."

    MC "How about we pick a few that we’re both curious about and narrow it down from there?"

    "With his agreement, both of you spend a few minutes reviewing the menu, listing which crepes both want to try."

    L "How does strawberries and whipped cream sound? It should be light enough for us to finish."

    MC "I’m curious about the salmon and cream cheese one, too."

    L "There are also the classics. Ham and cheese, banana and chocolate..."

    MC "How about on three, we both point at the one we want to try the most?"

    L "Sounds fun! One..."

    MC "Two..."

    L "Three!"

    "You both point at your favorite in the menu. A smile stretches across your face at your synchronized choice."

    MC "Well, it seems we're settling on..."
    hide Lucien with dissolve

    menu:
        "Strawberries and whipped cream.":
            $ player_choice = "strawberry"
        "Ham and cheese.":
            $ player_choice = "ham"
        "Salmon and cream cheese.":
            $ player_choice = "salmon"

    "Once the waiter heads off with your order, you slump backwards into your seat."
    "You’ll be needing a nap after all this food. Luci seemed to pick up on this."
    # Change Luci Expression to L_Confused
    show Lucien confused at waist_up_center4 with dissolve
    L "{w=0.5}Are you ok? You don’t have to eat anymore if you aren’t feeling well."

    MC "I’m fine, just tired."
    
    # Change Luci Expression to L_Neutral
    show Lucien neutral smile at waist_up_center4
    L "We made a lot of progress today. We can leave the rest for tomorrow after we're done here."

    MC "Yeah! Tomorrow, we can get to the fun part."

    "The waiter returns with your order, setting the crepe in the middle of the table."
    "You reach over and cut yourself a small piece."

    MC "Oooh, it’s perfect!"

    "Luci reaches over to dig in himself, and you both continue your discussion of possible crepe flavors for the festival."

    hide Lucien with dissolve
    #- - - - – - - - - - – - - - - - – - - - - - – - - - - - – - - - - - – - - - - - – -
    # Time passes

    # change scene to sunset street
    scene bg road sunset with fade
    "The sun is already setting by the time the two of you leave the café. Pretty red-orange hues illuminate the quiet city as it slips below the horizon."

    show Lucien neutral smile at waist_up_center4 with dissolve
    L "That was so good! I think I have a better idea of what recipes we can try."

    MC "I do too! Honestly, I was surprised by all the different flavors."

    L "Right? I hope we can make crepes that are just as delicious for the school festival!"

    MC "Speaking of, we should start heading back if we want an early start tomorrow."

    "Luci hums in agreement, but there’s a mischievous twinkle in his eyes."

    L "Yeah, we should head back, yeah..."
    L "Or... we could take advantage of the last rays of sunlight and go for a quick walk around the park? It’s not far from here, and I’ve heard it’s really pretty at night."
    hide Lucien with dissolve

    menu:
        "Walk around the park.":
            $ player_choice = "walk"
        "Head home directly.":
            $ player_choice = "home"

    if player_choice == "walk":

        show Lucien neutral smile at waist_up_center4 with dissolve
        MC "Why not? It’d be a shame to waste the last bit of such a nice day."

        "Luci nods in agreement before motioning with his head in the direction of the park."

        L "Sounds good. Let’s get going before we miss out by standing around."
        stop music fadeout 1.0
        hide Lucien with dissolve
        show screentint with dissolve
        "You both head off towards the park, enjoying the changing atmosphere around you. People rush home, emptying the paths and adding to the calmness of the environment."
        play music "audio/music/G5 - Romantic.wav" fadein 1.0 loop
        "Looking over, you can’t help but admire Luci’s relaxed expression and, in turn, feel yourself relax. It's like some kind of unnoticeable power, you think. Luci looks towards you, giving one of his usual smiles."

        # Change Luci Expression to L_Smug
        show Lucien smug at waist_up_center4 with dissolve
        L "Need something? Or do I have something on me?"

        "You can tell he’s teasing you about being caught."

        MC "Nope, I was just admiring that..."

        "Your eyes desperately look for the closest thing that seems interesting. On the ground, a bit away from you, is a uniquely colored lotus."

        MC "That lotus!"

        "He follows your gaze before walking over to pick it up. Its petals are still damp, only recently having been removed from its lake."

        # Change Luci Expression to L_Neutral
        show Lucien neutral smile at waist_up_center4
        L "I don’t think that’s supposed to be there."

        "He gently hands the lotus to you."

        MC "Maybe it's from a nearby lake?"

        L "Hmm, probably."

        MC "Let’s go put it back. Maybe it still has a chance if we do."
        hide Lucien with dissolve
        scene bg luci pond with fade
        "Walking around, you find a peaceful lake with lily pads and other black lotus floating on the surface. Fish disturb the stillness of the water as they swim below, ducks lazily waddle in and out of the water, and even a turtle happily munches away on some grass."

        MC "This looks like the spot."

        "Kneeling, you release the lotus back into the water before looking around, your eye being caught by brightly colored flowers near the edges of the pond."
        

        menu:
            "Pick one of the poppies.":
                $ flowerPoppy = True
                $ flowerDaisy = False
            "Pick one of the daisies.":
                $ flowerDaisy = True
                $ flowerPoppy = False
        
        "You reach for the flower, feeling the stem give way beneath your fingernails, and stand up."
        "The flower’s petals seem to shine against the dark ripples of the pond."
        show Lucien neutral smile at waist_up_right4 with dissolve

        "Luci is watching you with a gentle smile. The sun is almost gone now, your faces lit by distant streetlights and the glow of the moon."

    
        L "I told you this area was pretty, didn’t I?"

        MC "It is. It’s... really pretty, yeah."

        "You glance at your surroundings again, taking it all in, then look down at the flower."
        hide Lucien with dissolve

        menu:
            "Shove it in his face.":
                $ flowerAction = "shove-in-face"
            "Put it in his hair.":
                $ flowerAction = "put-in-hair"
        
        if flowerAction == "shove-in-face":

            show Lucien neutral smile at waist_up_right4 with dissolve
            "Luci’s expression is somewhat confused as you approach him, brows furrowed."

            # Change Luci Expression to L_Confused
            show Lucien confused at waist_up_right4
            L "What’s that for–"

            MC "It’s–{w=0.5} for you–"

            "Flustered by the weight of his gaze and the comfortable atmosphere, you shove the flower right up into his nose."

            L "Ah–{w=0.7}{nw}"
            show Lucien confused at waist_up_right4, singlejump
            extend " achoo!"

            "Petals fly everywhere as he sneezes, nose scrunching up."
            show Lucien neutral at waist_up_right4
            L "Excuse me."

            "He sniffles."

            MC "Oops, sorry."

            "You turn towards the street, embarrassed."

            MC "Maybe we should head home– I’d rather not catch a cold in the week of the festival."
        
        elif flowerAction == "put-in-hair":

            show Lucien neutral smile at waist_up_right4 with dissolve
            "Luci’s expression is somewhat confused as you approach him, brows furrowed."

            # Change Luci Expression to L_Confused
            show Lucien confused at waist_up_right4
            L "What’s that for?"

            MC "It’s for you."

            "You approach him shyly, twirling it between your fingers. Before you can realize what you’re doing, you gently thread the flower’s stem into his hair."
            show Lucien confused at waist_up_right4, restless
            "You both notice how close you're standing to each other simultaneously, causing Luci to turn away hurriedly."

            MC "Sorry, I should have asked–"

            # Change Luci Expression to L_Blushing
            show Lucien blushing at waist_up_right4

            "You turn towards the street, embarrassed."

            MC "Maybe we should head home–I’d rather not catch a cold in the week of the festival."
        
        # Change Lucien Expression to L_Neutral
        show Lucien neutral smile at waist_up_right4
        L "You’re right. I’ll walk you home."

        MC "T-thanks."
        hide Lucien with dissolve

    elif player_choice == "home":

        MC "Sorry, but I think I’d rather just head home."

        # Change Lucien Expression to L_Neutral
        show Lucien neutral smile at waist_up_center4 with dissolve
        L "No problem! You mentioned that you were tired earlier, and we have a lot of work to do tomorrow. I think we can both use some rest."

        "Relief rushes through you at his reassurance."

        MC "Yeah."

        L "I can walk you home, if you’d like?"

        "You’re about to reject his offer, but then you reconsider–it’ll be dark soon, and you’re not too familiar with the area."
        "And, of course, you appreciate his company."

        MC "That’d be great, thank you."

        "There’s a sense of relief knowing you’re at least avoiding getting lost alone."
        hide Lucien with dissolve
        "Together, the two of you walk as a peaceful silence falls between you. It isn’t awkward, however; it’s comforting. At one point, you even hear him humming."
        "You don’t say anything, instead opting to listen to it."

        MC "That was beautiful. What song was that?"
        show Lucien shocked at waist_up_center4, pop with dissolve
        "Luci startles, as if he’d been lost in his thoughts."
        show Lucien neutral smile at waist_up_center4
        L "Oh! It’s, ah... a song I’ve been working on."

        MC "It sounds nice. You should sing it for me sometime."
        hide Lucien with dissolve

        #----------------------------------------------------------------------
    stop music fadeout 1.0
    
    scene bg road sunset with fade
    "You let the door close behind you, chasing away the slight chill of the night."
    # switch scene to mc bedroom
    scene bg mc bedroom luci with fade
    "Not bothering to flick on the light switch, you drag yourself towards your bedroom as exhaustion begins to settle in."
    "As fun as everything had been, it was still a busy day, and you decided to turn in early. There was still a lot more to come, but you’re excited for it!"

    # [End Day 1]
    jump luci_route_day2

label luci_route_day2:
    # [Start of Luci Day 2]
    window hide
    $ quick_menu = False
    scene black with fade
    show screentint
    show text "{color=#ffff}{size=50}Lucien Route: Day 2{/size}{/color}" at truecenter
    with dissolve
    pause 1.0
    hide text
    with dissolve
    $ quick_menu = True
    hide screentint
    # MC wakes up in her room
    play audio "audio/sfx/bedside-clock-alarm.ogg" volume .7
    scene black with fade
    scene bg mc bedroom luci at partlyblurred with dissolve
    pause 0.2
    scene bg mc bedroom luci at unblur with dissolve
    play music "audio/music/C1 - Chill (1).wav" fadein 1.0 loop
    "Your early morning alarm rudely jolts you out of the very nice dream you were having."
    "You reach out from under the covers and slap your mattress a few times."
    "You somehow manage to silence the shrill beeping before burrowing back into the pillows, trying to return to the..."
    "What was your dream about again?"
    "Well, it's gone now. Might as well just get up."

    MC "Ugh{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3} Why am I waking up so early again?"
    MC "Right. The supermarket. Did Luci text me back yet?"

    
    # Phone asset appears
    show phone texting ltop lbottom luci1 luci2 at asset_center, move_up
    pause 0.5
    "You scroll through your messages, looking for a reply."
    # Luci: The only thing I'm missing from our list is whipped cream because the store I went to yesterday was completely out for some reason. I think one can should be enough?
    # Luci: Also, if you can find a small bag of flour, that would be great. I have less than I thought, and I don't want to run out in the middle of our recipe testing.
    L "\"{i}The only thing I'm missing from our list is whipped cream because the store I went to yesterday was completely out for some reason. I think one can should be enough?{/i}\""
    L "\"{i}Also, if you can find a small bag of flour, that would be great. I have less than I thought, and I don't want to run out in the middle of our recipe testing.{/i}\""
    # Phone Asset dissapears
    hide phone texting

    MC "Shouldn't take too long then. Whipped cream, flour..."

    "A devious grin spreads across your face as the one ingredient you know Luci won't have comes to mind."

    MC "And those too."

    "With that, you hop out of bed to get changed."
    stop music fadeout 1.0
    # Change to Zanny Supermarket BG
    scene bg zanny market with fade
    pause 1.0
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop

    "Unfortunately your local supermarket is in the exact opposite direction of Luci's house, so you make a stop at a Ballmart a few blocks away."
    "It's your typical Ballmart, all things considered." 
    "Neon lights, scuffed floors, tired employees who grumpily point you in the direction of the dairy aisle because supermarkets like these always seem to rearrange the entire store once every few months for no reason."
    "Your trip goes pretty eventfully otherwise, aside from the fact that you made it there just in time to buy the last of their whipped cream. Who's buying all the whipped cream in your city?"
    "You briefly consider asking the lone cashier, but decide against it since the bags under their eyes would get them stopped at TSA."
    
    # Change to scene Common Road daylight
    scene bg road daylight with fade
    "With your goods secured, you're still pondering the sorts of slapstick scenarios that would involve purchasing ungodly amounts of whipped cream as you wind your way down the sidewalk to Luci's house."
    
    MC "House number 1017... Here it is."

    "It's a pretty small building tucked away in the corner of a quiet cul-de-sac. You see no visible doorbell, so you knock on the door a couple times."

    play audio "audio/sfx/door-knocking.ogg"
    pause 0.5

    "You hear footsteps on the other side of the door before it swings open to reveal a messy-haired Luci in some sort of{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw} "
    
    show Lucien fullbody neutral apron at fullbody_center4 with dissolve
    extend "pink cat apron?"

    # Change Luci Expression to L_Laugh
    show Lucien fullbody laughing apron at fullbody_center4
    L "Hello!"

    MC "Ah-"

    "Somehow you're not {i}entirely{/i} surprised, but you'd have expected him to wear a black cat apron, not a pink one."
    
    hide Lucien with dissolve

    menu:
        "Is your hair always this messy before you leave the house?":
            $ player_choice = "ignore-apron"
        "A cat apron? Well, it's fitting.":
            $ player_choice = "attention-apron"

    if player_choice == "ignore-apron": 
        # Change Luci Expression to L_Confused
        show Lucien fullbody confused apron at fullbody_center4 with dissolve
        L "Is it really that messy?"

        MC "You don't think so? Your bedhead must be absolutely atrocious."

        # Change Luci Expression to L_Laugh
        show Lucien fullbody laughing apron at fullbody_center4, pop
        L "Whatever. Just come in."

    elif player_choice == "attention-apron":
        # Change Luci Expression to L_Blush
        show Lucien fullbody blushing apron at fullbody_center4 with dissolve
        
        L "What's that supposed to mean?"

        MC "Oh, nothing. It's cute."

        L "My mom gave it to me! What was I supposed to do, say no?"

        MC "Yeah, yeah. Let me in so we can get started."
    
    # [End of Choice]
    show Lucien fullbody neutral smile apron at fullbody_right4 with move
    "Luci steps aside to let you through the door, and you kick off your shoes before following him into the main living area on the left."

    hide Lucien with dissolve
    # BG change?
    show screentint with dissolve
    "It's small but cozy, with a comfy-looking couch parked in front of the TV wedged between two giant bookshelves. There's a strange ghost-looking plushie on the coffee table alongside a half-full coffee mug."
    "The star-shaped string lights draped around the mishmash of furniture and shelving are turned on, adding a warm glow to the space."   
    
    MC "You have one of those {i}Bario Racing{/i} steering setups? With the foot pedal and everything?"

    # Change Luci Expression to L_Neutral
    # show Lucien fullbody apron neutral at fullbody_center with dissolve
    show Lucien fullbody neutral smile apron at fullbody_center4 with dissolve
    L "Yup. Ten dollars on BBay"

    MC "Damn, not bad. No wonder you smoke us all when we play."

    hide Lucien with dissolve
    # Change Scene to Lucis Kitchen
    scene bg luci kitchen with fade
    "As you walk into the kitchen area, you notice that Luci seems to have unloaded every single pot, pan, and semi-flat cooking element he owns onto his poor kitchen island. You can barely see the countertop."

    MC "You know it's just the two of us testing recipes today, right? We're not trying to feed an army."
    
    # Change Luci Expression to L_Shocked
    show Lucien shocked apron at waist_up_center4, pop with dissolve
    L "Well, I didn't know what pan would be best for making crepes, so I just set all of them out..."

    MC "Fair enough."
    MC "Wait, isn't this Cass' nonstick skillet?"

    # Change Luci Expression to L_Angry
    show Lucien angry apron at waist_up_center4, pop
    L "Don't tell him I still have that!"

    MC "Man, I remember he was sooooo mad about losing it. Didn't he get it on sale too?"
    show Lucien neutral apron at waist_up_center4
    L "Well-"

    MC "But I won't tell him if you let me win the next time we play {i}Bario Racing{/i}."

    # Change Luci Expression to L_Crying
    show Lucien crying apron at waist_up_center4, pop
    L "Noooooo..."

    MC "Or you can return it after the festival."

    L "It's my only good skillet! Besides, he still has my dutch oven and he refuses to give that back."

    MC "Well, tough shit."
    MC "Alright, let’s get this show on the road. We have our ingredients, we have our tools... Do you have the final menu?"

    # Change Luci Expression to L_Smug
    show Lucien smug pose2 apron at waist_up_center4, pop
    L "Do you even need to ask?"

    "Luci pulls out a piece of paper from his back pocket. Scrawled on the paper is a short list of the decided-upon crepe flavors."

    # Change Luci Expression to L_Neutral
    show Lucien neutral smile apron at waist_up_center4
    L "So we have... tiramisu and strawberries with whipped cream for our sweet options-"

    MC "I wonder who snuck that tiramisu option in~"

    L "... and ham-egg-cheese and salmon-cream-cheese for savory."

    MC "That’s a good mix of classics and interesting flavors, however..."

    "A wide smile spreads through your face as you reach into the bag of groceries you brought."

    MC "I think we should make a small change."

    "You place a bunch of tomatoes on the counter, causing Luci’s face to immediately scrunch up."

    # Change Luci Expression to L_Angry
    show Lucien angry apron at waist_up_center4, pop
    L "What.{w=0.5} Are.{w=0.5} Those."

    MC "Tomatoes, of course! So for the savory crepes, I think it’d be good to change out the ham for tomatoes. A bold new direction for our bold little stand."

    L "Bold?!? More like a crime against crepes!"

    "Luci crosses his arms, eyes narrowing as he stares at the tomatoes with hatred."

    L "I'm not letting those near anything that's supposed to taste good."

    "You break out in loud laughter at his indignant tone."

    MC "Oh come on, ham’s too boring. Tomatoes are the future, trust me!"

    # Change Luci Expression to L_Annoyed
    show Lucien annoyed pose2 apron at waist_up_center4
    L "I think I’d rather stick to the past, thanks."
    show Lucien annoyed apron at waist_up_center4
    "You start sorting through the rest of the ingredients, taking them out of the bag completely unfazed by Luci’s protest. Giving up on complaining, he also starts putting away the tools you won’t need."

    # Change Luci Expression to L_Neutral
    show Lucien neutral apron at waist_up_center4
    L "So, which batter do we start with? Sweet or savory?"

    MC "Let’s start with the..."
    
    hide Lucien with dissolve

    menu:
        "...chocolate batter. Get the hardest one done with first.":
            $ player_choice = "chocolate-batter"
        "...classic batter. It will serve as good practice.":
            $ player_choice = "classic-batter"

    if player_choice == "chocolate-batter":
        "Luci brings out a large bowl, setting it in front of you. While he brings the ingredients closer, you pull out your phone, placing it on the counter with the recipe showing on the display."

        MC "Alright. First off, add one cup of flour. Can’t mess this up."

        "You sift the flour into the bowl, a small powder clouding up in the air."

        show Lucien neutral apron at waist_up_center4 with dissolve
        # Change Luci Expression to L_Smug
        show Lucien smug apron at waist_up_center4 with dissolve
        L "If you spill any of that, I’ll be very upset."

        MC "Oh please, I’m a pro."

        "You measure the sugar, salt, and cocoa powder, before dropping it in a little swirl over the flour. Luci claps excitedly at your silly performance."

        MC "I think I have showcased my skills enough; it’s your turn now."

        "You step away from the bowl, dramatically throwing your hands wide, offering your spot to him with a slight smirk pulling at your lips."

        # Change Luci Expression to L_Neutral
        show Lucien neutral smile apron at waist_up_center4
        L "Oh! My turn to shine now. What’s next?"

        "You read off the recipe out loud."

        MC "Add a quarter cup of milk and whisk until the texture is smooth."

        "Luci gets to work, pouring the milk and whisking with ease. He is carefully looking at the batter, making sure not to over-work the mix."

        # Change Luci Expression to L_Smug
        show Lucien smug apron at waist_up_center4
        L "I think that is smooth enough. What does the professional think?"

        MC "Looks good sous-chef! Time to add the eggs and butter... and more whisking for you."

        # Change Luci Expression to L_Laugh
        show Lucien laughing apron at waist_up_center4, pop
        L "I’m starting to believe you only tagged me in so I would be the one whisking."

        MC "Of course not! I would never..."

        "Luci works smoothly, adding the ingredients and whisking them carefully. He adds the rest of the milk, continuing to whisk until the mix is smooth again."

        MC "It looks great already!"

        # Change Luci Expression to L_Neutral
        show Lucien neutral smile apron at waist_up_center4
        L "All that is left is for it to rest."

    elif player_choice == "classic-batter":
        "Luci brings out a large bowl, setting it on the counter. While he brings the ingredients closer, you pull out your phone, settling it on the counter with the recipe showing on the display."

        MC "Alright. Step number one, add flour, salt, sugar, and a dash of olive oil into a bowl."

        show Lucien neutral apron at waist_up_center4 with dissolve
        # Change Luci Expression to L_Smug
        show Lucien smug apron at waist_up_center4
        L "Let me show you how it’s done."

        "Luci grabs the ingredients, separating the correct amounts before flashily adding the ingredients into the bowl. He looks over at you flashing a smug grin at his own performance."

        MC "Wow! Lunch and a show!"

        # Change Luci Expression to L_Laugh
        show Lucien laughing apron at waist_up_center4
        L "Okay what’s next?"

        "You continue reading the recipe out loud."

        MC "Add half a cup of milk and whisk until the texture is smooth. Add two eggs and the melted butter and whisk again until smooth."

        "You hand Luci a whisk, reaching over for the ingredients."

        MC "You can whisk while I add the ingredients."

        # Change Luci Expression to L_Neutral
        show Lucien neutral apron at waist_up_center4
        L "This batter will be for the tomato crepes and I’m forced to do all the labor."

        MC "Complaining won’t change your fate."

        "Luci gets to work whisking with ease. Together you carefully add the ingredients, making sure the batter remains smooth."
        show Lucien neutral smile apron at waist_up_center4
        L "It smells great, let’s let it sit for a few minutes."
    
    # [End of Choice]
    hide Lucien with dissolve
    "With one of the batters ready, you are both now more confident. You efficiently follow the steps and soon you find yourself with two perfectly smooth bowls of crepe batter."

    MC "So according to the instructions online, we need to add different amounts of batter depending on the pan size... which ones do you have?"

    "Luci looks over at the pans piled up on the side, before reaching out to a large-looking one."
    show Lucien neutral smile apron at waist_up_center4 with dissolve
    L "I think this one is a 10-inch. It should work fine and it’s not too heavy to handle."

    MC "Yeah that is perfect!"

    "Luci places the pan on the stove, turning it on and allowing it to preheat."

    L "Alright, time to cook these bad boys. Who’s going first?"

    hide Lucien with dissolve

    menu:
        "I'll go first...":
            $ player_choice = "mc-first"
        "You go first...":
            $ player_choice = "luci-first"

    if player_choice == "mc-first":
        MC "... Let’s see how bad it really is."

        "You step up to the pan grabbing the ladle while Luci watches closely, his arms crossed and an eyebrow raised in silent judgment."

        MC "Alright, here goes nothing."

        "You pour a small amount of batter into the pan, and it immediately spreads unevenly. The shape ends up looking more like a lopsided pancake than a crepe."
        "You try to flip it with a quick motion, but it ends up folding in half awkwardly, looking more like a crumpled mess than anything else."

        # Change Luci Expression to L_Laugh
        show Lucien laughing apron at waist_up_center4, pop with dissolve
        L "Well, that... {w=0.5} was certainly a crepe. Maybe a bit too experimental?"

        MC "Awww come on, it’s my first time trying this. You think you can do better?"

        "You pull the \"crepe\" off the pan and place it on a plate, trying to salvage its shape."

    elif player_choice == "luci-first":
        MC "... Show me how it's done."

        # Change Luci Expression to L_Smug
        show Lucien smug apron at waist_up_center4 with dissolve
        L "Tsk, easy. I could do this in my sleep."

        "Luci grabs the ladle with an exaggerated flourish, ready to show off his skills."
        "He pours the batter into the pan confidently, but the batter quickly spreads out too thin in some areas and too thick in others. His attempt looks more like a scrambled blob than a delicate crepe."

        # Change Luci Expression to L_Annoyed
        show Lucien annoyed apron at waist_up_center4, pop
        L "What the hell? This is supposed to be easy!"

        MC "And here I thought you were the expert!"

        "Luci tries to flip it, but the crepe rips in the middle, creating an even more chaotic mess. He shifts it to the plate, looking dejected..."

        L "Maybe...{w=0.3} you should give it a shot next."

        MC "Sure thing, sous-chef. You did great. Really great."

    # [End of Choice]
    
    hide Lucien with dissolve
    window hide
    $ quick_menu = False
    scene CG Luci 1 with fade
    
    pause 2.0
    $ quick_menu = True
    "After a few more attempts..."
    "You both take turns at the stove and after a few more messy and hilariously-shaped failures, you start to get the hang of it."
    "The blobs slowly start taking more recognizable shapes, looking smoother. Finally, you manage to make a perfect crepe."

    MC "This is it! Look at it!"
    scene bg luci kitchen with fade

    # Change Luci Expression to L_Laugh
    show Lucien laughing apron at waist_up_center4, pop with dissolve
    L "We did it! It’s perfect!"

    "All the practicing pays off, allowing you both to make quick work of the rest of the batter."

    MC "I guess we are ready to fill these with some delicious toppings now... And yes, that includes the tomatoes."

    # Change Luci Expression to L_Annoyed
    show Lucien annoyed apron at waist_up_center4
    L "I was hoping you had forgotten about them..."

    MC "It’s the last thing I’d forget about, Luci."

    "Picking up one of the washed tomatoes, you hold it out towards him, causing him to back away."

    # Change Luci Expression to L_Angry
    show Lucien angry apron at waist_up_center4,pop
    L "Hey! Keep that thing away!"

    MC "You’re being so overdramatic. They’re just tomatoes, not cursed artifacts."

    "You slice into one with theatrical care, watching Luci flinch at every cut like you’re defusing a bomb."

    MC "If you want to avoid {i}touching{/i} tomatoes that bad, just help me out by preparing the tiramisu mix."
    show Lucien neutral apron at waist_up_right4 with move
    "Luci nods in agreement, and you both set to work in a comfortable quiet."
    "You stick your tongue out as you continue prepping the fillings—ham, cheese, salmon, and cream cheese—making sure everything is sliced and separated into different bowls so the assembling is easier."

    "Luci is hard at work beside you, currently spooning mascarpone into a bowl. His coffee machine buzzes behind you as he readies the espresso for the mix. He starts humming the same song he did the day before as he whisks the ingredients together."
    show Lucien neutral apron at waist_up_center4 with move
    pause 0.3
    # Change Luci Expression to L_Neutral
    show Lucien neutral smile apron at waist_up_center4, pop
    L "The tiramisu mix is ready. Want to taste?"

    "He offers you a spoonful of the mix. The bite is rich and creamy, and you hum in satisfaction."

    MC "Hmm~ That’s incredible!"

    # Change Luci Expression to L_Smug
    show Lucien smug apron at waist_up_center4
    L "Obviously."

    "You hold up the bowl filled with the chopped tomatoes up to his face."

    MC "Want to taste?"

    # Change Luci Expression to L_Deadpan
    show Lucien deadpan apron at waist_up_center4
    L "Let’s move on, please."
    # Change Luci Expression to L_Neutral
    show Lucien neutral smile apron at waist_up_center4
    L "Alright, which one should we do?"

    MC "Let’s go with..."
    hide Lucien with dissolve

    menu:
        "Tiramisu.":
            $ player_choice = "tiramisu"
        "Tomato Egg Cheese.":
            $ player_choice = "tomato-egg-cheese"
        "Strawberries and Whipped Cream.":
            $ player_choice = "strawberries-whipped-cream"
        "Salmon Cream Cheese.":
            $ player_choice = "salmon-cream-cheese"

    if player_choice == "tiramisu":
        show Lucien neutral smile apron at waist_up_center4 with dissolve
        L "I was hoping you’d say that. The mix already tastes delicious."

        "You reach over for the tiramisu mix, lathering it in layers over the crepe."

        MC "Do you have any ideas on what to decorate it with?"
        
        "He quickly reaches over to grab the chocolate syrup as a start, holding it up with an expectant expression."

        MC "Oh! Good idea, maybe we can also use..."

        "You reach over to pick up the cocoa powder and some chocolate-covered coffee beans."

        MC "These?"

        L "If we don’t go too crazy using powder, it should go well with the syrup."

        MC "We could even use the cream left over from the filling to make a dollop and use the beans to top it off."

        "You bring the bowl filled with the remaining mixture and place it on the counter."

        L "Good idea. Let’s get to work then."

        "You get to work carefully putting it together, using a wooden spoon to lay the mix on the batter before letting it fold the crepe together."
        "As he wraps the wax paper, you place one final dollop of cream on top before finishing it off with the coffee beans."

        MC "I’d say that it's done!"
    
    elif player_choice == "tomato-egg-cheese":
        show Lucien neutral apron at waist_up_center4 with dissolve
        L "I was hoping you’d never say that. This feels like a targeted attack."

        MC "Maybe it is~ Can you preheat a new pan? We will need it for the eggs."

        "While Luci heads for the cabinet, you grab a few eggs off the carton and whisk them with ease before shredding some cheddar cheese over it."
        "The mixture sizzles in the pan. As it begins to set, you reach over to the bowl of tomatoes and carefully dump them into the pan."

        # Change Luci Expression to L_Confused
        show Lucien confused apron at waist_up_center4
        L "... Okay, that actually smells pretty good."

        MC "Told you it’d be good!"
        
        "Once the eggs are cooked, you slide them off the heat and carefully spoon the egg-cheese-tomato mixture into the crepes before folding them into a neat pocket."

        MC "What would be a good garnish?"

        L "What do you think of basil leaves and..."

        "Luci reaches over for the leaves, grabbing the balsamic glaze container along the way. He scatters the leaves on top and drizzles a spiral of glaze over the crepe."

        MC "Well? Want to take a bite?"

        # Change Luci Expression to L_Deadpan
        show Lucien deadpan apron at waist_up_center4
        L "Over my dead body."

        MC "Okay, okay. But if you aren’t trying this one, you owe me dinner tonight."

        L "As long as I don’t have to eat it..."

    elif player_choice == "strawberries-whipped-cream":
        show Lucien neutral smile apron at waist_up_center4 with dissolve
        "The strawberries and whipped cream! I’ve been dying to try these out."

        L "Same, the strawberries taste delicious."

        "You reach over for the strawberry-filled bowl, carefully filling the crepe. Once you are done, Luci reaches over with the whipped cream, dropping a dollop among the strawberries before folding it and adding a few peaks on the edge."

        MC "My mouth is watering already..."

        L "As for garnish..."

        "Luci trails off and grabs the powdered sugar, his voice trailing off as he thoughtfully looks at the options. You reach over and pick up the flowers."

        MC "How about these? Perfect for spring while at it."
        MC "Plus, we’re kind of out of strawberries..."

        "You both may have snacked on a few too many of the strawberries while working."

        L "And whose fault is that?"

        MC "Hey! Don’t go blaming that on just me."

        "You both go back and forth for a bit before laughing it off. After prepping your crepe, you get to decorate it. Luci takes over, powdering it lightly before passing it over to you for the final additions."
        "Placing the flowers in a neat arrangement, you step back and look it over before nodding approvingly."

        MC "I think we’re safe to say that this one is all good to go!"

        L "Mm, agreed. I hope it tastes as good as it looks, though."


    elif player_choice == "salmon-cream-cheese":
        show Lucien neutral smile apron at waist_up_center4 with dissolve
        L "I’m really curious about this one. I trust it will taste well, but it’s not a common flavor."

        MC "Let’s not mess it up!"

        "You reach over for the pre-sliced smoked salmon, tearing a few slices and making sure they are the right size."
        "Meanwhile, Luci grabs the cream cheese, spreading it lightly over the crepes before pushing the plate in your direction."

        L "How do we want to decorate this one?"

        "You carefully add the sliced salmon, folding the crepe before with care."

        MC "I think lemon will go well with the salmon... But what else?"

        L "Oh! I know."

        "He reaches over for the knife, finely chopping some dill and slicing a few lemon wedges."
        "He fiddles with the garnishes before taking a step back."

        # Change Luci Expression to L_Smug
        show Lucien smug apron at waist_up_center4
        L "I think this will be our best savory flavor crepe."

        MC "Of course you’d think that."

        hide Lucien with dissolve
        #- - - - – - - - - - – - - - - - – - - - - - – - - - - - – - - - - - – - - - - - – -
        # Time passes

        "Finally, many finished crepes fill the kitchen. Emphasis on ‘many’ as there were way too many for just yourselves."

        show Lucien smug apron at waist_up_center4 with dissolve
        L "We’re not going to eat all of these, are we?"

        MC "Nope. Not happening."

        "You have a feeling that by the end of this festival period, you’ll be sick of crepes for a good while."

    # [End of Choice]

    MC "Is that it, then?"
    # Change Luci Expression to L_neutral
    show Lucien neutral smile apron at waist_up_center4
    L "That’s it."

    "You look around the kitchen, noticing the mess that the two of you have made–used dishes clutter the sink and splotches of batter are scattered wildly, like battle scars."
    "Luci seems to deflate slightly at the mess."

    L "Ah, that’s{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3} a lot..."

    "You understand his reluctance–cleaning up the mayhem won’t be easy."
    "Snapping out of your thoughts, you realize that Luci has already started on the disordered kitchen island, putting items back in their respective places."
    "You want to help, but you’re unsure of where to start."

    hide Lucien with dissolve

    menu:
        "Wash the dirty dishes.":
            $ player_choice = "dishes"
        "Wipe the countertops.":
            $ player_choice = "countertop"
        "Mop the floors.":
            $ player_choice = "floors"

    "You move towards your task, but Luci’s voice stops you before you get there."
    
    show Lucien neutral smile apron at waist_up_center4 with dissolve
    L "Oh, you don’t have to worry about that."

    "Confused, you blink at him. He stares back."

    # Change Luci Expression to L_Confused
    show Lucien confused apron at waist_up_center4, pop
    L "I’ll tidy up the kitchen, you can wait in the living room if you’d like. You’re a guest here, after all."

    "It’s a ridiculous notion honestly, you had both contributed to the mess, but your heart still warms at the offer."

    MC "I’ll help you!"

    "He still looks doubtful, so you add:"

    MC "We made this mess together. And don’t forget, you’re making me dinner later~!"

    "You won’t pass up an opportunity for his cooking, after all!"

    # Change Luci Expression to L_neutral
    show Lucien neutral smile apron at waist_up_center4
    L "Well, if you insist. Maybe I can find a use for the ingredients we didn’t use up."
    
    "He nods to himself, then tosses you a moistened cloth."

    L "Hopefully, we can get this done quickly. Are you ready?"

    MC "Let’s do it!"

    "With your combined forces, the job seems effortless. When the two of you are finished, the kitchen is sparkling clean–save for the uneaten remains of the crepes you’d made."

    L "Whew, finally done." 

    MC "Yep, and we still have a couple of hours before dinner."

    L "Why don’t we pack up the crepes first, and then find something to do to kill time?"

    MC "That sounds like a plan."

    "Together, the two of you consolidate the remaining crepes into containers. There’s a lot more than you had expected."

    MC "Uh... I don’t think either of us can finish all of this before they get stale."

    L "You’re right, but I wouldn’t want to just throw them away..."

    MC "Oh, maybe..."

    hide Lucien with dissolve

    menu:
        "... We could give some to the other club members?":
            $ player_choice = "give-other-members"
        "Your neighbors might enjoy them?":
            $ player_choice = "give-neighbors"

    if player_choice == "give-other-members":

        # Change Luci Expression to L_shocked
        show Lucien shocked apron at waist_up_center4, pop with dissolve
        L "Hm, you’re right! I’m sure they’d like to sample the recipes before the festival as well."

        MC "Okay!"

    elif player_choice == "give-neighbors":
        show Lucien neutral smile apron at waist_up_center4 with dissolve
        L "Well, we’ll see... either way, I'm sure we can figure something out!"

    # [End of Choice]
    hide Lucien with dissolve

    "Satisfied with that idea, you set the remaining crepes to the side."
    "A quick glance at the oven clock reveals that it’s late afternoon. There’s still a lot of time before the end of the day, and you don’t have anything planned."
    "Task finished, the two of you stand a bit awkwardly in the space between the kitchen and the living room. You find yourself glancing over the area again, eyes catching on a set of controllers."

    MC "What games do you have?"

    show Lucien neutral at waist_up_center4 with dissolve
    L "Games... I have {i}Crazy Kitchen, Graffiti Sprints{/i}, some others...{w=0.3} Oh!"

    "His eyes light up as the two of you approach the TV."
    show Lucien neutral smile at waist_up_center4
    L "We should play {i}Bario Racing{/i}!"

    MC "Wait, yes! Can I try out your gamer setup?"

    # Change Luci Expression to L_Laugh
    show Lucien laughing at waist_up_center4, pop
    L "The foot pedals? Sure."

    MC "Thanks!"
    MC "... But you shouldn’t agree so easily."

    # Change Luci Expression to L_Smug
    show Lucien smug at waist_up_center4
    L "Is that some sort of challenge?"

    MC "I’m going to crush you!"
    hide Lucien with dissolve
    show screentint with dissolve
    "An intense competition begins. You and Luci are neck-to-neck, ending up in various positions on the leaderboard."
    "If you were to be keeping track, you would say that it’s a close tie. Each round is accompanied by exclamations as you clash. Time passes inadvertently."

    # Change Luci Expression to L_neutral
    show Lucien neutral smile pose2 at waist_up_center4 with dissolve
    L "It’s almost time for dinner, we should probably wrap up soon. I agreed to make you something, right?"

    MC "Uh-huh. And whoever loses the next round is doing the dishes!"

    # Change Luci Expression to L_Shocked
    show Lucien shocked pose2 at waist_up_center4, pop
    L "Hey, wait–!"

    "You decide to let Luci win, and \"accidentally\" fall off of the map one too many times. It wouldn’t be fair to make him cook {i}and{/i} clean for the both of you."
    "Once the games are put away, you migrate to the kitchen once more. Luci puts his hands on his hips."

    # Change Luci Expression to L_neutral
    show Lucien neutral smile at waist_up_center4
    L "So, what do you want to eat?"
    hide Lucien with dissolve

    menu:
        "Pasta alfredo!":
            $ player_choice = "pasta"
        "A ham sandwich would be nice...":
            $ player_choice = "sandwich"
        "Why not a classic? Some good fried rice?":
            $ player_choice = "friedrice"

    
    "In what seems to be no time at all, the two of you are sharing a meal together. He pops the cap of a bottle of sriracha mayo, applying it generously to his food before offering it to you."
    
    show Lucien neutral smile at waist_up_center4 with dissolve
    L "Have you ever tried sriracha mayo before?"

    MC "I haven’t, actually! Should I?"

    # Change Luci Expression to L_Laugh
    show Lucien laughing at waist_up_center4, pop
    L "I might be a little biased, but... I would say it’s pretty good."
    hide Lucien with dissolve

    menu:
        "Decline":
            $ player_choice = "decline"
        "Accept":
            $ player_choice = "accept"

    if player_choice == "decline":
        # Change Luci Expression to L_neutral
        show Lucien neutral smile at waist_up_center4 with dissolve
        MC "I think I’ll have to pass on this one for now–I’m not sure if it’ll go with the dish."
        
        L "Ah, understandable."

        "Even without the sriracha mayo, the food is undeniably delicious, and you leave with a full stomach and light steps."

    elif player_choice == "accept":
        show Lucien neutral smile at waist_up_center4 with dissolve

        MC "Sure, I’ll try it, why not?"

        "Luci beams at you, passing you the bottle."
        "It’s good, although a bit spicy, and you nod approvingly."

        MC "Better than I expected, wow... what do you normally eat this with?"

        L "A lot of things..."
    
        "The two of you hold a long conversation, and you make sure to thank him for the meal."
        "In turn, he thanks you for your company, and it dissolves into you both finding the most minuscule things to be thankful for. Before you know it, evening passes into night. It's time for you to go."
    
    # [End of Choice]
    hide Lucien with dissolve
    scene black with fade
    "You had a productive, exciting day."
    stop music fadeout 1.0
    # End of Day 2
    if "L" not in collected_routes:
        $ collected_routes.append("L")

    if len(collected_routes) == 5:
        $ renpy.save("chapter1_end")
        scene black with fade
        jump general_ending

    else:
        jump choose_route
