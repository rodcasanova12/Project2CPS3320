#Name: Rodrigo Casa Nova
from PIL import Image, ImageFilter
import os
#This will be a demonstration of some of the Pillow's library features:
#Such as, reformat(.save), resize(.thumbnail), color change (.convert), and
#blur (.GaussianBlur) which is part of the ImageFilter.

#for loop to convert all the .jpg files to .png files, and save them to the
#pngs folder
def reformat():
    userChoice = input("Do you want to change the format from .jpg to .png?\n Yes or no: ")
    userC = str.lower(userChoice)
    if userC == 'yes':
        for f in os.listdir('.'):
            if f.endswith('.jpg'):
                i = Image.open(f)
                fn, fext = os.path.splitext(f)
                i.save('pngs/{}.png'.format(fn))
        print("Check the pngs folder")

#for loop to resize all the photos in the directory and save them in the user_size folder
def reshape():
    userChoice = input("Do you want to change the size of the photo?\n Yes or no: ")
    userC = str.lower(userChoice)
    if userC == 'yes':
        userSize = input("Enter in number de Size that you want the photo to be?\n Example 300: ")
        userS = int(userSize)
        user_size = (userS,userS)
        for f in os.listdir('.'):
            if f.endswith('.jpg'):
                i = Image.open(f)
                fn, fext = os.path.splitext(f)

                i.thumbnail(user_size)
                i.save('user_size/{}.jpg'.format(fn, fext))

        print("Check the user_size folder ")

#for loop to change de colored photo to black and white and save them in the user_color folder
def black_and_white():
    userChoice = input("wanna make it black and white?\n Yes or no: ")
    userC = str.lower(userChoice)
    if userC == "yes":
        for f in os.listdir('.'):
            if f.endswith('.jpg'):
                i = Image.open(f)
                fn, fext = os.path.splitext(f)
                i.convert(mode='L').save('user_color/{}.jpg'.format(fn, fext))
        print("Check the user_color folder ")

#for loop to blur the photos in the directory and saving them to the user_blur folder
def blur_photo():
    userChoice = input("wanna blur the photos?\n Yes or no: ")
    userC = str.lower(userChoice)
    if userC == "yes":
        for f in os.listdir('.'):
            if f.endswith('.jpg'):
                i = Image.open(f)
                fn, fext = os.path.splitext(f)
                i.filter(ImageFilter.GaussianBlur(10)).save('user_blur/{}.jpg'.format(fn, fext))

        print("Check the user_blur folder ")

#main method to execute all the other def
def main():
    reformat()
    reshape()
    black_and_white()
    blur_photo()

if __name__ == '__main__':
    main()
