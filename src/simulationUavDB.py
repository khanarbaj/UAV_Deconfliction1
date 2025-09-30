"""This file stores the simulation UAV data"""

from uav_info_def import *

"""--------------------------------------------- Simulation objects --------------------------------------------------"""
SimulationUav1Info = UAV_Info(
    [
        UAV_Pos(123, -456, 78),
        UAV_Pos(-321, 234, -89),
        UAV_Pos(400, -500, 500),
        UAV_Pos(-499, 0, 250),
        UAV_Pos(312, -123, 456),
        UAV_Pos(-250, 499, -312),
        UAV_Pos(78, -78, 123),
        UAV_Pos(-400, 400, -500),
        UAV_Pos(500, -250, 0),
        UAV_Pos(-123, 312, -456),
    ],
    UAV_TimeWindow(UAV_TimeStamp(3,0), UAV_TimeStamp(3,30))
)
SimulationUav2Info = UAV_Info(
    [
        UAV_Pos(354, -123, 487),
        UAV_Pos(-412, 299, -56),
        UAV_Pos(78, -321, 145),
        UAV_Pos(-205, 410, -499),
        UAV_Pos(312, 123, -250),
        UAV_Pos(-321, -400, 250),
        UAV_Pos(499, 78, -312),
        UAV_Pos(-78, 400, 123),
        UAV_Pos(250, -250, 0),
        UAV_Pos(-123, 312, -456)
    ],
    UAV_TimeWindow(UAV_TimeStamp(2,0), UAV_TimeStamp(2,30))
)
SimulationUav3Info = UAV_Info(
    [
        UAV_Pos(347, -101, 397),
        UAV_Pos(-229, 156, 429),
        UAV_Pos(458, -312, -122),
        UAV_Pos(-499, 0, 250),
        UAV_Pos(312, -123, 456),
        UAV_Pos(-250, 499, -312),
        UAV_Pos(78, -78, 123),
        UAV_Pos(-400, 400, -500),
        UAV_Pos(500, -250, 0),
        UAV_Pos(-123, 312, -456)
    ],
    UAV_TimeWindow(UAV_TimeStamp(4,0), UAV_TimeStamp(4,30))
)
SimulationUav4Info = UAV_Info(
    [
        UAV_Pos(523, -876, 432),
        UAV_Pos(-345, 987, -654),
        UAV_Pos(123, -456, 789),
        UAV_Pos(-234, 567, -890),
        UAV_Pos(876, -321, 543),
        UAV_Pos(-765, 432, -123),
        UAV_Pos(345, -678, 901),
        UAV_Pos(-890, 123, -456),
        UAV_Pos(678, -234, 567),
        UAV_Pos(-567, 890, -321)
    ],
    UAV_TimeWindow(UAV_TimeStamp(5,0), UAV_TimeStamp(5,30))
)

SimulationUavInfo = [SimulationUav1Info, SimulationUav2Info, SimulationUav3Info, SimulationUav4Info]