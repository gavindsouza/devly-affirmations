import os
import json
import sys

WORKSPACE = os.environ.get("GITHUB_WORKSPACE")
AFFIRMATIONS_FILE = f"{WORKSPACE}/affirmations/affirmations.json"

if __name__ == "__main__":
    EXISTING_AFFIRMATIONS: list[dict] = json.loads(open(AFFIRMATIONS_FILE).read())
    USER_SUBMISSION: dict = json.loads(sys.argv[-1])
    EXISTING_AFFIRMATIONS.append(USER_SUBMISSION)

    # update affirmations file
    with open(AFFIRMATIONS_FILE, "w") as f:
        f.write(json.dumps(EXISTING_AFFIRMATIONS, indent=1))
