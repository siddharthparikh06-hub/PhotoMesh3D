import open3d as o3d
from pathlib import Path


def load_point_cloud(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        print("File not found:", file_path)
        return None

    point_cloud = o3d.io.read_point_cloud(str(file_path))

    print("Loaded:", file_path)
    print("Points:", len(point_cloud.points))

    return point_cloud


def show_point_cloud(point_cloud):
    if point_cloud is None:
        return

    o3d.visualization.draw_geometries([point_cloud])


def main():
    print("PhotoMesh3D - Point Cloud Evaluation")
    print("-------------------------------------")

    test_file = Path("data/processed/test_pointcloud.ply")

    point_cloud = load_point_cloud(test_file)

    if point_cloud is not None:
        show_point_cloud(point_cloud)


if __name__ == "__main__":
    main()