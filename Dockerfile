FROM python:2.7.13
MAINTAINER Sunil Kumar Garg "sunil.garg005@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]