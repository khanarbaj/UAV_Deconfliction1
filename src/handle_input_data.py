from uav_info_def import *

class primaryUavData:
    primary_uav = UAV_Info(
        [],
        UAV_TimeWindow(UAV_TimeStamp(0,0), UAV_TimeStamp(0,0))
    )
    def get_PrimaryUav_data():
        print("Enter Primary UAV Data:")
        hh,mm = map(int, input("Enter flight start time (hh mm): ").split())
        primaryUavData.primary_uav.time_window.start_time = UAV_TimeStamp(hh,mm)
        hh,mm = map(int, input("Enter flight end time (hh mm): ").split())
        primaryUavData.primary_uav.time_window.end_time = UAV_TimeStamp(hh,mm)
        print("path in the form of 10 data points(x,y,z)")
        for i in range(10):
            x,y,z = map(int, input(f"Enter data point {i + 1} (x y z): ").split())
            primaryUavData.primary_uav.path.append(UAV_Pos(x,y,z))

        return primaryUavData.primary_uav

    def print_PrimaryUav_data():
        print("Primary UAV Info:")
        print(f"Time Window: {primaryUavData.primary_uav.time_window.start_time.hh}:{primaryUavData.primary_uav.time_window.start_time.min} to {primaryUavData.primary_uav.time_window.end_time.hh}:{primaryUavData.primary_uav.time_window.end_time.min}")
        print("Path:")
        for pos in primaryUavData.primary_uav.path:
            print(f"({pos.x}, {pos.y}, {pos.z})")

    def print_uav_info(uav_info: UAV_Info):
        print("UAV Path:")
        print(f"Time Window: {uav_info.time_window.start_time.hh}:{uav_info.time_window.start_time.min} to {uav_info.time_window.end_time.hh}:{uav_info.time_window.end_time.min}")
        for pos in uav_info.path:
            print(f"co-ordinates(x,y,z): ({pos.x}, {pos.y}, {pos.z})")