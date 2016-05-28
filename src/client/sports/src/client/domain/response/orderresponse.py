from datetime import datetime

from client.domain.enums import PersistenceType, Side, OrderType, OrderStatus


class MarketProfitAndLoss:
    def __init__(self, market_id: str = None, commission_applied: float = None, profit_and_losses: list() = None):
        self._market_id = market_id
        self._commission_applied = commission_applied
        self._profit_and_losses = profit_and_losses


class RunnerProfitAndLoss:
    def __init__(self, selection_id: int = None, if_win: float = None, if_lose: float = None, if_place: float = None):
        self._selection_id = selection_id
        self._if_win = if_win
        self._if_lose = if_lose
        self._if_place = if_place


class OrderSummaryReport:
    def __init__(self, more_available: bool):
        self._more_available = more_available


class CurrentOrderSummaryReport(OrderSummaryReport):
    def __init__(self, current_orders: list(), more_available: bool):
        super().__init__(more_available)
        self._current_orders = current_orders


class ClearedOrderSummaryReport(OrderSummaryReport):
    def __init__(self, cleared_orders: list(), more_available: bool):
        super().__init__(more_available)
        self._cleared_orders = cleared_orders


class OrderSummary:
    def __init__(self, market_id: str, selection_id: int, handicap: float, bet_id: str, placed_date: datetime,
                 persistence_type: PersistenceType, order_type: OrderType, side: Side, size_cancelled: float):
        self._market_id = market_id
        self._selection_id = selection_id
        self._handicap = handicap
        self._bet_id = bet_id
        self._placed_date = placed_date
        self._persistence_type = persistence_type
        self._order_type = order_type
        self._side = side
        self._size_cancelled = size_cancelled


class CurrentOrderSummary(OrderSummary):
    def __init__(self, bet_id: str, market_id: str, selection_id: int, handicap: float, price_size: PriceSize,
                 bsp_liability: float, side: Side, status: OrderStatus, persistence_type: PersistenceType,
                 order_type: OrderType, placed_date: datetime, matched_date: datetime,
                 average_price_matched: float = None, size_matched: float = None, size_remaining: float = None,
                 size_lapsed: float = None, size_cancelled: float = None, size_voided: float = None,
                 regulator_auth_code: str = None, regulator_code: str = None):
        super().__init__(market_id, selection_id, handicap, bet_id, placed_date, persistence_type, order_type, side,
                         size_cancelled)
        self._price_size = price_size
        self._bsp_liability = bsp_liability
        self._status = status
        self._matched_date = matched_date
        self._average_price_matched = average_price_matched
        self._size_matched = size_matched
        self._size_remaining = size_remaining
        self._size_lapsed = size_lapsed
        self._size_voided = size_voided
        self._regulator_auth_code = regulator_auth_code
        self._regulator_code = regulator_code


class PriceSize:
    def __init__(self, price: float, size: float):
        self._price = price
        self._size = size


class ClearedOrderSummary(OrderSummary):
    def __init__(self, event_type_id: str = None, event_id: str = None, market_id: str = None, selection_id: int = None,
                 handicap: float = None, bet_id: str = None, placed_date: datetime = None,
                 persistence_type: PersistenceType = None, order_type: OrderType = None, side: Side = None,
                 item_description: ItemDescription = None, bet_outcome: str = None, price_requested: float = None,
                 settled_date: datetime = None, last_matched_date: datetime = None, bet_count: int = None,
                 commission: float = None, price_matched: float = None, price_reduced: bool = None,
                 size_settled: float = None, profit: float = None, size_cancelled: float = None):
        super().__init__(market_id, selection_id, handicap, bet_id, placed_date, persistence_type, order_type, side,
                         size_cancelled)
        self._event_type_id = event_type_id
        self._event_id = event_id
        self._item_description = item_description
        self._bet_outcome = bet_outcome
        self._price_requested = price_requested
        self._settled_date = settled_date
        self._last_matched_date = last_matched_date
        self._bet_count = bet_count
        self._commission = commission
        self._price_matched = price_matched
        self._price_reduced = price_reduced
        self._size_settled = size_settled
        self._profit = profit


class ItemDescription:
    def __init__(self, event_type_desc: str = None, event_desc: str = None, market_desc: str = None,
                 market_type: str = None, market_start_time: datetime = None, runner_desc: str = None,
                 number_of_winners: int = None, each_way_divisor: float = None):
        self._event_type_desc = event_type_desc
        self._event_desc = event_desc
        self._market_desc = market_desc
        self._market_type = market_type
        self._market_start_time = market_start_time
        self._runner_desc = runner_desc
        self._number_of_winners = number_of_winners
        self._each_way_divisor = each_way_divisor
