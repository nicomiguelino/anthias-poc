FROM balenalib/raspberrypi3-debian:buster

RUN install_packages dnsmasq wireless-tools

WORKDIR /usr/src/app

ARG VERSION="4.4.0"
ARG BALENA_ARCH="armv7hf"
RUN curl -Ls "https://github.com/balena-io/wifi-connect/releases/download/v$VERSION/wifi-connect-v$VERSION-linux-$BALENA_ARCH.tar.gz" \
  | tar -xvz -C  /usr/src/app/

COPY scripts/start.sh .

CMD ["bash", "start.sh"]
