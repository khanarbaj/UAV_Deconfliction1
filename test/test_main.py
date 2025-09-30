import unittest
import sys
import os

# Add src folder to sys.path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from collision_detection import UAV_Info, UAV_Pos, UAV_TimeWindow, UAV_TimeStamp, detect_collision

class TestMainFunctionality(unittest.TestCase):
    def setUp(self):
        # Helper to create a UAV_Info object
        self.default_path = [UAV_Pos(10, 10, 10), UAV_Pos(20, 20, 20)]
        self.default_time_window = UAV_TimeWindow(UAV_TimeStamp(2, 0), UAV_TimeStamp(2, 30))

    def test_no_collision(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test1\n")
        # UAVs with non-overlapping time windows
        primary = UAV_Info(self.default_path, UAV_TimeWindow(UAV_TimeStamp(1, 0), UAV_TimeStamp(1, 30)))
        sim = UAV_Info(self.default_path, UAV_TimeWindow(UAV_TimeStamp(2, 0), UAV_TimeStamp(2, 30)))
        import collision_detection
        collision_detection.SimulationUavInfo = [sim]
        collision_detection.SafeDistance = [50]
        detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

    def test_time_window_overlap_no_spatial_collision(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test2\n")
        # Overlapping time windows, but far apart
        primary = UAV_Info([UAV_Pos(0, 0, 0)], self.default_time_window)
        sim = UAV_Info([UAV_Pos(1000, 1000, 1000)], self.default_time_window)
        import collision_detection
        collision_detection.SimulationUavInfo = [sim]
        collision_detection.SafeDistance = [100]
        detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

    def test_time_window_and_spatial_collision(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test3\n")
        # Overlapping time windows and close positions
        primary = UAV_Info([UAV_Pos(10, 10, 10)], self.default_time_window)
        sim = UAV_Info([UAV_Pos(11, 11, 11)], self.default_time_window)
        import collision_detection
        collision_detection.SimulationUavInfo = [sim]
        collision_detection.SafeDistance = [100]
        detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

    def test_multiple_simulation_uavs(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test4\n")
        # Multiple simulation UAVs, some collide, some don't
        primary = UAV_Info([UAV_Pos(10, 10, 10)], self.default_time_window)
        sim1 = UAV_Info([UAV_Pos(10, 10, 10)], self.default_time_window)  # collision
        sim2 = UAV_Info([UAV_Pos(100, 100, 100)], self.default_time_window)  # no collision
        sim3 = UAV_Info([UAV_Pos(10, 10, 10)], UAV_TimeWindow(UAV_TimeStamp(3, 0), UAV_TimeStamp(3, 30)))  # no time overlap
        import collision_detection
        collision_detection.SimulationUavInfo = [sim1, sim2, sim3]
        collision_detection.SafeDistance = [100, 100, 100]
        detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

    def test_empty_path(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Test5\n")
        # UAV with empty path
        primary = UAV_Info([], self.default_time_window)
        sim = UAV_Info([], self.default_time_window)
        import collision_detection
        collision_detection.SimulationUavInfo = [sim]
        collision_detection.SafeDistance = [100]
        detect_collision(primary)
        print("-------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    unittest.main()
