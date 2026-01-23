#Start of Rosco Route
label rosco_route:
    scene bg clubroom 
    MC "I'll help Rosco."

    show Rosco shocked jacket at waist_up_center with dissolve
    R "Hell yeah! You're down to give me a hand!?"

    show Rosco laugh jacket
    R "I knew I could count on you!"

    show Rosco neutral jacket
    R "You've got good taste, after all…"
    R "In fashion, I mean, {i}obviously{/i}. It's best styling with someone who knows what they're doing, right?"
    R "Anyway, let's head down to the market tomorrow. There's no time to waste!"

label rosco_route_day1:
    scene black with fade
    show text "{size=50}Rosco Route: Day 1{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve

    # bg mc bedroom
    scene bg mc bedroom

    MC "Eugh, we've got so much to finish before the festival starts."
    MC "So much to cram! We probably should've pre-ordered the outfits and everything…"
    MC "Speaking of outfits, Rosco's probably waiting for me at the market. I shouldn't keep him waiting too long."

    #bg outdoors
    scene bg road daylight

    "When you arrive at the shopping district, the buzz of conversation and the shuffle of footsteps fill the air."
    "Rows of boutiques and open-air stalls stretch down the street, their displays bursting with color."
    "In the rush of people, you spot a familiar head of pink hair—Rosco is waiting at the corner, looking down at his phone with two barbecue skewers in his hands."

    # Choice: Greeting Rosco

    #variable for later outcome
    default sneaked_on_rosco = False

    menu:
        "Call out to him":
            $ sneaked_on_rosco = False

            MC "Rosco!"

            show Rosco confused jacket at waist_up_center with dissolve
            "!"
            "Rosco immediately looks up, searching for the sound of your voice."

            show Rosco laugh jacket
            "In a moment, he spots you, his eyes lighting up with excitement."

            R "[player_name]! You're here!"

            MC "Hey! You're here weirdly early."

        "Sneak up on him":
            $ sneaked_on_rosco = True

            "He seems intensely focused on his phone, considering how he doesn't notice you at all. You decide to give him a little surprise as a greeting."
            "Keeping your lips zipped tight, you approach him from the side, just out of view when you strike."

            MC "BOO!"
            
            show Rosco shocked jacket at waist_up_center with dissolve: 
                shake2
            R "!!!"

            "Blissfully unaware, he shrieks when you grab the back of his shoulders tightly, stumbling in place until he turns to face you."

            show Rosco angry jacket
            R "Oh my [player_name]! What the hell is wrong with you?! I could've dropped the barbecue!"

            MC "Morning!"

            R "M-morning, I guess!? What was that for?!"

            MC "Well… Consider it a lesson to pay attention to your surroundings!"

            show Rosco annoyed jacket
            R "Ugh… Whatever, you're so {i}annoying{/i}. "
            extend "I'll get you back one of these days."

            MC "Like you could do that."
            MC "Anyway, you're here weirdly early? Why's that?"
        #choice end
    show Rosco neutral jacket
    R "Yeah, well, I wanted to get us some barbecue. Need to charge up for the day, right?"

    "He pockets his phone and takes one of the two skewers from his other hand, offering it to you."

    MC "Just for me? Wow, so thoughtful, thank you~"

    show Rosco blushing jacket
    R "What—No, goofy, I got one for me too!"
    R "That's why I have two! I wasn't intending it to—I'm just making sure you're not skipping out on meals 'cause—and I—"
    
    #find angry blush expression
    show Rosco pout blush jacket
    R "Agh, just shut up, dude!"

    MC "See? No one's buying it, not even you!"

    R "I'm not even gonna try and argue with you. {i}Whatever{/i}, bro."

    show Rosco neutral jacket
    "You take a bite of your barbecue—it's still hot in your mouth as you chew, and definitely freshly made. Rosco glares at you and takes a bite of his own, mumbling under his breath as you savour the taste."

    MC "Woah, this is so good!"

    show Rosco smug jacket
    R "Right? I know this seller, and their festival food hits {i}every{/i} year."

    show Rosco neutral jacket
    R "That aside, let's get to looking for clothes! We can eat while walking."

    MC "Mhm!"

    "Rosco starts down the road at a relaxed pace and you follow, idly nibbling at your skewer as the warmth of the evening settles around you."
    "The hum of distant conversation blends with the occasional rustle of fabric from nearby stalls, shopfronts glowing softly under the fading daylight."
    "Suddenly, you notice that Rosco's pace slows even more, and you slide the last piece of meat off the skewer as you come to a halt."

    MC "Mm? What's wrong?"

    show Rosco laugh jacket
    R "Look at that store there."

    "Rosco points at a storefront at the end of the road."
    "You tilt your head, not quite understanding what had caught his eye."

    show Rosco neutral jacket
    MC "What about it?"

    show Rosco annoyed jacket
    R "The poster in the window, goofy! The new game is coming out, Parker x Light Generations!"

    show Rosco neutral jacket
    "You and Rosco gradually approach the door, looking over the poster."

    menu:
        "I know that guy!":
            MC "Oh, wait! I know that guy!"

            "You point at the blue porcupine-humanoid standing at the right of the poster, running on a floating platform beside two other porcupines."

            MC "Parker… uh, Parker the Porcupine, right?"

            R "Yeah! He's a lightning fast porcupine and the protagonist of the game series, and the other porcupine is Light, his rival!"

            MC "Right, that name's familiar too…"
            MC "But {i}Light{/i}? Why's his name Light, he's black and red…?"

            show Rosco confused jacket
            R "I—Well…"

            show Rosco neutral jacket
            R "… Don't read into the details too much. Maybe the developers just had a hard time naming him."
            R "Anyway, this is the latest game coming out! I think pre-orders are open—Let's go and look around!"

        "I don’t recognize him…":

            MC "I don’t think I've seen him before…"

            show Rosco shocked jacket
            R "Are you serious right now?! You really haven't played any of the {i}Parker{i} games?"

            "You tilt your head as you listen to him ramble about the games."
            "There is a black and red porcupine standing in the center with two blue porcupines on either side of him."

            MC "He's supposed to be a porcupine?"

            "You aren't sure what you think he looks like, but he definitely doesn't look like a porcupine to you."

            show Rosco annoyed jacket
            R "{i}Yes{/i}, goofy. Look, the one in the center is Light, and the one on the right is Parker."

            MC "And the one on the left is a baby Parker! He's so cute."

            R "What? That's not—"

            "He pauses, letting out an audible sigh. You don't quite catch what he mutters under his breath."

            show Rosco neutral jacket
            R "Never mind, let's just go inside. It looks like they're doing pre-orders right now."
        #choice end

    "He doesn't wait for you to respond as he pushes the door open and strolls into the store."

    MC "Wait, but the outfits—?!"

    show Rosco laugh jacket
    R "It'll be fine~! We've got all day."

    MC "But…!"

    "You let out a sigh when you realize that he isn't listening."

    scene bg rosco game shop with fade
    show Rosco neutral jacket at waist_up_center with dissolve

    "By the time you follow him into the store, he's already standing at the register, speaking to the employee and waving to the poster in the window."

    MC "… This guy…"

    "You don't really feel angry with him. A part of you thinks it's cute that he's so excited."

    "Not that you'd say that to his face."

    "In the meantime, you decide to look around the shop. Your eye immediately catches a familiar cartridge on a nearby shelf."

    MC "{i}Oh! That's the new Pipmon game! I didn't realize it was out already. Oh, and they remastered that one?{/i}"

    "You stand by the shelf filled with Pipmon games, internally debating on whether or not you have the time to play one with your current schedule."

    show Rosco neutral jacket
    R "Are you thinking of buying something?"

    MC "!"

    MC "Don't sneak up on me like that!"

    # NOTE:
    # conditional branch here:
    # if user chose to sneak up behind Rosco before

    if sneaked_on_rosco:

        show Rosco smug jacket
        R "That's what you get, goofy!"

        MC "Yeah, yeah. Whatever."

        R "Ahhhh, you mad!"

        show Rosco laugh jacket
        "He laughs as you roll your eyes, following you when you start walking away."

        R "Your reactions are funny. I should do this more often."

        MC "You most definitely should not."

    else:
        show Rosco laugh jacket
        R "What can I say? Heh. Your reactions are too priceless!"

        MC "Shut up!"

        show Rosco smug jacket
        R "You're just mad because it's true."

        MC "No. I just want you to shut up."

        R "Make me."

        "You feel a chill down your spine for a moment, something treading between déjà vu and anticipation."

        MC "… Careful what you wish for, Rosco."

        show Rosco shocked jacket
        R "!"

        "With that, you walk away, glancing back to see his expression of shock."
        ##CHOICE END

    show Rosco neutral jacket
    MC "Hey, look! They have Maria Kart. I actually don't have a hard copy of this."

    "You approach the display computer on the start screen of Maria Kart, picking up a controller from the desk."

    MC "Look, we can play! Come here, let's do it!"

    "Rosco walks forward and grabs a controller as well, glancing to check his watch as his fingers hover over the buttons."

    R "Yeah… We have time to play a round, I think."

    MC "We’ll make it quick."

    "It only takes a few moments to choose your favorite character along with the car preferences you always use."

    MC "Hurry up."

    show Rosco smug jacket
    R "I didn't know you were so impatient to lose, [player_name]."

    MC "You know yapping won't help you win, right?"

    R "You're just salty 'cause you know you'll lose."

    "You roll your eyes, smirking when you realize that you're holding controller one."
    "Without any warning, you press the button to start the race."

    show Rosco shocked jacket
    R "Wait, I wasn't ready!"

    MC "You snooze, you lose."

    # NOTE:
    # Consider timer based decision making
    # currently implementation is no timer

    #start choice
    menu:
        "Hold button down at 3":
            "You groan as the race starts, staring at the way your car wriggles on the screen."

            show Rosco smug jacket
            R "Hah! Rookie mistake."

        "Hold button down at 2":
            MC "Hah! Take that!"

            show Rosco smug jacket
            R "You're too slow!"


    # --- Dice choice ---
    menu:
        "Go for the double dice":
            MC "Yes!"

            show Rosco annoyed jacket
            R "I was about to take that!"

        "Go for the single dice":
            MC "That stupid NPC took the double dice!"

            show Rosco smug jacket
            R "Sucks to suck."

    # --- Coin vs Banana ---
    menu:
        "Go towards the coin":
            MC "What do coins do again?"

            show Rosco neutral jacket
            R "They help you go faster."

            MC "Wait, really?"

        "Go towards the banana":
            MC "What—?! Who puts a banana THERE?!"

            show Rosco laugh jacket
            "Rosco laughs at your clear irritation, too focused on the race to say anything."

    # --- Shell choice ---
    menu:
        "Throw a green shell":
            "You launch a shell in front of you, not even glancing at the other screens. When you hear Rosco's laughter, you roll your eyes."

            show Rosco laugh jacket
            R "Nice try! You missed, goofy."

            MC "Careful, it’s still going~ You might jinx yourself!"

            R "Nope! It just broke."

            MC "Whatever."

        "Throw a red shell":
            "You launch a shell ahead of you, and Rosco makes a strangled noise as he glares at the side of your head."

            show Rosco angry jacket
            R "What the fuck, [player_name]?!"

            MC "I didn't mean to."

            R "Nobody believes that!"

    "Now at the last lap, you and Rosco occupy second and first place respectively, but he's too far ahead for you to catch up during this last straight."
    "You take your eyes off the screen for half a second to see his shit-eating grin, knowing that first place is his if things keep going the way they are…"

    #final decision
    menu:
        "Play fair and try to win":
            #variable for later dialogue
            $ rosco_won = True

            "You try your best on the final stretch of the game, pulling out all the little tricks you know from playing the game over the years."
            "Despite your best efforts, the gap between your two cars doesn't shrink."
            "Skillfully dodging and preserving his place, Rosco's car crosses the chequered line first. He pumps his fist in the air in triumph."

            show Rosco smug jacket
            R "Hell yeah! Eat dust, [player_name]!"

            MC "What the hell?! It was half a second off!"

            R "You're too slow~"

            "You put the controller down, reaching over to pinch his cheek and giving it a sharp tug."

            MC "Oh, shut up already!"

        "Distract Rosco":
            #variable for later dialogue
            $ rosco_won = False

            "Without hesitating, you stand in front of Rosco, blocking his view of the screen."

            show Rosco confused jacket
            R "Hey, what the heck—!"

            MC "All's fair in love and war!"

            "You smirk as a blue shell flies past you, hitting him just before he reaches the finish line."

            MC "Bless whatever NPC just threw that!"

            show Rosco annoyed jacket
            R "[player_name], get out of the way—!"

            MC "Nope!"

            "You move with every step he takes, making sure to block his view as you cross the finish line."

            MC "Let's go! First place!"

            "Rosco lets out a huff as you cheer."
            "He rolls his eyes, not missing the way you stick your tongue out at him."

            R "Yeah, yeah. Congratulations, goofy."

    show Rosco neutral jacket
    R "Okay, as fun as that was…"

    MC "We definitely need to get to those outfits."

    show Rosco shocked jacket at waist_up_left
    "Rosco’s about to respond but all of a sudden, his eyes go wide. You turn to follow his gaze, just as surprised as he was to see a familiar face."

    R "{i}…Cass?!{/i}"

    show Cassian neutral at waist_up_right with dissolve
    C "Oh, hey guys. What's up?"

    MC "Hey Cass! We were just looking around."

    #conditional depending on maria kart result
    if rosco_won:

        show Rosco smug jacket
        R "And I just destroyed [player_object] at Maria Kart!"

        MC "\"Destroyed\" is a stretch! The difference was literally half a second!"

        R "I still got first! The difference doesn't matter!"

        MC "It's all luck."

        show Rosco angry jacket
        R "Hey, don't start with me again!"

        C "No need to get all worked up. It's just a game."

        show Rosco shocked jacket
        R "…"

        MC "…"

        show Rosco annoyed jacket
        R "Cass, you are seriously the last person I {i}ever{/i} wanna hear that from."

        show Cassian shocked
        C "!"

        show Cassian angry
        C "Shut up!"

    else:

        MC "And guess who just won at Maria Kart?"

        show Rosco angry jacket
        R "Dishonestly! You totally cheated!"

        show Cassian confused
        C "Cheated in a game shop's Maria Kart…?"

        R "{i}Yes!{/i}"

        MC "The game's over, Rosco. Get over it!"

        show Rosco annoyed jacket
        R "I—"

        R "Whatever, goofy. Don't think you're off the hook."

    "Cass sighs and places a hand on his hip, glancing back at the aisles behind him before addressing you both again."

    show Cassian thinking
    C "Anyway, found anything that you wanna get? I was looking at the Pipmon aisle and I kinda wanna buy something…"

    MC "I was looking there too, actually! But I don't know if my schedule will let me, so I'm holding off for now."

    C "Ha, same. It's actually the only thing stopping me from getting the remastered copy."

    show Rosco laugh jacket
    R "Wait, Cass! Did you see the Parker x Light Generations poster outside? Pre-orders are open!"

    show Cassian neutral
    C "Yeah, I saw it when I walked in. I knew you'd want to get it."

    show Cassian confused
    C "Huh…? Wait a minute!"

    C "Aren't you guys meant to be looking for outfits…?"

    show Rosco shocked jacket
    "You give Rosco a sidelong glare, quick enough for him to catch it."

    show Cassian neutral
    MC "About that…"

    show Rosco neutral jacket
    R "We're exploring the town. For inspiration."

    show Cassian confused
    C "… For inspiration…?"

    #Variable for later dialogue
    default backed_rosco = False

    menu:
        "Back Rosco up":
            $ backed_rosco = True

            MC "Yeah, for morale."

            MC "We couldn't skip straight to the most important part, y'know?"

            R "Exactly! Gotta warm ourselves up a bit first."

            show Cassian smug
            C "Suuuure."

            MC "Why does it sound like you're doubting us?! Everyone needs a little downtime!"

            show Rosco angry jacket
            R "Yeah! No way we're gonna go in headfirst and potentially mess something up. A little hanging out is required beforehand!"

            C "And it's not because you guys got distracted or anything, mhm."

            show Rosco shocked jacket
            "You and Rosco glance at each other guiltily."

            show Cassian neutral
            C "Anyway, whatever. As long as you guys get it done."

        "Blame Rosco":
            $ backed_rosco = False

            MC "It was all Rosco's idea!"

            show Rosco shocked jacket
            R "Hey!"

            MC "I told him we had stuff to do, but he just had to come in here."

            show Rosco annoyed jacket
            R "Last time I checked, you weren't trying very hard to convince me otherwise!"

            MC "You didn't even let me speak before you opened the door!"

            R "Yeah, well—"

            show Cassian laughing
            C "So, are you guys going to keep bickering like an old married couple, or…?"

            show Rosco blushing jacket
            "!"
            
            "Rosco & [player_name]" "We are NOT bickering like a married couple!"

            C "Okay, whatever you say!"


    show Rosco neutral jacket
    show Cassian neutral 
    MC "But seriously, we should get going. Time is of the essence!"

    if backed_rosco:

        C "And you guys said you didn't get distracted…"

        R "We {i}didn't{/i}! This was… I don't know, to blow off steam or something! It's part of our plan!"

        "Cass rolls his eyes, and you nudge Rosco—it's evident Cass isn't buying it at all."

        R "Ugh, fine… I'll stop, I'll stop."

        "Cass rolls his eyes with a soft laugh as Rosco's shoulders drop in an instant."

    else:
        MC "We've gotten distracted enough for the day!"

        R "I'm telling you, it's all part of the plan!"

        C "I don't know, man… I'm kind of with [player_name] for this one."

        R "Well, [player_name] was having just as much fun as I was so [player_subject] can’t talk!"

        MC "Yeah, but—"

        R "Nah, nah, nah. Don't start with me."

        "Cass rolls his eyes, making a gagging sound from the back of his throat."

        C "You're literally an old married couple, I'm {i}telling{/i} you."


    C "That aside, I can't wait to see what you guys come up with!"

    show Cassian laughing
    C "I'm going to go grab that Pipmon game I was eyeing. I'll see you two later!"

    R "Okay, have fun, bro!"

    MC "See you later, Cass!"

    hide Cassian with dissolve
    show Rosco neutral jacket at waist_up_center with dissolve
    "You and Rosco wave at Cass as he retreats to the Pipmon aisle of the store."
    "When his white hair dips out of view, you immediately turn to Rosco, a stern expression on your face."

    MC "Okay. No more distractions."

    R "Look, we still have plenty of time! Relax."

    "He's right, of course. In reality, you have only been in the store for an hour at most."

    MC "Still!"

    "You pull the door open and shoo Rosco out, following in his wake."
    scene bg road daylight with fade
    show Rosco neutral jacket at waist_up_center with dissolve

    MC "We don't have any ideas. We need to get inspiration. {i}Real{/i} inspiration."

    "Rosco hums in agreement, his gaze wandering over the stores on the street."
    "You walk side by side, strangely very aware of how close you're standing to him."
    "You briefly think about the fact that you are close enough to hold hands."
    "You blush slightly, shaking your head to get rid of the thought."

    show Rosco confused jacket
    R "You good?"

    MC "I'm fine—"

    hide Rosco with dissolve
    "Just as you're reassuring him, you feel someone practically body slam your shoulder."

    MC "What the—"

    show bg road daylight at screenshake
    "You feel yourself falling, knocked off-balance."

    menu:
        "Reach out for help":

            show Rosco shocked jacket at waist_up_center with dissolve
            R "Woah!"

            "Everything is a blur as you reach out for something to hold on to."

            scene black with fade

            "You close your eyes, bracing yourself for the eventual impact with your fall."

            "The impact that you're expecting never happens."

            "Instead, you feel an arm wrap around your waist."

            MC "Eh?"

            scene bg road daylight with fade
            show Rosco concerned jacket at waist_up_center with dissolve
            R "Are you okay?"

            "He keeps his arm around your waist as you stand back up."

            MC "Y-yeah, I think so."

            show Rosco angry jacket
            R "What the hell was that?!"

            "You notice his arm is still wrapped around you as he glares over his shoulder, looking for the person who had rammed into you."
            "You feel your cheeks flush as he starts walking again, unexpectedly holding you close as he rants."

            R "What kind of person just runs into someone and doesn't say anything?! I should've given them a piece of my mind!"

            show Rosco annoyed jacket
            R "They didn't even apologize! I should go—"

            MC "Rosco."

            "He immediately focuses his gaze back on you at the sound of your voice."

            show Rosco concerned jacket
            R "What? What is it? Are you hurt?"

            MC "No! I'm fine. Really, I'm not hurt."

            "He stops in his tracks, looking you up and down as if to double check that you're telling him the truth."

            R "Then what's wrong?"

            "You blush as he tilts his head at you. You clear your throat as you gesture to his hand on your waist."

            MC "You're kinda… holding on really tightly right now…"

            show Rosco blushing jacket
            R "Oh shit—Sorry!"

            "He immediately lets go, taking a step away from you."
            "Strangely, you feel a bit of regret. A part of you was enjoying the way it felt."

            MC "It's okay. Thanks for catching me."

            show Rosco embarrassed jacket
            R "Y-eah! No problem. I'm glad you're not hurt."

            MC "…"

            show Rosco blushing jacket
            R "…"

            "You start walking again, but things feel a bit different than before."
            "You don't quite have the words to explain it… but it doesn't seem like a bad thing."
            "The smile you keep to yourself is wider than it should be."

            show Rosco neutral jacket
            R "Oh!"

            "Coming to a stop at the next block, Rosco suddenly halts in his tracks. Turning to look at you, he points up ahead."

        "Regain your balance (fail)":

            MC "!"

            "As the stranger glides past you, not even stopping to apologize, you instinctively search for something to keep you stable."

            "When you feel something solid, now with your face far closer to the pavement than you would like it to be, you grab onto it to pull yourself up."

            show Rosco shocked jacket at waist_up_center with dissolve
            R "!"

            R "Woah, are you good?"

            "Steadying, you let out a huff of breath as you regain your footing."

            MC "I'm… I'm good."

            "Your grip loosens, and you look over in shock to see that you'd grabbed Rosco's arm."

            MC "Oh—Sorry!"

            "Quickly letting go, you take a half step to the side."

            show Rosco neutral jacket
            R "Nah, don't worry about it. It's not you who should be sorry."

            show Rosco angry jacket
            R "That asshole didn't even apologize!"

            "Rosco turns back to glare at the figure, who disappears around the corner of the block as he looks."

            show Rosco concerned jacket
            MC "… It's all good. I didn't get hurt, so."

            R "Is your shoulder good, though?"

            "You nod, moving your shoulder in circles carefully."

            MC "Yeah. Doesn't really hurt at all."

            show Rosco neutral jacket
            "Relieved, Rosco's eyebrows unfurrow, his chest falling as he lets out a reassured breath."

            R "Okay. Good."

            "As you continue walking down the road, you notice him glancing over from time to time to check on you. His eye on the sidewalk ahead is more keen than ever."

            R "Oh!"

            "Suddenly, Rosco stops in his tracks, pointing straight ahead."
        #choice end

    show Rosco neutral jacket
    R "Hey, look!"

    "You notice the building he's pointing to at the end of the road, well lit with pale yellow light seeping from the huge glass windows."

    R "That's the outfit store I was looking at. Their haoris are really well made."

    MC "Ooh, great!"

    R "Let's go and grab ourselves some outfits, then!"


    # BACKGROUND: Generic Clothing Store
    scene bg rosco clothing shop with dissolve

    "Racks upon racks of clothing items surround you on all fronts, but Rosco navigates the aisles expertly as he makes his way to the center of the store."

    R "Haoris…"

    R "Ah, there! It should be over in that aisle."

    "He makes a start and you follow closely behind, entering the labyrinth of circular clothing racks lined with different haori styles and colours."

    MC "Woah, they have a lot of these here…"

    R "Maybe too many."

    "You watch as he takes a hanger off the rack, inspecting the pattern of it before slotting it back where it was."

    R "We need plain ones, right? So that we can customize them tomorrow."

    MC "Right."

    "You look over the haoris on the straight rack nearest to you, mostly empty other than a few items. Simple fabric flutters as you walk by, your eyes catching sight of light yellow, pale red, and lavender."

    jump haori_selection
    
    label haori_selection_return:

    MC "This one's perfect. Let's go with this."

    R "Nice. It definitely suits you."

    MC "Yeah, I'm glad—"

    MC "!"

    MC "Oh, look!"

    show haori_rosco with dissolve:
            pos (1100, 100)
    "You grab his wrist without further thought when you notice a light pink haori, dragging him towards the rack a few feet away."

    MC "Rosco, this one's perfect for you!"

    show Rosco laugh jacket
    R "You're right! It's exactly what I was looking for!"

    hide haori_rosco with dissolve
    "He grins, eyes crinkling with happiness."

    R "Hey, that means our shopping is done!"

    show Rosco neutral jacket
    R "And to think Cass was doubting us… We got this on lock."

    hide Rosco with dissolve
    "He takes all the haoris from you, leading the way to the cashier and finding it in no time."
    "You look around as he speaks to the employee, your attention captured by some accessories that are displayed by the counter."
    "There are a lot of animal-themed items lined on the stand by the counter, featuring keychains, pop-locks, and more."
    "Curious, you pick up one of the fluffy headbands, smiling to yourself as the attached dog ears flop around."

    MC "{i}Ha… This would be perfect on Gale.{/i}"

    "After a few more moments, Rosco pops up beside you."

    show Rosco neutral jacket at waist_up_center with dissolve
    R "Whatcha doing?"

    MC "Look at all these animal ears they have! Don't you think it's so Gale coded?"

    "As you turn to speak to him, you notice his empty hands, slightly panicked."

    MC "Wait, where are the haoris?"

    R "They're gonna iron it out and package them so we can take 'em back safely."

    MC "Oh. Alright, well, maybe we can—"

    MC "Oh. " 
    extend "My. " 
    extend "Gosh. "

    screen catears_screen:
        frame:
            xpos 1300
            ypos 300
            background Solid("#000000c0")
            padding(5,5)
            vbox:
                add "nyanbie_headband"

    screen roscalears:
        frame:
            xpos 1300
            ypos 300
            background Solid("#000000c0")
            padding(5,5)
            vbox:
                add "roscal_headband"

    show screen catears_screen with dissolve

    "You pick out a pink and blue headband, smiling devilishly as you lift it up next to his face."

    hide screen catears_screen with dissolve

    show Rosco neutral jacket catears with dissolve
    "Before he can protest, you plop it on his head, your smile widening as you look him over."

    MC "These cat ears are perfect for you."

    show Rosco annoyed jacket catears
    R "Seriously?"

    MC "Well, duh. You're pretty cat coded, you know?"

    "He rolls his eyes in response. Then he glances behind you, looking over the different headbands."

    show Rosco smug jacket catears
    "Rosco leans over, reaching around you to grab one of the headbands from the display. You stiffen slightly, realizing just how close he is."

    "Before you can process anything, you see him lift up a pair of mouse ears."

    show screen roscalears with dissolve

    R "If you choose one for me, I get to choose one for you."

    "Glancing at the headband, you tilt your head curiously."

    MC "A mouse? {i}Really?{/i}"

    hide screen roscalears with dissolve
    R "Yeah. We'll be like that one cartoon duo."

    "You roll your eyes, ignoring his smug grin as he puts the mouse ears on you. With a quiet chuckle, he pulls out his phone, lifting it to snap a picture."

    R "Say cheese~"

    "As soon as he takes the picture, an employee appears behind the counter again; you recognize them as the person Rosco had just been speaking with earlier."

    "They place the bag on the counter, giving you a wave to come over."

    show Rosco neutral jacket catears 
    R "Perfect timing."

    MC "Here, I'll put these back."

    hide Rosco with dissolve
    "You take both of the headbands, putting them back in place as he gets the bag from the cashier."

    MC "I think this is everything, right?"

    show Rosco neutral jacket at waist_up_center with dissolve
    R "Mhm… This should be all that we need to do today."

    show Rosco laugh jacket
    MC "Woo! Let's go!"

    scene black with fade
    show bg road daylight with fade
    show Rosco neutral jacket at waist_up_center with dissolve

    "You feel a sense of relief as you walk out of the store, grateful that you were able to finish at least one part of the festival task Rosco was assigned to."
    "Instead of saying goodbye like you expect, Rosco insists on walking you home, saying something about night time bringing out the living dead or whatnot."
    "You don't argue with him, despite his strange excuse. After all, you want to spend more time with him as well."

    MC "You really didn't have to walk me home, you know."

    "You slow down as you reach the front of your dorm building."

    R "Yeah, well, it doesn't sit right with me that I'd leave you to walk all this way alone."

    show Rosco annoyed jacket
    R "I mean, you almost got hurt just earlier with that jackass. What if it happened again, huh?"

    "With a hint of a smile on your face, you roll your eyes and push his shoulder gently."

    MC "Talk about paranoia…"

    show Rosco laugh jacket
    "Laughing, he stumbles back and plays along."

    show Rosco neutral jacket
    R "Whatever. Better safe than sorry, goofy."

    MC "Okay, okay. I'll be safe, promise!"

    R "Good."

    R "Good.{fast} Or else."

    show Rosco smug jacket

    menu:
        "Challenge him":

            MC "Or else what?"

            "You tilt your head at him, mind running through the different possibilities. Rosco merely smirks, leaning a bit closer."

            R "You'll see."

            "You fight the shiver that runs down your neck as his breath brushes against your ear."

            show Rosco laugh jacket
            "Clearly, you don't do a great job at hiding it—smug as ever, he laughs as he pulls away."

            show Rosco neutral jacket
            R "Okay, get inside now. We still have a lot of work to do tomorrow."

            MC "Right. Yeah! Okay, I'll see you tomorrow."

            "He waves, watching you enter the building before leaving."

            "You glance back to see him walking away, your heart beating a bit faster for some inexplicable reason."

            MC "What the heck was that?"

            "You shake your head, chalking it up to being a bit tired as you hurry to your room."

        "Acquiesce with him":

            MC "Yeah, yeah, I'll be safe."

            MC "I don't wanna find out what \"or else\" implies…"

            show Rosco laugh jacket
            "Laughing, Rosco nods, a toothy grin on his face."

            show Rosco neutral jacket
            R "Okay, get inside now. We still have a lot of work to do tomorrow."

            MC "Right. Yeah! Okay, I'll see you tomorrow."

            "He waves, watching you enter the building before leaving."

    #Day 1 end
    hide Rosco with dissolve

    show bg mc bedroom with fade
    "You spend the rest of the evening relaxing at home and catching up on schoolwork. After all, you want to be well rested and relatively free for the next day."

    "When you head to bed, you feel a bit of excitement."

    "You convince yourself it's because you're excited to decorate the haoris—and not because you get to spend another day with a certain someone."

label rosco_route_day2:

    scene black with fade
    show text "{size=50}Rosco Route: Day 2{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve

    show bg mc bedroom with dissolve

    "Blinking your eyes open, the clock reads noon when you finally get out of bed."

    "You're halfway through brushing your teeth when your phone dings with a notification."

    r_nvl "hi"
    r_nvl "i just woke up"

    "Staring down at the gray messages, you blink at it in disbelief."

    "You take a moment to finish washing up before replying."

    menu:
        "Make fun of him":

            mc_nvl "it's literally lunchtime" 
            mc_nvl "wdym you just woke up"

            r_nvl "and???"
            r_nvl "what time did you wake up then."
            r_nvl "and don't lie"

            "You stare at the message for a moment too long, fingers hovering above the buttons but not clicking any when your phone vibrates again."

            r_nvl "you just woke up too huh"

            mc_nvl "i didn't even say anything?!"

            r_nvl "i know"
            r_nvl "you're just too obvious :3"

            mc_nvl "???"
            mc_nvl "whatever >:/"

            r_nvl "you should appreciate it bro"
            r_nvl "i know u that well????"
            r_nvl "be happy?????"

            "You scoff as you turn off the bathroom light, unable to believe the audacity."

            mc_nvl "wowww tysmmmm omggg"

            r_nvl "that's what i like to hear"
            r_nvl "ur so welcome"

            mc_nvl "i hate u"

            r_nvl "no u don't"

            mc_nvl "whatever!!!!!"

        "Admit you also woke up late":

            mc_nvl "yeah me too, ngl"

            r_nvl "figures"
            r_nvl "now i know why you didn't text sooner"

            mc_nvl "what can i say"
            mc_nvl "sleep is just too good <3"

            r_nvl "yeah the bed is too comfy :3"

            "You smile at his response, stretching as you leave your bathroom."

            mc_nvl "i knew we'd understand each other :D"

            r_nvl "lol"
            r_nvl "this is why we're a dream team"

            mc_nvl "awwwwww we are? :3c"

            r_nvl "ur ruining it"

            mc_nvl ":,)"

    mc_nvl "anyway"
    mc_nvl "meet in an hr?"

    r_nvl "sure"
    r_nvl "let's meet at my place"
    r_nvl "i'm trying to finish up the game demo"

    mc_nvl "okay!"
    mc_nvl "need me to bring anything?"

    r_nvl "maybe some snacks"
    r_nvl "i've got everything else we need"

    mc_nvl "perfect"
    mc_nvl "see you soon!"

    r_nvl "see ya"

    "You're gathering your things to get ready to leave when your phone buzzes again, almost as if he'd just sent another message as an afterthought."

    r_nvl "and be safe"
    r_nvl "goofy"

    mc_nvl "no 'or else' this time?"

    r_nvl "that part's a given"

    "You laugh at his message, shaking your head. You set your phone down, quickly getting ready to go to his place."

    scene bg rosco bedroom noon with fade
    show Rosco laugh at waist_up_center with dissolve
    R "Right on time! Make yourself comfortable."

    R  "Sorry for the, uh..."
    show Rosco embarrassed
    extend " mess…"

    "You glance around the room, laughing to yourself."

    show Rosco concerned
    MC "Did you think I was gonna get here late? Looks like you were halfway through cleaning…"
    extend " or an attempt at doing that."

    show Rosco pout blush
    R "…"
    R "Let's not talk about it."

    MC "Right…"

    "As you look around for something to poke fun at, you notice his PC is still on, quiet game sounds emitting from the speaker."

    show Rosco neutral
    MC "Wait, is that B.I.T.E Protocol? Have you been working on it?"

    R "Oh, yeah. I was working on the combat portion of it. I think I just finished it? But I haven't had it tested yet."

    MC "Wait, really?"

    R "Yup. We can do some beta testing at the festival, but we should probably do some tests for bugs before that."
    R "Wouldn't want it to be on display without any trials at all…"

    "You pause for a moment, glancing at his computer before looking at him curiously."

    menu:
        "Ask to test it now.":

            "Your lips curve up in a sly smile."

            MC "What if we test it now?"
            show Rosco laugh
            "His gaze lights up at your suggestion, and his smile is soon matching yours."

        "Ask when he's going to test it.":

            MC "When do you plan on testing it?"

            R "Good question… We don't have that much time 'til the festival."
            R "It'll be hard to schedule a fixed time for the boys to all come together and test it…"

            "His eyes go wide, lips quirking up."
            show Rosco laugh
            R "Why don't we do that now?"


    R "I mean, if you're free and I'm free, this is a perfect time to do it."

    MC "Will we still have time for the outfits, though…"

    show Rosco neutral
    R "Psh, of course we will! It's not gonna take forever to do one run of it."
    R "C'mon, don't doubt it! Let's just do it!"

    "He gestures for you to get into the chair, outstretching his hand and smiling widely."

    "With a sigh, you surrender, glaring at him as he ushers you into the chair."

    R "Okay, ooone sec, just gotta maneuver back to the title screen…"

    menu:
        "I love MOBA games!":

            MC "Let's go! MOBA games are always fun."

            R "Oh, do you play them often? Do you have a favorite?"

        "I love Pipmon Connect!":
            show Rosco laugh
            R " That's a fun one!"

            MC "You play it too? We should queue up together sometime!"

            R "Sure! Do you have a favorite Pipmon?"

            MC "In Pipmon Connect, it'd have to be… Bibble!"

            R "Good choice! Let's play when we get some free time."

        "Big fan of LOL.":
            show Rosco annoyed
            R "You're kidding, right?"

            MC "Goofy, don't start with me. I know you've spent hours on that game."

            R "Hey! Goofy's my thing!"

            MC "Goofy."

            "You stick your tongue out at him, laughing as he rolls his eyes in response."

            R "Okay, anyways."

        "I don't really play these kinds of games.":

            MC "I'm a little nervous… I don't really play these kinds of games."
            
            show Rosco laugh
            R "It's fine! That'll make testing even better!"
            R "You get to learn about a new game, and your fumbling around will be great at locating glitches or bugs I might've missed!"

            MC "Did you just call my attempt at gaming \"fumbling around\"?!"

            show Rosco smug
            R "Eh, well, it's true 'til you show me it isn't…"

            MC "I hate it here."

    "He flicks back to the main screen with a laugh, and the menu boots to life in no time."

    show Rosco neutral 
    MC "Woah! The graphics on this have gotten far better since the last time I saw it!"

    R "You think so? I think it could be a bit better, objectively speaking."

    MC "Are you kidding? It's already amazing."

    R "Yeaaaah, but it could be better, you know what I mean?"

    MC "Can you just take the compliment?"

    R "Alright, alright!"

    "He puts his hands up in surrender, looking slightly embarrassed."
    show Rosco embarrassed
    R "Thanks…"

    "You smile but choose not to push the subject any further."
    "You could always save your words of praise for later…"
    extend "When you feel more like a menace."

    MC "So… what is it that I have to actually do?"

    show Rosco neutral
    R "Here, let me make this a bit easier."

    scene bg rosco monitor with fade
    "He presses a few buttons on the keyboard and maneuvers the mouse until you find yourself on a new screen, this one looking like an actual battlefield."

    R "Okay, before we get to the combat portion, you gotta pick a character."

    MC "Oh, are these the ones we got Altus to do sketches of?"

    R "Yeah! They're modelled fully now, but we also have these sick graphics."
    R "Go ahead and pick one to start with!"

    jump mascot_selection

    label mascot_info_return:

    jump mascot_playtest
    
    label mascot_playtest_return:
    # Continuing Story
    "Time flies as you progress through the game. Your determination to win has never been so strong, and you're this close to winning."

    "Out of the blue, you're surrounded on all fronts, locked in an unfamiliar battle setting on your own."

    MC "I'm going to die— I'm going to die— I'm going to die— I'm goING TO DIE-"

    "You freak out as your health bar drops dangerously low, some of the spikes from the opposing Dewdrop hitting you even as you run away."

    scene bg rosco monitor:
        screenshake
    MC "STUPID SLIME CREATURE—"

    R "You're not going to die! Jeezus! Here—"

    "He suddenly leans over. Before you can ask any questions, his arm reaches around you and slides past your back."

    "His hand is placed tentatively over yours, fingers aligned, and his other hand wraps yours against the mouse."

    MC "!"

    MC "Wha—"

    "All thoughts of the game leave your mind at the unexpected proximity."

    show Rosco annoyed at waist_up_center with dissolve
    R "Come on, focus! Use your skills! Ah—whatever."

    "He presses down on the keyboard, using your fingers to activate the best skills for the situation."

    show Rosco neutral 
    R "See? And the enemy Dewdrop's ult just ended. This is the perfect time to strike."

    hide Rosco with dissolve
    "His fingers move quickly, tapping different keys and moving the mouse efficiently."
    "Despite your efforts to focus, your thoughts keep getting drawn to the way his cooler, larger hand feels against yours."
    "The scent of his cologne does nothing to help your focus, drawing your gaze to look up at him instead—you're awed at how determined he looks, eyebrows knit with concentration."
    "He doesn't notice your stare, his gaze flitting over the screen as he continues to play for you."

    show Rosco laugh at waist_up_center with dissolve
    R "Annnd we're done. Triumph!"

    show Rosco neutral
    MC "What?"

    "Your gaze snaps back to the screen, surprised to find the word TRIUMPH written in golden letters."

    show Rosco smug
    R "So what'd you think? Fun, huh?"

    scene bg rosco bedroom afternoon with fade
    show Rosco neutral at waist_up_center with dissolve
    "He looks proud of himself as he pulls away, standing properly again with his arm propped on the chair. For a brief moment, you miss the feel of his hand against yours."
    "You clear your throat, mentally shaking away your thoughts as you answer him."

    MC "Yeah! Yeah, definitely."

    "He seems oblivious to your flustered state, giving you a hopeful smile."

    show Rosco concerned
    R "Do you think people will enjoy it at the festival?"

    MC "Of course! It'll be a hit for sure."

    show Rosco laugh
    R "Nice! Then I'm all done with this. Should we get started on haori decorating?"

    hide Rosco with dissolve
    "You nod, getting out of the chair and walking to the closet with Rosco. He takes out the haoris and holds them up."

    show Rosco neutral at waist_up_center with dissolve
    R "There's five of them. What order do we wanna go with?"

    MC "Let's go with Gale's. What stickers do you have that we can pick from?"

    "Rosco pulls out a box from under his bed, bringing it over to his empty desk."

    R "I brought this from the clubroom. It's a bunch of random stickers we've collected over the years."

    "He dumps it out on the desk, tossing the box aside as you start shuffling through them all."

    R "I thought maybe we could use these as inspo to make the patches for all the haoris."

    show haori_badge_gale_dog with dissolve:
        pos (200, 350)
    
    screen gale_dog:
        frame:
            xpos 1300
            ypos 350
            xsize 350 
            ysize 350
            background Solid("#00000079")
            padding(1,1)
            vbox:
                add "haori_badge_gale_dog":
                    xpos -25
                    ypos 0


    show screen gale_dog with dissolve

    "He picks out a dog, handing it to you."

    R "Doesn't this one lowkey look like Gale's dog? If we gave it that bandana that Gale puts on Pup, then it'll be a pretty good replica."

    "You turn the sticker over in your fingers, humming thoughtfully."

    hide haori_badge_gale_dog with dissolve
    hide screen gale_dog with dissolve
    MC "Yeah, that sounds good. And then…"

    # no plain tv screen do i just use the straight kerfurr sticker?
    screen gale_kerfurr:
        frame:
            xpos 1300
            ypos 350
            xsize 350 
            ysize 350
            background Solid("#00000079")
            padding(1,1)
            vbox:
                add "haori_badge_gale_kerfurr":
                    xpos -25
                    ypos -25


    show screen gale_kerfurr with dissolve
    
    "You pick out a TV screen, turning it to face Rosco."

    MC "If we added cat ears and a cat face, doesn't it remind you of Ferkur, that robot unit from the game Gale likes?"

    R "Oh yeah! What was it again? App… Apparitions in the Abyss?"

    MC "Yeah. He spends hours playing that thing."

    MC "Okay, we need one more."

    "You hold the two stickers in your hand, glancing through the other ones that are scattered over the desktop."

    screen gale_helm:
        frame:
            xpos 1300
            ypos 350
            xsize 350 
            ysize 350
            background Solid("#00000079")
            padding(1,1)
            vbox:
                add "haori_badge_gale_helm":
                    xpos -25
                    ypos -25


    show screen gale_helm with dissolve

    "Rosco offers up a ship steering wheel, narrowing his eyes."

    show Rosco confused
    R "Out of everything here, I feel like this one kinda fits Gale. I'm not sure why?"

    MC "He does kind of like pirates… I think. He's mentioned it from time to time, and he definitely likes swords. And pirates use swords. And ships! So I think it works."

    show Rosco neutral
    R "Okay, then that's all settled."

    hide screen gale_helm with dissolve
    "Taking the stickers, he piles them together on the side, making sure you don't pick the same ones again."

    R "Let's do Cass now…"

    screen cass_teabag:
        frame:
            xpos 1300
            ypos 350
            xsize 400 
            ysize 350
            background Solid("#00000079")
            padding(10,10)
            vbox:
                add "haori_badge_cass_teabag":
                    xpos 15
                    ypos 0


    show screen cass_teabag with dissolve

    "You grab a tea bag sticker, lifting it up so that he could see."

    R "That's perfect! He's always talking about oolong tea."

    MC "Hmm… Maybe we can add a little leaf to the end to make it a bit cuter too."
    hide screen cass_teabag with dissolve

    R "Speaking of cute…"

    "Rosco's eyes glint with amusement, his lips twitching with the hint of a smirk as he picks up a cow sticker."

    screen cass_cow:
        frame:
            xpos 1300
            ypos 350
            xsize 350 
            ysize 350
            background Solid("#00000079")
            padding(1,1)
            vbox:
                add "haori_badge_cass_cow":
                    xpos -25
                    ypos 0


    show screen cass_cow with dissolve

    R "Don't you think this one's also pretty cute?"

    MC "I mean, yeah, but what does that have to do with—"

    show Rosco smug
    "You pause as Rosco's smirk widens."

    MC "You're evil."

    R "I told him I'd never let him live it down, and I meant it."

    hide screen cass_cow with dissolve
    show Rosco laugh 
    "He laughs as he puts the two stickers together, only laughing harder when you shake your head at him."

    screen cass_valo:
        frame:
            xpos 1300
            ypos 350
            xsize 350 
            ysize 350
            background Solid("#00000079")
            padding(1,1)
            vbox:
                add "haori_badge_cass_valo":
                    xpos -20
                    ypos 0


    show screen cass_valo with dissolve

    MC "Oh, hey! Isn't this icon from Catorant?"

    show Rosco neutral 
    "Rosco finally pulls himself back together, looking over at the sticker you hold up."

    R "I think so! That looks like the icon from the one Cass mains."

    hide screen cass_valo with dissolve
    MC "Nice. Then that's two down and three to go. Luci next?"

    "He nods in agreement, letting you take Cass's stickers and set them off to the side."

    R "Immediately, we have got to go with the guitar."

    screen luci_guitar:
        frame:
            xpos 1300
            ypos 350
            xsize 350 
            ysize 350
            background Solid("#00000079")
            padding(1,1)
            vbox:
                add "haori_badge_luci_guitar":
                    xpos -10
                    ypos 0


    show screen luci_guitar with dissolve

    "He leans forward and grabs an acoustic guitar sticker, double checking it in his hands."

    R "We can make it look a little bit more like Luci's actual guitar, too! Add the little design… Yeah, this is perfect."

    hide screen luci_guitar with dissolve
    MC "Mhm, and this—"

    screen luci_coffee:
        frame:
            xpos 1300
            ypos 350
            xsize 350 
            ysize 350
            background Solid("#00000079")
            padding(1,1)
            vbox:
                add "haori_badge_luci_coffee":
                    xpos 0
                    ypos 0


    show screen luci_coffee with dissolve
    "You grab a sticker with two coffee beans next to each other."

    MC "Luci's obsessed with coffee, so this should fit him well."

    hide screen luci_coffee with dissolve
    R "Absolutely!"

    R "For this last one, though… hm."

    "You spend some time checking over all the stickers, but none of them really draw you in. Hesitantly, you reach for a plain heart."

    screen luci_crownheart:
        frame:
            xpos 1300
            ypos 350
            xsize 350 
            ysize 350
            background Solid("#00000065")
            padding(1,1)
            vbox:
                add "haori_badge_luci_crownheart":
                    xpos -5
                    ypos 0


    show screen luci_crownheart with dissolve
    
    MC "Hear me out. You know the unique little heart doodles Luci does in his notebooks?"

    R "Yeah, that heart with the slit in the middle and a little diamond crown at its base?"

    MC "Yeah! I think that's pretty unique to Luci, and I remember the design pretty well. I think I have a photo of it somewhere on a worksheet he gave me, but it's just a rough doodle."

    R "Works for me!"

    hide screen luci_crownheart
    "He sets Luci's three aside, next to Cass's pile."

    screen zanny_dumbbell:
        frame:
            xpos 1300
            ypos 350
            xsize 350 
            ysize 350
            background Solid("#00000079")
            padding(1,1)
            vbox:
                add "haori_badge_zanny_patch3":
                    xpos -5
                    ypos 0


    show screen zanny_dumbbell with dissolve

    R "Then Zander… I was thinking about him the second I saw the dumbbell. We've got to include it for this gym rat."

    hide screen zanny_dumbbell with dissolve

    #NOTE: Stopped here
    "He already puts the dumbbell to the side, reserving it."

    MC "Then… Ooh, look at this."

    "You pick out a sticker of an unspecified drink in a cocktail glass."

    MC "Doesn't he love that one cocktail, the Empress… Emperor… I don't remember what it was."

    R "Empress Gin! He's mentioned it as his favourite a lot."

    MC "Yeah, why don't we make a little sticker of that? With the grapefruit slice and everything."

    R "He's definitely gonna get mad at us for having that on his haori, but I love the idea. Let's do it."

    R "And lastly, this coffee cup should work? Distinct enough from Luci, but still enough to demonstrate his love for coffee."

    MC "Mhm, works for me!"

    "You look around the table as Rosco sets aside all the stickers."

    MC "Now all that's left is ours, right?"

    R "Yep. Why don't we both pick our own, then we can make each other's when we distribute the workload?"

    MC "That's cute. I like it! Okay, let me pick the references first…"

    "A beat of silence stretches as you both get to choosing your stickers."

    MC "Okay, I think I've got mine."

    R "Me too! Talk me through yours first."

    MC "Sure."

    "You spend a minute or so explaining your picks, detailing what you envision on the final haori."

    R "All very doable. I like it."

    MC "And yours?"

    R "Right. I actually couldn't settle on three, so I picked four of them out of the pile and thought it might be better for you to pick which ones to go with."

    "He slides four small stickers over to the middle of the desk, laying them out in a row. You look over them, your expression growing increasingly confused."

    MC "A crown, a shield, a scroll, and a candle?"

    MC "These are all very… medieval picks. Not what I expected."

    R "Alright, medieval is crazy. Don't criticize my picks!"

    MC "I'm not criticizing them! I'm just curious as to why you picked… I don't know, these not-so-Rosco-esque items!"

    R "… I dunno, I just felt really drawn to them when looking over the pile. See, they don't have stuff I'm actually into! It's too niche!"

    R "If they had, like, a gaming device or something, then I would've picked that!"

    MC "True, I didn't see anything video game or internet related… Hm, fair enough. This is gonna be an interesting haori."

    "Rosco sighs, gaze roaming over all the stickers the both of you have picked out for yourselves and the rest of the club."

    R "Alright, let's get to work. Other than mine, which others do you want to make?"
    
    #CHOICE (menu) saved as variable since idk if it will be used in the final day
    menu:
        "Gale":
            $ chosen_haori = "Gale"
        "C":
            $ chosen_haori = "C"
        "Luci":
            $ chosen_haori = "Luci"
        "Zanny":
            $ chosen_haori = "Zanny"

    R "Gotcha. I'll handle the other two, then."

    R "Let me get some snacks for us, and then we can get started."

    "You turn on some music when he gets back, and you both start working on making the patches for the haoris."

    # show sunset background
    "You don't notice time passing as you focus on making the patches."

    "Even as you work, you can't help but feel relaxed by the comfortable quiet of the room."

    "Your mind wanders as you get used to the task."

    "You think about how easy things feel when you're with Rosco and how much fun you have with him."

    "Your thoughts flit back to how close he was when he was helping you with the game."

    "For a moment, you remember how it felt to have him practically hugging you from behind."

    "You blush involuntarily, shaking your head to distract yourself."

    # show Rosco confused
    R "You good?"

    MC "Mhm."

    "He looks at you a moment longer before shrugging and getting back to work."

    # show night background
    "After a while, you notice that Rosco's being quieter than usual."

    "You look up, smirking at the realization that he fell asleep."

    MC "…"

    "Without hesitation, you pull out your phone, not noticing that the music had stopped."

    "CLICK"

    "You freeze in place, the sound of your camera going off louder than expected in the quiet room."

    # show Rosco confused
    R "Mm… What…?"

    "Rosco blinks at you in confusion, taking in the way you were holding your phone with an almost guilty expression."

    # show Rosco annoyed
    R "Did you just take a picture?"

    MC "… No."

    R "Let me see your phone."

    MC "No!"

    "You stand up and step out of reach when his arm stretches out, and you clutch your phone to your chest."

    # show Rosco shocked
    R "Get back here!"

    MC "Stay away from me!"

    "You laugh as you keep dodging his attempts to grab your phone."

    MC "I'm not going to delete it no matter what you do!"

    R "Well, you can't keep it!"

    MC "Yes, I can! You look so c—"

    "You let out a squeak before you can finish calling him cute, losing your balance as you dodge another one of his swings."

    # show Rosco shocked
    R "Woah—Hey!"

    # dark screen transition
    "You close your eyes, bracing yourself for the impact."

    "Yet instead of falling, you feel Rosco's hands on your waist, yanking you in a different direction."

    # screen shake effect
    "You open your eyes at the soft thump, blinking rapidly as you try to process what happened."

    # show Rosco CG 1
    show rosco_cg1

    R "Are you good???"

    MC "Y-yeah."

    R "Are you sure?"

    "You nod, looking down at him as you slowly realize that you were practically straddling him on his bed. Your cheeks flush involuntarily, drawing a concerned look from him."

    R "Your face is red. Are you hurt somewhere? Don't hide it if you are, goofy."

    MC "That's not it! I'm not hurt or anything, it's just…"

    R "Just what?"

    "You press your lips together, shaking your head slightly as you respond."

    MC "Just… our position is very…"

    "You can't bring yourself to finish your sentence, but he gets your point regardless."

    "He starts to blush, his gaze darting away from you."

    "Even so, his hands stay on your hips—whether it's to keep you steady or to ground himself, you can't tell."

    R "At least you're not hurt."

        # First choice after the straddling situation
    menu:
        "Move to get off him":
            MC "Yeah, thanks. Sorry about that, didn't mean to, um, trip on whatever I just did—"
            
            R "Don't worry about it. It's all good."
            
            "An air of tension permeates the room again. His eyes don't quite meet yours. When they do, your eyes flit away instinctively."
            
            MC "R-right. Well. Let me just—"
            
            "You prepare to hoist yourself off him, but his hands don't shift from your waist. His hold roots you more firmly in place, stopping your attempt to move."
            
            MC "Um, Rosco?"
            
            "Your voice comes out smaller than it'd sounded in your head. His eyes slowly meet yours, inquisitive and feline."
            
            MC "Your hands…"
            
            "As if the realization only hit him now, he immediately drops his hands to his sides, face pinching with embarrassment. You chuckle softly and move off him."
            
            "[CG END]"
            
            MC "Thanks again for, um, catching me."
            
            "For Rosco's sake, you don't address the gesture; nor do you address the mixture of emotions and red-hot mortification glowing on his face."
            
            R "'S all good."
            
            "He stands up and walks back to where he'd been working, and you follow closely behind when he mutters some kind of acknowledgement to your gratitude."

        "Tease him":
            "You pause for a moment, looking down at him. Your embarrassment fades as you take in his flushed expression."
            
            MC "Aww, were you worried about me?"
            
            "He sputters at your sudden question, refusing to meet your gaze."
            
            R "It was instinct! What was I supposed to do, let you fall?"
            
            "He scoffs quietly, but you only smirk when you notice his grip on your waist tighten."
            
            MC "Aren't you the one who laughed at Gale when he fell in the clubroom the other day?"
            
            R "Well yeah, but that was different!"
            
            MC "Different how?"
            
            R "Cause Gale's not you."
            
            MC "What's that supposed to mean?"
            
            "He lets out a groan as he pushes you off him."
            
            R "Oh, nevermind. Let's just get back to work."
            
            "[CG END]"
            
            "You sit on the bed as he gets up, staring at him as he walks away."
            
            "You can't help but be confused by his behavior, but you decide not to push him about it as you follow after him."

    # Choice ends, continue narration
    "After the little fiasco, the two of you once again fall into a comfortable silence as you finish off the patches."

    "It's well into the night when you finally stretch and push away from the table."

    MC "There! I'm done."

    R "Just in time. I finished too."

    "You watch as he gathers all the patches together, taking a moment to look over all of them."

    MC "Hey! We did a pretty good job, don't you think?"

    R "Yeah, better than I expected honestly."

    R "But what are these for?"

    # Show the gaming device and nyambie patch
    MC "Those are for you, goofy."

    "You giggle at the half-hearted glare he gives you for calling him goofy."

    MC "You mentioned that the stickers didn't have anything that really called out to you, so I figured I'd try making some."

    "You hesitate, shifting in your seat as you try to assess his reaction."

    # Second choice (reaction to his gift)
    menu:
        "Be normal":
            MC "Do you like them?"
            
            R "Of course I do! I can't believe you made these in such a short time."
            
            "You smile, relieved at his reassurance. With a shrug, you try to act like it wasn't a big deal."
            
            MC "The other ones I made were pretty simple, so I had some extra time."
            
            R "Either way, I appreciate it. Thanks!"

        "Be dramatic":
            MC "You hate them."
            
            "He blinks at your statement, taking a moment to process your words."
            
            # show Rosco confused
            R "What? No, I don't! Where did you get that from?"
            
            MC "You didn't say anything! You clearly hate them!"
            
            R "You didn't even wait ten seconds for me to respond!"
            
            # show Rosco annoyed
            R "…"
            
            "He pauses, narrowing his eyes at you. You feel your lips twitch. After a moment, you burst out laughing."
            
            R "You're ridiculous, you know that?"
            
            "He rolls his eyes at you, shaking his head as he flicks your forehead."
            
            MC "You should've seen your face!"
            
            R "Yeah, yeah. Whatever."

    # Continue narration
    R "It's getting late. You should head home."

    MC "We still need to put the patches on."

    R "I'll handle it tomorrow."

    MC "Are you sure?"

    R "Yeah, it's not too much work. Besides, I feel like you'd burn yourself."

    MC "I am NOT that clumsy."

    "He laughs at your immediate protest, guiding you out of his room."

    # Third choice (leaving or staying)
    menu:
        "Go home":
            MC "Alright, I'll see you later then."
            
            R "Did you drive here?"
            
            MC "Nah, I took the bus. But I checked the schedule, and there's another one coming soon."
            
            "He makes a face, almost as if he was offended by your statement."
            
            R "I'll drive you, c'mon."
            
            MC "No, it's fine—"
            
            R "Don't argue."
            
            MC "… Okay."
            
            "You smile as he opens the door, gesturing for you to walk to the car."
            
            MC "Thanks, Rosco."
            
            R "Don't mention it."
            
            "The drive home is peaceful, your conversation bouncing around different topics until he drops you off."
            
            "You wave as he drives away, grateful to be home so quickly. Once his car is gone, you head inside with a yawn."

        "Stay longer":

            "You pause before you reach the door, glancing at him with a slight smirk."
            
            MC "Are you planning on sleeping soon?"
            
            R "Probably not. Why?"
            
            MC "Wanna watch a movie?"
            
            R "Now? Aren't you tired?"
            
            MC "Not really. I woke up late today, remember?"
            
            "He mulls over your suggestion before giving in with a shrug."
            
            R "Alright, sure. But don't complain to me if you're tired tomorrow."
            
            MC "No promises."
            
            scene black with fade
            "You accept the blanket he hands you, wrapping it around yourself as he puts a movie on."
            
            "You settle down on the comfortable sofa, finding it easy to relax with Rosco beside you."
            
            "Even if you did find yourself tired tomorrow, you knew you wouldn't have any regrets."
    #Choice End

    return
