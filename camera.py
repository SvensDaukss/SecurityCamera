import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder

def capture_image(file_path):
    picam2 = Picamera2()
    config = picam2.create_still_configuration(main={"size": (1024, 768)})
    picam2.configure(config)
    picam2.start()
    time.sleep(2)  # Allow time for the camera to stabilize
    picam2.capture_file(file_path)
    picam2.stop()
    picam2.close()  # Ensure the camera is properly released
    print(f"Image captured and saved to: {file_path}")

def capture_video(file_path, duration=3):
    picam2 = Picamera2()
    encoder = H264Encoder(10000000)
    config = picam2.create_video_configuration(main={"size": (640, 480)})
    picam2.configure(config)
    picam2.start()
    picam2.start_recording(encoder, file_path)
    time.sleep(duration)
    picam2.stop_recording()
    picam2.stop()
    picam2.close()  # Ensure the camera is properly released
    print(f"Video captured and saved to: {file_path}")
