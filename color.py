import board
import neopixel
import argparse

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 8

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False,
                           pixel_order=ORDER)

# number of elements
n = 3
 
# Below line read inputs from user using map() function
rgb = list(map(int,input("\nEnter R, G and B values : ").strip().split()))[:n]
 
print("\nList is - ", rgb)

pixels.fill((rgb))
pixels.show()

