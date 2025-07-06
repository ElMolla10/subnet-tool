
# Subnet Analysis Answers

## 1. Which subnet has the most hosts?

The following /22 networks tie for the highest number of usable hosts (1,022 each):

- 10.15.4.0/22
- 10.2.0.0/22
- 10.20.4.0/22
- 10.3.0.0/22
- 172.16.48.0/22
- 172.16.60.0/22
- 192.168.100.0/22
- 192.168.20.0/22

## 2. Are there any overlapping subnets?

No. A pair‑wise overlap check across all 25 subnets returned **zero** overlaps.

## 3. What is the smallest and largest subnet in terms of address space?

| Size | CIDR(s) | Total addresses | Usable hosts |
|------|---------|-----------------|--------------|
| **Smallest** | Ten /24 networks such as 10.0.3.0/24, 172.16.20.0/24, 192.168.1.0/24 | 256 | 254 |
| **Largest** | The eight /22 networks listed in answer #1 | 1,024 | 1,022 |

## 4. Suggested subnetting strategy to reduce wasted IPs

The current address plan uses mostly class‑like /22–/24 blocks but allocates only **one** host per subnet in the dataset. Implementing **Variable‑Length Subnet Masking (VLSM)** would allow you to:

1. Split the large /22 and /23 networks into just‑big‑enough sub‑prefixes (/29 to /27) based on host count.
2. Reserve a small pool (e.g., /28) in each region for future growth.
3. Aggregate prefixes on router interfaces (using route summarization) so routing tables stay small.
4. Document the plan in an IPAM system to avoid accidental overlaps.

This reduces address waste while maintaining hierarchical summarization.
