#imports
from PIL import Image
import random

###Generate a Color###

#a list of rgb color codes
colors = [(26, 188, 156),(46, 204, 113),(39, 174, 96),(22, 160, 133),(52, 152, 219),(41, 128, 185),(155, 89, 182),(142, 68, 173),(52, 73, 94),(44, 62, 80),(230, 126, 34),(211, 84, 0),(231, 76, 60),(192, 57, 43)]

bg = Image.new('RGB', (800, 800), random.choice(colors)) #choose a random number out of the list


#add Logo

#Logo Black
#logo = Image.open("logoblack.png") #logo image size need to be 128x128
#Grey, Alpha = logo.split()

#White Logo
logo = Image.open("logowhite.png") #logo image size need to be 128x128
Red, Green, Blue, Alpha = logo.split()


bg.paste(logo, (660, 672), Alpha)
bg.save("bg.png")


#GET a random quote

#put Quote on the picture

#save final pictutre