from pathlib import Path
from zipfile import ZipFile

# תוכן קובץ ה-bat
bat_content = '''@echo off
cd /d "C:\\Users\\dvira\\Downloads\\StarSpotifyAlarmClock-master\\Executables\\latest"
StarSpotifyAlarmClock.exe "https://open.spotify.com/playlist/3on9pxkJUD6fEW7zvW1Tq8" 1
'''

# נתיב לקובץ הזמני
bat_path = Path("/mnt/data/spotify_alarm.bat")

# כתיבה לקובץ .bat
bat_path.write_text(bat_content, encoding='utf-8')

# יצירת קובץ ZIP עבור הורדה נוחה
zip_path = Path("/mnt/data/spotify_alarm.zip")
with ZipFile(zip_path, 'w') as zipf:
    zipf.write(bat_path, arcname='spotify_alarm.bat')

zip_path.name
