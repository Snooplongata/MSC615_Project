# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:40:44 2018

@author: Marcel
"""

from itertools import permutations
import numpy as np

def get_sample(arr, n_iter=None, sample_size = 10, fast = True):
    """
    
    """
    
    if fast:
        start_idx = (n_iter * sample_size) % n
        if start_idx + sample_size >= n:
            np.random.shuffle(arr)
        return arr[start_idx:start_idx+sample_size]
    else:
        return np.random.choice(arr, sample_size, replace = False)
    
def collect_samples(arr, sample_size, n_samples, fast = False):
    """
    
    """
    
    samples = np.zeros((n_samples + 1, sample_size), np.int32)
    
    for sample_n in range(0, n_samples):
        sample = get_sample(arr, n_inter = sample_n, sample_size = sample_size, fast = fast)
        samples[sample_n] = sample
        
    return samples

def some_func(tc):
    places = list(tc.keys())
    idx = list(range(1,len(tc.keys())+1))
    perm = permutations(idx,5)
    perm = np.array(list(perm))
    
    costs = []
    for perm_i in perm[:10]:
        total = 0
        last = 0
        for j in perm_i:
            if not last:
                total += tc["Dominoe's Pizza"][places[j]]
                last = j
            else:
                total += tc[places[last]][places[j]]
                last = j
        
        costs.append(np.hstack((total,perm_i)))  
    
    costs = np.array(costs)
    return costs

costs = some_func(transportation_costs)

def pulp_test():
    
    pass