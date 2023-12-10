""" This is the module to hold SeaworldConfig class """


class SeaworldConfig:
    """class for setting up config parameters"""
    def __init__(self, nfish_min, nfish_max, fish_size_min, fish_size_max,
                 nseastar_min, nseastar_max, seastar_size_min,
                 seastar_size_max, nseagrassCluster_min, nseagrassCluster_max,
                 seagrassCluster_size_min, seagrassCluster_size_max,
                 light_mode):
        """Instantiate all the config parameters for SeaworldConfig object"""
        self.nfish_min = nfish_min
        self.nfish_max = nfish_max
        self.fish_size_min = fish_size_min
        self.fish_size_max = fish_size_max
        self.nseastar_min = nseastar_min
        self.nseastar_max = nseastar_max
        self.seastar_size_min = seastar_size_min
        self.seastar_size_max = seastar_size_max
        self.nseagrassCluster_min = nseagrassCluster_min
        self.nseagrassCluster_max = nseagrassCluster_max
        self.seagrassCluster_size_min = seagrassCluster_size_min
        self.seagrassCluster_size_max = seagrassCluster_size_max
        self.light_mode = light_mode
