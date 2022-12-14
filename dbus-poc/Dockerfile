FROM screenly/srly-ose-base as builder

WORKDIR /usr/src/app

RUN curl https://api.github.com/repos/balena-io/wifi-connect/releases/latest -sL \
    | grep -hoP 'browser_download_url": "\K.*armv7hf\.tar\.gz' \
    | xargs -n1 curl -Ls \
    | tar -xvz -C /usr/src/app/

FROM balenalib/raspberrypi3:buster

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        build-essential \
        dnsmasq \
        wireless-tools \
        wget \
        libzmq3-dev \
        python-dev \
        python-pip \
        python-setuptools && \
    apt-get clean

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/ui /usr/src/app/ui
COPY --from=builder /usr/src/app/wifi-connect /usr/src/app/wifi-connect

COPY requirements.wifi-connect.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY send_zmq_message.py ./

RUN touch /var/lib/misc/dnsmasq.leases

COPY start_wifi_connect.sh ./

CMD ["bash", "start_wifi_connect.sh"]
