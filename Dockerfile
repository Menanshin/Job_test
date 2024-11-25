FROM --platform=linux/amd64 selenium/standalone-chrome:latest

USER root
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    python3 \
    python3-pip \
    python3-setuptools \
    libx11-xcb1 \
    libglu1-mesa \
    libxi6 \
    libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y upgrade \
    && apt-get clean

COPY requirements.txt /tests/requirements.txt
WORKDIR /tests
COPY . /tests

RUN ls -al /tests
RUN pip install -r /tests/requirements.txt

CMD ["pytest", "/tests"]


CMD ["pytest", "/tests"]
