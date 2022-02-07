# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:36:47 2022

@author: Zaid
"""

import NeuroPy
from threading import Thread
from time import time, sleep
from multiprocessing import Process
import csv
from itertools import zip_longest
from time import sleep
import pyautogui
import threading

attentionV = []
rawV = []
meditationV = []
lowalphaV = []
lowbetaV = []
lowgammaV = []
highalphaV = []
highbetaV = []
X = []
Y = []
delta_x = []
delta_y = []
label = []
N=NeuroPy.NeuroPy.NeuroPy("COM6",57600)
def data():
    sleep(1.4)
    while t1.is_alive():
        sleep(0.8)
        attentionV.append(N.attention)
        meditationV.append(N.meditation)
        lowalphaV.append(N.lowAlpha)
        lowbetaV.append(N.lowBeta)
        lowgammaV.append(N.lowAlpha)
        highalphaV.append(N.highAlpha)
        highbetaV.append(N.highBeta)
        x = pyautogui.position().x
        y = pyautogui.position().y
        X.append(x)
        Y.append(y)
