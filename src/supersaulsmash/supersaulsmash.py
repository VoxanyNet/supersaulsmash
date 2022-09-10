import socket

from supersaulsmash.framework.game import Game
from supersaulsmash.framework.entity import Entity
from supersaulsmash.fighter import Fighter
from supersaulsmash.headered_socket import headered_socket

class SuperSaulSmash(Game):
    def __init__(self, is_host, ip, fps_cap = 80):
        super().__init__(fps_cap = 80)

        self.fps_cap = fps_cap

        self.server = headered_socket.HeaderedSocket(socket.AF_INET, socket.SOCK_STREAM)

        self.ip = ip
        self.port = 5555

        self.entities = {
            "local_player": None,
            "remote_players": []
        }

    def connect(self):

        # connect to one of the peers
        self.server.connect((self.ip, self.port))

        # receive our uuid from the server
        self.uuid = self.server.recv_headered().decode("utf-8")
