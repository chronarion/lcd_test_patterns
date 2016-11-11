#!/usr/bin/python

from PIL import Image, ImageDraw
# 1920x1080
# lenovo is 2560x1440

screen_height = 2560
screen_width = 1440

mid_gray = (128, 128, 128, 0)
bright_gray = (200, 200, 200, 0)

def bottom_right(draw, color, size, x_offset, y_offset):
  c1 = {}
  c2 = {}
  c3 = {}

  c1['x'] = x_offset
  c1['y'] = y_offset
  c2['x'] = size+x_offset
  c2['y'] = y_offset
  c3['x'] = x_offset
  c3['y'] = size+y_offset 
  draw.polygon([(c1['x'], c1['y']),(c2['x'], c2['y']),(c3['x'], c3['y'])], fill = color)


def bottom_left(draw, color, size, x_offset, y_offset):
  c1 = {}
  c2 = {}
  c3 = {}

  c1['x'] = x_offset
  c1['y'] = y_offset
  c2['x'] = size+x_offset
  c2['y'] = y_offset
  c3['x'] = size+x_offset
  c3['y'] = size+y_offset
  draw.polygon([(c1['x'], c1['y']),(c2['x'], c2['y']),(c3['x'], c3['y'])], fill = color)


def top_left(draw, color, size, x_offset, y_offset):
  c1 = {}
  c2 = {}
  c3 = {}

  # top left
  c1['x'] = size+x_offset
  c1['y'] = 0+y_offset #top right corner
  c2['x'] = 0+x_offset
  c2['y'] = size+y_offset #bottom left corner
  c3['x'] = size+x_offset
  c3['y'] = size+y_offset  #bottom right corner
  draw.polygon([(c1['x'], c1['y']),(c2['x'], c2['y']),(c3['x'], c3['y'])], fill = color)

def top_right(draw, color, size, x_offset, y_offset):
  c1 = {}
  c2 = {}
  c3 = {}

  # top right
  c1['x'] = 0+x_offset
  c1['y'] = 0+y_offset #top left corner

  c2['x'] = 0+x_offset
  c2['y'] = size+y_offset

  c3['x'] = size+x_offset
  c3['y'] = size+y_offset

  draw.polygon([(c1['x'], c1['y']),(c2['x'], c2['y']),(c3['x'], c3['y'])], fill = color)

def cursor_pattern(draw, color, x_offset, y_offset):
  size = 128 
  spacer = size / 2 
  top_left(draw, color, size, 0+x_offset,0+y_offset)
  top_right(draw, color, size, x_offset + size + spacer, 0+y_offset)
  bottom_left(draw, color, size, 0+x_offset,size + spacer+y_offset) 
  bottom_right(draw, color, size, size+spacer+x_offset,size + spacer+y_offset) 

def clear(img, draw, color="black"):
  draw.rectangle([(0,0),img.size], fill=color)

def main():
  img = Image.new('RGB', (screen_width, screen_height), "black")
  draw = ImageDraw.Draw(img)

  speed = 1

  i = 0
  x = 0
  y = 0

  while (x < screen_width):
    while (y < screen_height):
      clear(img, draw, color="gray")
      cursor_pattern(draw, "white", x, y)
      filename = "cursor_pattern_{:0>6d}.png".format(i);
      print(filename)
      i = i + 1
      y = y + speed
      img.save(filename, 'PNG')
    y = 0
    x = x + speed

main();
