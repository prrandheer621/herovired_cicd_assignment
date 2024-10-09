#!/bin/bash
# Run the Python script to check for changes
python3 /home/devops_practice/gradedAssignmentCICD/checkGitCommits.py
# If the Python script exits with 0 (changes detected), run the update script
if [ $? -eq 0 ]; then
 sudo bash /home/devops_practice/gradedAssignmentCICD/githubSync.sh
fi
