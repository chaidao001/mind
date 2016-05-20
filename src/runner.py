import logging
import logging.config
import threading

from src.client.client import EsaClient
from src.client.domain.request.marketfilter import MarketFilter
from utils.config import Configs
from utils.sessionmanager import SessionManager


def main():
    # loading configs
    configs = Configs()

    # configuring logger
    logging.config.fileConfig(configs.log_conf)

    # session manager
    session_manager = SessionManager(configs)

    market_filter = MarketFilter()

    [client, esa_thread] = start_esa(configs, session_manager, market_filter)

    try:
        esa_thread.join()
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt")
    finally:
        logging.info("Terminating")
        client.terminate()


def start_esa(configs: Configs, session_manager: SessionManager, market_filter: MarketFilter):
    client = EsaClient(configs, session_manager, market_filter)
    esa_thread = threading.Thread(name="EsaThread", target=client.init)
    esa_thread.start()
    return [client, esa_thread]


if __name__ == "__main__":
    main()
