
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# General description of the solution
## calculate.py

### def calc(fig, func, size):

This module computes the result of a specified function based on the selected shape (e.g., square, circle, or triangle), the operation to perform (e.g., perimeter or area), and the provided dimensions.
Examples of function calls:

- Input: calc("square", "area", [4])
- Output: 16
- Input: calc("circle", "perimeter", [5])
- Output: 31.4159
- Input: calc("triangle", "area", [5, 5, 6])
- Output: 12

## square.py
### def area(a):

This function computes the area of a square using the side length provided by the user.

Example:

- Input: area(5)
- Output: 25
### def perimeter(a):

This function calculates the perimeter of a square using the side length provided by the user.

Example:

- Input: perimeter(6)
- Output: 24
## triangle.py
  ### def area(a, b, c):

This function computes the area of a triangle using the semi-perimeter method, based on the lengths of its sides.

Example:

- Input: area(5, 5, 8)
- Output: 12
### def perimeter(a, b, c):

This function calculates the perimeter of a triangle using the lengths of its sides.

Example:

- Input: perimeter(4, 5, 6)
- Output: 15
## circle.py
  ### def area(r):

This function calculates the area of a circle using the radius provided by the user.
Example:

- Input: area(4)
- Output: 50.26548
### def perimeter(r):

This function calculates the circumference (perimeter) of a circle based on the radius provided.
Example:

- Input: perimeter(7)
- Output: 43.9823

# Project change history with commit hashes
1. d080c7888b81955bad2ed78d58ad910526b5132a L-04: Triangle added
2. 51c40ebfd0e0b65f52fe5e54740cbb038e492db3 L-04: Doc updated for triangle
3. d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71 L-04: Add calculate.py
4. b5b0fae727ca72c317c383b39c0af73d6adcd81c L-04: Update docs for calculate.py
5. 53dd56aa07482df6606de0b664b6574e5c4cb16e Update triangle.py
6. 42bf0973e4cf2f1d5806cd1e8fb34aa9048de099 Update square.py
7. aca64fefc34c82d0aecac5d00fe1ea4054bb9254 Update circle.py 
8. 8ee1ed793250ec2ed759621bc0d4e9d5a29f4033 Update calculate.py 




