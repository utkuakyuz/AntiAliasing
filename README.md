# Anti-aliasing Algorithm

This is a Python implementation of an anti-aliasing algorithm, which uses circle shapes as an example. Anti-aliasing is a technique used to smooth the edges of an image or graphic to make it appear more realistic and less pixelated. 
The below image shows original circle:

![image](https://user-images.githubusercontent.com/79662515/235304723-bb413d37-0ff6-44df-a60f-37995ce04f6c.png)

And the below image shows antialiased circle:

![image](https://user-images.githubusercontent.com/79662515/235304751-374af1fc-75d1-4428-befb-601c47998227.png)


## Requirements

To run this program, you need to have the following installed:

- Python 3.x
- NumPy library
- Matplotlib library

## Usage

The program provides three functions:

1. `make_circle()`: This function creates a circle shape with a given radius and returns a matrix of pixels that represent the circle.

2. `anti_alias(matrix2, T)`: This function applies the anti-aliasing algorithm to the given matrix `matrix2` T times.

3. `visualize(matrix)`: This function visualizes the final matrix using the Matplotlib library.

To use this program, run the `visualize()` function with the result of the `anti_alias()` function as the input. You can modify the parameters of the `make_circle()` function to change the size and shape of the circle.

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue. All contributions are welcome!

## Acknowledgments
This implementation was inspired by this on supersampling and anti-aliasing. 
https://en.wikipedia.org/wiki/Supersampling
The NumPy and Matplotlib libraries were used for this implementation.
