class StationNode:
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits


station_0 = StationNode('교대역', 14)
station_1 = StationNode('사당영', 14)
station_2 = StationNode('종로3가역', 16)
station_3 = StationNode('서울역', 16)

stations = [station_0, station_1, station_2, station_3]

stations = {
    '교대역': station_0,
    '사당역': station_1,
    '종로3가역': station_2,
    '서울역': station_3,
}
