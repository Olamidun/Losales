FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /losales

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# copy directory into losales

ADD . .

RUN python manage.py collectstatic --noinput

# EXPOSE 8000

# gunicorn config
CMD gunicorn losales.wsgi:application --bind 0.0.0.0:$PORT 
