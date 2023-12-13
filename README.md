# Tree Generator Project
## Overview

This tree generator project allows users to create stylized trees with customizable leaves, fruits, and flowers utilizing the Turtle graphics library in Python. The latest version (v.02) represents a substantial improvement over the initial code (v.01), focusing on code organization, readability, and user interaction.

## Features
#### 1. Drawing the Trunk
The program starts by drawing the trunk of the tree. The trunk's color, length, and width can be customized.

#### 2. Drawing Leaves
Leaves are drawn as circles at the top of the trunk. Users can choose the color of the leaves.

#### 3. Drawing Fruits
Fruits are drawn in a circular pattern around the tree. The number and color of fruits can be specified by the user. The program uses parametric equations to calculate the (x, y) coordinates for each fruit, creating a visually pleasing arrangement.

#### 4. Drawing Flowers
Similar to fruits, flowers are drawn in a circular pattern around the tree. Users can customize the number and color of flowers. The program uses parametric equations to calculate the (x, y) coordinates for each flower.

#### 5. Input Validation
The program includes input validation to ensure that the user provides the correct types of input. If the user enters invalid input, the program prompts them to enter the correct information.

---

### Parametric Equations for Flower and Fruit Placement
**x = r * cos(theta)**</br>**y = r * sin(theta)**

The placement of flowers and fruits around the tree is achieved using parametric equations. These equations calculate the (x, y) coordinates based on the number of flowers or fruits specified, ensuring a symmetrical and aesthetically pleasing arrangement. The equations use the polar coordinate system, with the radius determined by the distance between each flower or fruit and the angle calculated based on the *n* amount of flowers/fruits.

## Getting Started

To run the tree generator, follow these steps:
  1. Ensure you have Python installed.
  2. Clone the repository to your local machine.
  3. Run the script by executing the command `python tree_generator.py` in your terminal.
  4. Follow the prompts to customize the tree's appearance.

---

### Notes

    The program allows users to draw multiple trees by repeatedly prompting them to input tree parameters.
    To exit the program, simply enter 'n' or 'q' when prompted to draw a tree.
