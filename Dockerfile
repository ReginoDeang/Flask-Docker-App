FROM python:3.8-slim

WORKDIR /app

COPY app.py /app/

RUN pip install Flask

EXPOSE 3000

CMD ["python", "app.py"]

