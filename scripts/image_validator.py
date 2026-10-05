import cv2
from pathlib import Path


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

BLUR_THRESHOLD = 100.0


def calculate_blur_score(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()


def validate_images(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("Folder does not exist:", folder)
        return

    image_files = [
        file for file in folder.iterdir()
        if file.suffix.lower() in IMAGE_EXTENSIONS
    ]

    if not image_files:
        print("No images found.")
        return

    valid_images = 0
    blurry_images = 0
    invalid_images = 0

    print("Image Validation Report")
    print("-----------------------")
    print("Folder:", folder)
    print("Images found:", len(image_files))
    print("Blur threshold:", BLUR_THRESHOLD)
    print()

    for image_file in sorted(image_files):
        image = cv2.imread(str(image_file))

        if image is None:
            print(f"INVALID  | {image_file.name}")
            invalid_images += 1
            continue

        height, width = image.shape[:2]
        blur_score = calculate_blur_score(image)

        if blur_score < BLUR_THRESHOLD:
            print(
                f"BLURRY   | {image_file.name} | "
                f"{width}x{height} | Score: {blur_score:.2f}"
            )
            blurry_images += 1
        else:
            print(
                f"VALID    | {image_file.name} | "
                f"{width}x{height} | Score: {blur_score:.2f}"
            )
            valid_images += 1

    print()
    print("Summary")
    print("-------")
    print("Valid images:", valid_images)
    print("Blurry images:", blurry_images)
    print("Invalid images:", invalid_images)
    print("Total images:", len(image_files))


if __name__ == "__main__":
    validate_images("data/raw/images")