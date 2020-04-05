# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:37:16 2020

@author: Julie
"""

from phy import IPlugin

class MyPlugin(IPlugin):
    def attach_to_controller(self, controller):
        print("Hey Julie!")