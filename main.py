from vpython import * #import vpython library

t = text(text = "Congrats! You've installed it all!") #display congrats text
t.pos.x = -2 #move text to the left
s = sphere(pos = vector(-7.5, 0, 0), radius =5, texture = textures.earth) #display earth

while True:
    rate(10) #rate of rotation
    s.rotate(angle = 0.05, axis = vector(0, 1, 0)) #rotate earth

