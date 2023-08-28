# Celeste Setup Guide

## Required Software
- [Everest](https://everestapi.github.io)
- [Celeste AP Mod](https://github.com/CommandTM/celeste-ap-mod/releases)

## Mod Installation
1. Download and install Everest using [their guide](https://everestapi.github.io/#installing-everest).
2. Drag the latest stable release of the AP mod into your mods folder.

## Configuring your YAML file

### What is a YAML file and why do I need one?

Your YAML file contains a set of configuration options which provide the generator with information about how it should
generate your game. Each player of a multiworld will provide their own YAML file. This setup allows each player to enjoy
an experience customized for their taste, and different players in the same multiworld can all have different options.

### Where do I get a YAML file?

you can customize your settings by visiting
the [Celeste Settings Page](/games/Celeste/player-settings).

## Connecting to the Multiworld
1. Launch Everest with the mod enabled.
2. Find the mod's settings under the `Mod Settings` tab.
3. Change `Archipelago Address`, `Archipelago Port`, and `Archipelago Slot` to match with your Multiworld.
   - If your Multiworld has a password, change `Archipelago Password Toggle` to true and set `Archipelago Password`, otherwise leave it blank.
4. Restart Everest after saving the options.
