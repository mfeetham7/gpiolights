import board
import neopixel

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 8

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False,
                           pixel_order=ORDER)


pixels.fill((0, 0, 255))
pixels.show()
