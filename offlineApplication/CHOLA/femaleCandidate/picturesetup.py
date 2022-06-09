
import os
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
from tkinter import messagebox
def addCurvedCorners(im, rad):
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


def addPicture(index, path, savepath):
    image = Image.open(path)
    print('Opened')
    final_image = addCurvedCorners(image, 55)
    print('Curved')
    try:
        final_image.save(f'Face{index}.png')
    except FileNotFoundError:
        os.mkdir(savepath)
        final_image.save(f'Face{index}.png')


def askPicture(index, savepath):
    from tkinter import filedialog as fd
    file_filter = (('Image Files', '*.*'),)
    filename = fd.askopenfilename(title='Open File', initialdir='/', filetypes=file_filter)
    try:
        addPicture(index, filename, savepath)
        messagebox.showinfo('Import Image', f'Sucessfully imported image for Candidate {index}')
    except UnidentifiedImageError:
        messagebox.showerror('Import Image', 'Error - Unsupported ImageType')        
        askPicture(index)
    

print('You are about to setup images for CHOLA Candidate - Female')
candi = int(input('Enter number of candidates: '))
for i in range(1,candi+1):
    askPicture(i, '/')
