FROM screenly/srly-ose-base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        jq \
        wget && \
    apt-get clean

WORKDIR /usr/src/app

ARG WC_DL_URL
ENV WC_DL_URL=$WC_DL_URL

RUN jq_filter='.assets[] | select (.name|test("linux-armv7hf")) | .browser_download_url' \
    archive_url=$(curl -sL $WC_DL_URL | jq -r "$jq_filter") && \
    wget $archive_url && \
    archive_file=$(basename $archive_url) && \
    tar -xvz -C /usr/src/app -f $archive_file

COPY ./start.sh .

CMD ["/bin/bash", "./start.sh"]
