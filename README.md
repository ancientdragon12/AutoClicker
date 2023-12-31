# AutoClicker

## Overview
This Python script implements a simple autoclicker using the `mouse` and `keyboard` libraries. The autoclicker clicks repeatedly based on user-defined input and allows for starting, stopping, and killing the autoclicker through keyboard commands.

## Requirements
- Python 3.x
- `mouse` and `keyboard` libraries (install via `pip install mouse keyboard`)

## Usage
1. Install the required Python libraries if you haven't already:

    ```bash
    pip install mouse keyboard
    ```

2. Run the `autoclicker.py` script:

    ```bash
    python autoclicker.py
    ```

3. While the script is running:
   - Press `r` to start/restart the autoclicker.
   - Press `s` to stop the autoclicker.
   - Press `k` to kill the program.

## Important Notes
- Use this autoclicker responsibly and ensure compliance with the rules and terms of service of the applications you interact with.
- Be cautious when using autoclickers in gaming or other applications to avoid unintended consequences or rule violations.

## Additional Information
- The autoclicker uses threads to simultaneously monitor keyboard input and perform clicking actions.
- Keyboard interrupts (Ctrl+C) will stop the program and terminate the autoclicker.
