from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap


def draw_this(phrases):
    cordinates = [70, 350, 860]
    for x in range(0, 3):
        if int(len(phrases[x])) > 10:
            print(int(len(phrases[x])))
            if 40 > int(len(phrases[x])):
                lines = textwrap.wrap(phrases[x], width=int(len(phrases[x]) / 2))
            else:
                lines = textwrap.wrap(phrases[x], width=int(len(phrases[x]) / 3))
            if int(len(phrases[x])) > 125:
                font_size = 30
            else:
                if x == 1:
                    font_size = 90
                else:
                    font_size = 50
        else:
            print(int(len(phrases[x])))
            lines = [phrases[x]]
            if int(len(phrases[x])) < 10:  ## Could turn this into a list but might safrific readbalility?
                font_size = 150
            elif int(len(phrases[x])) < 25:
                font_size = 100
            elif int(len(phrases[x])) < 30:
                font_size = 70
            else:
                font_size = 50

        y = cordinates[x]
        for x in range(0, len(lines)):
            Font = ImageFont.truetype("font.ttf", font_size)
            width, height = Font.getsize(str(lines[x]))
            draw.multiline_text(((1080 - width) / 2, y), lines[x], (0, 0, 0), font=Font, align="center")
            y += height

def choose_string():
    this_phrase = str(input("What phrase do you want for number " + str(x)))
    if len(this_phrase) > 125:
        print("that string is too long")
        return None
    else:
        return this_phrase

##main
finish = False
number_made = 0
while finish != "Done":
    img = Image.open("template.jpg")
    draw = ImageDraw.Draw(img)
    phrases = []
    for x in range(3):

        this_phrase = str(input("What phrase do you want for number " + str(x)))
        if len(this_phrase) > 125:
            print("Warning: that is a long string it might not look great")
        phrases.append(this_phrase)

    draw_this(phrases)
    img.save('output'+ str(number_made) + '.jpeg')
    img.show()
    finish = str(input("Input Done if you are finish or anything else to make another one"))
    img.close()
    number_made += 1
