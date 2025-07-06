FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pandas openpyxl matplotlib
CMD ["python", "subnet_analyzer.py", "-i", "ip_data.xlsx", "-o", "subnet_report.csv"]
