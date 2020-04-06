# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:39:20 2020

@author: Julie
"""

# import from plugins/action_status_bar.py
"""Show how to create new actions in the GUI.

The first action just displays a message in the status bar.

The second action selects the first N clusters, where N is a parameter that is entered by
the user in a prompt dialog.
WORK IN PROGRESS
"""

from phy import IPlugin, connect


class select10simActionPlugin(IPlugin):
    def attach_to_controller(self, controller):
        @connect
        def on_gui_ready(sender, gui):

            # Add a separator at the end of the File menu.
            # Note: currently, there is no way to add actions at another position in the menu.
            gui.Actions.separator()
            
            @gui.Actions.add(
                shortcut='ctrl+c')
            @controller.supervisor.cluster_view.get_ids
            def get_cluster_ids(cluster_ids):
                """This function is called when the ordered list of cluster ids is returned
                by the Javascript view."""

                # We select the first 10 clusters.
                controller.supervisor.select(cluster_ids[:10])