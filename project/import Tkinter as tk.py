from tkinter import *
from tkinter import messagebox
from turtle import Turtle
import random
from PIL import ImageTk,Image

master = Tk()


type1 = " "
quality1 = 1
rate1 = 1
energy1 = 1


def powerplant():
    t.goto(0,200)
    t.pendown()
    t.setheading(0)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.goto(20,200)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(30)
    t.penup()

def house(x,y,size):
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.goto(x+size/2,y+size/2)
    t.goto(x+size,y)
    t.penup()

def houses(x,y,size):
    house(x,y,size)
    house(x+40,y+20,size)
    house(x-30,y+10,size)

def building(x,y,size):
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.forward(10)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.penup()

def buildings(x,y):
    building(x,y,120)
    building(x+10,y,100)
    building(x+30,y,110)

def run():
    global type1
    t.pencolor("orange")
    if(type1=="Centralized"):
        t.goto(0,200)
        t.pendown()
        t.goto(-200,0)
        t.goto(0,200)
        t.goto(0,0)
        t.goto(0,200)
        t.goto(300,0)
        t.penup()
    if(type1=="Decentralized"):
        t.goto(-300,0)
        t.pendown()
        t.goto(300,0)
        t.penup()
    if(type1 =="Distributed"):
        t.goto(0,200)
        t.pendown()
        t.goto(-200,0)
        t.goto(0,200)
        t.goto(0,0)
        t.goto(0,200)
        t.goto(300,0)
        t.penup()
        t.goto(-300,0)
        t.pendown()
        t.goto(300,0)
        t.penup()
    t.pencolor("black")


    global quality1
    quality1 = 11-quality1
    chance = random.randint(50,100)
    stands = False
    if(chance%(quality1*2)==0):
        stands = True

    global rate1
    rate1 = 11-rate1
    chance = random.randint(50,100)
    hit = False
    if(chance%(rate1*2)==0):
        hit = True

    global energy1
    energy1 = 11-energy1
    chance = random.randint(50,100)
    demand = False
    if(chance%(energy1*2)==0):
        demand = True

    if(hit and stands):
        print("You were saved by strong infrastructure")

    if(hit and not stands):
        print("You lost power")

    if(not hit):
        print("You were not hit by a storm")

    if(hit and not stands and demand):
        print("You lost power when it was needed")

    if(hit and not stands and not demand):
        print("You lost power but there was low energy demand at the time")



    funds = 3
    if(type1 == "Decentralized"):
        funds = funds - 1
        if(hit and not stands):
            print("A moderate amount people were affected")
    if(type1 == "Distributed"):
        if(hit and not stands):
            print("A small amount of people were affected")
        funds = funds - 2
    if(type1=="Centralized" and hit and not stands):
        print("Most people were affected")
    if(quality1 <= 5):
        funds = funds - 1

    print("You have " ,funds, " funds left (out of 3 possible)")
    print("The amount of funds determines how well you will recover if a storm happens.")


    print("================")



def submit():
    t.clear()
    global type1
    type1= types.get()
    global quality1
    quality1 = qualityList.get()
    global rate1
    rate1 = disaster.get()
    global energy1
    energy1 = currentEnergyList.get()
    powerplant()
    houses(0,0,10)
    houses(-300,0,30)
    buildings(300,0)
    run()


type = Label(master, text="What is the type of grid arrangement?")
type.grid(row = 0, column = 0, sticky = W, pady = 2)
types = StringVar(master)
types.set("Centralized")
quality = OptionMenu(master, types, "Centralized", "Decentralized", "Distributed")
quality.grid(row = 1, column = 0, sticky = W, pady = 2)

qualityLabel = Label(master, text="Quality of infrastructure? (1-10)")
qualityLabel.grid(row = 2, column = 0, sticky = W, pady = 2)
qualityList = IntVar(master)
qualityList.set(1)
quality = OptionMenu(master, qualityList, 1,2,3,4,5,6,7,8,9,10)
quality.grid(row = 3, column = 0, sticky = W, pady = 2)

rate = Label(master, text="What is the rate of natural disasters? (1-10)")
rate.grid(row = 4, column = 0, sticky = W, pady = 2)
disaster = IntVar(master)
disaster.set(1)
naturalDisasters = OptionMenu(master, disaster, 1,2,3,4,5,6,7,8,9,10)
naturalDisasters.grid(row = 5, column = 0, sticky = W, pady = 2)

currentEnergy = Label(master, text="What is the current energy demand in your community? (1-10)")
currentEnergy.grid(row = 6, column = 0, sticky = W, pady = 4)
currentEnergyList = IntVar(master)
currentEnergyList.set(1)
Energy = OptionMenu(master, currentEnergyList, 1,2,3,4,5,6,7,8,9,10)
Energy.grid(row = 7, column = 0, sticky = W, pady = 4)

Button(master, text="Submit", command=submit).grid(row = 8, column = 0, sticky = W, pady = 4)

t = Turtle()
t.penup()
t.hideturtle()
t.speed(0)


t.screen.mainloop()
master.mainloop()