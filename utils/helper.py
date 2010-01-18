#-*- coding: utf-8 -*-
import os, logging, Image

def trace(message="-= Starting logging =-", 
          log_filename='debug.log', 
          log_format='%(asctime)s %(levelname)s: %(message)s', 
          log_datefmt='%Y-%m-%d %H:%M:%S'):
    """
    Ghi lại thông tin, dùng để debug.
    """
    logging.basicConfig(level=logging.DEBUG, 
                        filename=log_filename, 
                        format=log_format, 
                        datefmt=log_datefmt)
    logging.info(message)


def thumnail(file_path, image_with, image_height):
    image = Image.open(file_path)
    image.thumnail([image_with, image_height], Image.ANTIALIAS)
    dirname = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    save_to = os.path.join(dirname, "/thumnails/", "%d-%d"%(image_with, image_height))
    save_as = save_to + filename
    image.save(save_as, image.format)
    