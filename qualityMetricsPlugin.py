# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:52:57 2020

@author: Julie
"""

import numpy as np
from phy import IPlugin


class qualityMetricsPlugin(IPlugin):
    def attach_to_controller(self, controller):
        """Note that this function is called at initialization time, *before* the supervisor is
        created. The `controller.cluster_metrics` items are then passed to the supervisor when
        constructing it."""
# frac refractory period violations, isolation distance, l-ratio, silhouette score, 

        
        def fracRPV(cluster_id):
            t = controller.get_spike_times(cluster_id).data #get spike times 
            rpv = np.size(sum(np.diff(t) <= 0.002) - sum(np.diff(t) <= 0.0005)) #get isi inferior to 2ms and superior to 0.5 ms (duplicate spikes)
            return rpv/len(t) if len(t) >= 2 else 0
        
        def fracRPVEstimate(cluster_id):
            t = controller.get_spike_times(cluster_id).data #get spike times
            N = len(t)
            T = np.max(t)/30000 #hard-coded, i should change this!
            a = 2*(0.002-0.0005) * N / T
            rpv = np.size(sum(np.diff(t) <= 0.002) - sum(np.diff(t) <= 0.0005))
            
            if rpv== 0:
                Fp = 0
            else:
                rts = np.roots([-1, 1 ,-rpv/a])
                Fp = np.min(rts)
                if np.isreal(Fp):
                    Fp=Fp
                else:
                    Fp = float("NaN");
                    


            return Fp

        # Use this dictionary to define custom cluster metrics.
        # We memcache the function so that cluster metrics are only computed once and saved
        # within the session, and also between sessions (the memcached values are also saved
        # on disk).

        controller.cluster_metrics['fracRPV'] = controller.context.memcache(fracRPV)
        controller.cluster_metrics['fracRPVEstimate'] = controller.context.memcache(fracRPVEstimate)