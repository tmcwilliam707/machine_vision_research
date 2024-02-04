import os
from PIL import Image, ImageFilter, ImageEnhance
from tkinter import filedialog
from tkinter import Tk, messagebox

def edit_image(filepath):
    img = Image.open(filepath)

    # Apply sharpen filter
    img = img.filter(ImageFilter.SHARPEN)

    # Increase contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(factor)

    # Apply edge enhancement filter
    img = img.filter(ImageFilter.EDGE_ENHANCE)

    # Apply smooth filter
    img = img.filter(ImageFilter.SMOOTH_MORE)

    # Add a little bit of noise
    img = img.effect_spread(10)

    img = img.filter(ImageFilter.UnsharpMask(radius=5, percent=30))

    # Get the base name of the file (without the directory path)
    base = os.path.basename(filepath)
    filename, ext = os.path.splitext(base)

    # Get the path to the Documents folder
    documents_path = os.path.expanduser('~/Documents')

    # Save the edited image in the Documents folder
    edited_filepath = os.path.join(documents_path, f'{filename}_edited{ext}')
    img.save(edited_filepath)

    return edited_filepath

def open_file_dialog():
    root = Tk()
    root.withdraw()  # Close the Tkinter window
    messagebox.showinfo("Information","Please select an image file to edit.")
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    return root.filename

def main():
    filepath = open_file_dialog()
    edited_filepath = edit_image(filepath)
    messagebox.showinfo("Information",f"Edited image is saved as {edited_filepath}")

if __name__ == "__main__":
    main()