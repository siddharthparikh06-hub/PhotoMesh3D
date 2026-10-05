import open3d as o3d
import numpy as np

points = np.random.rand(1000, 3)

point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

o3d.visualization.draw_geometries([point_cloud])