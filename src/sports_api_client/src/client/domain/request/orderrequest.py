from datetime import datetime


class TimeRange:
    def __init__(self, since: datetime = None, to: datetime = None):
        self._since = since
        self._to = to
