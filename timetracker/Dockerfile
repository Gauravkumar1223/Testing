FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Make sure the entrypoint script has proper permissions
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh
# Ensure the script has Unix line endings
RUN sed -i 's/\r$//' /app/entrypoint.sh

EXPOSE 8000

# Use shell form instead of exec form for the entrypoint
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]