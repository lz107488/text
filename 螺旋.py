import turtle as t
t.bgcolor("black")
n=6
colors=['red','yellow','blue','orange','green','purple']
for x in range(200):
    t.pencolor(colors[x%n])
    t.forward(x*3/n+x)
    t.left(360/n+1)
    t.width(x*n/100)
