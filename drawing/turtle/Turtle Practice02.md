# Turtle Practice
Date: 20200716
## A Rectangle

Drawing a rectangle is almost exactly the same as drawing a square, except that the turtle needs to draw two sides that are longer than the other two:

```python
import turtle
t = turtle.Pen()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
```

## A Triangle

Do you know there're 3 types of triangles?

- equilateral
- isosceles
- scalene

Let's concentrate on the first two types, because they are the most straightforward to draw.

An equilateral triangle has three equal sides and three equal angles (every angles is 180 / 3 = 60 degrees):

```python
import turtle
t = turtle.Pen()
t.forward(100)
t.left(120)	# turn left with 120 degrees
t.forward(100)
t.left(120)
t.forward(100)
```

Now, an isosceles triangle has two equal sides and two equal angles:

```python
import turtle
t = turtle.Pen()
t.forward(50)
t.left(104.47751218592992)	# turn left with 104.47751218592992 degrees
t.forward(100)
t.left(151.04497562814015)
t.forward(100)
```

In this solution, the turtle moves forward 50 pixels, and then turns 104.47751218592992 degrees. It moves forwards 100 pixels, followed by a turn of 151.04497562814015 degrees, and then forward 100 pixels again. To turn the turtle back to face its starting position, we can call the following line again:

```python
t.left(104.47751218592992)
```



## Practice: A box without corners

The solution to this puzzle (an octagon missing four sides) is to do the same thing four times in a row.

Move forward, turn left 45 degrees, lift the pen, move forward, put the pen down, and turn left 45 degrees again:

```python
t.forward(50)
t.left(45)
t.up()
t.forward(50)
t.down()
t.left(45)
```

so, the final set of commands would be like the following code, let's use Text Editor to write down them and save as a file named as __nocorners.py__:

```python
import turtle
t = turtle.Pen()
t.forward(50)
t.left(45)
t.up()
t.forward(50)
t.down()
t.left(45)
t.forward(50)
t.left(45)
t.up()
t.forward(50)
t.down()
t.left(45)
t.forward(50)
t.left(45)
t.up()
t.forward(50)
t.down()
t.left(45)
t.forward(50)
t.left(45)
t.up()
t.forward(50)
t.down()
t.left(45)
```

Finally let's think about how to make that shorter, we are doing something 4 times exactly same, that's the part we can consider LOOP:

```python
import turtle
t = turtle.Pen()
for i in range (1, 5):	# Note: the range (1,5) mean 1, 2, 3, 4, and not include 5
    t.forward(50)
    t.left(45)
    t.up()
    t.forward(50)
    t.down()
    t.left(45)
    i += 1
```

Let's take rest for today!
