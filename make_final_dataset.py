from pandas import read_csv

with open("packages.txt", "r") as f:
    package_names = f.read().splitlines()


def get_license_type(license_name):
    if license_name == "":
        return "None"
    elif "MIT" in license_name:
        return "MIT"
    elif "Apache" in license_name:
        return "Apache"
    elif "BSD" in license_name:
        return "BSD"
    elif "GNU" in license_name:
        return "GPL"
    else:
        return "Other"


def is_package(repo_name):
    return repo_name in package_names


df = read_csv("license_names.csv", index_col=False, keep_default_na=False)


df["license_type"] = df["license"].apply(get_license_type)
df["is_package"] = df["repo"].apply(is_package)

df.to_csv("final_dataset.csv", index=False)
