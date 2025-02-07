![img](https://github.com/glzr-io/glazewm/raw/main/resources/assets/logo.svg)

# GlazeWM Window Minimizer

Python script to minimize all displayed windows on the focused workspace in [GlazeWM](https://github.com/glzr-io/glazewm) tiling manager.

## Description
This script allows you to quickly minimize all windows on the current workspace in GlazeWM. It can be useful for clearing your desktop or switching between tasks efficiently.

## Usage
1. Build *exe* (or just see [releases](https://github.com/Pacan4ik/MinimizeAllGlazeWM/releases)):

   ```(shell)
   pyinstaller --onefile --noconsole --name=minimizeglazewm main.py
   ```

2. Copy *exe* from ./dist
3. Bind the *exe* in the config file
   ```(yaml)  
   # Minimize all windows on current workspace
   - commands: ['shell-exec ...yourpath\minimizeglazewm.exe']
     bindings: ['f13+rshift'] # Your shortcuts
   ```
