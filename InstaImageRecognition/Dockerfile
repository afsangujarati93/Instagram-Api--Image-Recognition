#FROM python:3.6-alpine3.6 
#FROM rcarmo/alpine-python:3.5-onbuild
FROM rcarmo/alpine-python:3.6
# dependencies into the virtualenv.
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app

ENTRYPOINT gunicorn -b 0.0.0.0:8000 InstaImageRecognition.wsgi 
CMD python manage.py
EXPOSE 8000