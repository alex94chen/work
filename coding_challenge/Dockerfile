FROM python:3.11
WORKDIR /app
RUN pip install fastapi==0.68.1
RUN pip install pydantic
RUN pip install uvicorn
RUN pip install redis
ADD . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]



#FROM python:3.11
#WORKDIR /app
#ADD . /app
#RUN pip install redis
#RUN pip install fastapi==0.68.1 
#RUN pip install uvicorn
#RUN pip install httpx
#CMD ["python", "main.py"]

