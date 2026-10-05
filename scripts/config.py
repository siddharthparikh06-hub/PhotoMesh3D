from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DIR = DATA_DIR / "raw"

PROCESSED_DIR = DATA_DIR / "processed"

IMAGES_DIR = RAW_DIR / "images"

OUTPUT_DIR = PROCESSED_DIR / "reconstruction"

COLMAP_PATH = Path(r"C:\Users\yashs\colmap\COLMAP.bat")


print("PhotoMesh3D Configuration")
print("--------------------------")
print("Project:", PROJECT_ROOT)
print("Raw data:", RAW_DIR)
print("Images:", IMAGES_DIR)
print("Processed:", PROCESSED_DIR)
print("Reconstruction:", OUTPUT_DIR)
print("COLMAP:", COLMAP_PATH)