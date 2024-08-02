import cv2
import os

frame_count = 0
frame_out = 1

# Function to extract frames from video and saving it as images
def videos_to_frames(video):
    global frame_count, frame_out
    cap = cv2.VideoCapture(video)
    
    frame_rate = 5
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_count += 1
        
        # Only extract frames at the desired frame rate
        if frame_count % int(cap.get(5) / frame_rate) == 0:
            output_file = f"{output_directory}/frame_{frame_out}.jpg"
            cv2.imwrite(output_file, frame)
            print(f"Frame {frame_count} has been extracted and saved as {output_file}")
            frame_out += 1
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    output_directory = f"TestFrames"
    os.makedirs(output_directory, exist_ok=True)

    for i in range(1,23):
        video_file = f"Tekken8Dataset/Test/{i}.mp4"
        videos_to_frames(video_file)
