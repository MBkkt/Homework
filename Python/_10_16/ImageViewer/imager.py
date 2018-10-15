from PIL import Image, ImageTk
import random
import math


def tk_image(path):
    img = Image.open(path)
    img = filters[random.randrange(6)](img, img.size)
    return ImageTk.PhotoImage(img)


def clear(source, size):
    return source


def rotate(source, size):
    result = Image.new('RGB', size)
    width = size[0]
    height = size[1]
    angle = math.radians(random.randrange(360))
    sin_ = math.sin(angle)
    cos_ = math.cos(angle)
    x0 = (width - 1) / 2
    y0 = (height - 1) / 2
    for col in range(width):
        for row in range(height):
            a = col - x0
            b = row - y0
            cc = int(a * cos_ - b * sin_ + x0)
            rr = int(a * sin_ + b * cos_ + y0)
            if 0 <= cc < width and 0 <= rr < height:
                result.putpixel((col, row), source.getpixel((cc, rr)))
    return result


def swirl(source, size):
    result = Image.new('RGB', size)
    width = size[0]
    height = size[1]
    x0 = (width - 1) / 2
    y0 = (height - 1) / 2
    for col in range(width):
        for row in range(height):
            cc = col - x0
            rr = row - y0
            r = math.sqrt(cc * cc + rr * rr)
            angle = math.pi * r / 256
            sin_ = math.sin(angle)
            cos_ = math.cos(angle)
            tCol = int(cc * cos_ - rr * sin_ + x0)
            tRow = int(cc * sin_ + rr * cos_ + y0)
            if 0 <= tCol < width and 0 <= tRow < height:
                result.putpixel((col, row), source.getpixel((tCol, tRow)))
    return result


def wave(source, size):
    result = Image.new('RGB', size)
    width = size[0]
    height = size[1]
    for col in range(width):
        for row in range(height):
            cc = col
            rr = int(row + 20 * math.sin(col * 2 * math.pi / 64))
            if (rr >= 0) and (rr < height):
                result.putpixel((col, row), source.getpixel((cc, rr)))
    return result


def glass(source, size):
    result = Image.new('RGB', size)
    width = size[0]
    height = size[1]
    for col in range(width):
        for row in range(height):
            cc = (width + col + random.randrange(-5, 6)) % width
            rr = (height + row + random.randrange(-5, 6)) % height
            result.putpixel((col, row), source.getpixel((cc, rr)))
    return result


def negative(source, size):
    result = Image.new('RGB', size)
    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b = source.getpixel((x, y))
            result.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    return result


filters = [clear, rotate, swirl, wave, glass, negative]
