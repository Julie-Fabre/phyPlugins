# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:52:57 2020

@author: Julie
"""

import numpy as np
from phy import IPlugin
import scipy.optimize as opt
import scipy.special as sp
import warnings

class qualityMetricsPlugin(IPlugin):
    def attach_to_controller(self, controller):
        """Note that this function is called at initialization time, *before* the supervisor is
        created. The `controller.cluster_metrics` items are then passed to the supervisor when
        constructing it."""
# frac refractory period violations, perc. missing, spatial decay, (isolation distance, l-ratio, silhouette score, d-prime, nearest-heighbour-> normalize these? and take smallest?)

        
        def fracRPV(cluster_id):
            warnings.filterwarnings("ignore")
            t = controller.get_spike_times(cluster_id).data #get spike times 
            numr = sum((np.diff(t) <= 0.002)) - sum((np.diff(t) <= 0.0005))
            #rpv = len(np.array(numr)) #get isi inferior to 2ms and superior to 0.5 ms (duplicate spikes)
            return numr/len(t)*100 if len(t) >= 2 else 0
        
        def falsePos(cluster_id):
            warnings.filterwarnings("ignore")
            t = controller.get_spike_times(cluster_id).data #get spike times
            N = len(t)
            T = np.max(t)/controller.model.sample_rate 
            a = 2*(0.002-0.0005) * N / T
            rpv = (sum(np.diff(t) <= 0.002) - sum(np.diff(t) <= 0.0005))            
            if rpv== 0:
                Fp = 0
            else:
                rts = np.roots([-1, 1 ,-rpv/a])
                Fp = np.min(rts)
                if np.isreal(Fp):
                    Fp = Fp
                else:
                    Fp = float("NaN");
            return Fp*100

        def spatialDecay(cluster_id):
            wv = controller.model.get_template_waveforms(cluster_id)
            troughs = np.amin(wv, axis=0)
            # pos = controller.model.channel_positions
            deK = [np.max(np.abs(troughs))/np.min(np.abs(troughs))]  #QQ do in order of chan distance
            return deK

#this is slow and was giving bugs when creating new clusters. more rudimentary method above instead
#        def percSpikesMissing(cluster_id):
#            warnings.filterwarnings("ignore")
#            amp = controller.get_amplitudes(cluster_id)
#            num, bins = np.histogram(amp, bins=50)
#
#            def gaussian(x, a, x0, sigma):
#                return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
#
#            def gaussian_cut(x, a, x0, sigma, xcut):
#                g = a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
#                g[x < xcut] = 0
#                return g
#
#            mean_seed = bins[np.argmax(num)]  # mode of mean_seed
#            bin_steps = np.diff(bins[:2])[0]
#            x = bins[:-1] + bin_steps / 2
#            next_low_bin = x[0] - bin_steps
#            add_points = np.flipud(np.arange(next_low_bin,
#                                             0, -bin_steps))
#            x = np.append(add_points, x)
#            num = np.append(np.zeros(len(add_points)), num)
#
#            p0 = (num.max(), mean_seed, 2 * amp.std(),
#                  np.percentile(amp, 1))
#            try:
#                popt, pcov = opt.curve_fit(gaussian_cut, x, num, p0=p0,
#                                           maxfev=10000)
#                was_fit = True
#            except:
#                was_fit = False
#                percent_missing_ndtr = float("NaN")
#            if was_fit:
##                n_fit = gaussian_cut(x, popt[0], popt[1],
##                                     popt[2], popt[3])
#                min_amplitude = popt[3]
##                n_fit_no_cut = gaussian_cut(x, popt[0], popt[1],
##                                            popt[2], 0)
##                maxs = n_fit.max()
#                # norm area calculated by fit parameters
#                norm_area_ndtr = sp.ndtr((popt[1] - min_amplitude) /
#                                         popt[2])
#                percent_missing_ndtr = 100 * (1 - norm_area_ndtr)
#            return percent_missing_ndtr

#        def percSpikesMissing(cluster_id):
#            amp = controller.get_amplitudes(cluster_id)
#            num, bins = np.histogram(amp, bins=50)
#            max(num)
#            return percent_missing_ndtr

        # Use this dictionary to define custom cluster metrics.
        # We memcache the function so that cluster metrics are only computed once and saved
        # within the session, and also between sessions (the memcached values are also saved
        # on disk).

        controller.cluster_metrics['numRPV/numSpikes'] = controller.context.memcache(fracRPV)
        controller.cluster_metrics['contamEstimate'] = controller.context.memcache(falsePos)
        controller.cluster_metrics['spatDeK'] = controller.context.memcache(spatialDecay)
#        controller.cluster_metrics['%missing'] = controller.context.memcache(percSpikesMissing)