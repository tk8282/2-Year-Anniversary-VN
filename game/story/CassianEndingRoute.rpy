label cass_ending_route:
    scene bg stalls
    play music "audio/music/G1 - Cheerful (2).wav" fadein 1.0 loop
    "Free from your crepe making and customer service purgatory, you drape yourself onto a nearby bench and release a heavy sigh."
    "It's finally your break time, and you're able to do whatever for the time being. From your seat, you take time to observe the spring festival in full swing. The several stalls lining the walkway pique your interest. Maybe you should go check them out!"
    "With a new goal in mind, you stand and dust yourself off, ready to conquer whatever this festival throws at you."

    C "[player_name]!"

    #play music "audio/music/E1 - Cass.wav" fadein 1.0 loop
    
    "Apparently, it decides to throw {i}him{/i} at you."
    show Cassian fullbody at fullbody_center with dissolve
    "You stop in your tracks and turn to find Cass amidst the falling leaves and soft breeze of the wind. He stands a few feet away from you, smiling with his hands in his pockets."

    MC "Cass! You're here."

    C "Duh. This is our school festival."

    "You frown at the smirk on his face. Why must this man be so sassy?"

    MC "I meant in front of me. Why are you looking for me?"

    hide Cassian with dissolve

    # [Choice Start]

    menu:
        "Do you need me?":
            $ player_choice = "need-me"
        "Do you miss me?~":
            $ player_choice = "miss-me"

    show Cassian fullbody at fullbody_center with dissolve

    if player_choice == "need-me":

        MC "Do you need me?"

        show Cassian relieved fullbody at fullbody_center
        C "I do."

        show Cassian relieved fullbody at fullbody_center, zoomin4
        pause 1.0
        hide Cassian
        show Cassian relieved at waist_up_center
        "He takes the steps necessary to get closer to you, and the distance closes. He holds unwavering eye contact, tilting his head ever so slightly as you lock gazes."
        

        "Suddenly, it feels like there's hardly any space to breathe."
        "Wasn't it spring? Why did it feel a little hot?"

        C "I need you for a lot of things."

        "That's... worded pretty..."
        "{i}Ah! Get it together! He's talking about the festival, you idiot!{/i}"

        MC "Hm? How much else is needed for the stand?"

        "You thought you'd taken care of everything. Then again, this {i}was{/i} pretty rushed."
        "Maybe you missed a few things."

        show Cassian neutral at waist_up_center
        C "Well..."

        "You blink at him owlishly"
        "It seems like he's lost the flow of his words, because as you continue to stare at him, he gets more and more tongue-tied."

        show Cassian soft at waist_up_center
        C "Actually—"

    elif player_choice == "miss-me":
        show Cassian fullbody at fullbody_center, zoomin4
        pause 1.0
        hide Cassian
        show Cassian neutral at waist_up_center
        MC "Do you miss me?~"
        show Cassian extreme blush at waist_up_center, pop
        "You let a teasing smile grow on your face, watching his slowly reddening face with slight fascination."
        "Even the tips of his ears are red!"
        "You can't help but laugh at his strong reaction."

        MC "How cute~ You can say you miss me, you know?"

        show Cassian soft at waist_up_center
        C "Shut up, man."

        "He runs his hands over his face and turns away from you. From the movement of his shoulders, it looks like he's taking deep breaths."
        show Cassian at waist_up_center
        "Then, he turns around just as swiftly with his composure all collected, like a completely different person."

        show Cassian smug at waist_up_center
        C "Yeah."

        "???"

        MC "Huh."

        "He shrugs nonchalantly, the very opposite of his reaction just a minute ago."

        C "Yeah."

        "Is this guy serious right now?"

        MC "You miss me?"

        C "Yeah."

        MC "{i}You miss me?{/i}"

        show Cassian confused at waist_up_center
        C "Yeah???"
        show Cassian bruh at waist_up_center
        C "You wanna hear it in German? Ja."

        "It takes you a bit to respond. Once everything is processed in your head, you let out a laugh and lightly punch his shoulder."
        "Wow! You almost thought he meant that in a way that was completely different from being just friends!"

        MC "Alright. Quit the bullshit. What do you need me for?"

        show Cassian disappointed at waist_up_center
        "He frowns and grumbles about something under his breath. You try to strain your ears to hear, but he quickly switches the topic before you can even ask about it."

    # [Choice End]
    show Cassian neutral at waist_up_center
    C "You said you'd hang out with me during your break, remember?"

    MC "Ohhhh, right. No yeah, definitely remembered that!"

    "You quickly spit out the assurance because the last thing you need is to give this guy more ammo to tease you for."

    show Cassian bruh at waist_up_center
    C "Mhm... Well, whatever. That's not what I wanted to ask you."

    show Cassian neutral at waist_up_center
    C "Do you remember the promise I made to you when you helped me out with the equipment?"

    MC "Promise?"

    "Had he made a promise? All you can remember is teasing him, losing the paper, teasing him some more, buying the equipment, teasing him a bit more, and the clubroom..."
    "... And everything that happened after that."

    MC "Ahem! Uh! W-what promise?"

    "He rolls his eyes at you, like the attitude king he is, and takes a hold of your hand while tugging gently."
    stop music fadeout 1.0
    C "Follow me."
    
    show Cassian winking at waist_up_center
    C "I'm about to show you magic."
    hide Cassian with dissolve

    "What kind of stupid catchphrase is \"magic\"?"
    "... Is what you want to say until you reach the place where it had all started with him."
    play music "audio/music/G5 - Romantic.wav" fadein 1.0 loop
    scene bg cass garden flowers with fade
    "And oh wow, it really is magic."
    "With the flowers finally blooming, color fully exploded within the garden he's cultivated for who knows how long."
    "There are rows of pinks and yellows and blues dotted all around the bushes, bringing life and an audience to the dancing currents of the water fountain."
    "It's like watching a live reenactment of a fantasy anime. All it needs left is a handsome elf singing sweet serenades to seal the deal."

    MC "Cass, it's beautiful!"

    "You're sure your eyes are sparkling as you take in the view. From behind you, you can hear a chuckle coming from the caretaker of the garden."
        
    show Cassian soft at waist_up_center with dissolve
    C "I told you. When the flowers finally bloom, you'll be the first to see."
    C "I've... never really brought anyone else in here. Or at least, in the heart of the garden."
    C "Especially when everything is perfectly aligned like this with the flowers, the fountain, and the falling leaves."

    MC "So I'm the first?"

    "Your smile has to be especially bright because as you direct your joy to him, he seems awestruck."
    "He walks closer to you and very shyly takes your hand into his."

    C "You're my first in a lot of things, [player_name]."

    "The side-eye you throw at him is bombastic."

    MC "Should we rephrase that?"

    show Cassian confused at waist_up_center
    C "How would you rephrase it, huh?"

    MC "Any other possibilities, dawg."

    show Cassian bruh at waist_up_center
    C "Fine, how about, \"Wow [player_name], I so dearly cherish our time together and the valuable memories we've made together so far.\""
        
    MC "Can't you be nice to me for once?"

    show Cassian confused at waist_up_center
    C "I've been nice to you!!!"

    MC "Oh yeah? Like when?"

    show Cassian smug pose2 at waist_up_center, pop
    C "Pick any moment in the two days we spent together gathering the equipment for the stand. That's when I've been nice to you."
    show Cassian smug at waist_up_center

    MC "Sure, sure, whatever you say. Hmmm, how about..."

    hide Cassian with dissolve

    # [Choice Start]
    menu:
        "Corny Pick Up Lines":
            $ cassRomantic = True
        "Cassian Floros Crashout of the Century":
            $ cassRomantic = False
    
    show Cassian smug at waist_up_center with dissolve
    if cassRomantic == True:
        MC "When you threw a bunch of corny lines at me???"

        
        C "Corny lines??? Okay. For your information, I was flirting with you—"

        MC "Wait, you were flirting??"

        show Cassian confused at waist_up_center
        C ".{w=0.3}.{w=0.3}.{w=0.3} Yes?"

        "He stares at you stunned, a pregnant pause hanging in the air between the two of you."

        C "What did you think I was doing???"

        MC "I thought you were crashing out??? Bro, you were tweaking. It was lowkey concerning."

        show Cassian upset at waist_up_center
        C "You..."

        "He turns away from you and looks up to the sky, fists clenching and an expression of disbelief on his face. When he looks back at you, he's staring at you like you killed him in {i}Chicken Chicken Goose{/i}."

        show Cassian suspicious at waist_up_center
        C "You didn't get my message at all??"

        MC "What message??? You called me a dog!!"

        show Cassian panic at waist_up_center, pop
        C "I did not?! Well—I guess, but that's not what I meant!!"

        MC "How did you mean it then?? 'Cause all I got was that I'm A DOG!"

        "The two of you stare at each other silently. Your mind proceeds to ponder the deeper meaning of Cass' dog comment but, unfortunately, the subtext avoids you like the plague."
        "On the other side of the stand off, Cass glares right at you. He searches your face for a sliver of its usual teasing but, just as unfortunately, the man is stunned to find you are not joking. Bro really threw all his greatest pick up lines at you only for them to come back and incorrectly kick his ass... Nice going!"
        show Cassian extreme blush
        "Stuck between your puzzled gaze and the consequences of his actions, Cass flushes in embarrassment. There goes his awesomely cool, nonchalant plan..."

        C "I meant—You're cute, okay!"
        C ".{w=0.3}.{w=0.3}."

        "Haha wow, are your ears going bad? Is old age getting to you already?? No, seriously 'cause what did Cassian motherhecking Floros just say to you??"

        MC "I'm WHAT."

        # play sound effects of a breeze and wild west sounds
        play sound "audio/sfx/western-wind.ogg"
        "A breeze passes by you two. Distantly, you might hear the sound of tumbleweeds. You're not even in the wild west."

        C "Nevermind, I—Let's get back to the stand—"

        "You can't even get a word out before he spins the other way and speed-walks towards the exit of the garden."

    elif cassRomantic == False:
        MC "When you lost your marbles because of the list?"

        show Cassian confused at waist_up_center
        C "What???"
        C "I did {i}not{/i} lose my marbles."

        MC "Are you sure...? Weren't you, like, on the floor crying?"

        show Cassian panic at waist_up_center, shake2
        C "WHAT."

        show Cassian angry at waist_up_center, pop
        C "HELLO? When did I ever get on the floor?? Even during that one club meeting when the rest of you decided it would be funny to make snow angels from the dust on the ground, I didn't join in. Why would I cry on the floor??? Why would I cry over the list?!?! Why would I—"

        MC "Okay damn, I'm sorry. Defensive, much?"

        show Cassian suspicious pose2 at waist_up_center
        C "When you insult my honor like that I have to defend it."

        "This time, he throws YOU a criminal offensive side-eye."
        "Who does this man think he is?"

        MC "Hey, I protect your honor too."
        MC "Sometimes."

        show Cassian bruh at waist_up_center, pop
        C "You hate me."

        MC "I literally do not—Don't you remember my super sugoi speech uplifting you and stuff?"

        show Cassian upset at waist_up_center
        C "Well, I don't know if I'd use the word \"speech\"..."

        MC "Shut up. Be grateful."

        "Eventually, you two burst into giggles, previous arguments forgotten. His smile softens a bit, gaining a more serious look in his eyes."

        show Cassian laughing at waist_up_center, pop
        C "Of course I remember. I think that's the nicest thing you've said to me in our entire time of knowing each other."

        MC "Hey—"

        show Cassian neutral at waist_up_center
        C "I'm joking."
        show Cassian soft at waist_up_center
        C "Thank you for your friendship and unending support."
        C "I meant what I said back then, about how I'll always cherish our memories together."

        MC "You speak like we're not gonna be friends anymore in the future."

        show Cassian smug at waist_up_center
        C "Of course not."

        "He gives you a cheeky grin, leaning forward with malicious intent."

        show Cassian smirking at waist_up_center
        C "We're gonna be besties for the resties of our life-sies."

        MC ".{w=0.3}.{w=0.3}."

        "As you stare at the mischievous expression on his face, the realization of his words hit you. He essentially just called you his best friend."
        "You feel a growing urge to..."

        # !slight! zoom into cass
        show Cassian smirking at slightzoominnout
        # add chomping sfx screenshake
        pause 0.5
        play sound "audio/sfx/chomping.ogg"
        with hpunch
        pause 0.5
        
        show Cassian panic at waist_up_center, shake2
        
        C "!!!!"
        C "What the hell???"
        show Cassian panic at waist_up_center, zoomout_jump, singlejump
        pause 1.0
        # zoom out faar + jump to fullbody?
        "He jumps back an insane amount, the distance growing comedically fast with just one action."
        "Guess he doesn't like friendly biting."

        C "Why did you just bite my cheek?!"

        MC "Sorry. Cuteness aggression."

        show Cassian confused
        C "For humans...????"

        MC "I can do it again to prove it—eh?"

        "He doesn't say anything in response, but that might be the quickest you've ever seen him run away from you."

    # Choice end
    hide Cassian with easeoutright
    "Is he just… leaving you here?!"
    "Oh, hell no!"

    MC "Cassian Floros!!!!"
    stop music fadeout 1.0
    "You run after him immediately, taking a hold of his arm and forcefully turning him towards you."
    # first CG
    play music "audio/music/E1 - Cass.wav" fadein 1.0 loop
    window hide
    $ quick_menu = False
    scene CG Cass 2 with fade
    pause 2.0
    $ quick_menu = True
    "He looks at you with a bright flush on his face as unshed tears twinkle in his eyes, feeling incredibly caught off guard. The breeze passes by again, catching his ponytail in the wind."
    "Like this, among the flowers and falling petals, he looks…"
    show cherry_blossom_leaves_blowing
    "Like this, among the flowers and falling petals, he looks..."
    "Almost like the main character of a shoujo manga."
    scene bg cass garden flowers with fade
    show Cassian extreme blush at waist_up_center with dissolve
    show cherry_blossom_leaves_blowing

    if cassRomantic == True:
        MC "There's no way you're leaving like this after revealing you'd been flirting with me for who knows how long?! You bum!!!"
        MC "First, you take me to a special place that apparently no one else has been in??"
        MC "Second, you make me laugh {i}all the damn time{/i}!! I don't think there's been a day that has passed where I didn't smile because of you!"
        MC "Third, you pull a bunch of weird rizz lines on me, half of which I couldn't tell were actually real or not—"
        MC "AND THEN you do some weird freak shit and you pin me to the ground!!"

        show Cassian panic at waist_up_center, pop
        "A shocked expression passes over Cass as he watches you, more or less, scold him for all he's worth, yet he can't help as that familiar warmth bubbles in his chest as he looks at you."

        MC "Every single sign you've shown is just!! So mixed!! Not just friends, not just clubmates, not platonic at all!! But I can't even ask because you keep {i}running away{/i}."

        "Unconsciously, your face scrunches in pure desperation and panic, your body nearly curling into itself as you hang onto Cass. Here you are, spilling your whole heart out to one of your best friends who can't even bring himself to say anything to you."
        "Of all the people... you really had to choose this one, huh?"

        MC "Be more straightforward with me, Cassian Floros."

        "You lift your head to meet Cass. Wide, disbelieving hazel eyes stare back at you. Even now, you couldn't understand a single thing going through that stupid head of his."

        MC "I really, {i}really{/i} like you."

        "Each syllable felt like weights on your tongue, begging to stay hidden instead of left out in the open spring."

        MC "Do you like me too?"

        "Cass stares at you incredulously, short, and unsure sounds leaving his mouth. They barely sound coherent. To be honest, you can't even hear them over the sound of your own heartbeat."

        C "I..."
        show Cassian soft at waist_up_center
        "A smile breaks out on his face and he shakes his head, unable to even look at you in his stunned stupor."

        C "You really... never fail to surprise me, huh, [player_name]?"

        "The smile on his face turns gentle, much softer than any he's shown so far. Rays of sunshine perfectly highlight each feature of his. The same ones you've admired many, many times before."
        "If he didn't blend in with the petals and flowers in the garden back then, he definitely does now."
        "He's beautiful."
        "But—"

        MC "You dumbass... That's not an answer?!"

        show Cassian confused at waist_up_center
        C "Well, what do you want me to say to that?!"

        MC "YES????"
        MC "Or, I don't know, an \"I like you too\" would be nice?? But fuck me, I guess."

        "You try your best to maintain a piercing glare at Cass, but his clueless and close-to-laughter face makes you break character before you can actually take this whole situation seriously."

        show Cassian laughing at waist_up_center, pop
        C "You're not actually gonna make me say it, are you?"

        MC "Stop laughing!! Yes, I'm making you say it!! Hello??"
        MC "Unless you want to just turn around and run away again. Whatever."

        "This time, it's your turn to let go of him and turn away, crossing your arms in front of your chest and feigning indifference. You hear a soft laugh before your wrist is gently taken into a warm grasp, fingers slowly intertwining with yours."

        show Cassian soft at waist_up_center
        C "[player_name]?"

        "His free hand tilts your chin over to face him again, but it doesn't leave your face. It rises to rest on the skin of your cheek—and you let yourself relax into his hold."

        C "I won't run away this time."
        C "I like you too."
        C "Tragically.{w=0.3} Devastatingly.{w=0.3} Any other advanced English word I probably can't pronounce, but I'll try to—"

        MC "You're so unserious."

        C "I mean it!!"

        "The two of you laugh, the melodies of your voices twinkling in the passing breeze."

        show Cassian relieved at waist_up_center
        C "No—I do mean it, though. Trust."

        MC "You like me back?"

        C "Mhm."

        MC "Are you sure?"

        show Cassian smirking at waist_up_center
        C "Did my flawless rizz not convince you of that the last time we met?"

        MC "You mean the sad attempts you tried before we got locked in the storage room?"

        show Cassian disappointed at waist_up_center
        C "... Don't call them sad."

        "The shifting of his expression and how he takes his hand off your face instantly makes you laugh again. It's easy to feel so light and free, giddy at the situation you're both in."
        "Maybe also because you're experiencing this with {i}him{/i}."

        MC "I'm sorry."

        "You take his hand again and match it with yours—fingers intertwined and palms closely locked together."

        MC "I'm happy. I swear."

        show Cassian soft at waist_up_center
        C "You better be."

        "A smile blooms on Cass' face, chasing away all the doubts and worries you had. Right now, all you can focus on is him: the way his eyes look at nothing but you even as colorful petals float in the wind; how sweaty and shaky his hands are, but they still hold yours snugly."
        "Man, this guy is kinda whipped."
        "Alas, it's a mutual curse."

        MC "Sooooo, does this mean we're a thing now?"

        "You feel like bouncing on the balls of your feet. How could the past few minutes be real? Even now, seeing the huge blush covering his face feels like a dream."

        show Cassian extreme blush at waist_up_center
        C "I—well, I would think so?"

        MC "You just think so? You're making me kind of sad here, Cass."
        MC "I mean, we had that whole shoujo romance confession, but we might not be a couple now? How you hurt my heart, Cassian Floros."

        "Pulling out your inner theater kid that you had discussed in detail about with Zanny in the past, you slowly let your hands fall away from his with a heartbroken expression on your face. It's only exaggerated with your over-the-top sniffling and backwards lean."
        "Cass looks like he can hardly tell if you're serious or not."

        show Cassian panic at waist_up_center, pop
        C "W-WHAT?"
        C "I just don't want to rush into things! I mean, if you're ready, sure! But—"
        show Cassian disappointed at waist_up_center
        "He grumbles in a frustrated manner, hands going through his hair and even messing up his locks. He goes through numerous expressions as he wrangles his thoughts into something communicable."

        show Cassian extreme blush at waist_up_center, pop
        C "If you want to put a label on it, then we're dating! We're a couple! God, you need to stop teasing me."

        "You tilt your head back to Cass, satisfied with all your teasing. You sway yourself back to his side, admiring the beauty that is a madly blushing and embarrassed Cassian Floros."

        MC "Awww, you'll have to forgive me, y'know! You're just so cute when you're embarrassed. I can't help myself!"

        "Speaking in your sweetest voice, your hand moves up to Cass' burning face. You feel your mouth turn to a soft grin as you gaze at your (now official!) partner."
        "Flustered, Cass darts his eyes away to the floor, suddenly realizing the immeasurable beauty of rectangle tiles... yeah, exactly that."

        C "Mhmm..."

        "Goodness, this guy really is too adorable."
        "As softly as you can, like handling a spooked deer, you cradle his cheek in your palm and begin patting Cass in repetitive motions."
        show Cassian soft at waist_up_center
        "While he keeps his furrowed brow and avoids your playful stare, Cass leans into your hand as if the curve was made just to hold him. You cheer inside as you watch Cass begrudgingly accept the gesture."

    elif cassRomantic == False:
        MC "Sorry—Did the bite hurt though, like actually?"
        
        show Cassian confused at waist_up_center
        C "N-no?? No, I don't know what you're talking about—"

        MC "Oh shit, it really hurt, huh."

        show Cassian angry at waist_up_center, pop
        C "NO."

        "Although you feel bad for hurting him, you can't help but laugh at the expression on his face."
        "He looks like a bullied child who'll go tattling to his mother."
        "You're filled with the urge to console but also tease him."

        MC "There, there~"

        "You lift a hand to pat his bitten cheek like petting a whimpering dog."
        "Oh, how the tides have turned."

    show Cassian thinking at waist_up_center
    "After a while, Cass starts to awkwardly squirm in place. He doesn't seem to know what to do with the affection you're giving him, if you can even call it affection."

    show Cassian upset at waist_up_center
    C "You can stop now..."

    MC "Why? Are you sure??"

    C "Yes, you're acting like a weirdo."

    MC "Aww~ I'm just consoling the club's little baby boy—"

    "He slaps your hand away with a resounding smack. That's easily the meanest glare you've earned from him without mentioning the act of stealing his {i}Pipmon{/i} cards."

    show Cassian angry at waist_up_center, pop
    C "Don't call me that again."

    MC "I'm sure the others would agree. You're definitely the baby boy of the club."

    C "I am NOT the baby boy of the club."
    C "That's Rosco!!"

    MC "He'd get mad at you for that... but to be honest, I agree too."
    "You pinch his cheek, watching as the skin between your fingers turns a deeper red. The little part of your brain demanding some mischief cheers at your actions."

    show Cassian confused at waist_up_center
    C "What the—"

    MC "You can both be baby boys. I'll tell the rest of the guys later."

    show Cassian suspicious at waist_up_center
    C "You're not making that official."

    MC "Ummm, says who?"
    hide Cassian with dissolve
    show screentint with dissolve
    "Before he can get a word out in defense of himself, you bolt out the garden immediately. You hear a garbled shout behind you, likely Cass trying to get you to come back."
    "Funny how you're the one running now but not from embarrassment and fear."

    scene bg stalls 
    show screentint
    with fade

    if cassRomantic == True:
        "Instead, butterflies flap in your chest and the spring wind flies through your hair."
        hide screentint with dissolve
        "The stands enter your view, and you're reminded that you'll soon reunite with the rest of your friends too."
        "Only now, you and Cass will share lingering touches, shy glances, and soft smiles. You'll seek each other's company—each other's warmth—in a way no one else can offer."
        "Yes... no one but you two know the intimacy you've shared and will continue to have."
        "Really, it was only a matter of time until you both found your rightful places in the world."
        "Always, {i}always{/i} with each other."
    
    # [Romantic Cass Route End!] 

    elif cassRomantic == False:
        hide screentint with dissolve

        "Now, you're running towards the stands, towards the other guys you hold to close your heart."
        "The group you can now call family."

        show Cassian angry pose2 at waist_up_right with dissolve
        C "You're not gonna convince them to make it official!!"

        MC "Watch me, bitch!!!!"
        hide Cassian with dissolve

        "Though he throws profanities your way as well, you know he meant what he said earlier."
        "This friendship will last a lifetime."
        "Besties for the resties of your life-sies."
    
    "End of Cass Ending"
    stop music fadeout 1.0
    # jump back to general end