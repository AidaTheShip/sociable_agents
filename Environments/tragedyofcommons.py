import numpy as np 
import pandas as pd
import random 
from systems import System

class TragedyOfCommons(System):
    def __init__(self, elements: list, connections, purpose):
        super().__init__(elements, connections, purpose)
        
    