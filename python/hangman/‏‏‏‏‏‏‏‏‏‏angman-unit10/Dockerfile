FROM python:3.11
WORKDIR /app
ADD . /app
RUN pip install pytest
EXPOSE 7777
CMD ["python", "main.py"]