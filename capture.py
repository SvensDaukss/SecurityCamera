import time
from concurrent.futures import ThreadPoolExecutor
from camera import capture_image as capture_image_function, capture_video as capture_video_function
from s3_uploader import upload_to_s3

def capture_image():
    image_path = "/home/crab/Pictures/"
    bucket_name = "raspberrycameramodule3bucket"  # Change this to the name of your S3 bucket
    timestamp = time.strftime("%Y-%m-%d %H%M%S")
    image_file_path = f"{image_path}Image_Capture_{timestamp}.jpg"
    
    # Capture image and save locally first
    capture_image_function(image_file_path)
    
    # Upload to S3 asynchronously
    with ThreadPoolExecutor() as executor:
        executor.submit(upload_to_s3, image_file_path, bucket_name, f"Image_Capture_{timestamp}.jpg")

def capture_video():
    video_path = "/home/crab/Videos/"
    bucket_name = "raspberrycameramodule3bucket"  # Change this to the name of your S3 bucket
    timestamp = time.strftime("%Y-%m-%d %H%M%S")
    video_file_path = f"{video_path}Video_Capture_{timestamp}.h264"
    
    # Capture video and save locally first
    capture_video_function(video_file_path, duration=3)
    
    # Upload to S3 asynchronously
    with ThreadPoolExecutor() as executor:
        executor.submit(upload_to_s3, video_file_path, bucket_name, f"Video_Capture_{timestamp}.h264")
