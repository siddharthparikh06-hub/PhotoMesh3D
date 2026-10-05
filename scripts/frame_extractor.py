import cv2
from pathlib import Path


def extract_frames(video_path, output_folder, every_n_frames=10):
    video = cv2.VideoCapture(str(video_path))

    if not video.isOpened():
        print("Could not open video:", video_path)
        return

    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)

    print("Video:", video_path)
    print("Total frames:", total_frames)
    print("FPS:", fps)

    frame_number = 0
    saved_frames = 0

    while True:
        success, frame = video.read()

        if not success:
            break

        if frame_number % every_n_frames == 0:
            filename = output_folder / f"frame_{saved_frames:04d}.jpg"
            cv2.imwrite(str(filename), frame)
            saved_frames += 1

        frame_number += 1

    video.release()

    print()
    print("Frame extraction complete!")
    print("Frames processed:", frame_number)
    print("Frames saved:", saved_frames)
    print("Output folder:", output_folder)


if __name__ == "__main__":
    extract_frames(
        "data/raw/video.mp4",
        "data/raw/images",
        every_n_frames=10
    )