import os
import subprocess
import sys

#Opens the pairs of images in the dub.txt file

# Path to the directory containing the images
image_directory = sys.argv[1]
dup_file_path = 'dup.txt'

# Function to open an image using the default system viewer
def open_image(filename):
    image_path = os.path.join(image_directory, filename + '.jpeg')
    subprocess.run(['xdg-open', image_path])

# Read the list of duplicates from the file
with open(dup_file_path, 'r') as file:
    for line in file:
        if " # " in line:
            image1, image2 = line.strip().split(" # ")
            print(f"Open {image1} and {image2}")
            user_input = input()
            if user_input.lower() != 'n':
                open_image(image1)
                open_image(image2)
