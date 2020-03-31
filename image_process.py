import sys
import os
from PIL import Image


def image_converter(image_directory, output_directory, format):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    try:
        for filename in os.listdir(image_directory):
            image = Image.open(f'{image_directory}/{filename}')
            getname = os.path.splitext(filename)[0]
            image.save(f'{output_directory}/{getname}.{format}', format)
            print("all done")
    except:
        pass


def image_resizer(input_directory, output_directory, width, height):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    try:        
        for filename in os.listdir(input_directory):
            getextension = os.path.splitext(filename)[1].split('.')[1]
            getname = os.path.splitext(filename)[0]
            print(1) 
            image = Image.open(f'{input_directory}/{filename}')
            print(2)
            new_image = image.resize((int(width), int(height)))
            print(3)
            print(new_image.size)
            print(f'{output_directory}/{filename}', getextension)
            new_image.save(f'{output_directory}/{getname}.{getextension}')
            print("all done")
    except:
        print("found error")
        pass

# image_converter(sys.argv[1], sys.argv[2], sys.argv[3])
image_resizer(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

