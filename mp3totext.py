import whisper
from tkinter import Tk, filedialog, messagebox

def format_transcription(text, line_length=80):
    """
    מחלק את התמלול לשורות קצרות יותר לשיפור קריאות.
    :param text: מחרוזת התמלול המקורית
    :param line_length: אורך מקסימלי לשורה
    :return: מחרוזת מעוצבת
    """
    formatted_text = ""
    current_line = ""
    
    for word in text.split():
        if len(current_line) + len(word) + 1 > line_length:
            formatted_text += current_line.strip() + "\n"
            current_line = ""
        current_line += word + " "
    
    if current_line:
        formatted_text += current_line.strip() + "\n"
    
    return formatted_text

def add_punctuation(text):
    """
    מוסיף פיסוק בסיסי לטקסט עברי לפי מבנה פשוט.
    """
    sentences = text.split(".")  # מחלק את הטקסט למשפטים על בסיס נקודה.
    punctuated_text = ""
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:  # אם המשפט לא ריק
            if not sentence.endswith(("?", "!", ".")):  # אם אין סימן פיסוק בסוף
                sentence += "."  # הוספת נקודה.
            punctuated_text += sentence + " "
    
    return punctuated_text.strip()

def transcribe_audio():
    # פתיחת חלון לבחירת קובץ
    Tk().withdraw()  # להסתיר את חלון Tkinter הראשי
    audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")], title="Select Audio File")
    
    if not audio_path:
        messagebox.showinfo("Info", "No file selected.")
        return

    # טוען את המודל של Whisper
    try:
        model = whisper.load_model("large")  # ניתן לשנות ל"small" או "large" לפי הצורך
        print("Model loaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load Whisper model: {e}")
        return

    # תהליך התמלול
    try:
        print("Starting transcription...")
        result = model.transcribe(audio_path, language="he", task="transcribe", verbose=False)
        transcription = result["text"]

        # עיצוב הטקסט
        formatted_transcription = format_transcription(transcription)

        # הוספת פיסוק
        punctuated_transcription = add_punctuation(formatted_transcription)

        # שמירת הטקסט המעוצב עם פיסוק
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")], title="Save Transcription As")
        if save_path:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(punctuated_transcription)
            messagebox.showinfo("Success", f"Transcription with punctuation saved to {save_path}")
        else:
            messagebox.showinfo("Info", "Transcription not saved.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to transcribe audio: {e}")

if __name__ == "__main__":
    transcribe_audio()
