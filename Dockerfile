FROM python:3.6-alpine3.7

RUN apk update

WORKDIR /app

COPY ./requirements requirements
RUN pip install pip setuptools --upgrade
RUN pip install -r requirements/production.txt --no-cache-dir
ADD ./petshop /app

EXPOSE 8080

RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "petshop.wsgi"]

