# Activity Browser plugin : Template

An empty plugin to start from

This repos build an empty Activity Browser template available through conda. 
It is meant to be the starting point for creating new plugins.

## Activity Browser

[The activity browser](https://github.com/LCA-ActivityBrowser/activity-browser) is an open source software for Life Cycle Assessment (LCA) that builds on top of the [Brightway2](https://brightway.dev) LCA framework.

The plugin system is currently not available on the main Activity Browser version.
See [Quickstart](#QuickStart) for how to get it.

# QuickStart

This section will let you get the modified version of Activity Browser and add the template plugin.

## Get Activity Browser with plugins 

See instructions in [Activity Browser README](https://github.com/Pan6ora/activity-browser).

## Add the template plugin

- install the plugin with conda :

```
conda install -c pan6ora ab-plugin-template
```

- start Activity Browser
- Open the menu `Tools > Plugins`
- Select the plugin and click "Save"

A new tab called "Template" should appear in the right panel.

# Creating a plugin

If everything works you can start adding real code into the plugin.

We encourage you to follow th Activity Browser files tree structure and guidelines.

## What you can do

- adding content in the two tabs (sub-tabs, text, graphics...)
- adding wizards
- importing databases
- put stuff in the project folder
- connect to Activity Browser signals and generate them

## What you can't do

- modifying other tabs or GUI parts

## Hooks

The plugin class has 4 methods that are run by AB at a certain point :

- `load()` is run each time the plugin is added tp the project or reloaded. It kind of replaces the init method.
- `close()` is run when AB get closed.Put there the code to end your plugin properly.
- `remove()` is run when the plugin is removed from the current project. Use it to clean the place.
- `delete()` is run when the plugin is fully removed from AB.

## Coding "in place"

When developing a plugin it is painful to import it every time you want to test your work (don't forget to test the import tho).

To avoid doing so you could replace the plugin code in your Brightway project by a link to your development folder.

After that you will only have to restart Activity Browser to see your changes without importing the plugin over and over again.

**on Linux**

The project path should be something like `$HOME/.local/share/Brightway3`. 

Creating the link should look like:

```
rm -rf $HOME/.local/share/BrightwayX/default.xxxx/plugins/*
ln -rs ./ $HOME/.local/share/BrightwayX/default.xxxx/plugins/Template
```

**on windows**

The project path should be something like `C:\users\<user>\AppData\Local\pylca\BrightwayX`.

Delete the `\default.xxx\plugins\Template` folder and replace it by a link to your development folder.

**on OSX**

The project path should be something like `/Users/<User>/Library/Application Support/Brightway2`.

Delete the `\default.xxx\plugins\Template` folder and replace it by a link to your development folder.

