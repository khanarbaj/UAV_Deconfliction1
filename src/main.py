import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from uav_info_def import UAV_TimeStamp, UAV_TimeWindow, UAV_Pos, UAV_Info
from src.simulationUavDB import SimulationUav1Info, SimulationUav2Info, SimulationUav3Info, SimulationUav4Info  

# Primary UAV
primary_uav = UAV_Info(
    [
        # Dummy path values
        UAV_Pos(10, 11, 12),
        UAV_Pos(13, 14, 15),
        UAV_Pos(16, 17, 18),
        UAV_Pos(19, 20, 21),
        UAV_Pos(22, 23, 24),
        UAV_Pos(25, 26, 27),
        UAV_Pos(28, 29, 30),
        UAV_Pos(31, 32, 33),
        UAV_Pos(34, 35, 36),
        UAV_Pos(37, 38, 39),
    ],
    UAV_TimeWindow(UAV_TimeStamp(2,0), UAV_TimeStamp(2,30))
)

def print_uav_info(uav_info: UAV_Info):
    print("UAV Path:")
    for pos in uav_info.path:
        print(f"co-ordinates(x,y,z): ({pos.x}, {pos.y}, {pos.z})")
    print(f"Time Window: {uav_info.time_window.start_time.hh}:{uav_info.time_window.start_time.min} to {uav_info.time_window.end_time.hh}:{uav_info.time_window.end_time.min}")



SimulationUavInfo = [SimulationUav1Info, SimulationUav2Info, SimulationUav3Info, SimulationUav4Info]
SimulationUavRadius = [50,50,50,50]  # in centimeters

def detect_collision(primary_uav_info: UAV_Info):

    collision_Info = UAV_Info([], UAV_TimeWindow(UAV_TimeStamp(0,0), UAV_TimeStamp(0,0)))

    # check if time window of primary UAV overlaps with any other simulation UAVs
    Is_collision = False
    Final_collision = False
    for idx, sim_uav in enumerate(SimulationUavInfo):
        if not(
            primary_uav_info.time_window.end_time.hh < sim_uav.time_window.start_time.hh or
            (primary_uav_info.time_window.end_time.hh == sim_uav.time_window.start_time.hh and primary_uav_info.time_window.end_time.min <= sim_uav.time_window.start_time.min) or
            primary_uav_info.time_window.start_time.hh > sim_uav.time_window.end_time.hh or
            (primary_uav_info.time_window.start_time.hh == sim_uav.time_window.end_time.hh and primary_uav_info.time_window.start_time.min >= sim_uav.time_window.end_time.min)
        ):
            #print(f"condition 1 met for Simulation UAV {idx+1}") #for debugging purpose
            # check if x,y,z coordinates overlap
            for pos1 in primary_uav_info.path:
                for pos2 in sim_uav.path:
                    if ((pos1.x == pos2.x) and (pos1.y == pos2.y) and (pos1.z == pos2.z)):
                        collision_Info.path.append(pos1)
                        collision_Info.time_window = primary_uav_info.time_window
                        Is_collision = True
        
        if Is_collision:
            print(f"Collision detected with Simulation UAV {idx+1}")
            print("Collision Info:")
            print_uav_info(collision_Info)
            #print(f"Simulation UAV {idx+1} Info:")
            #print_uav_info(sim_uav)
            Is_collision = False  # reset for next simulation UAV
            Final_collision = True
    if not Final_collision:
        print("clear")


detect_collision(primary_uav)

