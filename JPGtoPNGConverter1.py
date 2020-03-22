import sys
import os
from PIL import Image

print(sys.argv[0])
print(len(sys.argv))
print(str(sys.argv))
print(sys.argv)

#grab first two arguments to use
image_folder = sys.argv[1]
new_folder = sys.argv[2]

print(image_folder, new_folder)
print(os.path.exists(new_folder))

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

print(os.listdir(image_folder))
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print('All Done')