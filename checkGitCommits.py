import requests, os, sys

# GitHub repository details
REPO_OWNER = 'prrandheer621'
REPO_NAME = 'herovired_cicd_assignment'
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits'
# File to store the last commit SHA
LAST_COMMIT_FILE = '/home/devops_practice/gradedAssignmentCICD/lastCommit.txt'

def get_latest_commit():
  response = requests.get(GITHUB_API_URL)
  if response.status_code == 200:
    commits = response.json()
    return commits[0]['sha']
  else:
    print(f"Failed to fetch commits: {response.status_code}")
    return None

def get_stored_commit():
  if os.path.exists(LAST_COMMIT_FILE):
    with open(LAST_COMMIT_FILE, 'r') as f:
      stored_commit = f.read().strip()
      f.close()
      return stored_commit
  return None

def update_stored_commit(latest_commit):
  with open(LAST_COMMIT_FILE, 'w') as f:
    f.write(latest_commit)
    f.close()

def main():
  latest_commit = get_latest_commit()
  if not latest_commit:
    sys.exit(1)
  stored_commit = get_stored_commit()
  if latest_commit != stored_commit:
    print("New changes detected")
    update_stored_commit(latest_commit)
    sys.exit(0)
  else:
    print("No new changes")
    sys.exit(1)


if __name__ == "__main__":
  main()
