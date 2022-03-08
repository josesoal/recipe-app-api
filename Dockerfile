FROM python:3.9-alpine

LABEL maintainer="Jose Soncco"

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt

# --begin: support for postgresql
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
# --end

RUN pip install -r /requirements.txt

# --eliminate temporal dependencies
RUN apk del .tmp-build-deps


# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user