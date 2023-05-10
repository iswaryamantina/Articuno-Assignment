FROM python:3.9-alpine

USER root
ADD . /home/app/
WORKDIR /home/app/


COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
