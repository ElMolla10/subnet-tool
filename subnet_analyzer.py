#!/usr/bin/env python3
"""Quick & simple subnet analyser.
   Written by a bored CS undergrad while eating instant noodles.
"""

import pandas as pd
import ipaddress
import argparse

def calc_subnet(row):
    ip   = row["IP Address"]
    mask = row["Subnet Mask"]
    net  = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
    return pd.Series({
        "CIDR": f"/{net.prefixlen}",
        "Network Address": str(net.network_address),
        "Broadcast Address": str(net.broadcast_address),
        "Usable Hosts": net.num_addresses - 2 if net.num_addresses > 2 else 0
    })

def main(in_file, out_file):
    df = pd.read_excel(in_file)  # needs openpyxl
    extra = df.apply(calc_subnet, axis=1)
    df = pd.concat([df, extra], axis=1)
    df.to_csv(out_file, index=False)
    print(f"[+] Report saved to {out_file}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Subnet Analyzer (college edition)")
    p.add_argument("-i", "--input",  default="ip_data.xlsx", help="Excel sheet with IPs")
    p.add_argument("-o", "--output", default="subnet_report.csv", help="CSV to write")
    args = p.parse_args()
    main(args.input, args.output)
