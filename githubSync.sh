#! /bin/bash
#python3 checkGitCommits.py | grep 'New changes detected' && git pull && python3 moveFiles.py ./ /var/www/html

REPO_DIR="/home/devops_practice/gradedAssignmentCICD/herovired_cicd_assignment"
WEBSITE_DIR="/var/www/awesomeweb"
# These lines set up some information about where your files are
# Pull latest changes
cd $REPO_DIR || exit
git pull origin main
# This part goes to your local copy of the website and gets the latest changes
# Copy files to website directory
rsync -av --delete $REPO_DIR/ $WEBSITE_DIR/
# This copies the new files to where Nginx can find them
# Restart Nginx
sudo systemctl restart nginx
# This restarts Nginx to make sure it sees the new files
echo "Website updated successfully"
# This prints a message saying the update is done

