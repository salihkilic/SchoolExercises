# Things to do, chapter 17
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch17.html#idm45794970309480

import multiprocessing
import random
import time
import socket
import pickle
import zmq
import redis
from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


class SocketServer:
    def __init__(self):
        self.server = None

    def start_server(self):
        # Server setup
        server_address = ("localhost", 6789)
        max_size = 4096
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(server_address)

        print(f"Started the server at: {datetime.now()}")
        print(f"Server object: {self.server}")
        print(f"Waiting for clients...")

        # Message handling
        data, client = self.server.recvfrom(max_size)
        print(f"Client sent the following data: {data}")

        if data == b'time':
            self.server.sendto(pickle.dumps(datetime.now()), client)
        # After receiving a message, we close the server
        self.server.close()


class SocketClient:
    def __init__(self):
        self.server_address = ('localhost', 6789)
        self.max_size = 4096
        print('Starting the client at', datetime.now())
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self):
        # Let's give the server some time to boot up before we send a msg
        time.sleep(1)
        # Send our request with the string "time" as a command.
        self.client.sendto(b'time', self.server_address)
        data, server = self.client.recvfrom(self.max_size)
        print(f"The server ({server} sent us the following msg back: {pickle.loads(data)}")
        self.client.close()


class ZmqServer:
    def __init__(self):
        self.context = None
        self.server = None
        self.host = '127.0.0.1'
        self.port = 6789
        self.running = False

    def start_server(self):
        self.context = zmq.Context()
        self.server = self.context.socket(zmq.REP)
        self.server.bind("tcp://%s:%s" % (self.host, self.port))
        self.running = True
        while self.running:
            #  Wait for next request from client
            request_bytes = self.server.recv()
            request_str = pickle.loads(request_bytes)
            print(f"Received msg: {request_str}")
            if request_str == b'time':
                self.server.send(pickle.dumps(datetime.now()))
                # We stop the server after a successful interaction
                self.running = False
            else:
                self.server.send(pickle.dumps(b'WHOOPS, WRONG MSG'))
            # reply_str = "Stop saying: %s" % request_str
            # reply_bytes = bytes(reply_str, 'utf-8')
            # self.server.send(reply_bytes)


class ZmqClient:
    def __init__(self):
        self.client = None
        self.context = None
        self.host = '127.0.0.1'
        self.port = 6789

    def send_message(self):
        self.context = zmq.Context()
        self.client = self.context.socket(zmq.REQ)
        self.client.connect("tcp://%s:%s" % (self.host, self.port))
        request_str = b"time"
        request_bytes = pickle.dumps(request_str)
        self.client.send(request_bytes)
        reply_bytes = self.client.recv()
        reply_str = pickle.loads(reply_bytes)
        print("Sent %s, received %s" % (request_str, reply_str))


class XmlRpcServer:
    def __init__(self):
        self.server = None

    def send_message(self):
        return datetime.now()

    def start_server(self):
        self.server = SimpleXMLRPCServer(("localhost", 6789))
        self.server.register_function(self.send_message, "time_msg")
        # We use handle_request here instead of serve_forever so the server stops when it's done with one msg.
        # Otherwise, we won't get past this and finish the exercises.
        self.server.handle_request()


class XmlRpcClient:
    def __init__(self):
        pass

    def send_message(self):
        proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
        result = proxy.time_msg()
        print(f"Received time: {result}")


class RedisServer:
    def __init__(self):
        self.conn = None
        self.chocolates = ['dark', 'hazelnut', 'pistachio', 'milk', 'white']

    def start_server(self):
        self.conn = redis.Redis()
        time.sleep(0.5)
        for msg in range(10):
            choco = random.choice(self.chocolates)
            print(f"Published a chocolate ({msg + 1}): {choco}")
            self.conn.publish("ChocolateChannel", choco)
        print(f"No more messages to send! Closing server.")
        self.conn.close()


class RedisClient:
    def __init__(self):
        self.msgs_in_queue = None
        self.conn = None
        self.subscription = None

    def start_client(self):
        self.conn = redis.Redis()
        self.subscription = self.conn.pubsub()
        self.subscription.subscribe("ChocolateChannel")
        self.msgs_in_queue = 10
        # Let's wait for the messages to fill the channel a bit
        time.sleep(1)

        for msg in self.subscription.listen():
            if msg['data'] == 1:
                pass
            else:
                time.sleep(0.5)
                self.msgs_in_queue -= 1
                print(f"We handled a chocolate: {msg['data']} at {datetime.now()} --- {self.msgs_in_queue} more "
                      f"chocolates to go.")
            if not self.msgs_in_queue:
                print("No more messages! Closing subscription and connection...")
                # This is important to escape the process
                self.subscription.close()
                self.conn.close()


class ZmqServer2:
    def __init__(self):
        self.context = None
        self.server = None
        self.host = '127.0.0.1'
        self.port = 6779
        self.running = False
        self.poem = "We have seen thee queen of cheese " \
                    "Lying quietly at your ease " \
                    "Gently fanned by evening breeze " \
                    "Thy fair form no flies dare seize " \
                    "All gaily dressed soon you'll go " \
                    "To the great Provincial show " \
                    "To be admired by many a beau " \
                    "In the city of Toronto " \
                    "Cows numerous as a swarm of bees " \
                    "Or as the leaves upon the trees " \
                    "It did require to make thee please " \
                    "And stand unrivalled queen of cheese " \
                    "May you not receive a scar as " \
                    "We have heard that Mr Harris " \
                    "Intends to send you off as far as " \
                    "The great world's show at Paris " \
                    "Of the youth beware of these " \
                    "For some of them might rudely squeeze " \
                    "And bite your cheek then songs or glees " \
                    "We could not sing oh! queen of cheese " \
                    "We'rt thou suspended from balloon " \
                    "You'd cast a shade even at noon " \
                    "Folks would think it was the moon " \
                    "About to fall and crush them soon"

    def start_server(self):
        self.context = zmq.Context()
        self.server = self.context.socket(zmq.PUB)
        self.server.bind("tcp://%s:%s" % (self.host, self.port))
        # Wait for client to be ready, but only AFTER the pub is live
        time.sleep(3)
        for word in self.poem.split(" "):
            print(f"Publishing word: {word}")
            self.server.send_string(word)

        self.server.send_string("LAST MESSAGE")
        self.server.disconnect("tcp://%s:%s" % (self.host, self.port))


class ZmqClient2:
    def __init__(self):
        self.client = None
        self.context = None
        self.host = '127.0.0.1'
        self.port = 6779

    def receive_messages(self):
        time.sleep(1)
        self.context = zmq.Context()
        self.client = self.context.socket(zmq.SUB)
        self.client.setsockopt_string(zmq.SUBSCRIBE, "")
        self.client.connect("tcp://%s:%s" % (self.host, self.port))
        self.client.subscribe("")
        print(f"Wait for server to start sending messages...")
        time.sleep(4)
        print(f"Client ready to receive messages...")

        while True:
            receive_str = self.client.recv_string()
            # Starts with vowel
            if receive_str[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
                print(f"Starts with vowel: {receive_str}")
            # Has five characters
            if len(receive_str) == 5:
                print(f"Has five characters: {receive_str}")
            if receive_str == "LAST MESSAGE":
                break
        print("Done handling messages!")
        self.client.disconnect("tcp://%s:%s" % (self.host, self.port))


if __name__ == '__main__':
    # 17.1 Use a plain socket to implement a current-time-service. When a client sends the string time to the server,
    # return the current date and time as an ISO string.
    print("\n------ 17.1 ------")

    # Because we are using a client and server in the same file, we want to create a separate process for the server.
    sock_server = SocketServer()
    sock_client = SocketClient()
    server_process = multiprocessing.Process(target=sock_server.start_server)
    client_process = multiprocessing.Process(target=sock_client.send_message)

    server_process.start()
    client_process.start()
    # Give the processes time to run before shutting it off
    time.sleep(2)
    server_process.join()
    client_process.join()

    # 17.2 Use ZeroMQ REQ and REP sockets to do the same thing.
    print("\n------ 17.2 ------")
    zmq_server = ZmqServer()
    zmq_client = ZmqClient()
    server_process = multiprocessing.Process(target=zmq_server.start_server)
    client_process = multiprocessing.Process(target=zmq_client.send_message)

    server_process.start()
    client_process.start()
    # Give the processes time to run before shutting it off
    time.sleep(2)
    server_process.join()
    client_process.join()

    # 17.3 Try the same with XMLRPC.
    print("\n------ 17.3 ------")
    xmlrpc_server = XmlRpcServer()
    xmlrpc_client = XmlRpcClient()
    server_process = multiprocessing.Process(target=xmlrpc_server.start_server)
    client_process = multiprocessing.Process(target=xmlrpc_client.send_message)

    server_process.start()
    client_process.start()
    # Give the processes time to run before shutting it off
    time.sleep(2)
    server_process.join()
    client_process.join()

    # 17.4 You may have seen the classic I Love Lucy television episode in which Lucy and Ethel worked in a chocolate
    # factory. The duo fell behind as the conveyor belt that supplied the confections for them to process began
    # operating at an ever-faster rate. Write a simulation that pushes different types of chocolates to a Redis list,
    # and Lucy is a client doing blocking pops of this list. She needs 0.5 seconds to handle a piece of chocolate.
    # Print the time and type of each chocolate as Lucy gets it, and how many remain to be handled.
    print("\n------ 17.4 ------")
    redis_server = RedisServer()
    redis_client = RedisClient()
    server_process = multiprocessing.Process(target=redis_server.start_server)
    client_process = multiprocessing.Process(target=redis_client.start_client)

    server_process.start()
    client_process.start()
    # Give the processes time to run before shutting it off
    time.sleep(2)
    server_process.join()
    client_process.join()

    # 17.5 Use ZeroMQ to publish the poem from exercise 12.4 (from Example 12-1), one word at a time. Write a ZeroMQ
    # consumer that prints every word that starts with a vowel, and another that prints every word that contains five
    # letters. Ignore punctuation characters.
    print("\n------ 17.5 ------")

    zmq_server = ZmqServer2()
    zmq_client = ZmqClient2()
    server_process = multiprocessing.Process(target=zmq_server.start_server)
    client_process = multiprocessing.Process(target=zmq_client.receive_messages)

    server_process.start()
    client_process.start()
    # Give the processes time to run before shutting it off
    time.sleep(2)
    server_process.join()
    client_process.join()
