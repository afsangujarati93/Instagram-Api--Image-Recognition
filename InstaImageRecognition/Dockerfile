FROM python:3.6-alpine3.6 
# dependencies into the virtualenv.
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app

ENTRYPOINT [ "gunicorn", "-b", "8080", "Django_Twitter_Sentiment_Analysis.wsgi"]
CMD [ "python","manage.py"]
EXPOSE 8080