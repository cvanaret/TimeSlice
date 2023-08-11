# Copyright (c) 2023 Charlie Vanaret, Fabien Bourrel
# Licensed under the MIT license. See LICENSE file in the project directory for details.

import glob
import imageio
import numpy as np

# read command line options
# TODO

# load image files
def load_image_files(directory, extension):
   # scan the directory for image files
   files = sorted(glob.glob(directory + '/*' + extension))
   if len(files) == 0:
      raise Exception("Error: no image could be found.")
   
   # load the images as RGB matrices
   return [imageio.imread(file) for file in files]

# check dimensions
def check_image_dimensions(images):
   for i in range(len(images)-1):
      if images[i].shape[0:2] != images[i+1].shape[0:2]:
         raise Exception("Error: the images do not have the same dimensions.")

# perform chosen timeslice with given options
def perform_timeslice(images):
   number_images = len(images)
   (height, width) = images[0].shape[0:2]
   result = np.zeros(shape=(height, width, 3), dtype='uint8')
   
   # compute the width of a vertical slice
   slice_width = width // number_images
   for image_index in range(number_images):
      columns = slice(slice_width*image_index, slice_width*(image_index+1))
      result[:, columns, :] = images[image_index][:, columns]
   return result

# save result
def save_result(result_image, result_file_name):
   imageio.imsave(result_file_name, result_image)
   print("The timeslice was saved in the file %s." % result_file_name)

# main function
def main():
   # TODO replace hard-coded options with command line options
   directory = '.'
   extension = '.jpg'
   result_file_name = 'output.jpg'
   
   # workflow
   images = load_image_files(directory, extension)
   check_image_dimensions(images)
   result_image = perform_timeslice(images)
   save_result(result_image, result_file_name)

if __name__ == "__main__":
   main()
