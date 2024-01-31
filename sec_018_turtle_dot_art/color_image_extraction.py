import colorgram

colors = colorgram.extract("sec_018_turtle_dot_art/color_dot_art_damien_hirst.png", 30)
color_pallet = []
for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_color = (r, g, b)
    color_pallet.append(new_color)

print(color_pallet)

