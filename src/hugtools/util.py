from typing import Any, Callable, List, Optional, Type, Union


def get_if_exception(
    callable: Callable,
    default: Optional[Any] = None,
    exception_types: Union[Type[Exception], List[Type[Exception]]] = Exception,
):
    """
    Given a callable, (easiest to implement this as a lambda, e.g. `lambda: my_func(a, something=b)`
    this will call and catch an exception and return a default value rather than throwing the exception.
    The purpose here is to allow a try/except clause in locations where this is not possible normally,
    for example a list comprehension or a lambda function.

    args:
        callable (Callable):                                 Any callable,
        default (Optional[Any]):                             The default value to return given an expected exception,
        exception_types (Union[Exception, List[Exception]]): The exception to allow, by default this will allow
                                                             any exception. This can be either a single exception
                                                             or a list of exceptions
    """
    exceptions: List[Type[Exception]] = exception_types if isinstance(exception_types, list) else [exception_types]
    try:
        return callable()
    except tuple(exceptions):
        return default


def try_else(source: Any, target_type: Union[Type, Callable], default_type: Union[None, Type, Callable] = None) -> Any:
    """
    try to do something, and catch and return either some default operation, or the original object
    use sparingly, this is mostly for typecasting in comprehensions

    >>> try_else(10, str)
    '10'

    >>> try_else('a10', int)
    'a10'

    >>> try_else('a10', int, ascii)
    "'a10'"

    Args:
        source (Any): any input that you want to call something on to the target_type
        target_type (Type, Callable):  some callable to try
        default_type (Type, Callable, None): some callable, or just none if you want to return the original object

    Returns:
        A recast object or the original object, depending on default_type

    """

    # noinspection PyBroadException
    try:
        return target_type(source)
    except Exception:
        return default_type(source) if default_type else source
