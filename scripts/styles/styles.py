from scripts.iconsNconst import inc
font_size = str(int(inc.win_w * 0.0159325))
if int(font_size) < 17:
    font_size = "17"

stylef = """
    .button {
        font-size:""" + font_size + """px;
    }
    .label {
        font-size:""" + font_size + """px;
    }
"""

style = bytes(stylef, encoding="utf-8")
