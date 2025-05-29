FROM python:3.10
WORKDIR /app
COPY . .
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "multitenant_project.wsgi:application", "--bind", "0.0.0.0:8000"]
