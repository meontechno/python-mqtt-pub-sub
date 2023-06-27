import sys
import argparse

import paho.mqtt.client as mqtt


def connect_mqtt(broker, port):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"{broker} connected!")
        else:
            print(f"Broker connection failed! Exiting...")
            sys.exit(1)

    def on_disconnect(client, userdata, rc):
        print(f"{broker} disconnected.")
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(broker, port)
    return client


def subscribe(client, topics):
    def on_message(client, userdata, msg):
        print(f"Topic: {msg.topic}\nMessage: {msg.payload.decode()}")
    
    client.subscribe(topics)
    client.on_message = on_message


def main(opt):
    broker = opt.broker
    port = opt.port
    sub_topics = [(topic, 0) for topic in opt.topics]

    mq_client = connect_mqtt(broker, port)
    subscribe(mq_client, sub_topics)
    mq_client.loop_start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting...")

    mq_client.loop_stop()
    mq_client.disconnect()


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--broker', type=str, default='broker.hivemq.com')
    parser.add_argument('--port', type=int, default=1883)
    parser.add_argument('--topics', type=str, nargs='+', default=['example/test-topic'])
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main(arg_parser())