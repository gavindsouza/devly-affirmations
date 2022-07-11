import os
import json
import sys


if __name__ == "__main__":
    WORKSPACE = os.environ.get("GITHUB_WORKSPACE")
    AFFIRMATIONS_FILE = f"{WORKSPACE}/affirmations/affirmations.json"

    EXISTING_AFFIRMATIONS: list[dict] = json.loads(open(AFFIRMATIONS_FILE).read())
    USER_SUBMISSION: dict = json.loads(sys.argv[-1])
    EXISTING_AFFIRMATIONS.append(USER_SUBMISSION)

    # update affirmations file
    with open(AFFIRMATIONS_FILE, "w") as f:
        f.write(json.dumps(EXISTING_AFFIRMATIONS, indent=1))
    print(f"Updated {AFFIRMATIONS_FILE} with {USER_SUBMISSION}")
