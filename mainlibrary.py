import pandas as pd
import numpy as np
import math

def lenfunc(year) :

    newArray = []

    for x in range(len(year)) :

        newArray.append(len(year[x]))
    
    return newArray

def mostFrequent(List):
    return max(set(List), key = List.count)

