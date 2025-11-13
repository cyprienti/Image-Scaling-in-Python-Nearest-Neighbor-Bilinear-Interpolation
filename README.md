# Image-Scaling-in-Python

This project implements two classic image scaling algorithms — Nearest Neighbor and Bilinear Interpolation — using pure Python and NumPy (without OpenCV or other high-level libraries). The provided main.py script loads a bitmap image, applies both scaling methods with different factors, and saves the results to a single output file.

# Features

  Manual image scaling using:
    -  Nearest Neighbor interpolation
    -  Bilinear interpolation
    -  Works with arbitrary scaling factors (upscaling and downscaling).
    -  Generates and saves a single comparison image (results.png).

Uses only NumPy and Matplotlib — no OpenCV, PIL, or automated scaling functions.

#  How to Run
  -  Download and extract the provided ZIP archive.
  -  Open a terminal in the project folder.
  -  Install dependencies:

         pip install -r requirements.txt


# Run the main script:

    python main.py


The file results.png will be generated, showing:
  -  The original image
  -  Nearest Neighbor (scale 2/3 and 3×)
  -  Bilinear (scale 2/3 and 3×)

# Algorithm Overview
  -  Nearest Neighbor Interpolation
    For each pixel in the scaled image, find the nearest pixel in the original image.
    Fast but may result in a blocky or pixelated look.

Formula:

    𝐼′(𝑥′,𝑦′)=𝐼(round(𝑥/𝑠𝑥),round(𝑦/𝑠𝑦))I′(x′,y′)=I(round(x/sx),round(y/sy))

  -  Bilinear Interpolation
Computes the new pixel value using a weighted average of the four nearest pixels.
Produces smoother results than Nearest Neighbor.

Formula:

    𝐼′(𝑥′,𝑦′)=(1−𝑎)(1−𝑏)𝐼(𝑥1,𝑦1)+𝑎(1−𝑏)𝐼(𝑥2,𝑦1)+(1−𝑎)𝑏𝐼(𝑥1,𝑦2)+𝑎𝑏𝐼(𝑥2,𝑦2)I′(x′,y′)=(1−a)(1−b)I(x1,y1)+a(1−b)I(x2,1)+(1−a)bI(x1,y2)+abI(x2,y2)
 

  # Restrictions
  -  You must not use automated scaling functions from NumPy or Matplotlib.
  -  You must not use external libraries such as OpenCV or PIL.

Only basic operations with arrays and manual interpolation logic are allowed.

# Learning Objectives

  -  Understand and implement fundamental image scaling algorithms manually.
  -  Learn how to manipulate image data using NumPy arrays.
  -  Compare visual and performance differences between interpolation methods.
