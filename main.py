import numpy as np
import  random
import copy
import matplotlib.pyplot as plt
import seaborn as sns


def pop(population):
    for i in population:
        print(i)

def initial_map (p, N):
    map = np.zeros((N,N))