# phy plugins

Plugins to:

- add some quality metrics in phy2's clusterview: 
  - estimate of false positives (method from Hill et al., 2011, based on number of refractory period violations. Returns NaN is number of violations is too high), 
  - spatial decay (defined as trough size on peakchannel/trough size on 12th furthest away channel), 
  - percentage of spikes missing (defined by fitting a gaussian to the amplitude distributions. Returns NaN if fit is impossible, doesn't work for clusters with few spikes (<1000))

- remove some useless columns in clusterview 

- change the 'mua' color to yellow and the 'noise' color to red, for better visualization 

Copy the plugins to your .phy/plugins/ folder (usually located at C:/Users/You/.phy/plugins/ for windows users, or ~/.phy for Linux users), and modify your phy_config file located in your .phy folder to add the following lines: 


`c = get_config()`


`c.Plugins.dirs = ['C:/Users/Julie/.phy/plugins/'] `


`c.TemplateGUI.plugins = ['qualityMetricsPlugin', 'removeUselessColumnsPlugin', 'clusterViewStylingPlugin']`


