from client.domain.enums import OrderType, Side, PersistenceType


class PlaceInstruction:
    def __init__(self, order_type: OrderType, selection_id: int, side: Side, handicap: float = None,
                 limit_order: LimitOrder = None, limit_on_close_order: LimitOnCloseOrder = None,
                 market_on_close_order: MarketOnCloseOrder = None):
        self._order_type = order_type
        self._selection_id = selection_id
        self._side = side
        self._handicap = handicap
        self._limit_order = limit_order
        self._limit_on_close_order = limit_on_close_order
        self._market_on_close_order = market_on_close_order


class LimitOrder:
    def __init__(self, size: float, price: float, persistence_type: PersistenceType):
        self._size = size
        self._price = price
        self._persistence_type = persistence_type


class LimitOnCloseOrder:
    def __init__(self, liability: float, price: float):
        self._liability = liability
        self._price = price


class MarketOnCloseOrder:
    def __init__(self, liability: float):
        self._liability = liability


class CancelInstruction:
    def __init__(self, bet_id: str, size_reduction: float = None):
        self._bet_id = bet_id
        self._size_reduction = size_reduction


class UpdateInstruction:
    def __init__(self, bet_id: str, new_persistence_type: PersistenceType):
        self._bet_id = bet_id
        self._new_persistence_type = new_persistence_type


class ReplaceInstruction:
    def __init__(self, bet_id: str, new_price: float):
        self._bet_id = bet_id
        self._new_price = new_price
