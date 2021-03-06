import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../AnnoDomini')))

#from AnnoDomini.AutoDiff import AutoDiff as AD
from AnnoDomini.AutoDiff import AutoDiff as AD
from AnnoDomini.newtons_method import Newton
import numpy as np

def test_newton():
    x0 = -3
    f = lambda x: x**2 + 2*x + 1
    demo = Newton(f,x0)
    root_est = demo.find_root()
    real_root = -1
    assert np.round(real_root,2) == np.round(root_est,2)
