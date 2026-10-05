import subprocess
from pathlib import Path

from config import COLMAP_PATH, IMAGES_DIR, OUTPUT_DIR


def run_colmap(command):
    print()
    print("Running COLMAP:")
    print(" ".join(command))
    print()

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        print("COLMAP command failed.")
        return False

    print("COLMAP command completed successfully.")
    return True


def check_colmap():
    return COLMAP_PATH.exists()


def feature_extraction(database_path):
    command = [
        str(COLMAP_PATH),
        "feature_extractor",
        "--database_path",
        str(database_path),
        "--image_path",
        str(IMAGES_DIR)
    ]

    return run_colmap(command)


def main():
    print("PhotoMesh3D - COLMAP Pipeline")
    print("--------------------------------")

    if not check_colmap():
        print("COLMAP was not found.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    database_path = OUTPUT_DIR / "database.db"

    print("COLMAP found:")
    print(COLMAP_PATH)

    print()
    print("Images directory:")
    print(IMAGES_DIR)

    print()
    print("Database:")
    print(database_path)

    print()
    print("Pipeline configuration is ready.")

def feature_matching(database_path):
    command = [
        str(COLMAP_PATH),
        "exhaustive_matcher",
        "--database_path",
        str(database_path)
    ]

    return run_colmap(command)

def sparse_mapping(database_path, model_path):
    model_path = Path(model_path)
    model_path.mkdir(parents=True, exist_ok=True)

    command = [
        str(COLMAP_PATH),
        "mapper",
        "--image_path",
        str(IMAGES_DIR),
        "--database_path",
        str(database_path),
        "--output_path",
        str(model_path)
    ]

    return run_colmap(command)

def image_undistortion(model_path, dense_path):
    dense_path = Path(dense_path)
    dense_path.mkdir(parents=True, exist_ok=True)

    command = [
        str(COLMAP_PATH),
        "image_undistorter",
        "--image_path",
        str(IMAGES_DIR),
        "--input_path",
        str(model_path),
        "--output_path",
        str(dense_path),
        "--output_type",
        "COLMAP"
    ]

    return run_colmap(command)

def patch_match_stereo(dense_path):
    command = [
        str(COLMAP_PATH),
        "patch_match_stereo",
        "--workspace_path",
        str(dense_path),
        "--workspace_format",
        "COLMAP"
    ]

    return run_colmap(command)

def stereo_fusion(dense_path, output_path):
    command = [
        str(COLMAP_PATH),
        "stereo_fusion",
        "--workspace_path",
        str(dense_path),
        "--workspace_format",
        "COLMAP",
        "--output_path",
        str(output_path)
    ]

    return run_colmap(command)

def poisson_meshing(dense_path, output_path):
    command = [
        str(COLMAP_PATH),
        "poisson_mesher",
        "--input_path",
        str(dense_path / "fused.ply"),
        "--output_path",
        str(output_path)
    ]

    return run_colmap(command)

if __name__ == "__main__":
    main()