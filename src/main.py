import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

# Input:
#   1. UAV x,y,z pos
#   2. UAV TimeWindow

class UAV_TimeStamp:
    def __init__(self, hh, min):
        self.hh = hh
        self.min = min

class UAV_TimeWindow:
    def __init__(self, start_time: UAV_TimeStamp, end_time: UAV_TimeStamp):
        self.start_time = start_time
        self.end_time = end_time

class UAV_Pos:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class UAV_Info:
    def __init__(self, path: list, time_window: UAV_TimeWindow):
        """
        path: list of UAV_Pos objects representing the drone's path (multiple x, y, z coordinates)
        time_window: UAV_TimeWindow object
        """
        self.path = path  # list of UAV_Pos
        self.time_window = time_window
"""--------------------------------------------- Simulation objects --------------------------------------------------"""   
SimulationUav1Info = UAV_Info(
    [
        UAV_Pos(10, 20, 30),
        UAV_Pos(11, 21, 31),
        UAV_Pos(12, 22, 32),
        UAV_Pos(13, 23, 33),
        UAV_Pos(14, 24, 34),
        UAV_Pos(15, 25, 35),
        UAV_Pos(16, 26, 36),
        UAV_Pos(17, 27, 37),
        UAV_Pos(18, 28, 38),
        UAV_Pos(19, 29, 39)
    ],
    UAV_TimeWindow(UAV_TimeStamp(2,0), UAV_TimeStamp(2,30))
)
SimulationUav2Info = UAV_Info(
    [
        UAV_Pos(11, 21, 31),
        UAV_Pos(12, 22, 32),
        UAV_Pos(13, 23, 33),
        UAV_Pos(14, 24, 34),
        UAV_Pos(15, 25, 35),
        UAV_Pos(16, 26, 36),
        UAV_Pos(17, 27, 37),
        UAV_Pos(18, 28, 38),
        UAV_Pos(19, 29, 39),
        UAV_Pos(20, 30, 40)
    ],
    UAV_TimeWindow(UAV_TimeStamp(3,0), UAV_TimeStamp(3,30))
)
SimulationUav3Info = UAV_Info(
    [
        UAV_Pos(21, 31, 41),
        UAV_Pos(22, 32, 42),
        UAV_Pos(23, 33, 43),
        UAV_Pos(24, 34, 44),
        UAV_Pos(25, 35, 45),
        UAV_Pos(26, 36, 46),
        UAV_Pos(27, 37, 47),
        UAV_Pos(28, 38, 48),
        UAV_Pos(29, 39, 49),
        UAV_Pos(30, 40, 50)
    ],
    UAV_TimeWindow(UAV_TimeStamp(4,0), UAV_TimeStamp(4,30))
)
SimulationUav4Info = UAV_Info(
    [
        UAV_Pos(10, 11, 12),
        UAV_Pos(32, 42, 52),
        UAV_Pos(33, 43, 53),
        UAV_Pos(34, 44, 54),
        UAV_Pos(35, 45, 55),
        UAV_Pos(36, 46, 56),
        UAV_Pos(37, 47, 57),
        UAV_Pos(38, 48, 58),
        UAV_Pos(39, 49, 59),
        UAV_Pos(40, 50, 60)
    ],
    UAV_TimeWindow(UAV_TimeStamp(5,0), UAV_TimeStamp(5,30))
)

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



sim_uavs = [SimulationUav1Info, SimulationUav2Info, SimulationUav3Info, SimulationUav4Info]

def detect_collision(primary_uav_info: UAV_Info):
    # check if time window of primary UAV overlaps with any other simulation UAVs
    Is_collision = False
    for idx, sim_uav in enumerate(sim_uavs):
        if not(
            primary_uav_info.time_window.end_time.hh < sim_uav.time_window.start_time.hh or
            (primary_uav_info.time_window.end_time.hh == sim_uav.time_window.start_time.hh and primary_uav_info.time_window.end_time.min <= sim_uav.time_window.start_time.min) or
            primary_uav_info.time_window.start_time.hh > sim_uav.time_window.end_time.hh or
            (primary_uav_info.time_window.start_time.hh == sim_uav.time_window.end_time.hh and primary_uav_info.time_window.start_time.min >= sim_uav.time_window.end_time.min)
        ):
            # check if x,y,z coordinates overlap
            for pos1 in primary_uav_info.path:
                for pos2 in sim_uav.path:
                    if ((pos1.x == pos2.x) and (pos1.y == pos2.y) and (pos1.z == pos2.z)):
                        Is_collision = True
        
        if Is_collision:
            print(f"Collision detected with Simulation UAV {idx+1}")
            print("Primary UAV Info:")
            print_uav_info(primary_uav_info)
            print(f"Simulation UAV {idx+1} Info:")
            print_uav_info(sim_uav)

    if not Is_collision:
        print("clear")


detect_collision(primary_uav)

# if yes, check if distance between two UAVs is less than safe distance
# UAV_SIZE = 20
# safe distance = 2 * UAV_SIZE
