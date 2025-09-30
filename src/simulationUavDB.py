"""This file stores the simulation UAV data"""
from uav_info_def import UAV_TimeStamp, UAV_TimeWindow, UAV_Pos, UAV_Info

"""--------------------------------------------- Simulation objects --------------------------------------------------"""
SimulationUav1Info = UAV_Info(
    [
        UAV_Pos(10, 11, 12),
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
    UAV_TimeWindow(UAV_TimeStamp(2,0), UAV_TimeStamp(2,31))
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