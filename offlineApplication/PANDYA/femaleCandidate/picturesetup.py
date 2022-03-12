
import os
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
from tkinter import messagebox
def add_curved_corners(im, rad):
    im = im.resize((369,369))
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


def add_text(image,text):
    my_image = image
    title_text = text
    title_font = ImageFont.truetype('SF-Pro-Display-Semibold.otf', 60)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((10,270), title_text, (255, 169, 110), font=title_font)
    return my_image

def add_picture(index,path, sname, savepath):
    image = Image.open(path)
    print('Opened')
    curved_image = add_curved_corners(image,55)
    print('Curved')
    final_image = add_text(curved_image,sname)
    print('Scripted')
    try:
        final_image.save(f'Face{index}.png')
    except FileNotFoundError:
        os.mkdir(savepath)
        final_image.save(f'Face{index}.png')


def ask_picture(index,shortname, savepath):
    from tkinter import filedialog as fd
    file_filter = (('Image Files', '*.*'),)
    filename = fd.askopenfilename(title='Open File', initialdir='/', filetypes=file_filter)
    try:
        add_picture(index,filename,shortname, savepath)
        messagebox.showinfo('Import Image', f'Sucessfully imported image for Candidate {index}')
    except UnidentifiedImageError:
        messagebox.showerror('Import Image', 'Error - Unsupported ImageType')        
        ask_picture(index,shortname)
    

print('You are about to setup images for SPL Candidate - Female')
candi = int(input('Enter number of candidates: '))
for i in range(1,candi+1):
    sname = input('Enter the "Short Name" given by the candidate: ')
    if len(sname) > 12:
        print('Length of the short name is longer than expected (more than 12 characters including space). \nAppearance of the image maynot be correct')
    
    ask_picture(i, sname, '/')
