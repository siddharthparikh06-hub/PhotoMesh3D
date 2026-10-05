from pathlib import Path
from benchmark import timer


def run_pipeline():
    print("=" * 50)
    print("PhotoMesh3D - Reconstruction Pipeline")
    print("=" * 50)

    with timer("Pipeline setup"):
        Path("data/raw/images").mkdir(parents=True, exist_ok=True)
        Path("data/processed/validated_images").mkdir(
            parents=True,
            exist_ok=True
        )
        Path("data/processed/reconstruction").mkdir(
            parents=True,
            exist_ok=True
        )

    print()
    print("Pipeline directories are ready.")
    print()
    print("Next stages:")
    print("1. Frame extraction")
    print("2. Image validation")
    print("3. COLMAP reconstruction")
    print("4. Dense point cloud generation")
    print("5. 3D mesh generation")
    print("6. Evaluation")
    print("7. Benchmarking")


if __name__ == "__main__":
    run_pipeline()