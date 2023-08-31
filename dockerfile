FROM python:3

WORKDIR /usr/app/src

COPY app.py ./
COPY requirements.txt ./
COPY env.example ./.env

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

EXPOSE 25 8090
CMD [ "python", "./app.py"]
