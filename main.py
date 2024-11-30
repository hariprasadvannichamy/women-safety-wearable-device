from src.audio_processing import capture_audio
from src.ai_model import detect_distress
from src.alert_system import send_alert
from src.hardware_interface import initialize_hardware

def main():
    print("Initializing the women's safety monitoring device...")
    initialize_hardware()

    while True:
        audio_data = capture_audio()
        if detect_distress(audio_data):
            print("Distress signal detected! Sending alert...")
            send_alert()
        else:
            print("No distress detected.")

if _name_ == "_main_":
    main()
