from .config import OpenMLHubConf

class OpenMLHubClient:
    """ This client implements the communication with OpenMLHub
    """
    def __init__(self, conf: OpenMLHubConf) -> None:
        self.conf = conf
             
    def log(self):
        pass