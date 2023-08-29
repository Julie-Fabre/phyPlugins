
Plugins to:

- add some quality metrics in phy2's clusterview: 
  - estimate of false positives (method from Hill et al., 2011, based on number of refractory period violations. Returns NaN is number of violations is too high), 
  - spatial decay (defined as trough size on peakchannel/trough size on 12th furthest away channel), 
  - percentage of spikes missing (defined by fitting a gaussian to the amplitude distributions. Returns NaN if fit is impossible, doesn't work for clusters with few spikes (<1000))

- remove some columns in clusterview (this view become very cluttered if used in conjunction with [bombcell](https://github.com/Julie-Fabre/bombcell/)
  
![clus_cols](https://github.com/Julie-Fabre/phyPlugins/assets/29582008/abf70bb3-3fca-41a3-8b0c-86b0c6fe6b3a)


- change the 'mua' color to yellow and the 'noise' color to red, for better visualization

![clus_colors](https://github.com/Julie-Fabre/phyPlugins/assets/29582008/e4e4a651-dcb4-4477-a438-af39a3c1690b)


Copy the plugins to your .phy/plugins/ folder (usually located at C:/Users/You/.phy/plugins/ for windows users, or ~/.phy for Linux users), and modify your phy_config file located in your .phy folder to add the following lines: 

```
c = get_config()


c.Plugins.dirs = ['location of you .phy/plugins/ folder] (e.g. ['C:/Users/Julie/.phy/plugins/']) 


c.TemplateGUI.plugins = ['MyPlugin', 'qualityMetricsPlugin', 'removeColumnsPlugin', 'clusterViewStylingPlugin']
```

Select which columns you want to keep, by modifying the variable `controller.supervisor.columns` in `removeColumnsPlugins.py`

Based on wonderful examples in the phy documentation. 
