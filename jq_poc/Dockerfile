FROM screenly/srly-ose-base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        jq \
        wget && \
    apt-get clean

WORKDIR /usr/src/app

ARG TARGET_PLATFORM
ARG WC_DL_URL

COPY ./bin/install_wifi_connect.sh .
RUN bash ./install_wifi_connect.sh
COPY ./start.sh .

CMD ["/bin/bash", "./start.sh"]
