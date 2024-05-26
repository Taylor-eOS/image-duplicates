from PIL import Image #pip install Pillow ImageHash
import imagehash
import os
import sys

#Calculates a perceptual hash for each images and gives you a list of images that are likely duplicates.

# Path to the directory containing images
folder_path = sys.argv[1]
threshold = 1  # Define the threshold for accepting duplicates (smaller means more similar)

hashes = {}
duplicates = []

# Loop through image files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpeg'):
        print(f"Checking {filename[:-5]}")
        image_path = os.path.join(folder_path, filename)
        with Image.open(image_path) as img:
            hash = imagehash.average_hash(img)

            # Check if this hash is close to any other hash
            for existing_hash in hashes.keys():
                hamming_distance = hash - existing_hash
                if hamming_distance <= threshold:
                    duplicates.append((image_path, hashes[existing_hash]))
                    print(f"{hamming_distance}")
                    break
            else:
                hashes[hash] = image_path

# Output the list of duplicates
print(f"")
print(f"Duplicates:")
with open('dup.txt', 'w') as file:
    for dup in duplicates:
        print(f"{os.path.basename(dup[0])[:-5]} # {os.path.basename(dup[1])[:-5]}")
        file.write(f"{os.path.basename(dup[0])[:-5]} # {os.path.basename(dup[1])[:-5]}\n")
