import os
import tkinter as tk
from tkinter import filedialog, messagebox

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

def rename_images_in_folder(folder_path):
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith(IMAGE_EXTENSIONS)]

    image_files.sort()  # סדר קבוע

    for idx, filename in enumerate(image_files, start=1):
        file_ext = os.path.splitext(filename)[1]
        new_name = f"{idx}{file_ext}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)

def choose_folder_and_rename():
    folder_path = filedialog.askdirectory()
    if folder_path:
        rename_images_in_folder(folder_path)
        messagebox.showinfo("הסתיים", "שמות התמונות שונו בהצלחה!")

# GUI
root = tk.Tk()
root.title("שינוי שמות תמונות")
root.geometry("300x150")

label = tk.Label(root, text="לחץ על הכפתור לבחירת תיקייה")
label.pack(pady=20)

button = tk.Button(root, text="בחר תיקייה", command=choose_folder_and_rename)
button.pack()

root.mainloop()
