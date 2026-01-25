# Plays ONLY when the portrait first appears
transform portrait_enter:
    alpha 0.0
    xoffset 24
    ease 0.25 alpha 1.0 xoffset 0

# Plays when the image inside changes (expression swap)
transform portrait_swap:
    alpha 0.0
    ease 0.15 alpha 1.0

transform portrait_swap_talk:
    # First run the swap fade
    alpha 0.0
    ease 0.15 alpha 1.0

    # Then run the talking bounce
    yoffset 0
    ease 0.08 yoffset -6
    ease 0.08 yoffset 0

screen portrait(
    img,
    crop_x=0,
    crop_y=0,
    crop_w=400,
    crop_h=400,
    xalign=0.9,
    yalign=0.85
):

    frame:
        xalign xalign
        yalign yalign
        padding (6, 6)
        background Solid("#00000080")

        # The frame animates ONLY on first show
        at portrait_enter

        # The image inside handles expression swaps
        add Crop(
            (crop_x, crop_y, crop_w, crop_h),
            img
        ) at portrait_swap_talk