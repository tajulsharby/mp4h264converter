# mp4h264converter

## Author
**Name:** TJ S  
**GitHub:** [https://github.com/tajulsharby](https://github.com/tajulsharby)  
**LinkedIn:** [https://www.linkedin.com/in/tajulsharby/](https://www.linkedin.com/in/tajulsharby/)

## Description
`mp4h264converter` is a Python script designed to batch convert all `.mp4` files within a specified directory (including subfolders) to H.264 encoded `.mp4` files using FFmpeg. The script preserves the original directory structure and provides real-time progress updates as each file is converted.

### Features:
- Recursively processes all `.mp4` files in the source directory and its subdirectories.
- Displays conversion progress as a percentage completed.
- Logs conversion activities and errors to a `conversion_log.txt` file.
- Generates a summary report at the end of the process, listing the paths and sizes of successfully converted files, as well as any failed conversions.
- Simple and user-friendly interface.

If you like this project, please consider buying me a coffee through the Touch N Go QR code link below:  
[https://github.com/tajulsharby/treat-me-a-coffee-tng](https://github.com/tajulsharby/treat-me-a-coffee-tng)

## Prerequisites
- Python 3.x
- FFmpeg

## Installation

### Windows

1. **Install Python:**
   - Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Make sure to add Python to your system PATH during the installation.

2. **Install FFmpeg:**
   - Open PowerShell and install FFmpeg using `winget`:
     ```sh
     winget install ffmpeg
     ```
   - Restart PowerShell after installation to make sure FFmpeg is recognized in the PATH.

3. **Clone the Repository:**
   - Clone this repository using Git or download the ZIP file and extract it:
     ```sh
     git clone https://github.com/tajulsharby/mp4h264converter.git
     ```

### Linux

1. **Install Python:**
   - Python is usually pre-installed on most Linux distributions. To check if Python is installed, run:
     ```sh
     python3 --version
     ```
   - If Python is not installed, you can install it using your package manager:
     ```sh
     sudo apt-get install python3
     ```

2. **Install FFmpeg:**
   - Install FFmpeg using your package manager:
     ```sh
     sudo apt-get install ffmpeg
     ```

3. **Clone the Repository:**
   - Clone this repository using Git:
     ```sh
     git clone https://github.com/tajulsharby/mp4h264converter.git
     ```

### macOS

1. **Install Python:**
   - Python 3 can be installed via Homebrew:
     ```sh
     brew install python
     ```

2. **Install FFmpeg:**
   - Install FFmpeg via Homebrew:
     ```sh
     brew install ffmpeg
     ```

3. **Clone the Repository:**
   - Clone this repository using Git:
     ```sh
     git clone https://github.com/tajulsharby/mp4h264converter.git
     ```

## Usage
1. **Navigate to the Script Directory:**
   - Open your terminal or command prompt and navigate to the directory containing the script:
     ```sh
     cd path/to/mp4h264converter
     ```

2. **Run the Script:**
   - Run the script using Python:
     ```sh
     python3 mp4h264converter.py
     ```

3. **Enter Paths:**
   - When prompted, enter the source folder path where your `.mp4` files are located.
   - Enter the destination folder path where you want the converted files to be saved.

4. **Check Logs and Summary:**
   - After the script completes, check the `conversion_log.txt` file for detailed logs.
   - A summary file named `<timestamp>_summary.txt` will be generated, containing details of the conversions.

## Important Note on Lengthy Conversion Tasks

If your conversion tasks are lengthy and may take hours to complete, please be aware that the process will be paused if your computer goes to sleep. This could significantly delay the completion of your conversions.

### How to Prevent the Computer from Sleeping

To ensure the conversion process completes without interruptions, you can temporarily disable sleep mode or use a script to keep your computer awake while the conversion is running.

#### Windows

1. **Temporarily Disable Sleep Mode:**
   - Go to *Settings > System > Power & sleep*.
   - Set "Sleep" to "Never" for both "On battery power" and "When plugged in" (you can revert this after the conversion is done).

2. **Use a Command to Prevent Sleep:**
   - You can use `powercfg` to prevent sleep during conversion:
     ```sh
     powercfg /change standby-timeout-ac 0
     powercfg /change monitor-timeout-ac 0
     ```
   - These commands disable sleep and monitor timeout. Revert the settings after the task is done by resetting the values.

#### macOS

1. **Temporarily Disable Sleep Mode:**
   - Go to *System Preferences > Energy Saver*.
   - Drag the slider to "Never" under "Turn display off after" (you can revert this after the conversion is done).

2. **Use `caffeinate` to Prevent Sleep:**
   - Run the conversion script with the `caffeinate` command to prevent the system from sleeping:
     ```sh
     caffeinate -i python3 mp4h264converter.py
     ```
   - This command will keep the computer awake as long as the conversion script is running.

### Summary
For lengthy tasks, it is recommended to ensure your computer does not enter sleep mode to avoid pausing the conversion process. After the conversion is complete, remember to revert any changes to your sleep settings.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
