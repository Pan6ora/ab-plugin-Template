# Plugin name

[One line description]

[Multiline description]

# Activity Browser

The activity browser is an open source software for Life Cycle Assessment (LCA) that builds on top of the Brightway2 LCA framework.

Rémy Le Calloch <remy@lecalloch.net> has been working for the G-SCOP laboratory on a plugin manager to add functionalities to Activity-Browser. This repository is a template of plugin that can serve as an example to create new ones.

# QuickStart

Setup a dev environment and get the modified version of Activity Browser. You will need to have python3 and conda installed (as some dependencies are not on pip).

```
conda create -n local_dev -c conda-forge -c cmutel -c bsteubing activity-browser-dev
conda activate local_dev
conda remove --force activity-browser-dev
```

This create a conda environment named local_dev with all Activity Browser packages, then remove the package activity-browser itself (as we are going to launch it directly from the content of this repository).

To start Activity Browser clone the repo, switch to conda environment and run run-activity-browser.py in the plugin-manager branch.

```
git clone git@github.com:Pan6ora/activity-browser.git
git checkout plugin-manager
conda activate local_dev
python activity-browser/run-activity-browser.py
```

Activity Browser should start. A button _Import_ in the plugin section will let you import your plugin. After that two empty tabs named "Template" should appear.

# Creating a plugin

If everything works you can start adding real code into the plugin.

An example that may help you is the [plugin ReSICLED](https://espaces-collaboratifs.grenet.fr/share/s/2WXIRzOyQX6rPBc1g8peJw) created and maintained at G-SCOP laboratory. You can add it to Activity Browser to see how it works, then look at the code to help you create your own plugin.

A good idea to test as you are adding stuff may be to replace the `plugin/Template` folder in the Brightway project folder by a link to the folder you are coding into. Thus you will only have to restart Activity Browser to see your changes without importing the plugin over and over again.

To create the plugin itself simply create a 7z archive of the code and rename it to your_plugin.plugin.


