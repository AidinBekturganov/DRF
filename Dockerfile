FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /DRF
COPY requirements.txt requirements.txt
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install Pillow
RUN pip install -r requirements.txt
COPY . .