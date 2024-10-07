import cv2
import time
import random
import os
import sounddevice as sd
import wavio
import speech_recognition as sr
from GoogleSpeechRecognitionService import recognize_speech

import sys
print(sys.path)
def capture_random_photo():
    """Captures a random photo using the webcam."""
save_dir = 'captured_images'
os.makedirs(save_dir, exist_ok=True)  # Handle existing directory gracefully

    # Initialize the webcam
cap = cv2.VideoCapture(0)

    # Set a random delay for the photo capture (adjusted for 1-minute interval)
random_delay = random.uniform(30, 60)  # Random delay between 30 and 60 seconds

    # Wait for the random delay before capturing
time.sleep(random_delay)

    # Capture the photo
ret, frame = cap.read()
if ret:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = os.path.join(save_dir, f"student_photo_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Photo captured and saved as {filename}")
else:
        print("Failed to capture photo")

    # Release the camera
cap.release()
cv2.destroyAllWindows()


def verify_audio():
    """Records audio, transcribes it, and verifies speech activity."""

    # Record the last minute of audio
    audio_data, fs = sd.rec(int(60 * fs), samplerate=fs, channels=1)
    sd.wait()

    # Save the audio file
    wavio.write("recorded_audio.wav", audio_data, fs, sampwidth=2)

    # Transcribe the audio using a speech-to-text API
    recognizer = sr.Recognizer()
    with sr.AudioFile("recorded_audio.wav") as source:
        audio_data = recognizer.record(source)

    try:
        transcription = recognizer.recognize_google(audio_data)
        print("Transcription:", transcription.lower())

        # Analyze speech activity
        speech_active = detect_speech_activity(audio_data, fs)

        # Verification based on both photo and audio
        if speech_active and is_student_in_frame(captured_photo):
            print("Student is engaged")
        else:
            print("Student may not be engaged")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results ")
        from GoogleSpeechRecognitionService import recognize_speech
        def upload_to_cosmocloud(file_path, access_key, secret_key, bucket_name):
    """Uploads a file to CosmoCloud storage."""

    client = cosmocloud.Client(access_key, secret_key)
    client.upload_file(file_path, bucket_name, os.path.basename(file_path))

# Main loop
if __name__ == "__main__":
    access_key = "YOUR_COSMOCLOUD_ACCESS_KEY"  # Replace with your actual access key
    secret_key = "YOUR_COSMOCLOUD_SECRET_KEY"  # Replace with your actual secret key
    bucket_name = "YOUR_COSMOCLOUD_BUCKET_NAME"  # Replace with your bucket name

    while True:
        capture_random_photo()
        verify_audio()

try:
    transcription = recognize_speech(audio_data)
    # ... (rest of your code)
except Exception as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

def detect_speech_activity(audio_data, sample_rate):
    """Detects speech activity in the audio data."""

    # ... (your speech activity detection code from before)

def is_student_in_frame(image_path):
    """Determines if the student is present in the captured image."""

    # Implement your facial recognition or object detection logic here
    # For example, you could use OpenCV's face detection or custom object detection models

    # Return True if the student is detected in the image, False otherwise
    return True  # Replace with your actual implementation

# Run the function periodically (e.g., every 10 minutes)
while True:
    capture_random_photo()
    verify_audio()
    time.sleep(600)  # Adjust the interval as needed
    