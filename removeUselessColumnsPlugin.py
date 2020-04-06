# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:30:21 2020

@author: Julie
"""
# import from plugins/custom_columns.py
"""remove useless columns."""

from phy import IPlugin, connect


class removeUselessColumnsPlugin(IPlugin):
    def attach_to_controller(self, controller):
        @connect
        def on_controller_ready(sender):
            controller.supervisor.columns = ['id', 'n_spikes', 'depth', 'fr', 'amp', 'Fp', 'spatDeK', '%missing']

