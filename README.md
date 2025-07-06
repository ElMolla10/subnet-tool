
# Barq Systems – Subnet Analysis & Visualization Tool

## Overview
This tool reads an Excel sheet of IPv4 addresses and subnet masks, calculates subnet statistics, groups them, exports a CSV (or JSON) report, and (optionally) draws a bar chart of usable hosts per subnet.

## Requirements
- Python 3.10+
- pip

### Python dependencies
```bash
pip install pandas matplotlib openpyxl
```

## Run Locally
```bash
python subnet_analyzer.py --input ip_data.xlsx --report subnet_report.csv --plot network_plot.png
```
To only generate the CSV:
```bash
python subnet_analyzer.py --input ip_data.xlsx --report subnet_report.csv --plot ""
```

## Docker
Build the image:
```bash
docker build -t subnettool .
```

Run the container (results appear in the container's `/app` folder):
```bash
docker run --rm -v $(pwd):/app subnettool
```

## File Structure
```
barq-devops-subnet-task/
├── Dockerfile
├── ip_data.xlsx
├── subnet_analyzer.py
├── visualize.py
├── subnet_report.csv
├── network_plot.png
├── report.md
└── README.md
```
