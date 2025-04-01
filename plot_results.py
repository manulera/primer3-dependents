from pandas import read_csv
from matplotlib import pyplot as plt

df = read_csv("final_dataset.csv", index_col=False)

print(
    "Out of {} dependent repositories, {} use a GPL license".format(
        len(df), len(df[df["license_type"] == "GPL"])
    )
)

print(
    "Out of {} dependent packages, {} use a GPL license".format(
        len(df[df["is_package"]]),
        len(df[df["is_package"] & (df["license_type"] == "GPL")]),
    )
)

plt.figure(figsize=(10, 6))
license_counts = df["license_type"].value_counts()
license_counts_packages = df[df["is_package"]]["license_type"].value_counts()

plt.bar(license_counts.index, license_counts.values)
plt.bar(license_counts_packages.index, license_counts_packages.values)
plt.legend(["All Repos", "Packages"])
plt.xlabel("License Type")
plt.ylabel("Count")
plt.title("License Type Distribution")
plt.savefig("license_distribution.png")
