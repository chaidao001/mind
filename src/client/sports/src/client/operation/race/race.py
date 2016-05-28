from client.operation.operation import Operation
from utils.configs import Configs
from utils.sessionmanager import SessionManager


class Race(Operation):
    def __init__(self, configs: Configs, session_manager: SessionManager):
        super().__init__(configs.scores_endpoint, session_manager)

    def list_race_details(self):
        pass
