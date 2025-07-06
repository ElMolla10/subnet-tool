
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir pandas matplotlib openpyxl

# Copy project files
COPY . .

# Default command
CMD ["python", "subnet_analyzer.py", "--input", "ip_data.xlsx", "--report", "subnet_report.csv", "--plot", "network_plot.png"]
