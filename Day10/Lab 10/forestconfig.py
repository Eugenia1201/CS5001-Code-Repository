""" This is the module to hold ForestConfig class """


class ForestConfig:
    """class for setting up config parameters"""
    def __init__(self, nkids_min, nkids_max, kid_size_min, kid_size_max,
                 ntrees_min, ntrees_max, tree_size_min, tree_size_max,
                 nflyer_min, nflyer_max, flyer_size_min, flyer_size_max):
        """Instantiate all the config parameters for ForestConfig object"""
        self.nkids_min = nkids_min
        self.nkids_max = nkids_max
        self.kid_size_min = kid_size_min
        self.kid_size_max = kid_size_max
        self.ntrees_min = ntrees_min
        self.ntrees_max = ntrees_max
        self.tree_size_min = tree_size_min
        self.tree_size_max = tree_size_max
        self.nflyer_min = nflyer_min
        self.nflyer_max = nflyer_max
        self.flyer_size_min = flyer_size_min
        self.flyer_size_max = flyer_size_max
