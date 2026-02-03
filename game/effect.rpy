transform featherspin:
    xpos 0.5
    ypos 0.5
    linear 3 rotate 180 # take 1 second to rotate 360 degrees
    rotate 0 # reset position counter
    repeat
image cherry_blossom_leaves_blowing = Fixed(
    SnowBlossom(At("gui/effect/cherry_blossom_leaf.png", featherspin), count=45, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("gui/effect/cherry_blossom_leaf_big.png", featherspin), count=5, xspeed=(200, 20),horizontal=True),
    )
