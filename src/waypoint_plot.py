# Incomplete code snippet

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class PlotUAVPaths:
    def plot_uav_paths(uav_paths):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for pos in uav_paths:
            xs = pos.x
            ys = pos.y
            zs = pos.z
            ax.plot(xs, ys, zs, marker='o')

        #ax.plot(uav_paths.x,label="primary UAV path")

        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.set_zlabel('Z Coordinate')
        ax.legend()
        plt.show()