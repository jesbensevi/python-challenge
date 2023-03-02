FROM python:3.9-alpine

WORKDIR /ms-signout

COPY ./requirements.txt  /ms-signout/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /ms-signout/requirements.txt

COPY . /app /ms-signout/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "81"]