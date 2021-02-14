from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Class dedicated to the movement and behaviour of the snake."""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    # create_snake() and add_segment() together create the starting snake
    def create_snake(self):
        """Creates the snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Snake gains additional segment when successfully guided to food."""
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        """Extends snake by 1 additional segment when snake successfully eats
        food, via add_segment()"""
        # Gets position of last segment in segments list and adds it to the
        # end of segments list as the last segment. Effectively, extending the
        # snake.
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Movement behavior of snake."""
        # Arguments in range function = (start=2, stop=0, step=-1)
        for segment_number in range(len(self.segments) - 1, 0, -1):
            # Linking all segments so they move in a line and turn when they
            # should. eg. segment 3 goes to where segment 2s position,
            # segment 2 goes to segment 1s position, then segment 1 moves to
            # new location, then repeat. Essentially, segments 2 & 3 follow
            # segment 1.
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """Sets snake heading to an upwards movement. Corresponds with the
        'up' arrow key keybinding defined in main file."""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """Sets snake heading to a downwards movement. Corresponds with the
        'down' arrow key keybinding defined in main file."""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        """Sets snake heading to a leftwards movement. Corresponds with the
        'left' arrow key keybinding defined in main file."""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        """Sets snake heading to a rightwards movement. Corresponds with the
        'right' arrow key keybinding defined in main file."""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
