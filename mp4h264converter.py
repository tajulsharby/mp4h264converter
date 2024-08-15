import os
import subprocess
import re
import logging
from datetime import datetime

# Setup logging
log_filename = 'conversion_log.txt'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize counters and summary list
successful_conversions = []
failed_conversions = []

# Function to convert a single file and display progress as a percentage
def convert_to_h264(input_file, output_file):
    try:
        # Get the duration of the video
        result = subprocess.run([
            'ffmpeg', '-i', input_file], stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        duration_pattern = re.compile(r'Duration: (\d+):(\d+):(\d+\.\d+)')
        duration_match = duration_pattern.search(result.stderr)
        
        if duration_match:
            hours = int(duration_match.group(1))
            minutes = int(duration_match.group(2))
            seconds = float(duration_match.group(3))
            total_duration = hours * 3600 + minutes * 60 + seconds
        else:
            raise ValueError("Could not find duration of the video.")

        # Print the file being converted
        print(f"Converting: {input_file}")

        # Start the FFmpeg process for conversion
        process = subprocess.Popen([
            'ffmpeg',
            '-i', input_file,
            '-vcodec', 'libx264',
            '-acodec', 'aac',
            output_file
        ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        time_pattern = re.compile(r'time=(\d+):(\d+):(\d+\.\d+)')
        
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                # Extract the current processing time from the FFmpeg output
                time_match = time_pattern.search(output)
                if time_match:
                    elapsed_hours = int(time_match.group(1))
                    elapsed_minutes = int(time_match.group(2))
                    elapsed_seconds = float(time_match.group(3))
                    elapsed_time = elapsed_hours * 3600 + elapsed_minutes * 60 + elapsed_seconds
                    
                    # Calculate the percentage of completion
                    progress = (elapsed_time / total_duration) * 100
                    print(f"Progress: {progress:.2f}% completed", end='\r')
        
        process.wait()
        
        # Check if the conversion was successful
        if process.returncode == 0:
            file_size = os.path.getsize(output_file)
            successful_conversions.append((output_file, file_size))
            logging.info(f'Successfully converted: {input_file} -> {output_file}')
            print(f"\nCompleted: {input_file}")
        else:
            raise subprocess.CalledProcessError(process.returncode, process.args)
    
    except subprocess.CalledProcessError as e:
        failed_conversions.append(input_file)
        logging.error(f'Error converting {input_file}: {e}')
        print(f"\nFailed: {input_file}")
    
    except ValueError as ve:
        failed_conversions.append(input_file)
        logging.error(f'Error processing {input_file}: {ve}')
        print(f"\nFailed: {input_file}")

# Function to recursively find and convert MP4 files
def process_folder(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.mp4'):
                relative_path = os.path.relpath(root, source_folder)
                destination_dir = os.path.join(destination_folder, relative_path)
                os.makedirs(destination_dir, exist_ok=True)

                input_path = os.path.join(root, file)
                output_path = os.path.join(destination_dir, file)
                
                convert_to_h264(input_path, output_path)

# Function to generate summary text file
def generate_summary():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    summary_filename = f'{timestamp}_summary.txt'
    
    with open(summary_filename, 'w') as summary_file:
        summary_file.write('Conversion Summary\n')
        summary_file.write('===================\n\n')
        
        summary_file.write('Successful Conversions:\n')
        for file_path, file_size in successful_conversions:
            summary_file.write(f'{file_path} - {file_size / (1024*1024):.2f} MB\n')
        
        summary_file.write(f'\nTotal successful conversions: {len(successful_conversions)}\n')
        
        summary_file.write('\nFailed Conversions:\n')
        for file_path in failed_conversions:
            summary_file.write(f'{file_path}\n')
        
        summary_file.write(f'\nTotal failed conversions: {len(failed_conversions)}\n')
    
    logging.info(f'Summary file created: {summary_filename}')

# Prompt the user to enter the source and destination paths
source_folder = input("Enter the source folder path: ")
destination_folder = input("Enter the destination folder path: ")

try:
    # Start processing the target folder
    process_folder(source_folder, destination_folder)
finally:
    # Generate the summary file
    generate_summary()
