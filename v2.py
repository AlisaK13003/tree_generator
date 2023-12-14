import turtle
import math
from typing import Optional, Tuple

# Constants
TRUNK_COLOR = "burlywood4"
TRUNK_LENGTH = 40
TRUNK_WIDTH = 10

LEAF_RADIUS = 45

FRUIT_DIAMETER = 5
FRUIT_DISTANCE = 15  # Adjust the distance to fit inside the leaves

FLOWER_DIAMETER = 3
FLOWER_DISTANCE = 1 # Adjust the distance to fit inside the leaves


def draw_trunk(t: turtle.Turtle) -> None:
    """Draws the trunk of the tree."""
    t.clear()
    t.penup()
    t.home()
    t.left(90)
    t.pendown()
    t.color(TRUNK_COLOR)
    t.pensize(TRUNK_WIDTH)
    t.forward(TRUNK_LENGTH)


def draw_leaves(t: turtle.Turtle, color: str) -> Tuple[float, float]:
    """Draws the leaves of the tree and returns the center position."""
    t.color(color)
    t.begin_fill()
    t.right(90)
    # Iber magic happens HEre
    center_x, center_y = t.pos()
    t.circle(LEAF_RADIUS)
    t.end_fill()
    return center_x, center_y + TRUNK_LENGTH


def calculate_coordinates(amount: int, radius: float) -> list[Tuple[float, float]]:
    """Calculate coordinates for fruits or flowers."""
    coordinates = []
    for i in range(amount):
        angle = i * (360 / amount)
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        coordinates.append((x, y))
    return coordinates


def draw_items(
    t: turtle.Turtle,
    color: str,
    amount: int,
    item_diameter: float,
    item_distance: float,
    center_x: float,
    center_y: float,
) -> None:
    """Draws fruits or flowers."""
    t.penup()
    t.color(color)
    t.pensize(1)
    radius = LEAF_RADIUS - item_distance
    coordinates = calculate_coordinates(amount, radius)
    for x, y in coordinates:
        t.goto(center_x + x, center_y + y)
        t.begin_fill()
        t.circle(item_diameter)
        t.end_fill()


def draw_tree(
    t: turtle.Turtle,
    leaf_color: str,
    fruit_color: str,
    fruit_amount: int,
    flower_color: str,
    flower_amount: int,
) -> None:
    """Draws a tree with leaves, fruits, and flowers."""
    draw_trunk(t)
    center_x, center_y = draw_leaves(t, leaf_color)
    draw_items(
        t, fruit_color, fruit_amount, FRUIT_DIAMETER, FRUIT_DISTANCE, center_x, center_y
    )
    draw_items(
        t,
        flower_color,
        flower_amount,
        FLOWER_DIAMETER,
        FLOWER_DISTANCE,
        center_x,
        center_y,
    )

def load_valid_colors(file_path: str) -> set:
    """Load valid colors from a text file."""
    try:
        with open(file_path, 'r') as file:
            return {line.strip().lower() for line in file}
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return set()

def is_valid_color(color: str, valid_colors: set) -> bool:
    """Check if the color is in the set of valid colors."""
    return color.lower() in valid_colors

def should_exit(input_str: str) -> bool:
    """Check if the user wants to exit."""
    return input_str.strip().lower() in ['n', 'q']

def get_input(prompt: str) -> Optional[str]:
    """Get user input for a prompt."""
    user_input = input(prompt).strip().lower()
    if should_exit(user_input):
        return None
    return user_input

def get_color_input(prompt: str, valid_colors: set) -> Optional[str]:
    """Get user input for a color prompt."""
    while True:
        color = get_input(prompt)
        if color is None:
            return None  # User wants to exit

        if is_valid_color(color, valid_colors):
            return color
        else:
            print("Invalid color. Please enter a valid color.")

def get_amount_input(prompt: str) -> Optional[int]:
    """Get user input for an amount prompt."""
    while True:
        amount_str = get_input(prompt)
        if amount_str is None:
            return None  # User wants to exit

        try:
            amount = int(amount_str)
            if amount >= 0:
                return amount
            else:
                print("Invalid amount. Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def is_valid_amount(amount: str) -> bool:
    """Check if the amount is a non-negative integer."""
    try:
        amount = int(amount)
        return amount >= 0
    except ValueError:
        return False


def get_valid_input(prompt: str, validation_func, error_message:str, *args) -> Optional[str]:
    """Get user input for a prompt with validation."""
    while True:
        user_input = get_input(prompt)
        if user_input is None:
            return None  # User wants to exit

        if validation_func(user_input, *args) if callable(validation_func) else True:
            return user_input
        else:
            print(f"Invalid input. {error_message}")


def get_inputs(valid_colors: set) -> Optional[Tuple[str, str, int, str, int]]:
    """Gets user input for tree parameters."""
    prompts = [
        ("Enter the color of the tree leaves: \n", is_valid_color, valid_colors, "Please enter a valid color."),
        ("Enter the color of the fruits: \n", is_valid_color, valid_colors, "Please enter a valid color."),
        ("Enter the amount of fruits: \n", get_amount_input, "Please enter a non-negative integer."),
        ("Enter the color of the flowers: \n", is_valid_color, valid_colors, "Please enter a valid color."),
        ("Enter the amount of flowers: \n", get_amount_input, "Please enter a non-negative integer."),
    ]

    inputs = []
    for prompt, validation_func, *args, error_message in prompts:
        user_input = get_valid_input(prompt, validation_func, error_message, *args)
        if user_input is None:
            return None  # User wants to exit

        # Convert amount to integer if applicable
        if validation_func == get_amount_input:
            user_input = int(user_input)

        inputs.append(user_input)

    # Print debug information
    print("User input:", *inputs)
    #print("Valid colors from file:", valid_colors)

    return tuple(inputs)

def main() -> None:
    valid_colors = load_valid_colors('turtle_colors.txt')

    dan = turtle.Turtle()
    dan.speed(10)

    while True:
        answer = input("Would you like to draw a tree (y/n)? ").strip().lower()

        while answer not in ["y", "n", "q"]:
            print("Invalid input. Enter 'y', 'n', or 'q'.")
            answer = input("Would you like to draw a tree (y/n)? ").strip().lower()

        if answer == "n" or answer == "q":
            print("Exiting...")
            turtle.bye()
            break
        elif answer == "y":
            tree_parameters = get_inputs(valid_colors)
            if tree_parameters is not None:  # Check for None to handle user exit
                draw_tree(dan, *tree_parameters)



if __name__ == "__main__":
    main()
