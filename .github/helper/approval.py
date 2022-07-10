import sys
import os
import requests

ISSUE_NUMBER = os.environ.get("ISSUE_NUMBER") # "1200"
GITHUB_REPOSITORY  = os.environ.get("GITHUB_REPOSITORY") # "octocat/Hello-World"

if __name__ == "__main__":
    ENDPOINT_URL = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/issues/{ISSUE_NUMBER}/comments"
    COLLABORATOR_URL = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/collaborators/{{username}}"
    ISSUE_COMMENTS = requests.get(ENDPOINT_URL).json()

    for comment in ISSUE_COMMENTS:
        username = comment["user"]["login"]
        comment_body = comment["body"]

        if "LGTM" not in comment_body:
            continue

        is_collaborator = requests.get(COLLABORATOR_URL.format(username=username)).ok

        if is_collaborator:
            sys.exit(0) # exit with success code if a collaborator has dropped a LGTM comment

    sys.exit(1) # exit with error code if no collaborator has approved the affirmation
