##########################################

####################
# It's Working
####################

# To start the project:
# To install packages: pip install -r requirements.txt
# To run the program: python main.py

# Python version: 3.13

# Required packages in requirements.txt

##########################################


## Program begins from here

# Importing packages required
from PIL import Image
from rembg import remove
import easygui

def remove_background(input_path, output_path):
    """
    Remove background from an image and save the result
    :param input_path: Path to input image
    :param output_path: Path to save output image
    """
    try:
        # Open the input image file
        input_image = Image.open(input_path)

        # Remove the background
        output_image = remove(input_image)

        # Save the output image
        output_image.save(output_path + ".png")
        print(f"Successfully removed background! Saved to {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")


inputPath = easygui.fileopenbox(title='Select image file')
outputPath = easygui.filesavebox(title='Save file to...')


if __name__ == "__main__":

    # Run the background removal
    remove_background(inputPath, outputPath)
