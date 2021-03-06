FROM python:3.6-slim

RUN pip install --upgrade pip && pip install Flask gunicorn
COPY . /tmp
RUN pip install /tmp
EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "dummy.servers:get_dummy_app()"]
