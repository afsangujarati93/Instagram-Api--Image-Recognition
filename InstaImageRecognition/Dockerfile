#FROM python:3.6-alpine3.6 
#FROM rcarmo/alpine-python:3.5-onbuild
#FROM rcarmo/alpine-python:3.6
#FROM continuumio/anaconda3
FROM continuumio/miniconda3
#FROM condatest/linux-64-python-3.6
# dependencies into the virtualenv.
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app

ENTRYPOINT gunicorn -b 0.0.0.0:8000 InstaImageRecognition.wsgi  -t 240
#CMD python -u manage.py
RUN python manage.py collectstatic --noinput
CMD python manage.py runserver
EXPOSE 8000