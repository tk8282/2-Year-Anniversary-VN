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
            $ stall_style = "artistic"
        "Uh… I’m not sure I remember the last time I touched art supplies, honestly.":
            $ stall_style = "non-artistic"
        "I’m sure we can figure it out if we try…":
            $ stall_style = "neutral"

    if stall_style == "artistic":
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
    
    elif stall_style == "non-artistic":

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

    elif stall_style == "neutral":
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

    show Rosco confused jacket at waist_up_left
    show Gale neutral at waist_up_right2
    with dissolve
    R "Those the decorations?"

    G "Yeah! Most everything is done— [player_name] is just going to finish up the flyer at home and [player_subject]’ll print it in the morning."

    show Rosco neutral jacket
    R "Sick! Can’t wait to see it all set up."

    MC "We hope you’ll like it!"

    "Rosco nods, already half-absorbed back into whatever’s on the monitor, while you and Gale tuck the cart and boxes away."
    hide Rosco
    hide Gale
    with dissolve
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

    scene bg gale clubroom with dissolve
    play music "audio/music/C1 - Chill (2).wav" fadein 1.0 loop
    $ quick_menu = True

    show Gale shocked at walk_left_to_center, waist_up_center2
    "You are sitting down on the sofa, scrolling on your phone, when Gale runs into the club room where you agreed to meet yesterday, fifteen minutes late."

    "His shirt is partially unbuttoned and his bag is half opened, his hastily shoved lunch box sticking out from between the zippers."

    "His wallet’s shoved into his pocket while he's still attempting to tie a messy ponytail with his hair, a few rubber bands wrapped around his wrist."

    show Gale neutral at waist_up_center2, restless
    G "[player_name]! I’m really sorry for being late! I overslept, which caused me to miss my usual bus and-"

    MC "It’s fine Gale, chill. Here, take a croissant."

    G "Ugh! I could kiss you right now! I haven’t eaten breakfast, and... "
    extend "you got me a croissant, from my favourite bakery no less!"

    MC "Less talking, more eating, Gale~"

    show Gale neutral at waist_up_center2, singlejump
    G "Right away boss!"

    #boxes go where
    "While Gale is eating, you look for the cart to help move the boxes later on."

    "When you can’t find it, you frown."

    MC "Hey, Gale, do you remember where the cart is?"

    MC "I can’t seem to find it."

    G "It should be in the corner back there."

    MC "That’s the problem, it isn’t."

    G "I guess someone else must be using it, then."

    G "Just wait for me to finish the croissant, and I’ll come to help you."

    "Once he finishes, he comes over to help you, picking up a good few boxes to stack onto the cart and glances at you in concern."

    G "[player_name], let me help you transfer those boxes onto the cart."

    G "They’re stacked so high they cover your face. How do you even see like that?"

    MC "It’s fine, I can handle this on my own."

    MC "If I need help, I'll ask you."

    G "You sure?"

    MC "Yeah, promise."

    G "Alright, I guess."

    "You and Gale spend the next five minutes bringing the boxes over to the cart and stacking them neatly, ensuring that none will fall off."

    stop music fadeout 1.0
    scene black with fade
    scene bg_gale_day_stall
    show gale_boxes:
        xoffset 150
        yoffset 620
        zoom .50
    show Gale neutral bandana at waist_up_center2
    with dissolve

    play music "music/G6_C2 - Cheerful_Comedic.wav" fadein 1.0 loop

    show Gale neutral bandana at waist_up_center2 zorder 3.0 with dissolve

    MC "Phew, we finally finished moving the decorations outside."

    MC "What should we start with?"

    show Gale confused pose2 bandana
    G "Maybe the pennants and the string lights first. They seem the most simple to do, I guess."

    MC "Okay, lemme get them out of the box."

    # rummage sound?
    "You rummage through the box and pull out a bundle of string lights."

    MC "Eh? Why are the string lights so badly tangled up?? I swear I made sure they were untangled before I put them away...."

    show Gale laugh bandana
    G "Maybe it's just your bad luck."

    MC "Gale, you just had to jinx it. Alright, you’re gonna untangle the string lights while I put up the main banner."

    show Gale confused bandana 
    G "Huh? What? Hey, you can’t just do that!"

    MC "Yes, I can and will do that. Now bring the ladder over here before I kick your ass for real."

    show Gale neutral bandana at waist_up_center2, singlejump
    G "Right away, boss!"

    "Gale brings the ladder over for you and then starts work on detangling the string lights while you unfold the banner, balancing precariously on the ladder as you reach for the hooks where the banner is supposed to hang from."

    "Just as Gale’s almost done detangling the string lights– he spent the last 10 minutes detangling a last particularly annoying knot in the cord and actually cheered when it was done, and you’re about finished with hanging the main banner, disaster strikes."

    transform parrot_fly:
        pos (None, None)
        anchor (0.5, 0.5)

        alpha 0.0
        xalign -0.2
        yalign 0.05
        zoom 0.50
        easein 0.3 alpha 1.0
        ease 1.2 xalign 0.75
        easeout 0.3 alpha 0.0

    transform poop_fall:
        alpha 0.0
        xalign 0.67
        yalign 0.24
        zoom 0.15
        pause 0.6
        alpha 1.0
        ease 0.4 yalign 0.30


    stop music fadeout 1.0
    play music "music/G3 - Chaos.wav" fadein 1.0 loop

    play sound "sfx/pip.ogg" volume .6
    show gale_pipsqueak at parrot_fly zorder 1 with dissolve

    $ renpy.pause(0.5)
    #poop sound
    play sound "sfx/splat.ogg" volume .5

    show gale_birdpoop at poop_fall zorder 1 with dissolve
    

    # Wait for animation to finish
    $ renpy.pause(1.0)

    hide gale_pipsqueak
    #NOTE should still be first?

    "To start everything off, a pipsqueak flying by decides that the banner (your masterpiece) would make a great toilet."

    show Gale angry bandana at waist_up_center2, singlejump
    G "Oi! What d’you think you’re doing, defacing our masterpiece!"

    play sound "sfx/pip.ogg" volume .6
    "The pipsqueak simply chirps at him before flying away."

    show Gale annoyed bandana
    G "{i}sigh{/i} "
    extend "I must have done something bad in my past life to get this kind of bad luck."

    MC "Maybe you were a bird who pooped on someone else's artwork, Gale."

    show Gale neutral pose2 bandana
    G "Yeah, that does make sense."

    show Gale neutral bandana
    hide gale_birdpoop with dissolve
    "He takes a wet wipe from the packet in his pocket and walks over to the ladder, easily climbing up and quickly wiping it off."

    MC "Nice going! Crisis averted."

    #wind sfx
    play sound "sfx/wind-gust.ogg" volume 15.0
    "Just as you finish speaking, the wind starts to pick up, prompting you and Gale to look at each other."

    show Gale shocked bandana
    G "I think you just jinxed it."

    MC "Definitely."

    G "We should make sure the decorations don’t fly off before the wind becomes worse."

    MC "Yeah, let’s do it now."

    "As you hurry to secure the decorations, the wind suddenly picks up, causing the already hung decorations to flap around wildly."


    transform bandana_fly:
        pos (None, None)
        anchor (0.5, 0.5)

        alpha 0.0
        xalign 0.68
        yalign 0.10
        zoom 0.45

        # quicker fade in
        easein 0.20 alpha 1.0

        # smooth upward drift
        ease 0.30 xalign 0.78 yalign 0.075

        # soft crest
        ease 0.35 xalign 0.90 yalign 0.055

        # tiny blend step to smooth the curve
        ease 0.25 xalign 1.00 yalign 0.065

        # exit glide
        ease 0.40 xalign 1.20 yalign 0.12

        # quicker fade out
        easeout 0.30 alpha 0.0

    show gale_bandana at bandana_fly zorder 3
    show Gale shocked
    with dissolve

    #wind sfx
    play sound "sfx/wind-gust.ogg" volume 15.0
    "As if nature’s mocking you two, the next gust of wind causes Gale’s bandana to fly off."

    show Gale angry
    G "Hey, I was using that! Come back here!"

    hide Gale with dissolve
    "Gale hops off the ladder and runs off after his bandana. In the blink of an eye, the wind dies down."

    MC "Well, he’s gonna take a while. I guess I’ll start with the string lights first."

    G "Oh, come on! Are you kidding me? God of the wind or whoever, why do you hate me so much? Why does the wind only stop now?"

    show Gale annoyed bandana at waist_up_center2 with dissolve
    "Once Gale comes back, thankfully with his bandana wrapped safely around his hair this time, he insists on helping you with the second set of fairy lights, complaining that you didn’t wait for him to help with the first set."

    G "Reaping the merits of my hard work while I’m gone… Untangling that took me over half an hour!"

    MC "Eh, at least you can help me with the next set of lights."

    G "I guess. Come on, we gotta hurry or the boys are gonna be on our asses for not finishing on time."

    show Gale neutral bandana
    "You carefully climb onto the ladder with one end of the fairy lights in hand, securing it around the top of the pole with a tight knot."

    scene bg_gale_day_stall with dissolve

    stop music fadeout 3.0
    play sound "sfx/wind-gust.ogg" volume 15.0
    scene bg_gale_day_stall at screenshake
    "You’re starting to carefully climb down the ladder when another freak gust of wind hits, and you see your life flash before your eyes."

    menu:
        "Scream loudly":
            play sound "sfx/wind-gust.ogg" volume 15.0
            scene bg_gale_day_stall at screenshake
            MC "AHHHH!! GALE!!!!"
            MC "SAVE ME!!! I'M GONNA DIE!!! I'M TOO YOUNG FOR THIS!!!"
            play sound "sfx/wind-gust.ogg" volume 15.0
            scene bg_gale_day_stall at screenshake

        "Softly whimper":
            play sound "sfx/wind-gust.ogg" volume 15.0
            scene bg_gale_day_stall at screenshake
            MC "G.. Gale! Help!!"
            MC "Please… I don't want to die… I'm too young for this…"
            play sound "sfx/wind-gust.ogg" volume 15.0
            scene bg_gale_day_stall at screenshake

    pause 1.5

    hide window
    $ quick_menu = False
    scene black with fade
    show CG Gale 1 with dissolve
    play music "audio/music/G5 - Romantic.wav" fadein 1.0 loop
    pause 3.0
    $ quick_menu = True
    G "Don’t worry, I’ve got you."

    MC "Thank you so much, Gale, you saved my life!"

    G "No worries! Like I said, I've got your back!"

    MC "I guess I owe you one now."

    G "You know… there's that one Maria Racing game I've been eyeing recently, [player_name]."

    "Gale slings his arm over your shoulders as he says this, eyeing you suggestively. Not like you don't already know what he means."

    MC "{i}snorts{/i}"
    MC "All right, Gale. I do."

    stop music fadeout 1.0
    scene black with fade
    scene bg_gale_day_stall
    show gale_boxes:
        xoffset 150
        yoffset 620
        zoom .50
    show Gale neutral at waist_up_center2
    with dissolve

    play music "audio/music/G1 - Cheerful (2).wav" fadein 1.0 loop


    MC "Hey, Gale, is there anything else that’s missing?"

    show Gale confused pose2 
    G "Uh…"

    "Gale looks the entire stall setup up and down once, then again, scrutinizing every detail."

    show Gale shocked 
    G "Oh crap! We forgot one of the most important parts of the entire stall!"

    MC "What is it?"

    show Gale neutral at waist_up_center2, singlejump
    G "The fasteners!"

    G "We can't put up the flyers or make sure the decorations won't fall off without the fasteners!"

    MC "You’re right."

    MC "Do you remember seeing any boxes of fasteners inside the storage room?"

    show Gale confused pose2 
    G "No, I don’t think so."

    MC "How about we go back and check?"

    show Gale neutral 
    G "Okay!"

    scene black with fade
    
    scene bg gale clubroom
    show Gale neutral at waist_up_center2
    with dissolve
    MC "Gale, you take that side of the room, I’ll take this side."

    G "On it!"

    hide Gale with dissolve
    "The two of you spend five minutes in a comfortable silence, the only sound that of boxes being moved here and there in the search for the fasteners."

    MC "*Sigh*"

    show Gale confused pose2 at waist_up_center2 with dissolve
    MC "I think there’s really no more fasteners left in here…"

    show Gale neutral at waist_up_center2, singlejump
    G "[player_name]! There’s a store selling these types of party essentials just off campus, and that street stall you like to buy from is also nearby."

    MC "Oh yeah!"

    MC "Why didn’t I think of that earlier?"

    show Gale smug
    G "Heh! I’m a genius, right?"

    MC "Hmph! I would have thought of it sooner or later!"

    MC "Let’s go"

    "You fake-storm out of the clubroom, Gale following closely behind you."

    scene black with fade
    scene bg road daylight 
    show Gale neutral at waist_up_center2
    with dissolve

    MC "Oooh, Gale, look!"

    MC "There’s so many different things!"

    show Gale neutral  
    G "They do look interesting."

    G "Okay, wait, [player_name], stay focused!"

    G "Remember our mission?"

    MC "Right. Pendants."
    MC "Hmm, where should we start?"

    show Gale neutral pose2 
    G "Maybe the decorations section?"

    G "That seems like the most likely place to have what we need."

    show Gale neutral
    MC "Okay!"

    "You and Gale slowly walk over to the decoration section, oohing and aahing at all the different types of decorations and materials on display."

    MC "Wait!! Those heart shaped fairy lights are so cute!!"

    MC "And there's rainbow coloured ones too!"

    G "Oh, there’s snowflake shaped ones too."

    MC "Oh my god, there’s even ones in the shape of books!"

    G "[player_name], we need to stay focused."

    G "Remember what we came here for."

    MC "Yeah, I know, I know."

    MC "Now, where are the pennants?"

    show Gale neutral at waist_up_center2, singlejump
    G "ooh! I think I see a bunch over there."

    "Gale points to a shelf in the far corner, where there's a bunch of things that are hopefully pennants folded up in bags and stacked neatly on the shelves."

    MC "Okay! Let's go over and see."

    "You and Gale briskly walk over, both letting out sighs of relief when yes, it is pennants after all, and that there's still enough for the stall."

    MC "Thank god there's still pennants left."

    G "You're right."

    G "I think I'd go mad if we came all the way here only for them to be sold out of the only thing we need."

    MC "Agreed."

    MC "Anyways, Gale, which colour would be nicer?"

    MC "The pink ones or the white ones?"

    show Gale confused pose2 
    G "Hmm…"

    "Gale's looking between the two different colours that you're pointing at."

    show Gale neutral pose2 
    G "What about the rainbow one instead?"

    show Gale neutral 
    G "The colours do look pretty interesting."

    MC "Hm? What rainbow one?"

    G "Hold on a sec."

    "Gale pulls out a few packets of rainbow coloured pennants from underneath a packet of gaudy and aggressively yellow ones, waving them around like a trophy."

    show Gale laugh 
    G "See? Look, this is perfect!"

    show Gale neutral 
    G "It matches our stall’s theme perfectly, doesn’t it?"

    show Gale smug 
    MC "Yeah, you're right, actually."

    MC "Rainbow it is!"

    "Gale’s grin practically radiates smugness as you walk to the cashier together."

    "Gale is in the process of taking his wallet out when you pull your own card out and tap on the terminal."

    show Gale annoyed at waist_up_center2, singlejump
    G "Hey!"

    show Gale angry 
    G "What was that for?"

    G "I was gonna pay!"

    MC "Heh."

    MC "You can pay me back by buying the onigiri from the street stall later."

    show Gale annoyed
    G "*sigh* Okay."

    stop music fadeout 1.0
    scene black with fade
    scene bg road daylight 
    show Gale neutral at waist_up_center2
    with dissolve

    play music "audio/music/C1 - Chill (1).wav" fadein 1.0 loop

    MC "How I love nice, fresh air."

    MC "That store was kinda stuffy, wasn't it, Gale?"

    show Gale annoyed 
    G "That's probably just cuz you were squeezing so close to me."

    MC "Excuse me?"

    MC "It was you who was squeezing close to me, not the other way ‘round!"

    show Gale neutral 
    G "Yeah, yeah, whatever you say~"

    G "We still need to get lunch."

    G "Is there anywhere you wanna get lunch?"

    show Gale confused pose2 
    MC "I don't have a specific restaurant in mind, but I do feel like eating onigiri."

    show Gale neutral 
    G "Oh yeah remember the street stall you brought me to last time?"

    MC "That's not a bad idea."

    G "Do you know where the obaa-san selling onigiri might be at this time of the day?"

    MC "I'm guessing pretty sure she’s at her usual afternoon spot ‘round the corner from the convenience store."

    show Gale shocked 
    G "Woah, you know her usual spots?"

    MC "Yeah? Why wouldn’t I, as a regular?"

    G "That’s pretty cool. What’s her usual morning spot then?"

    show Gale confused pose2 
    G "Sometimes I really wanna get some of her onigiri before classes start but I can never seem to find her."

    MC "She’s near the campus gates, the main ones, about a five minute walk."

    show Gale shocked 
    G "Oh, that’s actually pretty close."

    MC "Yep!"

    MC "Oh! I see her cart now! Obaa-san!"

    show Gale neutral 
    "You wave enthusiastically at Obaa-san, who has spotted the two of you and is waving back."

    MC "Obaa-san! It’s nice to see you again!"

    MC "Gale, what do you want?"

    show Gale neutral pose2 
    G "Hmm, I’ll take the tuna onigiri."

    MC "And I’ll take the umeboshi!"

    show Gale neutral 
    "Obaa-san picks up the onigiri of your requested flavours, putting them into a bag and passing it to you to carry."

    "This time, Gale already has his wallet out, passing the Obaa-san the money for the onigiri in exact change."

    show Gale laugh 
    G "Thank you, obaa-san!"
    MC "Thank you, obaa-san!"

    show Gale neutral 
    "She smiles at the both of you and wave you off as you head back towards the direction of the campus."

    show Gale neutral at waist_up_center2, singlejump 
    G "Can't wait to eat my tuna onigiri!"

    G "I remember it was absolutely heavenly the last time!"

    show Gale shocked 
    G "[player_name], what abou-"

    "Gale was turning his head towards you to ask you a question, but stops mid sentence when he sees you've already bitten into your onigiri."

    show Gale laugh 
    G "It's really good, huh?"

    MC "Yesh, et iz"

    MC "Wut dar oo witin four? Ech orz doo."

    G "Haha, yeah, I was just about to."

    show Gale neutral
    "Gale eagerly unwraps his onigiri, tossing the wrapper onto the section of the bench next to him without a second thought, and takes what you think might be the biggest bite you've ever seen a human being taken."

    show Gale neutral at waist_up_center2, singlejump
    G "Mphh! Mm hh ph!"

    "You raise an eyebrow because #1, you can't tell what he's trying to say, and #2 he just sounds stupid"

    MC "Gale, how about you chew and swallow finish your food before trying to talk?"

    show Gale neutral at waist_up_center2, singlejump
    "Gale nods frantically, and you can see his jaw working double time as he attempts to quickly chew the gigantic bite of onigiri."

    "Finally, after a long time, he manages to get it all down."

    show Gale annoyed 
    G "Man, my jaw feels busted now."

    show Gale neutral 
    G "But that tasted so good. Absolutely zero regrets."

    MC "Really? Zero?"

    show Gale smug
    G "Zero."

    show Gale neutral
    MC "Anyways, what were you gonna say just now?"

    G "Eh, just that it was really really good and that you should try it."

    MC "We each have about half our onigiri left, right?"

    G "Yeah, I think so? I think mine might be a little less than half, since I took such a big bite."

    MC "How ‘bout trading?"

    G "I mean, sure, if you don't mind?"

    MC "Okay. Let's trade."

    "You and Gale pass each other your onigiri, being very careful such that neither of you would accidentally drop it."

    show Gale annoyed
    G "I can smell the umeboshi from here."

    MC "Do you not like umeboshi?"

    show Gale neutral pose2
    G "I would say I'm okay with it, but I don't particularly love it."

    MC "You sure? Tell me if you wanna swap back."

    show Gale neutral
    G "‘Kay."

    "The two of you spend the next few minutes taking the time to eat in silence, savouring every bite."

    show Gale confused
    $ renpy.pause(0.6)
    show Gale shocked
    $ renpy.pause(0.6)
    show Gale annoyed

    "Gale makes certain… interesting expressions while eating the umeboshi, but is otherwise fine."

    MC "Gale, you done?"

    show Gale neutral
    G "Yeah"

    G "Wanna head back now?"

    MC "Sure. Do you wanna pass me your wrapper? I’ll throw it away later."

    G "Alright, thanks!"

    MC "No worries!"

    MC "What time is it?"

    G "It’s…"

    "Gale looks down to check his watch."

    G "A few minutes to two."

    MC "That’s earlier than I expected."

    G "Right?"

    MC "Anyway, we should get back soon if we want to have time to walk around after we're done."

    G "‘Kay"

    show Gale neutral at waist_up_center2, singlejump
    "Gale stands up, pulling you up along with him."

    MC "Hey, give a person some warning next time!"

    show Gale annoyed
    G "Yeah, yeah, got it"

    show Gale neutral
    "Both of you spend the next few minutes in the walk back to campus enjoying each other’s company in silence."

    stop music fadeout 1.0
    scene black with fade
    scene bg_gale_day_stall
    show gale_boxes:
        xoffset 150
        yoffset 620
        zoom .50
    show Gale neutral at waist_up_center2
    with dissolve
    play music "audio/music/G1 - Cheerful (2).wav" fadein 1.0 loop

    "Once you've reached the stall, you pull the pennants out of your bag and triumphantly hold them aloft like a trophy."

    MC "The finishing touch!"

    G "It'll look so good after we're done, trust"

    MC "Yepp!!"

    MC "Now, how are we supposed to do this?"

    "You frown at the ‘pennants’ in your hands."

    MC "Gale, we have to restring these before we can put them up. It looks like they fell off the twine overnight."

    MC "Grab a pack and let's start working on it."

    show Gale laugh at waist_up_center2, singlejump
    G "Yes boss!"

    "Gale does a mock salute before he grabs the packet of pennants and starts working on them."

    show Gale confused
    G "[player_name], how do you do this? I can't make sense of it."

    MC "Man, I don't know either. I'm just winging it"

    G "‘Kay. But- don't blame me if it doesn't turn out too well."

    MC "Nah, it can't be that bad."

    show Gale laugh
    G "Clearly you underestimate my talent for messing things up"

    MC "Eh. We'll see, we'll see"

    show Gale neutral
    "Once the both of you are done, you stand up, comparing your pennants to Gale's."

    if stall_style == "artistic":
        show gale_tri_day_penn with dissolve
        MC "Hey, I'd say we're pretty good at this!"
        MC "It doesn't look half bad!"
        show Gale smug
        G "Damn right you are."
        hide gale_tri_day_penn with dissolve

    elif stall_style == "neutral":
        show gale_neutral_day_penn with dissolve
        MC "Eh-"
        MC "It's fine, I guess."
        show Gale laugh
        G "That looks better than I was expecting, not gonna lie"
        MC "Right?"
        hide gale_neutral_day_penn with dissolve

    elif stall_style == "non-artistic":
        show gale_loopsided_day_penn with dissolve
        show Gale confused pose2
        MC "Ermm"
        G "It's… passable?"
        G "I hope?"
        MC "You know what? We tried our best and that's what matters."
        hide gale_loopsided_day_penn with dissolve

    show Gale neutral
    "Gale nods in agreement."

    MC "Okay, now we gotta hang this up."

    MC "Can you bring the ladd-"

    show Gale smug
    G "Done and dusted~"

    "You look over to see that, indeed, Gale has already put the ladder exactly where you want it."

    MC "Thanks man"

    show Gale neutral
    G "No problemo!"

    MC "Gale, here, hold these for me while I climb up first."

    "You pass the pennants to Gale, who's standing next to the ladder to make sure you don't fall off."

    "Quickly, you climb up to the top, signalling for Gale to pass the pennants back to you."

    G "Here you go!"
    
    transform tiptoe_sway:
        subpixel True

        xoffset 0
        rotate 0

        ease 0.8 xoffset 8 rotate 2
        ease 0.8 xoffset -8 rotate -2
        ease 0.8 xoffset 0 rotate 0

        repeat

    show Gale confused at tiptoe_sway
    "Gale's tiptoeing to ensure you don't have to bend too low, lest you fall off the ladder again."

    show Gale neutral at waist_up_center2
    MC "Thanks"

    "You slowly start to hang up the pennants, hooking the ends into the little hooks at the top corners of the stall."

    "Once you're done, you give everything a once over to make sure everything is properly secured and climb down."

    show Gale shocked
    G "Hey, careful!"

    MC "Ai shit, I almost slipped there. Thanks for the warning."

    G "Are you alright?"

    MC "Yep! Thanks to you"

    show Gale laugh
    "Gale smiles in relief, then cranes his neck to look back up at the stall that the both of you have worked so hard to decorate over the past two days."

    show Gale neutral 
    G "It looks so different from before we first started, doesn't it?"

    MC "It sure does"

    show Gale confused pose2
    G "Do we need to do anything else?"

    MC "Uh, lemme see."

    MC "Banner, pennants, lights…"

    show Gale neutral
    MC "We should be done, but I'll check with the boys if we need to add anything."

    "You pull out your phone, unlocking your messages to check for anything."

    play sound "audio/sfx/phone-ping.ogg" volume .7
    MC "Oh! Rosco left us some flyers in the common room we could use."

    G "I’ll go get them."

    show Gale shocked
    MC "We should go get them together"

    show Gale annoyed
    G "Fineee"

    scene bg_gale_day_stall 
    show gale_boxes:
        xoffset 150
        yoffset 620
        zoom .50
    with dissolve
    "The two of you rush over to the common room so fast you might as well have teleported, Gale dramatically slamming open the door like an MC in a BL novel who’s finally confessing after slowburning for 20 chapters."

    scene black with fade
    scene bg gale clubroom 
    show Gale neutral at waist_up_center2
    with dissolve

    show Gale shocked at waist_up_center2, singlejump
    G "Where are the FLYERS?"

    MC "Uh, the mock-up should be on the coffee table."

    MC "I printed them out while waiting for you this morning."

    show Gale confused
    G "Hey, didn’t we agree that we’d do the printing together in the afternoon?"

    MC "Yeah, but then you were late, and I got bored playing Pipmon GO on my phone, so I just ended up printing the whole lot of ‘em."

    show Gale neutral
    G "You sure make good use of your time."

    G "Could you hold the door for me while I grab them?"

    MC "Sure, just make sure to grab them all.."

    hide Gale with dissolve
    "While you hold the door open, Gale quickly hops over to grab the stack of flyers, then dashes out the door to be next to you once he’s done."

    show Gale neutral at waist_up_center2 with dissolve
    G "MC, hey, they’re pretty cute, see?"

    "You look at the chibis that Gale’s pointing at and you can’t help but agree."

    MC "They are adorable…"

    MC "I’m lowkey kinda proud of my handiwork."

    MC "Okay let’s not get distracted and head back first, then we can admire the posters later."

    G "Okay~"

    "Once you’re back at the booth, Gale passes you some of the stack of flyers, and you quickly get down to business."

    "After a short five minutes, you guys are finally done."

    "Flyers hang from various places around the stall, put on display where others can see."

    "The remaining stack of flyers is placed neatly on the countertop of the stall, ready to be handed out the unsuspecting victims (read: passerby) on the day of the festival."

    G "And that is a wrap!"

    MC "Im so beat! But we did it…"

    "You lift your hand, and Gale quickly slaps it in a high five."

    G "Look at it [player_name]..."

    scene black with fade
    stop music fadeout 1.0

    play music "audio/music/G2 - Chill.wav" fadein 1.0 loop
    
    if stall_style == "artistic":

        $ quick_menu = False

        hide window
        scene bg artistic_stall_day
        with dissolve
        pause 3.0

        show Gale neutral at waist_up_left2 with dissolve
        $ quick_menu = True

        G "Well, we did a pretty good job overall, I guess?"

        MC "I think we make a pretty good team, if I say so myself."

        show Gale laugh at waist_up_left2, singlejump
        G "Yeah, we do! We could be professionals or something! The decorations are set perfectly, and the banner looks amazing!"

        MC "Yepp. I love the way I placed the flyers. Very artistic. And the table bunting is a nice touch to complement the big banner we made."

        show Gale neutral
        G "I’m glad you took the lead, honestly. With my horrendous art skills, it would have ended up looking like a tornado had swept through after we were done with it."

        MC "Well then, mister, you better be thanking me for saving your ass."

        show Gale laugh
        G "Of course! Have I ever mentioned how much I love you before?"

        MC "Gale, flattery won't get you anywhere."


    elif stall_style == "non-artistic":

        $ quick_menu = False

        hide window
        scene bg non_artistic_stall_day
        with dissolve
        pause 3.0

        show Gale neutral at waist_up_left2 with dissolve

        $ quick_menu = True
        MC "Well... it certainly has… character? It’s sure to attract people here."

        show Gale annoyed
        G "Why were we put in charge of this, again?"

        MC "I’d like to remind you that you volunteered for it."

        show Gale annoyed pose2
        G "In hindsight, that was kinda dumb of me. But at least we managed to complete it…"

        MC "Pffft… Look at how crooked the banner and pennants are! It looks like the stall just survived a hurricane."

        MC "The fairy lights and the flyers are a mess too…"

        show Gale neutral
        G "[player_name], look at the bright side! It's unique and has a human touch to it!"

        MC "That's one way to put it…"


    elif stall_style == "neutral":

        $ quick_menu = False

        hide window
        scene bg neutral_stall_day
        with dissolve
        pause 3.0

        show Gale neutral pose2 at waist_up_left2 with dissolve

        $ quick_menu = True
        G "Hey, it doesn't look too bad, I guess?"

        MC "It looks like every generic stall you always see at school fairs."

        show Gale neutral
        G "That’s quite impressive for us. I had no idea how it would turn out"

        MC "I totally agree."

        MC "And you know what? Considering neither of us have art backgrounds, I'm not going to complain."

        MC "It’s done, and it doesn’t look like it will fall apart… that’s enough for me!"
        show Gale laugh
        G "The guys won’t be able to complain. I’m sure they expected a total disaster."

    # ROUTES CONVERGE

    show Gale neutral at waist_up_center2 with dissolve
    MC "Should we go take a look at the other stalls? See how they're doing."

    show Gale neutral at waist_up_center2, singlejump

    G "Yeah! We need to get a good look at our competition!"

    MC "Is there any stall in particular that you wanna check out?"

    G "Oh-oh-oh, remember that ocean fishing stand we saw yesterday?"

    MC "Oh yeah, that one. I think it's just around the corner."

    show Gale confused pose2
    G "What do you think they're gonna do? They sure can't bring the ocean to our school."

    MC "Maybe a fishing game or something? Is it the closest to what their club does, after all."

    show Gale neutral
    G "Oooh, wait like those carnival games where you catch the fish with a paper scoop to bring home! I love those games!"

    MC "My childhood was filled with those catching fish games, and I still remember the scoop was partially made out of thin paper that would break if you moved it through the water too hard or too quickly."

    MC "But I did get lots of pet fish, although they all died pretty quickly."

    show Gale shocked pose2
    G "Oh? [player_name] bad at something? That's something I didn't think I'd see."

    show Gale neutral pose2
    MC "Gale, shut up. Anyways, we're here already."

    G "Hmmm, you're right! It really is one of those carnival fishing games! You should get a degree in fortune telling."

    MC "Nah, lucky guess."

    G "Maybe it is, maybe it isn’t."

    show Gale neutral 
    G "Actually, I forgot to mention just now, but a classmate mentioned that her club was going to be selling some crochet stuff as well."

    G "She showed me a tiny frog she made, it was really cute!"

    MC "That's really interesting!"

    G "Lemme show you the way!"

    G "I think their stall should be over there!"

    "Gale points at a stall far in the distance."

    MC "Why is it so far away…"

    show Gale shocked
    G "You wouldn't be so cruel as to make me go alone, right?"

    MC "*sigh* Alright, let's go."

    show Gale laugh at waist_up_center2, singlejump
    "Gale lets out a loud whoop of joy, then promptly grabs your hand and drags you towards the booth."

    MC "Oh, is no one around? I guess they've already finished preparations for the booth."

    show Gale neutral
    G "[player_name], look at that crochet rabbit! It's so adorable!"

    MC "Yeah, it is."

    MC "I wanna see what other interesting stalls there are around here…"

    MC "Are you alright if we walk around a little more?"

    G "Sure, why not?"

    "You start to walk in a random direction and come across a stall selling onigiri."

    MC "Oh! My friend from another class is in the club running that stall, if I remember correctly."

    G "An onigiri stall?! Let’s go check it out!"

    "You walk closer to the stall, which has a picture menu that looks delectable."

    show Gale shocked
    G "Woah, it looks so cool! And those picture of onigiri looks so delicious…"

    MC "I’ve tried my friend’s food before–and let me tell you, it is absolutely delicious!"

    show Gale neutral
    G "I’ll be sure to try it during the festival!"

    MC "You’re definitely not gonna regret it!"

    MC "What time is it, anyway?"

    "As if right on cue, your phone chimes loudly with a text message from Cassian."

    # TEXT MESSAGE: Cass
    # Use sound effect for now
    play sound "sfx/ReceiveText.ogg"
    C "{i}Hurry up and come back! It’s already fifteen minutes past our original meeting time!{/i}"

    MC "I guess we should hurry and get back. Come on, let’s run."

    hide Gale with dissolve
    "You and Gale both break into a sprint, running as if both your lives depend on it."

    stop music fadeout 1.0
    scene black with fade
    play music "audio/music/G1 - Cheerful (2).wav" fadein 1.0 loop
    scene bg clubroom 
    show Gale neutral at waist_up_right2
    with dissolve

    show Gale laugh at waist_up_right2, singlejump
    G "HEY GUYS! WE’RE BACK!"

    show Lucien neutral smile at waist_up_left4 with dissolve
    L "Gale, how are you still so energetic?"

    show Rosco neutral jacket at waist_up_center zorder 2.0 with dissolve
    R "Bro, I can hear you over my headphones. Might wanna tone it down a little, thanks."

    show Gale neutral at waist_up_right2, singlejump
    G "Sorry, dude. I’ll try to be MORE loud next time."

    hide Lucien
    show Zander neutral at waist_up_left3 zorder 1.0
    with dissolve

    Z "Soooo, how did it go? Anything happen while we weren’t there?"

    "Rosco takes off his headphones, eager to listen to any tea. From his spot on the beanbag where he was watching something on his phone, Cass perks up, eager to listen to that day's gossip."

    MC "The wind blew his bandana off, and a pipsqueak shat on the banner we made."

    show Zander laughing at waist_up_left3, singlejump
    Z "Holy shit, what did you do, Gale?"

    show Gale confused
    G "I don’t know? It just happened."

    show Rosco laugh jacket
    R "You might have offended a god somewhere, and this is your karma."

    show Gale neutral
    G "You know what? Knowing me, you’re probably right."

    hide Zander
    show Lucien neutral smile at waist_up_left4 zorder 1.0
    with dissolve
    L "I’m feeling a little bad for Gale right now."

    show Lucien laughing

    hide Rosco
    show Cassian neutral at waist_up_center2 zorder 2.0
    with dissolve

    "Laughter breaks out around the table. Cassian hides his smile as he tries to focus everyone’s attention back on the matters at hand."

    C "Okay, everyone, listen up!"

    C "We gotta lock in for this."

    C "Like seriously lock in, got it? If we wanna keep the Ichi tournaments."

    scene bg clubroom with dissolve

    "You and the boys nod seriously. Ichi tournaments are a big thing."

    "As the day of the festival slowly approaches, everyone gives out updates on their progress, having worked really hard in order to pull this last-minute stall off and keep our *true* club activities a secret from the outside world."

    "Everyone seems pleased with how they’ve progressed so far, and Cass claps once everyone’s gotten a chance to speak."

    show Cassian neutral at waist_up_center zorder 2.0
    show Gale neutral at waist_up_right2
    show Zander neutral at waist_up_left3 zorder 1.0
    with dissolve

    C "Alright! Good progress everyone!!"

    C "It’s getting quite late, so we should be heading home already."

    MC "You’re right. Goodbye guys! See y’all tomorrow!"

    show Gale laugh
    G "Ah, my muscles are aching after all the hard work today. I’m going to go now, bye guys!"
    hide Gale
    show Lucien neutral smile at waist_up_right4
    with dissolve

    Z "Bye"
    hide Zander
    show Rosco neutral jacket at waist_up_left
    with dissolve
    R "Bye-bye"

    hide Rosco
    L "Goodbye"

    hide Lucien with dissolve
    C "Goodbye and stay safe, everyone!"

    hide Cassian with dissolve
    "Everyone takes turns to leave, and one by one, the club room slowly empties."

    scene black with fade
    stop music fadeout 1.0

    if "G" not in collected_routes:
        $ collected_routes.append("G")

    if len(collected_routes) == 5:
        $ renpy.save("chapter1_end")
        scene black with fade
        jump general_ending

    else:
        jump choose_route
    #End of Day 2
