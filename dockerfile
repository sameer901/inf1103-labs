FROM python:3.14

WORKDIR /app

COPY auditor.py .

CMD ["python", "Lab5/lab5.py"]

#docker run --rm -it -v "${PWD}:/app" -w /app lab5-inventory-final