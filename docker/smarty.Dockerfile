FROM python:3.6-slim

RUN pip install --upgrade pip && pip install Flask gunicorn
COPY . /tmp
RUN pip install /tmp
EXPOSE 8081

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8081", "dummy.servers:get_smarty_app()"]
