from turtle import  Turtle
move_distance=20
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.snake_segment = []
        self.create_snake()
    def create_snake(self):
        x = 0
        for i in range(3):
            t = Turtle("square")
            t.color("white")
            x = t.xcor()
            t.penup()
            t.goto(t.xcor() - 20 * i, 0)
            self.snake_segment.append(t)
    def add_segment(self):
        t = Turtle("square")
        t.color("white")
        x_last=self.snake_segment[-1].xcor()
        y_last=self.snake_segment[-1].ycor()
        t.penup()
        t.goto(x_last,y_last)
        self.snake_segment.append(t)

    def move(self):
        for seg in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg - 1].xcor()
            new_y = self.snake_segment[seg - 1].ycor()
            self.snake_segment[seg].goto(new_x, new_y)
        self.snake_segment[0].forward(move_distance)

    def move_up(self):
        if self.snake_segment[0].heading()!=down:
            self.snake_segment[0].setheading(up)

    def move_right(self):
        if self.snake_segment[0].heading() != left:
            self.snake_segment[0].setheading(right)

    def move_left(self):
        if self.snake_segment[0].heading() != right:
            self.snake_segment[0].setheading(left)

    def move_down(self):
        if self.snake_segment[0].heading() != up:
            self.snake_segment[0].setheading(down)





