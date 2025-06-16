import os
from tkinter import Tk, filedialog, messagebox
from pydub import AudioSegment

class MP4ToMP3Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("MP4 to MP3 Converter")
        self.mp4_path = None
        self.mp3_path = None

    def select_file(self):
        self.mp4_path = filedialog.askopenfilename(
            filetypes=[("MP4 files", "*.mp4")],
            title="Select MP4 File"
        )
        if self.mp4_path:
            messagebox.showinfo("File Selected", f"Selected File: {os.path.basename(self.mp4_path)}")

    def save_file(self):
        self.mp3_path = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("MP3 files", "*.mp3")],
            title="Save MP3 File"
        )
        if self.mp3_path:
            messagebox.showinfo("Save Location", f"Save Location: {self.mp3_path}")

    def convert(self):
        if not self.mp4_path or not self.mp3_path:
            messagebox.showerror("Error", "Please select both the MP4 file and save location!")
            return
        try:
            audio = AudioSegment.from_file(self.mp4_path, format="mp4")
            audio.export(self.mp3_path, format="mp3")
            messagebox.showinfo("Success", "MP3 file created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

# ממשק גרפי
if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # הסתרת חלון ראשי
    converter = MP4ToMP3Converter(root)
    converter.select_file()
    converter.save_file()
    converter.convert()
