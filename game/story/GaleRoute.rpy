# Start of Gale route
label gale_route:
    scene bg clubroom
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop

    show Gale at waist_up_center2 with dissolve

    MC "I'll help Gale."

    show Gale laugh 
    G "Great! I have to run and turn in an assignment first, but we can meet out by the stalls later? I think they started setting everything up already."
    show Gale neutral
    
    MC "Sure! That’s no problem. Meet you by the north part of the campus lawn?"
    
    #
    #"Hell yeah! We're going to make the best decorations ever!"
    G "Great–thanks!"


    
label gale_route_day1:
    stop music fadeout 1.0
    window hide
    $ quick_menu = False
    scene black with fade
    show text "{color=#ffff}{size=50}Gale Route: Day 1{/size}{/color}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    $ quick_menu = True

    # Day 1
    play music "audio/music/C1 - Chill (1).wav" fadein 1.0 loop
    scene bg_gale_empty_stall with dissolve
    
    "The spring wind buffets you as you stand and wait for Gale to arrive. You take the chance to survey the area a bit, surprised at what you see."
    "Just outside of the hall where the club rooms are, stalls line the walkway. What is usually a pretty open green area is now packed with stands for every conceivable festival food and activity."
    "They are lined up in rows back to back, snaking around the lawn and providing a vast market for attendees to wander through."
    "Decorations range from empty to completely decked out, and club members run around with ribbons and banners, shouting as they get set up."

    show Gale neutral at waist_up_center2 with dissolve
    G "Man, they’ve really gotten some work done down here."

    "You turn to see him approaching and smile."
    
    MC "Yeah, even just a few days ago, none of this was set up."

    G "We work hard, but Nayu and the events team work harder. I hope you weren’t waiting long."

    MC "Not really, don’t worry. Did you get your assignment turned in?"

    G "Yep! Straight into the professor’s hand and everything."

    "You high-five before you both turn your attention towards the stalls."

    MC "Let’s go find our booth. We can scope out some of the ‘competition’ on the way."

    show Gale laugh
    "Gale laughs, and you start down the rows, checking the group messages to confirm which stall is for your club."
    "You get jolted from your careful examination of the booth numbers by Gale’s incredulous voice, looking up and around at the surrounding stalls’ banners, not just their ID numbers."
    
    show Gale confused pose2
    G "Is...that...an ocean fishing stand?? How are they going to manage that on campus?"
    
    MC "I’m more concerned about..."

    menu:
        "...the ultra spicy sauce booth.":
            $ player_choice = "opt-1"
        "...the stall boasting medieval weaponry.":
            $ player_choice = "opt-2"
        "...the vegetable-tasting stall.":
            $ player_choice = "opt-3"

    if player_choice == "opt-1":
        MC "...the ultra spicy sauce booth."
        #spic sauce asset?
        
        show Gale shocked at waist_up_center2, singlejump
        G "Eugh… after trying some of those with Luci last term, I’m staying as far away as possible from that one. My stomach {i}still{/i} hasn’t recovered."
       
        MC "It was hilarious as an observer, though."
    
    if player_choice == "opt-2":
        MC "...the stall boasting medieval weaponry."
        
        show Gale neutral at waist_up_center2, pop
        G "WAIT – where??"
        
        MC "According to the listing, it should be somewhere back there."

        "You point vaguely to the area near the main gate."
        
        MC "I don’t think they will be allowed to keep that one on campus, though…"
        
        G "Aw… It’d be so cool…"
    
    if player_choice == "opt-3":
        MC "...the vegetable-tasting stall."
        
        show Gale annoyed
        G "You can go to that one alone."
        
        MC "But it’s the homegrown versus store-bought taste-test!"
        
        G "{i}Alone.{/i}"
    
    show Gale neutral
    
    "You and Gale turn into another row of stalls, and he starts scanning the IDs as well."

    G "Hey, this is ours!"
    
    "There’s an empty stall with the gaming club’s name on a piece of paper taped to it."
    
    "The stall is tall, with a signboard above it for a banner and two poles on either side that are usually used for recreation on the lawn. A plastic screen has been set up on most of the open part of the booth, perfect for their food stall."
    
    MC "We have quite a bit to work with - this is pretty fancy!"

    
    G "Definitely - we could put some flags up between these poles."
    
    MC "And string some lights around them too!"
    
    G "Yeah! Great thinking, [player_name]. That will make us stand out."

    "Gale takes a little notebook from his pocket and steps up to the stall, circling it a few times while you watch."

    "He starts scribbling down notes, brows furrowed and muttering under his breath."
    
    show Gale confused pose2
    G "String lights, flags on a line…"

    MC "There’s a pretty big blank space up top - I think we should make a banner to fill that space and announce the crepes."

    "Gale nods and jots it down in his notebook."

    MC "We might also want to make some flyers to pass out - we can get some details from Rosco about the game, and we can put something together. That way it’s actually advertising our club and what we do!"
    
    show Gale neutral
    G "You mean you don’t want to advertise the {i}Ichi{/i} tournaments?"
    
    MC "Maybe not right off the bat. They can join {i}Ichi{/i} tournaments after they’ve been in the club for at least twenty days."
    
    G "Gatekeeping the {i}Ichi{/i}? Diabolical."

    MC "You just want someone you can win against–"
    
    G "Hey! I almost won our last game, and it’s not like you actually won."
    
    MC "Check the board in the club room! I have more wins than you."
    
    G "Being next to last isn’t the flex you think it is."
    
    MC "Still more than you."
    
    G "Yeah, yeah…"
    
    "You both chuckle and look back at the empty stall."
    
    G "Okay, so we have string lights, flags, a big banner, flyers… Anything else?"
    
    MC "Hmm… I think we should start with those. If we come up with anything else, it can just be extra."
    
    G "Great! Let’s hope the resource room isn’t too crowded with everyone trying to put together their stalls…"
    
    "You and Gale turn around and head back inside, winding through the hallways until you reach the resource room closest to your club room."

    stop music fadeout 1.0
    scene black with fade
    scene bg gale clubroom with dissolve
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop
    
    show Gale confused pose2 at waist_up_center2 with dissolve
    G "Oh wow, it’s empty!"
    
    MC "Yeah, this one tends to be less stocked than the others. Last I heard, Building 2 got a 3D printer in their resource room."
    
    show Gale annoyed
    G "Damn! Why don’t we get a 3D printer??"
    
    MC "They hate us, clearly."
    
    hide Gale with easeoutright
    "With a short laugh, you both step into the resource room and start poking through the different cabinets. Some have endless stocks of colored and plain paper; others hold buckets of brushes and palettes. Every art supply one could possibly want is stuffed into this place."
    "A few feet away, Gale is sifting through a drawer filled with thread, needles, and all sorts of attachments for a sewing machine that sits on top of the counter."
    "After looking through the supplies, you meet back in the middle and share a knowing look."

    show Gale laugh at waist_up_right2 with easeinright
    G "Okay, we may not have a 3D printer, but we have so much stuff to work with."

    MC "Yeah! Let’s start with the banner–that’ll probably take the longest to make. We can use this canvas over here and the paints."
    hide Gale with dissolve
    "You both spread out around the room, gathering paints and markers that look useful. It takes both of you to get a big enough stretch of canvas and lay it out smoothly on the table."
    "Once it’s laid out, you stand shoulder to shoulder with Gale and stare down upon the spread you have amassed, both of you silent for a moment."
    
    show Gale confused pose2 at waist_up_center2 with dissolve
    G "Hey, [player_name]... we know what we’re doing, right?"

    menu:
        "Absolutely. I love doing this kind of thing – this should be a piece of cake.":
            $ gale_choice1 = "artistic"
        "Uh… I’m not sure I remember the last time I touched art supplies, honestly.":
            $ gale_choice1 = "non-artistic"
        "I’m sure we can figure it out if we try…":
            $ gale_choice1 = "neutral"

    if gale_choice1 == "artistic":
        MC "Absolutely. I love doing this kind of thing –it should be a piece of cake."

        show Gale neutral at waist_up_center2, pop
        G "I’ll follow your lead, then!"
        show Gale neutral at waist_up_right2 with ease

        "You dive right in, pulling out different bottles of paint and shaking them to gauge how much is left before setting them down on the table."

        MC "Find me a pencil?"

        show Gale confused pose2

        G "Gale turns to rummage through a few bins before triumphantly pulling out a good sketching pencil and offering it to you."

        "He watches intently as you bend over the canvas and start making light, sweeping strokes."

        MC "We can do a nice big sign that says \"Crepes\" so people can see from a distance, but have some smaller text that they can read when they’re standing in line. One of us can hand out flyers too…"

        "You trail off as you finish drafting the canvas, tilting your head and moving to the side so Gale can take a look."
        "He steps up beside you and puts a hand on his hip."

        show Gale neutral at waist_up_right2 , pop
        G "Okay, yeah, you’re definitely the right person for this job. What do you want me to do?"
        
        MC "Can you sketch some little pixel creatures on the border of the sign? I want it to at least tie back into what we do as a club."

        "Gale mock salutes and grabs a pencil for himself before bending over the canvas and slowly making his way around the border with his doodles, while you pull over a sheet of printer paper and start sketching a flyer design."

        G "How’s this?"

        "After a few minutes of working quietly in tandem, Gale speaks and draws your attention back to the banner. Your eyebrows shoot up."

        MC "Those are cute! Are those some of the little creatures from Rosco’s game?"

        G "Yeah! These were some of my favorites that he’s shown me."

        MC "They look good! I like the little scattered pixel shapes too."

        G "Thanks! What color scheme should we do?"

        "You pass over a couple of bottles of paint and some brushes."
        "I think we can work on this part together. The flyer will be easy to color, so I’ll worry about that later."
        "You walk up to the sink and fill up two glass jars with water before returning to the table and settling down."

        MC "Let’s start–make sure you work from the center of the canvas and out so you aren’t dragging paint everywhere."

        G "You know, I never would have thought of that."

        MC "I saw the mess in my mind’s eye. {i}Your{/i} mess."

        show Gale blush at waist_up_right2, pop
        G "H-Hey now!"

        MC "Resent me all you want–I’ve seen what you do to the club room if you’re left alone. And I won’t even mention your dorm."

        show Gale neutral
        G "My dorm is the pinnacle of comfort, I’ll have you know!"

        "You snort and coat a wide brush with black paint, leaning in to begin slowly going over the lettering. “Gale watches you for a moment to absorb the process, before taking an identical brush and mirroring your movements on his end of the canvas."
        "A few minutes pass quietly before Gale groans."

        show Gale confused pose2
        G "It’s so quiet in here! Can I put on some music or something?"

        MC "Sure! I don’t care what you play."

        show Gale neutral
        G "Oh, thank fuck."

        hide Gale with dissolve

        "He heads over to the little speaker system and queues up a playlist. Quiet music begins to drift through the room as he returns to his place at the workbench."
        "You work side by side, filling in sketches with color and lines, topping up paint when needed until the banner is complete."
        "The lettering pops out over the whimsical swirls, pixels breaking, and little creatures bringing the banner to life."

        show Gale neutral at waist_up_center2 with dissolve
        G "Hey, this looks great!"

        MC "Have some faith, would you?"

        G "I had plenty of faith in you–I’m just not used to working with physical paint."

        MC "Sometimes I forget graphic design is your passion"

        "You laugh and look up to see a smudge of paint on Gale’s cheek, bright purple from where he must have swiped a finger over his skin without realizing."
          
        MC "You have a bit of…"

        "You point to your own face to show him where the paint is, but it doesn’t seem to help at all as he completely misses it."
        
        show Gale confused pose2 
        G "Huh? Do I have something on my face?"

        menu:
            "Reach out and clean the paint off.":
                $ player_choice_a = "opt-1"
            "Give him a paper towel.":
                $ player_choice_a = "opt-2"
        
        if player_choice_a == "opt-1":
            show Gale blush
            G "You reach out and carefully clean the paint from his cheek, frowning when you have to pull the skin a little to flake off the dry bits."
            
            "Gale is very still as you do so, and you only notice you’re practically caressing his face when it heats up and flushes beneath your hand, bright green eyes trained on the wall behind you."
            "You clear your throat and lean back, smiling at him."

            MC "All clean~"

        elif player_choice_a == "opt-2":
            show Gale neutral
            G "You reach for one of the paper towels nearby, one that doesn’t have paint on it from cleaning the brushes, and wet it in the nearby sink."

            "Gale takes the paper towel and scrubs across his cheek as you laugh, directing him as best you can."

            G "Good?"

            MC "All clean~"

        show Gale neutral

        MC "I think the banner is complete, so we can leave it to dry for now and focus on the next thing…"

        "Gale takes the banner over to a drying rack, carefully laying it flat so the paint won’t smudge."

        MC "Let’s get started on the pennants and bunting now. I think I saw some black cord in one of the drawers on the left."

        "Gale digs through the drawers until he happily lifts the spool into the air to confirm it’s what you’re looking for."
        "You gesture him over to the table, where you’ve set out the big paper cutter and stacks of thick cardstock in yellow, green, red, purple, and pink."

        MC "We’ll make the pennants out of this, and I can put quick stitches into some of the fabric to make the table bunting."

        G "Huh? Is it that easy?"

        MC "It should be - it’s just a simple stitch to hold the fabric together, and since it won’t be used again, it doesn’t have to be anything fancy."

        G "How do you even learn this stuff?"

        MC "Wouldn’t you like to know?"

        "Gale makes a face at you and turns back to the paper spread out in front of him, lining it up on the cutter to slice clean triangles to string together for the pennants."
        hide Gale with dissolve
        "As you work, you chat about the club and various classes, laughing when Gale brings up the {i}Ichi{/i} tournament again, grumbling about his near-win."
        "Before long, he’s strung together a respectable length of the colored flags, and you’ve pieced together enough bunting to cover the length of the table, double-checking both with a tape measure Gale scrounges up from one of the drawers."
        show Gale neutral at waist_up_center2 with dissolve
        G "This room really does have everything, damn."

        MC "Everything except a 3D printer."
        hide Gale with dissolve
        "You work together to carefully box up all the decorations you had made, as well as some stray string lights from one of the cabinets."
        "As the banner is dry, you carefully roll it up to be stored with the other things."

        MC "I’ll finish the flyer tonight and print the pages tomorrow. It’s getting late—we should probably put everything away in the club room and call it a night."
        show Gale neutral at waist_up_center2 with dissolve
        G "You got it, boss!"

        "Gale mock salutes as you both load the boxes filled with your new decorations onto a rolling cart and wheel it down the hallway to your club room for safekeeping overnight."
    
    elif gale_choice1 == "non-artistic":

        MC "Uh… I’m not sure I remember the last time I touched art supplies, honestly."

        show Gale confused pose2
        G "We may be slightly cooked."

        MC "Just shy of charred."

        "You both stand in silence, shuffling your feet and scratching your heads as you try to figure out where to even start."

        G "We should…probably write what the stall is on the banner, right?"

        MC "Right."

        "There’s another beat of silence before you both break out into giggles."

        show Gale laugh at waist_up_center2,pop
        G "Well, let’s do our best! I’ll start sketching out the lettering if you want to start drafting the flyers?"

        MC "Sure."

        show Gale confused pose2
        "You watch as Gale steps forward and decisively lays bold pencil strokes on the canvas, his brows furrowed in concentration."
        
        G "It needs to be pretty big so people can see from a distance, but still leave some room for something for people to look at while they’re in line…"

        MC "Are you expecting people to queue for our crepes?"

        G "It’s called being optimistic."
        hide Gale with dissolve

        "You both chuckle for a moment before his focus returns to the canvas, and you turn yours to the flyer paper."
        "It’s quiet for a few minutes as you both work, pencil scratching on both canvas and paper."
        "Eventually, Gale steps back, catching your attention."

        show Gale neutral pose2 at waist_up_center2 with dissolve
        G "How’s this?"
        show Gale neutral at waist_up_center2
        "You peek around him as he steps back and puts a hand on his hip."
        
        MC "Looks great!"

        G "Nice–let’s start putting it down properly, then."

        "You bustle around each other grabbing last-minute supplies—water for the brushes, emergency paper towels—getting in each other’s way and laughing."

        show Gale laugh 
        G "[player_name], c’mon, you have to be doing this on purpose! I’ve almost spilled the water twice!"

        MC "Maybe {i}you’re{/i} doing it on purpose–you’re in my way as much as I’m in yours!"

        "After a few moments of elbows bumping and playful shoving, you both settle back at the table.  Gale frowns at the canvas and taps a paintbrush against his bottom lip."

        show Gale confused pose2
        G "There’s something…off here, but I can’t figure out what it is."

        MC "It looked good to me?"

        "Gale shrugs and puts brush to canvas with broad movements, his tongue sticking out of the side of his mouth as he concentrates."
        hide Gale with easeoutleft
        "You stay out of his way and watch, pencil in hand, as you neglect the flyer’s design to watch the letters take shape."
        "As he finishes, you also start to get the feeling that something isn’t quite right, but you struggle to put your finger on it."
        "Instead of dwelling, you turn your attention back to the flyer and quickly sketch out what you think looks like most of the flyers you’ve seen pinned up on announcement boards around the campus."
        show Gale confused pose2 at waist_up_left2 with easeinleft
        G "I think the lettering is done?"

        "You set your flyer aside and squint at the canvas."

        MC "Well, people will certainly be able to see it from far away."

        show Gale blush
        G "Hey! It was hard to make it fit in such a small space!"

        "You laugh and pat his shoulder."

        MC "It’s fine, Gale. Should I start working on some decoration? I can finish the flyer up later and copy it tomorrow."

        show Gale neutral
        G "Sure. I’ll help! We can start on opposite sides and move clockwise around the borders."

        hide Gale with dissolve
        "You agree, and the two of you burst into action, once more lightly elbowing each other as you pick the paints you want before claiming your spots at the table."
        "Paintbrushes hit the canvas, and you start carefully painting all the little pixel shapes and swirls, trying to get used to the awkward feel of a brush in your hand."
        "A few minutes pass quietly before Gale groans."

        show Gale confused pose2 at waist_up_center2 with dissolve
        G "It’s so quiet in here! Can I put on some music or something?"

        MC "Sure! I don’t care what you play."

        show Gale neutral
        G "Oh, thank fuck."

        "He heads over to the little speaker system and queues up a playlist. Quiet music begins to drift through the room as he returns to his place at the workbench."
        "You work side by side, filling in sketches with color and lines, topping up paint when needed until the banner is complete."
        "The bold lettering is surrounded by colorful swirls and shaky pixel shapes squished into too little free space. It’s not perfect, but it definitely livens things up."

        G "Hmm… Well, it could certainly be worse."

        MC "Definitely."

        G "Still feels like something isn’t quite right about it, though."

        "You laugh and look up to see a smudge of paint on Gale’s cheek, bright purple from where he must have swiped a finger over his skin without realizing."

        MC "You have a bit of…"

        "You laugh and look up to see a smudge of paint on Gale’s cheek, bright purple from where he must have swiped a finger over his skin without realizing."

        MC "You have a bit of…"

        "You point to your own face to show him where the paint is, but it doesn’t seem to help at all as he completely misses it."

        show Gale confused pose2
        G "Huh? Do I have something on my face?"

        menu:
            "Reach out and clean the paint off.":
                $ player_choice_a = "opt-1"
            "Give him a paper towel.":
                $ player_choice_a = "opt-2"

        if player_choice_a == "opt-1":
            show Gale blush
            "You reach out and carefully clean the paint from his cheek, frowning when you have to pull the skin a little to flake off the dry bits."
            "Gale is very still as you do so, and you only notice you’re practically caressing his face when it heats up and flushes beneath your hand, bright green eyes trained on the wall behind you."
            "You clear your throat and lean back, smiling at him."

            MC "All clean~"

        if player_choice_a == "opt-2":
            show Gale neutral

            "You reach for one of the paper towels nearby, one that doesn’t have paint on it from cleaning the brushes, and wet it in the nearby sink."
            "Gale takes the paper towel and scrubs across his cheek as you laugh, directing him as best you can."

            G "Good?"

            MC "All clean~"
        show Gale neutral
        G "Is now a good time to tell you that I think you got some paint on your pants?"

        "You glance down and frown—he’s right. Splashes of different colors fleck the fabric."

        MC "Oh well, at least these wash out."

        "There’s a moment of silence only broken by the music still softly playing."

        MC "It {i}does{/i} wash out… right?"

        "Gale reaches over and scans the label on one of the bottles of paint as you scratch at a paint spot."

        G "... \"Washes out with cold water and detergent.\" You should be fine."

        MC "Okay, good. I wasn’t ready to retire these from public use yet."

        show Gale laugh at waist_up_center2, pop
        "Gale laughs and takes the banner over to a drying rack, carefully laying it out and making sure it’s flat and won’t smudge."
        show Gale neutral

        MC "Let’s get started on the pennants now. I don’t know if we’ll have time to do the bunting, especially because I realized that...I have no idea how to make that."

        G "I think I saw some black cord in one of the drawers on the left… we can string the pennants on it."

        #change position?
        hide Gale with easeoutleft
        "Gale wanders over and digs through the drawers until he happily lifts the spool into the air in triumph."
        "You cheer and start doling out some of the paper you had set out earlier, passing him a pair of scissors as he sits down across from you and starts cutting as well."
        "As you work, you chat about the club and various classes, laughing when Gale brings up the Ichi tournament again, grumbling about his near-win."
        "Before long, you’ve both cut out a small mountain of colored flags, but are left blinking down at the stack."

        show Gale confused pose2 at waist_up_left2 with easeinleft
        G "You know, I feel like we probably should’ve clarified beforehand what shape we were going to cut."

        "You sigh and lift up two yellow flags. One is a slightly lopsided triangle, and the other is a rough rectangle."

        MC "If we alternate them, it might look intentionally quirky."

        show Gale neutral
        G "Beats cutting out more–let’s roll with it."

        "It doesn’t take long until you’ve both strung together a respectable length of the colored flags, eyeballing it to make sure it will stretch between the two poles in front of your stall."

        G "That’s that, then!"

        "You work together to carefully box up all the decorations you had made, as well as some stray string lights from one of the cabinets."
        "As the banner is dry, you carefully roll it up to be stored with the other things."

        MC "I’ll finish the flyer tonight and print the pages tomorrow. It’s getting late—we should probably put everything away in the club room and call it a night."

        G "Yes, boss!"

        "Gale mock salutes as you both load the boxes filled with your new decorations onto a rolling cart. You leave together, wheeling the cart down the hallway to the club room for safekeeping overnight."

    elif gale_choice1 == "neutral":
        MC "I’m sure we can figure it out if we try…"

        show Gale confused pose2
        G "If we work together, we can definitely make something that everyone will like!"

        "You both reach for the same bottle of paint at the same time and laugh. You leave him to sort the paints while you wander off to grab a pencil."

        G "Once we get the sketch down, we can fill it in with paint and add something around the borders to fill in space and be a little more interesting."

        MC "Do we want to just put ‘crepes’ in bubble letters? It would be pretty cute and big enough to see from farther away."

        G "I like that idea. Rosco showed me a few of the characters from the game we’ll have the demo for–we can do little doodles of those around the edges?"

        MC "I’m sure we can get them close enough to be recognizable."

        show Gale laugh at waist_up_center2, pop
        G "I’ll leave that to you, then. I’ll send you the pictures and start on the letters."

        play sound "audio/sfx/phone-ping.ogg"
        "He pulls his phone out and taps for a few moments before your phone pings and lights up with a message from him, a few screenshots from Rosco’s game of the little creatures."
        # ping sound of phone
        "While you study them and doodle simplified versions on a stray piece of paper, Gale bends over the canvas and starts making light, hesitant strokes, his brow furrowed in concentration."

        show Gale confused pose2
        G "How does this look?"

        "You move up beside him to take a look as he takes a step back, a hand on his hip."

        MC "It looks good! Surprisingly even."

        show Gale laugh at waist_up_center2,pop
        G "See? I can be careful when I try to!"

        MC "Now if only you would be as careful about updating your schedule for club activities…"

        G "No comment."

        "You both laugh, and he elbows you gently before you trade spots."

        MC "I’ll put these little guys as decoration, but don’t expect all of them."

        show Gale neutral
        G "Eh, it’s not like they’ll know any better."

        "You nod and start sketching your simplified versions of the game characters onto the top corners of the banner, frowning as you focus."
        "Once you finish, Gale leans over and inspects the little guys, grinning."

        G "They look cute! I think Rosco’s gonna love this."

        MC "I really hope so! Do you want to do the more abstract decoration, and I’ll start putting a flyer draft together?"

        G "Sure. I can handle a few scribbles."

        "After trading spots, you turn your focus to the flyer, planning out the space for the graphics and information."
        "A few minutes later, Gale speaks up and draws your attention back to the larger canvas."

        G "Do you think this is enough?"

        "He’s surrounded the block letters with little pixels coming off them and some small shapes and swirls around the border to fill in the space around the mascot creatures."

        MC "I think so! It’s interesting without being too busy."

        G "Great! Let’s start painting so it has time to dry."
        show Gale at waist_up_left2 with move
        "You head to the sink to fill two glass jars with water, grab a few bottles of paint and brushes on your way back, then return to the table and settle in."

        MC "We can tackle this together. You take the right side and I’ll take the left."

        G "Aye, aye, Captain."

        "You snort and hand Gale a brush, before dipping your brush in black paint, carefully tracing the letters. He watches for a moment before copying your movements on his side."
        "A few minutes pass quietly before Gale groans."

        show Gale confused pose2
        G "It’s so quiet in here! Can I put on some music or something?"

        MC "Sure! I don’t care what you play."

        show Gale neutral
        G "Oh, thank fuck."

        hide Gale with dissolve
        "He heads over to the little speaker system and queues up a playlist. Quiet music begins to drift through the room as he returns to his place at the workbench."
        "You work side by side, filling in sketches with color and lines, topping up paint when needed until the banner is complete."
        "The block letters are filled in with yellow, and the other decorations burst with color on the white base of the canvas."

        show Gale neutral at waist_up_center2 with dissolve
        G "Hey, this doesn’t look too bad!"

        MC "Maybe we weren’t the worst choice for this."

        G "I believed in us the whole time."

        "You laugh and look up to see a smudge of paint on Gale’s cheek, bright purple from where he must have swiped a finger over his skin without realizing."

        MC "You have a bit of…"

        "You point to your own face to show him where the paint is, but it doesn’t seem to help at all as he completely misses it."

        show Gale confused pose2
        G "Huh? Do I have something on my face?"

        menu:
            "Reach out and clean the paint off.":
                $ player_choice_a = "opt-1"
            "Give him a paper towel.":
                $ player_choice_a = "opt-2"

        if player_choice_a == "opt-1":
            show Gale blush
            "You reach out and carefully clean the paint from his cheek, frowning when you have to pull the skin a little to flake off the dry bits."
            "Gale is very still as you do so, and you only notice you’re practically caressing his face when it heats up and flushes beneath your hand, bright green eyes trained on the wall behind you."
            "You clear your throat and lean back, smiling at him."

            MC "All clean~"

        elif player_choice_a == "opt-2":
            show Gale neutral
            "You reach for one of the paper towels nearby, one that doesn’t have paint on it from cleaning the brushes, and wet it in the nearby sink."
            "Gale takes the paper towel and scrubs across his cheek as you laugh, directing him as best you can."
            
            G "Good?"

            MC "All clean~"

        show Gale neutral
        "Following Gale’s direction, you take the banner over to a drying rack, carefully laying it flat so the paint won’t smudge."

        G "I think we can get the pennants done before it’s too late… What can we use to string them together?"

        MC "I think I saw some black cord in one of the drawers on the left."

        show Gale at waist_up_right2 with move
        "Gale wanders over and digs through the drawers until he finds the spool, lifting it in the air to confirm it’s what you were looking for before bringing it over."
        "You settle on opposite sides of the table with scissors you had found and a healthy stack of thick cardstock in yellow, green, red, purple, and pink."

        MC "We can make the pennants out of these papers."

        G "Triangles, right?"

        MC "Yeah, unless you think something else would be better."

        G "Why mess with the classics?"

        "You shrug and agree before you both turn to your stacks of paper and start cutting relatively even triangles out of the cardstock to string together for the decorations."

        "As you work, you chat about the club and various classes, laughing when Gale brings up the {i}Ichi{/i} tournament again, grumbling about his near-win."
        "Before long, he’s strung together a respectable length of the colored flags, and you’ve pieced together enough bunting to cover the length of the table, double-checking both with a tape measure Gale scrounges up from one of the drawers."

        G "What {i}doesn’t{/i} this room have?"

        MC "A 3D printer."

        show Gale confused pose2
        G "…Right."

        "You work together to carefully box up all the decorations you had made, as well as some stray string lights from one of the cabinets."
        "As the banner is dry, you carefully roll it up to be stored with the other things."

        MC "I’ll finish the flyer tonight and print the pages tomorrow. It’s getting late—we should probably put everything away in the club room and call it a night."

        G "Yes, [player_name]!"

        "Gale mock salutes as you both load the boxes filled with your new decorations onto a rolling cart and wheel it down the hallway to your club room for safekeeping overnight."

    show bg clubroom with fade
    #add music

    "As you enter the club room, you can see Rosco is there, fiddling with one of the computers.  He looks up at your greeting, stretching back from the screen with a yawn and a lazy wave."

    show Rosco confused jacket at waist_up_left with dissolve
    R "Those the decorations?"

    show Gale neutral at waist_up_right2 with dissolve
    G "Yeah! Most everything is done— [player_name] is just going to finish up the flyer at home and [player_subject]’ll print it in the morning."

    show Rosco neutral jacket
    R "Sick! Can’t wait to see it all set up."

    MC "We hope you’ll like it!"

    "Rosco nods, already half-absorbed back into whatever’s on the monitor, while you and Gale tuck the cart and boxes away."
    hide Rosco with dissolve
    hide Gale with dissolve
    "Once you finish, you pick up your things and get ready to head out. Gale, however, lingers by the sofa while checking his phone."

    MC "I’m heading out!~"
    show Gale neutral at waist_up_center2 with dissolve
    G "Meet back here tomorrow morning?"

    MC "Sure thing! Make sure you get some good rest–we have our work cut out for us tomorrow to put everything together. That means no staying up playing games with Cass."

    G "I’ll try~"

    "You point at him in mock-warning until he laughs."

    show Gale laugh
    G "Alright, alright. See you tomorrow, [player_name]."

    MC "See you!"

    scene black with fade
    "You head out into the quiet evening, walking home with a light skip, satisfied with everything you accomplished. By the time you reach your room, you notice a faint smell of acrylic still clinging to you—probably from the paint smudges on your pants."
    "You sit down to finish the flyer, pushing through to add the last bits of text and doodles until it finally feels complete. After a few moments, you lean back on your chair and grin at your work, satisfied with the result."
    "Gathering up the supplies and tucking the flyer mock-up into your bag, you settle into bed, exhausted but happy, already looking forward to seeing everything come together tomorrow."
    stop music fadeout 1.0
    jump gale_route_day2

label gale_route_day2:
    window hide
    $ quick_menu = False
    scene black with fade
    show text "{color=#ffff}{size=50}Gale Route: Day 2{/size}{/color}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    $ quick_menu = True


    if "G" not in collected_routes:
        $ collected_routes.append("G")

    if len(collected_routes) == 5:
        $ renpy.save("chapter1_end")
        scene black with fade
        jump general_ending

    else:
        jump choose_route
    #End of Day 2
