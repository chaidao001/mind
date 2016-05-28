from client.operation.operation import Operation
from utils.configs import Configs
from utils.sessionmanager import SessionManager


class Account(Operation):
    def __init__(self, configs: Configs, session_manager: SessionManager):
        super().__init__(configs.account_endpoint, session_manager)

    def get_account_funds(self):
        pass

    def get_account_details(self):
        pass

    def get_account_statement(self):
        pass
