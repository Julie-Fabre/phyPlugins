# Plugins for phy

Plugins to select which columns to display in phy's Cluster view, change the labeling colors and compute and display some quality metrics. 

## 🏁 Installation 

Copy the plugins to your .phy/plugins/ folder (usually located at C:/Users/You/.phy/plugins/ for windows users, or ~/.phy for Linux users), and modify your phy_config file located in your .phy folder to add the following lines: 

```
c = get_config()


c.Plugins.dirs = ['location of you .phy/plugins/ folder] (e.g. ['C:/Users/Julie/.phy/plugins/']) 


c.TemplateGUI.plugins = ['MyPlugin', 'qualityMetricsPlugin', 'removeColumnsPlugin', 'clusterViewStylingPlugin']
```

Select which columns you want to keep, by modifying the variable `controller.supervisor.columns` in `removeColumnsPlugins.py`

## Plugins
### Select which columns to display in Cluster view

The plugin `removeColumnsPlugin` select which some columns to display in clusterview (this view become very cluttered if used in conjunction with [bombcell](https://github.com/Julie-Fabre/bombcell/). Set which columns you wish to diplay in the plugin by modifying the variable `controller.supervisor.columns`. For instance, if using these plugins in conjunction with [bombcell](https://github.com/Julie-Fabre/bombcell/)), you can select the following columns: 

```
controller.supervisor.columns = ['id', 'depth', 'fr', 'Amplitude', 'n_spikes', 'fractionRPV', 'percentSpikesMissing', 
                                             '%_spikes_missing', 'presence_ratio', 'max_drift', 'n_peaks', 'n_troughs', 
                                             'is_somatic','waveform_dur', 'spatial_decay_slope','wv_baseline_flatness',
                                             'SNR','frac_RPVs']
```
  
![clus_cols](https://github.com/Julie-Fabre/phyPlugins/assets/29582008/abf70bb3-3fca-41a3-8b0c-86b0c6fe6b3a)

### Change labeling colors

To better see your manual curation labels, it can be useful to adjust the colors. The plugin `clusterViewStylingPlugin` defines which colors to use for the good, MUA and noise labels. 

![clus_colors](https://github.com/Julie-Fabre/phyPlugins/assets/29582008/e4e4a651-dcb4-4477-a438-af39a3c1690b)

### Calculate and display quality metrics
- _[not recommended: use [bombcell](https://github.com/Julie-Fabre/bombcell/) to output quality metrics instead] add some quality metrics in phy2's clusterview:_
  - _estimate of false positives (method from Hill et al., 2011, based on number of refractory period violations. Returns NaN is number of violations is too high),_ 
  - _spatial decay (defined as trough size on peakchannel/trough size on 12th furthest away channel),_
  - _percentage of spikes missing (defined by fitting a gaussian to the amplitude distributions. Returns NaN if fit is impossible, doesn't work for clusters with few spikes (<1000))_

## 🤗 Acknowledgments 

Based on some of the [wonderful examples](https://phy.readthedocs.io/en/latest/plugins/) in the phy documentation 
