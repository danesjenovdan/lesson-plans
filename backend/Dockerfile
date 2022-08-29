FROM python:latest

# Port used by this container to serve HTTP.
EXPOSE 8000

# Install the project requirements.
COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

WORKDIR /code
# Copy the source code of the project into the container.
COPY . /code

CMD python manage.py runserver 0.0.0.0:8000
