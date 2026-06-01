# ExifViewer

A lightweight command-line tool for reading EXIF metadata from images.
Built for photographers who want to quickly recall the camera settings
used in a specific shoot.

## Requirements

- Python 3.11.5
- `exif` package

## Installation

1. Clone the repository
   git clone https://github.com/jlopez0501/ExifViewer.git

2. Install dependencies
   pip install exif

3. Add the script to your PATH and create an `exif` alias for your OS

## Usage

View all EXIF attributes:
   exif photo.jpg

View specific attributes:
   exif photo.jpg aperture focal_length iso

## Notes

- If an attribute does not exist in the image, ExifViewer will handle
  it gracefully and continue printing any remaining valid attributes
- If no EXIF data exists in the image at all, ExifViewer will let you know
