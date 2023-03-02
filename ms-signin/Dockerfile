FROM python:3.9-alpine

WORKDIR /ms-signin

COPY ./requirements.txt  /ms-signin/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /ms-signin/requirements.txt

COPY . /app /ms-signin/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]