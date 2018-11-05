FROM resin/rpi-raspbian:latest

ENV INITSYSTEM on

RUN apt-get update && apt-get install -yq \
  python3-dev \
  python3-pip \
  python3-rpi.gpio \
  vim \
  wget && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app
WORKDIR /usr/src/app

# Finally, start our app
CMD ["python3", "src/main.py"]
