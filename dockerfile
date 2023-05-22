FROM python:3.9-slim-buster
#FROM python:3.9-alpine



WORKDIR /code

#RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y freetds-dev build-essential

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]