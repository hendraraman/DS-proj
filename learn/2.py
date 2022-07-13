# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 20:39:56 2022

@author: home
"""
path = "C:/Hendra/learn/chromedriver"
import glassdoor_scraper as gs
import pandas as pd
df = gs.get_jobs("data scientist", 15, False, path,15 )