FROM python:3.12-slim
RUN apt-get update \
  && apt-get install -y gcc libpq-dev --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --no-input
EXPOSE 8000
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "pydashboard.wsgi:application"]
