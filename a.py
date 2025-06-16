import tkinter as tk
from tkinter import messagebox
import json
import os

# נתיב הקובץ לשמירת ההתקדמות
PROGRESS_FILE = 'progress.json'

# רשימת מילים לדוגמה (ניתן להרחיב)
WORDS = [
    {"english": "Hello", "hebrew": "שלום"},
    {"english": "Goodbye", "hebrew": "להתראות"},
    {"english": "Please", "hebrew": "בבקשה"},
    {"english": "Thank you", "hebrew": "תודה"},
    {"english": "Yes", "hebrew": "כן"},
    {"english": "No", "hebrew": "לא"},
    {"english": "Good morning", "hebrew": "בוקר טוב"},
    {"english": "Good night", "hebrew": "לילה טוב"},
    {"english": "Excuse me", "hebrew": "סליחה"},
    {"english": "Sorry", "hebrew": "סליחה"}
]

class LanguageTrainer:
    def __init__(self, master):
        self.master = master
        self.master.title("English to Hebrew Trainer")

        # טעינת ההתקדמות
        self.load_progress()

        # יצירת תוויות ואלמנטים בממשק
        self.status_label = tk.Label(master, text=self.get_status_text(), font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.word_label = tk.Label(master, text="", font=("Arial", 16))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check_answer)

        self.submit_button = tk.Button(master, text="שלח", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack(pady=5)

        self.feedback_label = tk.Label(master, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        # התחלת התרגול
        self.next_word()

    def load_progress(self):
        if os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                self.progress = json.load(f)
        else:
            # אתחול ההתקדמות
            self.progress = {}
            for word in WORDS:
                self.progress[word['english']] = False

    def save_progress(self):
        with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, ensure_ascii=False, indent=4)

    def get_status_text(self):
        known = sum(1 for known in self.progress.values() if known)
        total = len(self.progress)
        return f"ידעת {known} מתוך {total} מילים"

    def next_word(self):
        # בחירת מילה שלא נלמדה עדיין
        remaining = [word for word in WORDS if not self.progress[word['english']]]
        if not remaining:
            messagebox.showinfo("סיום", "כל המילים נלמדו! כל הכבוד!")
            self.master.quit()
            return
        self.current_word = remaining[0]
        self.word_label.config(text=self.current_word['english'])
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.status_label.config(text=self.get_status_text())

    def check_answer(self, event=None):
        user_answer = self.entry.get().strip()
        correct_answer = self.current_word['hebrew']
        if user_answer == correct_answer:
            self.progress[self.current_word['english']] = True
            self.feedback_label.config(text="נכון!", fg="green")
        else:
            self.feedback_label.config(text=f"טעות! התשובה הנכונה: {correct_answer}", fg="red")
        self.save_progress()
        self.status_label.config(text=self.get_status_text())
        self.master.after(1500, self.next_word)  # מעבר למילה הבאה אחרי 1.5 שניות

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTrainer(root)
    root.mainloop()
