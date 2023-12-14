# Tree Generator Project
## Overview

This tree generator project allows users to create stylized trees with customizable leaves, fruits, and flowers utilizing the Turtle graphics library in Python. The latest version (v2.py) represents a substantial improvement over the initial code (v1.py), focusing on code organization, readability, and user interaction.

---

### Dependencies

This project is written in Python and uses the following libraries:
- the `turtle` graphics library.
- the `math` module for mathematical calculations
- the `typing` module for type hints.

---

## Features
#### 1. Drawing the Trunk
The program starts by drawing the trunk of the tree. The trunk's color, length, and width can be customized inside the code.

#### 2. Drawing Leaves
Leaves are drawn as circles at the top of the trunk. Users can choose the color of the leaves.

#### 3. Drawing Fruits
Fruits are drawn in a circular pattern around the tree. The number and color of fruits can be specified by the user. The program uses parametric equations to calculate the (x, y) coordinates for each fruit, creating a visually pleasing arrangement.

#### 4. Drawing Flowers
Similar to fruits, flowers are drawn in a circular pattern around the tree. Users can customize the number and color of flowers. The program uses parametric equations to calculate the (x, y) coordinates for each flower.

#### 5. Input Validation
The program includes input validation to ensure that the user provides the correct types of input. If the user enters invalid input, the program prompts them to enter the correct information.

#### 6. File Input/File Read:

The latest version (v2.py) introduces the capability to load valid colors from a text file (turtle_colors.txt). This file contains a list of valid colors, and the program reads it to validate user input for leaf, fruit, and flower colors.

---

### Parametric Equations for Flower and Fruit Placement
`x = r * cos(theta)`</br>`y = r * sin(theta)`

The placement of flowers and fruits around the tree is achieved using parametric equations. These equations calculate the (x, y) coordinates based on the number of flowers or fruits specified, ensuring a symmetrical and aesthetically pleasing arrangement. The equations use the polar coordinate system, with the radius determined by the distance between each flower or fruit and the angle calculated based on the *n* amount of flowers/fruits.

## Getting Started

To run the tree generator, follow these steps:
  1. Ensure you have Python installed.
  2. Clone the repository to your local machine.
  3. Run the script by executing the command `python tree_generator.py` in your terminal.
  4. Follow the prompts to customize the tree's appearance.

### Example Output/Input

`Would you like to draw a tree (y/n)?` y </br>
`Enter the color of the tree leaves:` </br>
green </br>
`Enter the color of the fruits:` </br>
azure </br>
`Enter the amount of fruits:` </br>
4 </br>
`Enter the color of the flowers:` </br>
mediumseagreen </br>
`Enter the amount of flowers:` </br>
6 </br>
`User input: green azure 4 mediumseagreen 6` </br>
`Would you like to draw a tree (y/n)?` n </br>
`Exiting...` </br>

---

## Notes

- The program allows users to draw multiple trees by repeatedly prompting them to input tree parameters.
- To exit the program, simply enter 'n' or 'q' when prompted to draw a tree.
- Ensure `turtle_colors.txt` is in the same path as `v2.py`

---
## Acknowledgments

Special thanks to my peer Iber for their invaluable assistance in refining the code architecture and more. For more of their work, visit their GitHub [here](https://github.com/IberAI/IberAI).

---

## License

This project is licensed under the [MIT License](LICENSE).
