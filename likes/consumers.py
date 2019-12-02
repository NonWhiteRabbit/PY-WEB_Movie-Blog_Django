from channels.generic.websocket import WebsocketConsumer
import json


class LikeConsumer(WebsocketConsumer):
    def __init__(self):
        super().__init__()
        self.__like_cnt = 0

    def connect(self):
        self.accept()
        print('LikeConsumer: connect')

    def disconnect(self, code):
        print(f"LikeConsumer: disconnect, Close Code {code}")

    def receive(self, text_data=None, bytes_data=None):
        print('LikeConsumer: receive')
        self.__like_cnt += 1
        self.send(text_data=f'{self.__like_cnt}')