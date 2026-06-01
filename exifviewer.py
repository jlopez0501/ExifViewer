#!/usr/bin/env python3
from exif import Image
import sys

# Creates an Image object using a source image.
def read_exif(source_image: str) -> Image:
    with open(source_image, 'rb') as image_file:
        my_image = Image(image_file)
        return my_image

# Displays the EXIF data of the Image object returned by read_exif()
def display_exif(image_exif: Image):
    # Check if EXIF data exists
    if len(image_exif.list_all()) == 0:
        print("No EXIF data found.")

    if len(sys.argv) > 2:
        # Lists all specified attributes and handles unknowns gracefully.
        # "i" represents the index of the first attribute
        i = 2
        while i < len(sys.argv):
            try:
                print(f"{sys.argv[i]}: {getattr(image_exif, sys.argv[i])}")
            except:
                print(f"EXIF attribute not found: {sys.argv[i]}")
            i += 1
                
   # If no attribute was specified, list all with their corresponding values.         
    else:
        for attribute in image_exif.get_all():
            print(f"{attribute}: {getattr(image_exif, attribute)}")

def main():
    image_exif = read_exif(sys.argv[1])
    display_exif(image_exif)

if __name__ == "__main__":
    main()