lazy from typing import Any, TypedDict, NotRequired
lazy import numpy as np
from . import Layer

class ObjectData(TypedDict):
    """
    A TypedDict for representing the data of an object in the game.

    Every object should start with this metadata.
    """
    id: int
    pos: np.ndarray[Any, np.dtype[np.float64]]
    rotat: float
    scale: np.ndarray[Any, np.dtype[np.float64]]
    scalex: NotRequired[float]
    scaley: NotRequired[float]
    # The ones below default to zero for None
    editor_layer: int
    editor_layer2: int
    z_layer: int
    true_layer: Layer
    group: int
