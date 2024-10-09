# herovired_cicd_assignment

Step - 1: Created a new Repo herovired_cicd_assignment.

Step - 2: Added files for testing.

Step - 3: Added python codes to check commits.

Step - 4: Added bash code to do git pull, and move the changed files, githubSync.sh.

Step - 5: Added python code to check the latest commit, checkGithub.py.

Step - 6: Added a bash script, cronGit.sh, to run the python file, checkGithub.py, which will check latest git commit, and based on error code, if it is 0, then it will run githubSync.sh.

Step - 7: Added the file cronGit.sh to the "sudo crontab -e" like below, which will save the logs in ci_cd.txt, after running every 5 mins.

       */5 * * * * /home/devops_practice/gradedAssignmentCICD/cronGit.sh >> /home/devops_practice/gradedAssignmentCICD/ci_cd.log 2>&1

Step - 8: Cronjob was writing permission denied in log file, so ran "sudo chmod +x cronGit.sh", to give executable permission.
