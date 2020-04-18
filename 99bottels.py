#This python code prints the 99 bottles song upto the user defined range.
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.

import time
plural="bottles"
singular="bottel"
num=int(100)
range_value=int(input("Enter the number of beer you want to take down:"))
song="{} {} of beer on the wall,{} {} of beer. Take one down, pass it around, {} {} of beer on the wall"
for x in range(range_value):
    time.sleep(0.5)
    if x < 99:
        print(song.format(num,plural,num,plural,num-1,plural))
    elif x == 99:
        print(song.format(num,singular,num,singular,num-1,singular))
    else:
        print("Buy some more beer")
    num-=1
    