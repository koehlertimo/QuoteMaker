#imports
from PIL import Image, ImageDraw, ImageFont
import random
import shutil, os
import csv

#Variables
img = None
sessions =  0
(x, y) = (400, 400)
message = ""
count = 0 
textcolor = (255, 255, 255)
font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
draw = None

#Intro
print("#" * 10)
print("Quote Maker")
print("#" * 10)
print("Which text do want to put on this Picture?")
message = input(":")
print("How much Quotes do you want to generate?")
sessions = int(input(":"))
print("Message:" + message)


while count != sessions:
    count = count + 1
    print(str(count) + ". Image in process")

    ###Generate a Color##
    #a list of rgb color codes
    colors = [(26, 188, 156),(46, 204, 113),(39, 174, 96),(22, 160, 133),(52, 152, 219),(41, 128, 185),(155, 89, 182),(142, 68, 173),(52, 73, 94),(44, 62, 80),(230, 126, 34),(211, 84, 0),(231, 76, 60),(192, 57, 43)]

    img = Image.new('RGB', (800, 800), random.choice(colors)) #choose a random number out of the list


    #Logo Black
    #logo = Image.open("logoblack.png") #logo image size need to be 128x128
    #Grey, Alpha = logo.split()

    #White Logo
    logo = Image.open("logowhite-64x64.png") #logo image size need to be 128x128
    Red, Green, Blue, Alpha = logo.split()
    img.paste(logo, (730, 736), Alpha)


    print("created Background")

    draw = ImageDraw.Draw(img)
    draw.text((x, y), message, fill=textcolor, font=font)

    print("Text on Image placed")

    filename = "Quote" + str(count) + ".png"
    img.save(filename)
    shutil.move(filename, 'img')
    print("File saved and moved to 'img' Folder ")

print("\n")
print("\n")
print(str(count) + " images succsesfully created")


