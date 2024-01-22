from turtle import *
from PIL import ImageGrab

title("Jai Shree Ram")
bgcolor("black")
pensize(8)
pencolor("ORANGE")
ram_jap = ["जय श्री राम"] * 60
angle = 360/50
penup()
sety(-1)
for _ in range(51):
    left(angle)
    forward(260)
    if ram_jap:
        write(ram_jap.pop())
    back(260)

penup()
goto(-40, -20)
pendown()
write("जय श्री राम  ଜୟ ଶ୍ରୀ ରାମ", font=("Arial", 15, "normal"))  

penup()
goto(-window_width()/2 + 10, -window_height()/2 + 10)
pendown()
write("Created By: Ramakrushna", font=("Arial", 10, "normal"))

screenshot = ImageGrab.grab(bbox=(int(-window_width()/2), int(-window_height()/2), int(window_width()/2), int(window_height()/2)))
screenshot.save("jai_shree_ram.gif")

done()
