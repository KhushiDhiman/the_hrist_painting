

**Hirst Painting Project**

This Python project creates a digital artwork inspired by Damien Hirst's Spot Paintings. It utilizes the `colorgram` module to extract a color palette from a reference image and then randomly paints circles on a canvas using the extracted colors.

**Requirements**

- Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- `colorgram` module: Install using `pip install colorgram`



**Customization**

- **Reference Image:** Modify the `reference_image.jpg` file to use a different image for color extraction. Experiment with various images to create unique color palettes.
- **Number of Rows/Columns:** Adjust the `rows` and `columns` variables in the script to control the canvas size (number of circles).
- **Circle Size:** Change the `circle_size` variable to alter the diameter of the circles.
- **Color Filter (Optional):** Add a condition within the color extraction loop to filter unwanted colors based on RGB values or other criteria.

**Explanation**

1. **Imports:** The script imports the necessary modules: `colorgram` for color extraction and `turtle` for drawing the canvas and circles.
2. **Color Extraction:**
   - `extract_colors(filename, number_of_colors)` function is defined to extract a specified number of dominant colors from the reference image.
   - The function uses `colorgram.extract` to extract the colors and returns a list of RGB color tuples.
3. **Canvas Setup:**
   - `turtle` is initialized to set up the drawing environment.
   - The canvas size is adjusted based on the chosen number of rows and columns.
   - The turtle's speed is set to the fastest (`0`).
4. **Painting Circles:**
   - A loop iterates for each row and column, positioning the turtle accordingly.
   - A random color is chosen from the extracted color palette.
   - The turtle's pen color is set to the chosen color.
   - A circle is drawn with the specified size.
5. **Hold Screen:** The turtle window remains open until the user clicks to close it.

**Additional Notes**

- Consider adding comments within the script to enhance readability and explain the code's functionality.
- Explore more advanced features of the `colorgram` module for color manipulation and customization.

This README file provides a detailed guide to execute, customize, and understand the Hirst Painting project. Feel free to experiment and create your own unique artistic creations!
