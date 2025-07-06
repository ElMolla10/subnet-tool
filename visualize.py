import pandas as pd, matplotlib.pyplot as plt

df = pd.read_csv("subnet_report.csv")
df["Subnet"] = df["Network Address"] + df["CIDR"]
agg = df.groupby("Subnet")["Usable Hosts"].first().reset_index()

plt.figure(figsize=(10,6))
plt.bar(agg["Subnet"], agg["Usable Hosts"])
plt.xticks(rotation=90, fontsize=7)
plt.ylabel("Usable Hosts")
plt.title("Hosts per Subnet")
plt.tight_layout()
plt.savefig("network_plot.png")
print("[+] network_plot.png saved – check the repo root")
