import os
import shutil
from PIL import Image

print('**************************')
print('JPG to PNG file converter!')
print('**************************')

jpg_folder_name = input(
    'The name(or relative path) of the folder with the JPG files: ')

img_folder = os.path.realpath(f'./{jpg_folder_name}')
filenames = os.listdir(img_folder)

# If the pngs folder already exists, remove it
if os.path.isdir('./pngs'):
    shutil.rmtree('./pngs')

os.mkdir('./pngs')

for file in filenames:
    img = Image.open(f'{img_folder}/{file}')
    img.save(f'./pngs/{file[:-4]}.png', 'png')
