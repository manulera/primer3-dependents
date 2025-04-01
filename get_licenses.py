import requests
import os
from pandas import DataFrame

# Load GitHub access token from environment variable
ACCESS_TOKEN = os.getenv("GITHUB_TOKEN")
if not ACCESS_TOKEN:
    raise ValueError("Please set the GITHUB_TOKEN environment variable")


# Constants
GITHUB_API_URL = "https://api.github.com"
REPO = "libnano/primer3-py"


def get_repo_license(repo_full_name):
    repo_url = f"{GITHUB_API_URL}/repos/{repo_full_name}"
    headers = {"Authorization": f"token {ACCESS_TOKEN}"}
    response = requests.get(repo_url, headers=headers)

    print(repo_full_name)
    if response.status_code == 200:
        repo_data = response.json()
        if repo_data["license"] is not None:
            return repo_data["license"]["name"]
        else:
            return ""
    else:
        print(f"Failed to fetch repo license: {response.status_code}")
        return None


def main():
    with open("dependents.txt", "r") as f:
        dependents = f.read().splitlines()
    license_names = [get_repo_license(dependent) for dependent in dependents]
    df = DataFrame({"repo": dependents, "license": license_names})
    df.to_csv("license_names.csv", index=False)


if __name__ == "__main__":
    main()
