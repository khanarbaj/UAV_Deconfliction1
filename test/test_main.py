import unittest
import sys
import os

# Add src folder to sys.path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from collision_detection import HandleCollission
from uav_info_def import UAV_Info, UAV_Pos, UAV_TimeWindow, UAV_TimeStamp

class TestMainFunctionality(unittest.TestCase):
    def setUp(self):
        self.default_path = [UAV_Pos(10, 10, 10), UAV_Pos(20, 20, 20)]
        self.default_time_window = UAV_TimeWindow(UAV_TimeStamp(2, 0), UAV_TimeStamp(2, 30))

    def test_no_collision(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test1\n")
        primary = UAV_Info(self.default_path, UAV_TimeWindow(UAV_TimeStamp(1, 0), UAV_TimeStamp(1, 30)))
        sim = UAV_Info(self.default_path, UAV_TimeWindow(UAV_TimeStamp(2, 0), UAV_TimeStamp(2, 30)))
        HandleCollission.SafeDistance = [50]
        HandleCollission.FinalCollisionResult = False
        HandleCollission.detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

    def test_time_window_overlap_no_spatial_collision(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test2\n")
        primary = UAV_Info([UAV_Pos(0, 0, 0)], self.default_time_window)
        sim = UAV_Info([UAV_Pos(1000, 1000, 1000)], self.default_time_window)
        HandleCollission.SafeDistance = [100]
        HandleCollission.FinalCollisionResult = False
        HandleCollission.detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

    def test_time_window_and_spatial_collision(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test3\n")
        primary = UAV_Info([UAV_Pos(10, 10, 10)], self.default_time_window)
        sim = UAV_Info([UAV_Pos(11, 11, 11)], self.default_time_window)
        HandleCollission.SafeDistance = [100]
        HandleCollission.FinalCollisionResult = False
        HandleCollission.detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

    def test_multiple_simulation_uavs(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test4\n")
        primary = UAV_Info([UAV_Pos(10, 10, 10)], self.default_time_window)
        sim1 = UAV_Info([UAV_Pos(10, 10, 10)], self.default_time_window)  # collision
        sim2 = UAV_Info([UAV_Pos(100, 100, 100)], self.default_time_window)  # no collision
        sim3 = UAV_Info([UAV_Pos(10, 10, 10)], UAV_TimeWindow(UAV_TimeStamp(3, 0), UAV_TimeStamp(3, 30)))  # no time overlap
        HandleCollission.SafeDistance = [100, 100, 100]
        HandleCollission.FinalCollisionResult = False
        HandleCollission.detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

    def test_empty_path(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test5\n")
        primary = UAV_Info([], self.default_time_window)
        sim = UAV_Info([], self.default_time_window)
        HandleCollission.SafeDistance = [100]
        HandleCollission.FinalCollisionResult = False
        HandleCollission.detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    unittest.main()
