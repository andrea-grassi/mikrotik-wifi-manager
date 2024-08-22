# MikroTik WiFi Manager

## Overview

MikroTik WiFi Manager is a simple Python GUI application that allows users to enable or disable the WiFi interface on a MikroTik router via SSH. This tool is especially useful for quickly managing WiFi settings without needing to log into the router's web interface or use terminal commands.

## Features

- **Enable WiFi**: Turn on the wireless interface with a single click.
- **Disable WiFi**: Turn off the wireless interface with a single click.
- **User-Friendly Interface**: Simple GUI with buttons for quick actions.
- **Cross-Platform**: Works on macOS and can be easily adapted for other platforms.

## Important Note

- **LAN Connection**: If you want to turn On WiFi, ensure that the device running this application is connected to the router via a LAN (Ethernet) connection or ensure that is connected to another access point of the same network. Instead, if you want to turn off the wireless network, since the application disables the WiFi interface, you may lose connectivity if you are connected via WiFi. Always use a LAN connection when running this tool to avoid being disconnected from the router.

## Prerequisites

Before running this application, make sure your system is set up with the following:

1. **Python 3.x**: Ensure Python 3.x is installed on your system.

   - You can check if Python is installed by running `python3 --version` in the terminal.
   - If not installed, download and install it from [python.org](https://www.python.org/).

2. **pip**: Ensure `pip` (Python's package installer) is installed.

   - You can check if `pip` is installed by running `pip3 --version` in the terminal.
   - If not installed, it comes bundled with Python 3.x, or you can install it using the command `sudo easy_install pip`.

3. **Paramiko**: Install the `paramiko` library, which is used for SSH connections.

   - Run the following command in the terminal:
     ```bash
     pip3 install paramiko
     ```

4. **PyInstaller** (Optional for building the executable):
   - Run the following command in the terminal:
     ```bash
     pip3 install pyinstaller
     ```

## How to Run the Application

1. **Clone the Repository (complete project) or download only mikrotik-wifi-manager.py**:

   - Open your terminal and run:
     ```bash
     git clone https://github.com/your-username/mikrotik-wifi-manager.git
     ```
   - Navigate to the directory:
     ```bash
     cd mikrotik-wifi-manager
     ```

2. **Configuration**:

   - Ensure your MikroTik router is accessible over SSH.
   - Modify the `router_ip`, `username`, and `password` variables in `wifi_manager_gui.py` to match your router’s configuration.

3. **Running the Script**:

   - To run the script directly, use the following command:
     ```bash
     python3 wifi_manager_gui.py
     ```

4. **(Optional) Create a Standalone Executable**:

   - If you want to create a standalone executable that can be run with a double-click, use `PyInstaller`:
     ```bash
     pyinstaller --onefile --windowed wifi_manager_gui.py
     ```
   - The executable will be located in the `dist` folder.

## Usage

1. **Double-click the Executable**:

   - If you've created a standalone executable, simply double-click it to open the application.

2. **Enable/Disable WiFi**:

   - Click on the **"Turn WiFi On"** button to enable the wireless interface.
   - Click on the **"Turn WiFi Off"** button to disable the wireless interface.
   - You will receive a success or error message based on the outcome.

3. **LAN Connection Reminder**:
   - **Always ensure your device is connected to the router via LAN (Ethernet) before using this tool.**
   - This precaution is necessary because disabling the WiFi interface will disconnect devices connected via WiFi, potentially making the router inaccessible.

## Troubleshooting

- **SSH Connection Issues**: If you encounter errors related to SSH connections, ensure that:

  - The SSH service is enabled on your MikroTik router.
  - The correct username and password are provided.
  - Your router’s IP address is accessible from your machine.

- **Executable Not Running**: If the standalone executable doesn't run:
  - Ensure it has the correct permissions: `chmod +x dist/wifi_manager_gui`.
  - Verify that you’re running it on a compatible version of macOS.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

---

_Happy Networking!_ 🚀
