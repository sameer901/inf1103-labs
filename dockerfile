FROM python:3.14

WORKDIR /app

COPY auditor.py .
COPY Lab5/ ./Lab5/
CMD ["python", "Lab5/lab5.py"]

#docker run --rm -it -v "${PWD}:/app" -w /app inf1103-lab8_latest