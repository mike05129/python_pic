"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys

from PIL.Image import Image
from simpleimage import SimpleImage



def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images


    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    dist = ((red - pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)**0.5
    return dist



def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_r = 0
    total_b = 0
    total_g = 0
    for x in range (len(pixels)):
        total_r += pixels[x].red
        total_b += pixels[x].blue
        total_g += pixels[x].green

    rgb=[total_r/len(pixels),total_g/len(pixels),total_b/len(pixels)]

    return rgb
    

def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg_rgb= get_average(pixels)
    Best_position = 0
    for x in range (len(pixels)): #using numpy is easier
        if x+1 != len(pixels):
            if get_pixel_dist(pixels[x],avg_rgb[0],avg_rgb[1],avg_rgb[2]) < get_pixel_dist(pixels[x+1],avg_rgb[0],avg_rgb[1],avg_rgb[2]):
                Best_position = x
            else:
                Best_position = x+1
        return pixels[Best_position]  
    


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    print(len(images))
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    """
    gre_im = SimpleImage.blank(20,20,'green').get_pixel(0,0)
    red_im = SimpleImage.blank(20,20,'red').get_pixel(0,0)
    blu_im = SimpleImage.blank(20,20,'blue').get_pixel(0,0)
    #gre_pix = images[1].get_pixel(0,0)
    best1 = get_best_pixel([gre_im,blu_im,blu_im])
    #print(get_pixel_dist(gre_pix,5,255,10))
    #print(get_average([gre_im,gre_im,gre_im,blu_im]))

    print(best1.red,best1.green,best1.blue)
    """
    image_pixel=[]
    for x in range (width):
        for y in range (height):
           
            for z in images:             
                image_pixel.append(z.get_pixel(x,y))
            best_pixel = get_best_pixel(image_pixel)
            image_pixel.clear()
            result.set_pixel(x,y,best_pixel)
            #result_pix = result.get_pixel(x,y)
            #result_pix.red = best_pixel.red
            #result_pix.green=best_pixel.green
            #result_pix.blue=best_pixel.blue


    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])

    solve(images)


if __name__ == '__main__':
    main()
