from client.domain.enums import SortDir, OrderBy, OrderProjection, Side, BetStatus, GroupBy
from client.domain.request.orderrequest import TimeRange
from client.operation.operation import Operation
from utils.configs import Configs
from utils.sessionmanager import SessionManager


class Order(Operation):
    def __init__(self, configs: Configs, session_manager: SessionManager):
        super().__init__(configs.betting_endpoint, session_manager)

    def list_market_profit_and_loss(self, market_ids: set(), include_settled_bets: bool = None,
                                    include_bsp_bets: bool = None, net_of_commission: bool = None):
        pass

    def list_current_orders(self, bet_ids: set() = None, market_ids: set() = None,
                            order_projection: OrderProjection = None, date_range: TimeRange = None,
                            order_by: OrderBy = None, sort_dir: SortDir = None, from_record: int = None,
                            record_count: int = None):
        pass

    def list_cleared_orders(self, bet_status: BetStatus, event_type_ids: set() = None, event_ids: set() = None,
                            market_ids: set() = None, runner_ids: set() = None, bet_ids: set() = None,
                            side: Side = None, settled_date_range: TimeRange = None, group_by: GroupBy = None,
                            include_item_description: bool = None, locale: str = None, from_record: int = None,
                            record_count: int = None):
        pass
