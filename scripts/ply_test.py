import open3d as o3d
import numpy as np

points = np.random.rand(1000, 3)

point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

output_file = "data/processed/test_pointcloud.ply"

o3d.io.write_point_cloud(output_file, point_cloud)

print("Point cloud saved successfully!")
print("File:", output_file)
print("Number of points:", len(point_cloud.points))