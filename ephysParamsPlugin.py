# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:28:18 2020

@author: Julie
"""

import numpy as np
from phy import IPlugin


class ephysParamsPlugin(IPlugin):
    def attach_to_controller(self, controller):
        """Note that this function is called at initialization time, *before* the supervisor is
        created. The `controller.cluster_metrics` items are then passed to the supervisor when
        constructing it."""
# isi, propISI, duration, somatic, cv2 
        def meanisi(cluster_id):
            t = controller.get_spike_times(cluster_id).data
            return np.diff(t).mean() if len(t) >= 2 else 0

        # Use this dictionary to define custom cluster metrics.
        # We memcache the function so that cluster metrics are only computed once and saved
        # within the session, and also between sessions (the memcached values are also saved
        # on disk).
        controller.cluster_metrics['meanisi'] = controller.context.memcache(meanisi)
