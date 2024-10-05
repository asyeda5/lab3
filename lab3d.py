#!/usr/bin/env python3
'''Lab 3 Part 2 script - free disk space'''
# Author ID: asyeda5
import subprocess
def free_space():
    # Launch the command and get the output
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()

    # Check for errors
    if error:
        return 'Error: ' + error.decode('utf-8').strip()

    # Decode and process the output
    output_str = output.decode('utf-8').strip()
    
    # Split output by lines and find the line for root filesystem
    lines = output_str.split('\n')
    for line in lines:
        if line.endswith('/'):
            # Extract the free space (4th column)
            return line.split()[3]
if __name__ == '__main__':
    print(free_space())

