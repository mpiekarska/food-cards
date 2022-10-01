# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from html2image import Html2Image
from PIL import Image
#hti = Html2Image(size=(360,250))
hti = Html2Image()

def print_image_card():
    hti.screenshot(url='/Users/magdalena/PycharmProjects/food-cards/food-card.html',
                   save_as='food_card.png')

def crop_image_card():
    im = Image.open('food_card.png')
    im_crop = im.crop((19, 19, 701, 475))
    im_crop.save('food_card_crop.png', quality=100)

def resize_image_card():
    ratio = 0.5
    im_in = Image.open('food_card_crop.png')
    im_resize = im_in.resize([int(ratio * s) for s in im_in.size])
    im_resize.save('food_card_resized.png', quality=100)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_image_card()
    crop_image_card()
    resize_image_card()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
