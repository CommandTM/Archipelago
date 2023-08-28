# Celeste Setup Guide

## Required Software
- [Everest](https://everestapi.github.io)
- [Celeste AP Mod](https://github.com/CommandTM/celeste-ap-mod/releases)

## Mod Installation
1. Download and install Everest using [their guide](https://everestapi.github.io/#installing-everest).
2. Drag the latest stable release of the AP mod into your mods folder.
3. Launch the game once to initalize the mod.

## Configuring your YAML file

### What is a YAML file and why do I need one?

Your YAML file contains a set of configuration options which provide the generator with information about how it should
generate your game. Each player of a multiworld will provide their own YAML file. This setup allows each player to enjoy
an experience customized for their taste, and different players in the same multiworld can all have different options.

### Where do I get a YAML file?

you can customize your settings by visiting
the [Celeste Settings Page](/games/Celeste/player-settings).

## Connecting to the Multiworld
1. Navigate to your saves folder inside the game directory.
2. Find the `modsettings-APCeleste.celeste` file and open it inside a text editor.
3. Change `ArchipelagoAddress`, `ArchipelagoPort`, and `ArchipelagoSlot` to match with your Multiworld.
   - If your Multiworld has a password, change `ArchipelagoPassword`, otherwise leave it blank.
4. Launch Celeste with Everest and your game should connect on start-up.
