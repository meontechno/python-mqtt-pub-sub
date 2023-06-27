# python-mqtt-pub-sub
Example MQTT Publish-Subscribe Implementation in Python.

This Git repository provides a simple Python implementation of the MQTT (Message Queuing Telemetry Transport) publish-subscribe system. Enables easy publishing and subscribing to topics with support for different quality of service levels (Code in this repo uses QoS 0).

## Requirements
`pip3 install -r requirements.txt`

## mq-subscriber.py
The code begins by establishing a connection to the specified MQTT broker and port. It handles the connection status using callback functions: `on_connect` is triggered upon successful connection, while `on_disconnect` is called when the client disconnects from the broker.

The `subscribe` function enables subscribing to the specified topics and defines an `on_message` callback that is triggered whenever a new message is received. Each received message is printed, displaying the topic and the message payload.

In the `main` function, command-line arguments are parsed using the `argparse` library. The broker, port, and topics to subscribe to can be customized through the command line. The `connect_mqtt` function is called to establish the MQTT connection, and the `subscribe` function is used to subscribe to the specified topics.

The MQTT client's event loop is started (`loop_start`), allowing it to handle incoming messages asynchronously. The program runs indefinitely until interrupted by a keyboard interrupt (`KeyboardInterrupt`), at which point it gracefully stops the event loop, disconnects from the broker, and exits.

To use this code, simply execute it as a Python script - 

`python mq-subscriber.py --broker <broker> --port <port number> --topics <topic1> <topi2>`

The optional command-line arguments include the MQTT broker address, port number, and topics to subscribe to. By default, it connects to 'broker.hivemq.com' on port 1883 and subscribes to the 'example/test-topic' topic.


## mq-publisher.py
The code starts by establishing a connection to the specified MQTT broker and port. 

A 5-second delay is introduced between each message publication using the time.sleep function. This delay can be adjusted as per requirements. The counter value is incremented to generate different test messages for publication.

To use this code, simply execute it as a Python script - 

`python mq-publisher.py --broker <broker> --port <port number> --topic <topic1>`

The optional command-line arguments include the MQTT broker address, port number, and topic to publish to. By default, it connects to 'broker.hivemq.com' on port 1883 and publishes to the 'example/test-topic' topic.
