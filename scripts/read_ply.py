import open3d as o3d

file_path = "data/processed/test_pointcloud.ply"

point_cloud = o3d.io.read_point_cloud(file_path)

print("PLY file loaded successfully!")
print("Number of points:", len(point_cloud.points))

o3d.visualization.draw_geometries([point_cloud])