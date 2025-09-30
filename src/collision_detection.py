import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, 'src')
if project_root not in sys.path:
    sys.path.append(project_root)
if src_dir not in sys.path:
    sys.path.append(src_dir)

from config.config import PrimaryUavRadius, SimulationUavRadius
from uav_info_def import *
from src.simulationUavDB import SimulationUavInfo


class HandleCollission:

    detectedDistance = [UAV_DetectedDistance(0,0,0)] * len(SimulationUavInfo)
    collision_Info = UAV_Info([], UAV_TimeWindow(UAV_TimeStamp(0,0), UAV_TimeStamp(0,0)))
    Is_collision = False
    FinalCollisionResult = False
    SafeDistance = [0] * len(SimulationUavInfo)

    for index in range(len(SimulationUavInfo)):
        SafeDistance[index]  = 2*(PrimaryUavRadius + SimulationUavRadius[index])  # in centimeters


    def detect_collision(primary_uav_info: UAV_Info):
        
        for index, sim_uav in enumerate(SimulationUavInfo):
            # check if time window of primary UAV overlaps with any other simulation UAVs
            if not(
                primary_uav_info.time_window.end_time.hh < sim_uav.time_window.start_time.hh or
                (primary_uav_info.time_window.end_time.hh == sim_uav.time_window.start_time.hh and 
                 primary_uav_info.time_window.end_time.min <= sim_uav.time_window.start_time.min) or
                primary_uav_info.time_window.start_time.hh > sim_uav.time_window.end_time.hh or
                (primary_uav_info.time_window.start_time.hh == sim_uav.time_window.end_time.hh and 
                 primary_uav_info.time_window.start_time.min >= sim_uav.time_window.end_time.min)
            ):
                 #print(f"condition 1 met for Simulation UAV {index+1}") #for debugging purpose
                # check if x,y,z coordinates overlap
                for pos1 in primary_uav_info.path:
                    for pos2 in sim_uav.path:
                        if ((abs(pos1.x - pos2.x) < HandleCollission.SafeDistance[index]) and 
                            (abs(pos1.y - pos2.y) < HandleCollission.SafeDistance[index]) and 
                            (abs(pos1.z - pos2.z) < HandleCollission.SafeDistance[index])
                            ):
                            HandleCollission.detectedDistance[index] = UAV_DetectedDistance(
                                abs(pos1.x - pos2.x),
                                abs(pos1.y - pos2.y),
                                abs(pos1.z - pos2.z)
                            )
                            HandleCollission.collision_Info.path.append(pos1)
                            HandleCollission.collision_Info.time_window = primary_uav_info.time_window
                            HandleCollission.Is_collision = True

                if HandleCollission.Is_collision:
                    HandleCollission.Is_collision = False
                    HandleCollission.FinalCollisionResult = True
                    HandleCollission.PrintCollissionInfo(HandleCollission.index)

        if HandleCollission.FinalCollisionResult == False:
            print("clear")

    def PrintCollissionInfo(index):

        print(f"Collision detected with Simulation UAV {index+1}")
        print("Collision Info:")
        print(f"Safe Distance: {HandleCollission.SafeDistance[index]} cm")
        print(f"Detected Distance (x_distance,y_distance,z_distance): ({HandleCollission.detectedDistance[index].x_distance} cm, {HandleCollission.detectedDistance[index].y_distance} cm, {HandleCollission.detectedDistance[index].z_distance} cm)")
        HandleCollission.print_uav_info(HandleCollission.collision_Info)

    def print_uav_info(uav_info: UAV_Info):
        print("UAV Path:")
        for pos in uav_info.path:
            print(f"co-ordinates(x,y,z): ({pos.x}, {pos.y}, {pos.z})")
        print(f"Time Window: {uav_info.time_window.start_time.hh}:{uav_info.time_window.start_time.min} to {uav_info.time_window.end_time.hh}:{uav_info.time_window.end_time.min}")

