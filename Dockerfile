FROM python:3.12-alpine 

WORKDIR /app 

RUN apk add --no-cache gcc musl-dev linux-headers 
COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . . 
EXPOSE 5000 
CMD ["python","app.py"]
