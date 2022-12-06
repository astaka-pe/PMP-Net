import open3d as o3d
import glob
import os


all_pcd = glob.glob("data/**/*.pcd", recursive=True)

for p in all_pcd:
    pcd = o3d.io.read_point_cloud(p)
    out_path = p.split(".")[0] + ".ply"
    o3d.io.write_point_cloud(out_path, pcd)