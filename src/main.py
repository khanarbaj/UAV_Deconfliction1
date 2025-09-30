import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, 'src')
if project_root not in sys.path:
    sys.path.append(project_root)
if src_dir not in sys.path:
    sys.path.append(src_dir)
from uav_info_def import *
from collision_detection import HandleCollission
from handle_input_data import primaryUavData
from src.simulationUavDB import SimulationUavInfo


def main():

    primary_uav = UAV_Info(
        [],
        UAV_TimeWindow(UAV_TimeStamp(0,0), UAV_TimeStamp(0,0))
    )

    print("Welcome to UAV Deconfliction System")
    print("===================================")
    primary_uav = primaryUavData.get_PrimaryUav_data()
    #primaryUavData.print_PrimaryUav_data()
    #primaryUavData.print_uav_info(SimulationUavInfo[3])
    print("===================================")
    HandleCollission.detect_collision(primary_uav)


if __name__ == "__main__":
    main()