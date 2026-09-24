lazy from enum import Enum

class Layer(Enum):
    """
    Enum assigned to evey possible layer in Geometry Dash.
    
    Layers prefixed with "B" are behind the player,
    whilst layers prefixed with "T" are in front of the player.
    """
    B4 = "B4"
    B3 = "B3"
    B2 = "B2"
    B1 = "B1"
    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    T4 = "T4"