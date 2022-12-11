FROM python:latest
RUN pip install --upgrade pip

LABEL maintainer="oggiwer@gmail.com"

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/

EXPOSE 5000
CMD ["python", "app.py"]
