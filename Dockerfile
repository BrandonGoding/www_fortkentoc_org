FROM python:3.11-slim

WORKDIR /usr/src/app


COPY ./app/membership /usr/src/app/membership
COPY ./app/templates /usr/src/app/templates
COPY ./app/website /usr/src/app/website
COPY ./app/www_fortkentoc_org /usr/src/app/www_fortkentoc_org
COPY ./app/__init__.py /usr/src/app/__init__.py
COPY ./app/manage.py /usr/src/app/manage.py
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "--bind", "0.0.0.0:80", "www_fortkentoc_org.wsgi:application"]
