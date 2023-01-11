#!/bin/bash

IS_CONNECTED=''

if [[ ! -z $CHECK_CONN_FREQ ]]
    then
        freq=$CHECK_CONN_FREQ
    else
        freq=120
fi


sleep 5

while [[ true ]]; do
    if [[ "$VERBOSE" != 'false' ]]; then echo "Checking internet connectivity ..."; fi
    wget --spider --no-check-certificate 1.1.1.1 > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        if [[ "$VERBOSE" != 'false' ]]; then
            echo "Your device is already connected to the internet."
            echo "Skipping setting up Wifi-Connect Access Point. Will check again in $freq seconds."
        fi

        # @TODO: POC only. Uncomment when ready.
        # if [[ "$IS_CONNECTED" = 'false' ]]; then
        #     python send_zmq_message.py --action='show_splash'
        # fi

        IS_CONNECTED='true'
    else
        if [[ "$VERBOSE" != 'false' ]]; then
            echo "Your device is not connected to the internet."
            echo "Starting up Wifi-Connect."
            echo "Connect to the Access Point and configure the SSID and Passphrase for the network to connect to."
        fi

        # @TODO: POC only. Uncomment when ready.
        # if [[ "$IS_CONNECTED" = 'true' ]] || [[ "$IS_CONNECTED" = '' ]]; then
        #     python send_zmq_message.py --action='setup_wifi'
        # fi

        IS_CONNECTED='false'

        # @TODO: You can just put this as an environment variable inside Docker compose file.
        DBUS_SYSTEM_BUS_ADDRESS=unix:path=/run/dbus/system_bus_socket /usr/src/app/wifi-connect -u /usr/src/app/ui
    fi

    sleep $freq

done
