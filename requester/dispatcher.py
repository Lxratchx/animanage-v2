from typing import Any


class RequestDispatcher:
    def __init__(self) -> None:
        self._handlers = {}
    
    def add_handler(self, k, f):
        if k not in self._handlers:
            self._handlers[k] = f
    
    def dispatch(self, v) -> Any|None:
        if not v in self._handlers:
            return

        return self._handlers[v]()
