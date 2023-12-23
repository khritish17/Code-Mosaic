def calculate_hypotenuse(side1, side2):
    # This function calculates the hypotenuse of a right-angled triangle
    # using the Pythagorean theorem: c = sqrt(a^2 + b^2)

    # Calculate the square of side1
    side1_squared = side1 ** 2

    # Calculate the square of side2
    side2_squared = side2 ** 2

    # Sum the squares of side1 and side2
    sum_of_squares = side1_squared + side2_squared

    # Calculate the square root of the sum_of_squares
    hypotenuse = sum_of_squares ** 0.5

    return hypotenuse


# Test the function with a right-angled triangle with sides 3 and 4
triangle_hypotenuse = calculate_hypotenuse(3, 4)

# Print the result
print(f"The hypotenuse of the triangle is: {triangle_hypotenuse}")
