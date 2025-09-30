
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

class UAV_DetectedDistance:
    def __init__(self, x_distance, y_distance, z_distance):
        self.x_distance = x_distance
        self.y_distance = y_distance
        self.z_distance = z_distance
