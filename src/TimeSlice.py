# Copyright (c) 2023 Charlie Vanaret, Fabien Bourrel
# Licensed under the MIT license. See LICENSE file in the project directory for details.

import glob
import imageio

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
   (height, width) = images[0].shape[0:2]
   # TODO
   return images[0]

# save result
def save_result(result_image, result_file_name):
   imageio.imwrite(result_file_name, result_image[:, :, 0])
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
