# Plugin name

[One line description]

[Multiline description]

# Activity Browser

[The activity browser](https://github.com/LCA-ActivityBrowser/activity-browser) is an open source software for Life Cycle Assessment (LCA) that builds on top of the [Brightway2](https://brightway.dev) LCA framework.

I have been working lastly on a plugin system to add functionnalities to it on-the-fly (see the [fork](https://github.com/Pan6ora/activity-browser) on github).

This repository is a basic plugin that does nothing but can serve as an example to create new ones.

# QuickStart

This section will let you get the modified version of Activity Browser and add the template plugin that works as a demo.

## Get Activity Browser with plugins 

See instructions in [Activity Browser README](https://github.com/Pan6ora/activity-browser).

## Add the template plugin

Use the _Import_ button in the **Plugins** section on the left panel. Select the file `template.plugin` from this repository.

After the import is completed you should now see 2 new tabs (one on each panel) named _Template_.

Well done ! You have imported your first plugin.

See the next section to create your own.

# Creating a plugin

If everything works you can start adding real code into the plugin.

Put your code in the `plugin` folder. We encourage you to follow th Activity Browser files tree structure and guidelines.

## What you can do

- adding content in the two tabs (sub-tabs, text, graphics...)
- adding wizards
- importing databases
- put stuff in the project folder
- connect to Activity Browser signals and generate them

## What you can't do

- modifying other tabs or GUI parts

## Hooks

In the main plugin class (defined in `__init__.py`) there is three methods:

**load** is run each time the plugin is imported or reloaded. It replaces the init method. Add your init content their and not in \__init__ .

**initialize** is run once at plugin import. Use it for example to import databases to the current project that your plugin will use.

**remove** is run once at plugin removal. Use it to clean the place (for example removing databases you had previously imported).

## Metadata

The `metadata.py` file contains the plugin description. Don't forget to change it by your own !

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

## Creating the plugin file

To create the plugin itself simply create a 7z archive of the code and rename it to `your_plugin.plugin`.


