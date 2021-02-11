from operator import lt, le, gt, ge
from typing import Any, Callable, Iterable, List, Optional, Tuple, Union
from itertools import zip_longest
from math import inf


class _MinMax:
    def __init__(self, operation: Callable, initial_value: Union[Iterable[Any], Any]) -> None:
        self.op = operation
        try:
            self.value = list(initial_value)
            self._is_iterable = True
        except TypeError:
            self.value = initial_value
            self._is_iterable = False

    def update(self, ob: Union[List[Any], Tuple[Any]]):
        if self._is_iterable:
            results = []
            for value_idx, (current, update) in enumerate(zip_longest(self.value, ob, fillvalue=None)):
                if self.op(update, current):
                    self.value[value_idx] = update
                    results.append(True)
                else:
                    results.append(False)
        else:
            if self.op(ob, self.value):
                self.value: Any = ob
                return True
            return False

    def get(self) -> Union[List[Any], Any]:
        return self.value


class Minimum(_MinMax):
    def __init__(self, initial_value: Optional[Union[List[Any], Any]] = None, update_on_equal: bool = False) -> None:
        operation = le if update_on_equal else lt
        try:
            initial_value = list(initial_value) if initial_value else inf
        except TypeError:
            initial_value = initial_value
        super().__init__(operation, initial_value)


class Maximum(_MinMax):
    def __init__(
        self, initial_value: Optional[Union[Iterable[Any], Any]] = None, update_on_equal: bool = False
    ) -> None:
        operation = ge if update_on_equal else gt
        try:
            initial_value = list(initial_value) if initial_value else -inf
        except TypeError:
            initial_value = initial_value
        super().__init__(operation, initial_value)
