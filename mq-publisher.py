import sys
import time
import argparse

import paho.mqtt.client as mqtt


def connect_mqtt(broker, port):
    def on_connect(client, userdata, flags, rc):
        if rc != 0:
            print(f"Connection to {broker} failed! Exiting...")
            sys.exit(1)
        print(f"{broker} connected!")
    
    def on_disconnect(client, userdata, rc):
        print(f"{broker} disconnected.")
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(broker, port)
    return client


def main(opt):
    broker = opt.broker
    port = opt.port
    topic = opt.topic

    client = connect_mqtt(broker, port)

    try:
        ct = 0
        while True:
            message = f"Test message {ct}"
            client.publish(topic, message)
            print(f"Published: {message}")
            time.sleep(5)
            ct += 1
    except KeyboardInterrupt:
        print("Exiting...")

    client.disconnect()


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--broker', type=str, default='broker.hivemq.com')
    parser.add_argument('--port', type=int, default=1883)
    parser.add_argument('--topic', type=str, default='example/test-topic')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main(arg_parser())