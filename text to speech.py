from gtts import gTTS
import os
import platform

def text_to_speech():
    text = input("Enter the text you want to convert into speech: ").strip()

    if not text:
        print("❌ You must enter some text!")
        return

    # Save file to Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filename = os.path.join(desktop, "output.mp3")

    try:
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        print(f"✅ Audio saved as: {filename}")

        # Play audio depending on OS
        system_platform = platform.system()
        if system_platform == "Windows":
            os.system(f'start "" "{filename}"')
        elif system_platform == "Darwin":  # macOS
            os.system(f'afplay "{filename}"')
        elif system_platform == "Linux":
            os.system(f'mpg123 "{filename}"')
        else:
            print("⚠ Audio playback not supported on this OS.")
    except PermissionError:
        print("❌ Permission denied. Try running your terminal or IDE as administrator.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

text_to_speech()
