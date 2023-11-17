FROM python:3.11.3
COPY . /aplicacao
WORKDIR /aplicacao
RUN pip install -r requiremenets.txt
EXPOSE $PORT 
CMD gunicorn --WORKERS=4 --bind 0.0.0.0:$PORT aplicacao:aplicacao