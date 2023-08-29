# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:28:30 2020

@author: Julie
"""

# import from plugins/cluster_view_styling.py
"""Change mua color to yellow and noise to red for easy visualization. Slightly modified from an example here: https://phy.readthedocs.io/en/latest/plugins/"""

from phy import IPlugin
from phy.cluster.supervisor import ClusterView


class clusterViewStylingPlugin(IPlugin):
    def attach_to_controller(self, controller):
        # We add a custom CSS style to the ClusterView.
        ClusterView._styles += """

            /* This CSS selector represents all rows for good clusters. */
            table tr[data-group='good'] {

                /* We change the text color. Many other CSS attributes can be changed,
                such as background-color, the font weight, etc. */
                color: #2BBD28;
                font-weight: bold;
            }

        """
        ClusterView._styles += """

            /* This CSS selector represents all rows for good clusters. */
            table tr[data-group='mua'] {

                /* We change the text color. Many other CSS attributes can be changed,
                such as background-color, the font weight, etc. */
                color: #9C874A;
            }

        """
        ClusterView._styles += """

            /* This CSS selector represents all rows for good clusters. */
            table tr[data-group='noise'] {

                /* We change the text color. Many other CSS attributes can be changed,
                such as background-color, the font weight, etc. */
                color: #D92061;
            }

        """
