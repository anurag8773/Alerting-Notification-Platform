FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

# Ensure entrypoint script is executable
RUN chmod +x /app/scripts/entrypoint.sh

# Run entrypoint.sh as the container entrypoint
ENTRYPOINT ["/app/scripts/entrypoint.sh"]
