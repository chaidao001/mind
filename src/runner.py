import logging
import logging.config
import threading

from src.client.client import EsaClient
from src.client.domain.request.marketfilter import MarketFilter
from utils.config import Config
from utils.utils import get_new_session


def main():
    # loading configs
    config = Config()

    # configuring logger
    logging.config.fileConfig(config.log_conf)
    logging.info("Configs:\n%s" % config)

    app_key = config.app_key

    logging.info("Requesting session token")
    session_token = get_new_session(config.username, config.password, app_key)

    market_filter = MarketFilter()
    market_filter.event_type_ids = [4339]

    [client, esa_thread] = start_esa(config, app_key, session_token, market_filter)

    try:
        esa_thread.join()
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt")
    finally:
        logging.info("Terminating")
        client.terminate()


def start_esa(config, app_key, session_token, market_filter):
    client = EsaClient(config.host, config.port, app_key, session_token, market_filter,
                       config.heartbeat_interval_second)
    esa_thread = threading.Thread(name="EsaThread", target=client.init)
    esa_thread.start()
    return [client, esa_thread]


if __name__ == "__main__":
    main()
