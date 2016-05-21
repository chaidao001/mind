import logging
import threading

from flask import Flask
from flask import render_template
from flask import request

from src.client.client import EsaClient
from src.client.domain.request.marketfilter import MarketFilter
from src.client.utils.utils import format_to_html, format_json
from utils.config import Configs
from utils.sessionmanager import SessionManager


def main():
    # loading configs
    configs = Configs()

    # session manager
    session_manager = SessionManager(configs)

    market_filter = MarketFilter()

    [client, esa_thread] = start_esa(configs, session_manager, market_filter)

    app = Flask(__name__)

    @app.route('/')
    def my_form():
        return render_template("index.html")

    @app.route('/', methods=['POST'])
    def get_market():
        market_id = request.form['text']
        market = client.cache.get_market(market_id)
        if market:
            market_def = format_to_html(format_json(market.market_def))
            prices = format_to_html(market.formatted_string())
            return market_def + prices
        else:
            return "market %s doesn't exist" % market_id

    try:
        app.run()
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
