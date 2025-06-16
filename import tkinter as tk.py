import tkinter as tk
from tkinter import filedialog, messagebox

def remove_commas():
    # פותח דיאלוג לבחירת קובץ
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    
    if not file_path:
        return  # אם המשתמש סגר את הדיאלוג
    
    try:
        # קריאת תוכן הקובץ
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # הסרת כל הפסיקים
        modified_content = content.replace(',', '')
        
        # שמירה חזרה לאותו קובץ
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        messagebox.showinfo("Success", f"All commas have been removed from the file:\n{file_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# יצירת חלון GUI
root = tk.Tk()
root.title("Remove Commas from File")
root.geometry("400x200")

# יצירת כפתור להפעלת הפונקציה
button = tk.Button(root, text="Select Text File", command=remove_commas, font=("Arial", 14))
button.pack(pady=50)

# הפעלת הלולאה הראשית של tkinter
root.mainloop()
