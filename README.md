# Activity Browser plugin : Template

An empty plugin to start from.

This repos build an empty Activity Browser template available through conda. 
It is meant to be the starting point for creating new plugins.

## Activity Browser

[The activity browser](https://github.com/LCA-ActivityBrowser/activity-browser) is an open source software for Life Cycle Assessment (LCA) that builds on top of the [Brightway2](https://brightway.dev) LCA framework.

## Test this plugin

- activate your Activity Browser conda environment
- install this plugin with conda :

```
conda install -c pan6ora ab-plugin-template
```

- start Activity Browser
- Select the plugin in plugins list

# Creating a plugin

This document will guide you through the process of creating a plugin for Activity Browser.

## 1. Setup the repository

- Go to [this repository main page](https://github.com/Pan6ora/ab-plugin-Template) and click on `Use this template`
- Give your project a name (ideally something like `ab-plugin-MyPlugin`)
- Check the `Include all branches` box
- Create the repository

The template contains 2 branches:
- `main` which is a real plugin named Template and contains this documentation
- `template` which is the branch to be completed with your project infos

After cloning your repository you need to set it up to start from the `template` branch. This can be done with the following git commands:

```
git checkout main
git reset --hard template
git push -f
git branch -d template
git push origin --delete template
```

You should now have only one branch called `main` and containing the content of the old branch `template`

## 2. Add your plugin infos

The repository already contains some files to get you started:

- `.github` and `ci` folders to deploy your plugin to Anaconda
- `ab_plugin_plugin_name` contains the plugin code
- `setup.py` file to create a python package
- basic CHANGELOG, LICENSE and README

Before starting to add functionalities to the plugin we need to fill some metadata.

### 2.1. Plugin infos

Some keywords need to be changed in multiple files. The best way of doing that might be using a Search & Replace functionality in the project folder. These are keywords to change:

- `plugin_name` (4 results in 3 files)
- `one_line_description` (3 results in 2 files)
- `plugin_url`: replace by github url (3 results in 2 files)
- `plugin_author_email` (1 result in setup.py)
- `plugin_author` (1 result in setup.py)

The name of the code folder also needs to be changed with your plugin name.

### 2.2. Deploy to Anaconda

In case you want to make your plugin available on the Anaconda packages repository you will need to set the appropriate repository secret on Github.

- Get an Anaconda token (with read and write API access) at anaconda.org/USERNAME/settings/access
- Add it to the Secrets of the Github repository as `CONDA_UPLOAD_TOKEN`

More infos about Anaconda deployment later.

### 2.3. Test

Your plugin should be ready for a test !

Open a terminal in your conda environment and install your plugin in development mode with pip:

```
pip install -e .
```

Then start activity-browser and go to `Tools>Plugins` menu. Your plugin should appear in the list. Activate it and close the window. Two tabs should appear with your plugin name.

The project path should be something like `C:\users\<user>\AppData\Local\pylca\BrightwayX`.

Delete the `\default.xxx\plugins\Template` folder and replace it by a link to your development folder.

**on OSX**

The project path should be something like `/Users/<User>/Library/Application Support/Brightway2`.

Delete the `\default.xxx\plugins\Template` folder and replace it by a link to your development folder.

