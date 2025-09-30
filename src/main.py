import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from uav_info_def import *
from collision_detection import HandleCollission
from handle_input_data import primaryUavData


def main():

    primary_uav = UAV_Info(
        [],
        UAV_TimeWindow(UAV_TimeStamp(0,0), UAV_TimeStamp(0,0))
    )

    print("Welcome to UAV Deconfliction System")
    print("===================================")
    primary_uav = primaryUavData.get_PrimaryUav_data()
    HandleCollission.detect_collision(primary_uav)


if __name__ == "__main__":
    main()