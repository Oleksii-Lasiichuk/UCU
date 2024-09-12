from turtle import *
color('black')
a = int(input())
b = int(input())
c = input("choose operation: +, -")

if a == 1: 
    penup() 
    goto(-200, 0)
    pendown()
    left(90)
    forward(50)
    left(90)
    forward(20)
    left(90)
    forward(100)
    left(90)
    forward(20)
    left(90)
    forward(50)

if b == 1: 
    penup() 
    goto(20, 0)
    pendown()
    forward(50)
    left(90)
    forward(20)
    left(90)
    forward(100)
    left(90)
    forward(20)
    left(90)
    forward(50)

if c == "+": 
    penup() 
    goto(-100, 0)
    pendown()
    left(90)
    forward(50)
    left(90)
    forward(20)
    left(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(20)
    left(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(20)
    left(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(20)
    left(90)
    forward(50)

answer = 0
if c == "+":
    answer = a+b
    print(answer)


if answer == 2:
    penup() 
    goto(200, 0)
    pendown()
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(20)
    left(90)
    forward(30)
    right(90)
    forward(40)
    right(90)
    forward(30)
    left(90)
    forward(60)
    left(90)
    forward(30)
    left(90)
    forward(20)
    left(90)
    forward(30)
    right(90)
    forward(40)
    right(90)
    forward(30)







done()