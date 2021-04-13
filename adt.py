from typing import Generic, TypeVar, Generic, Union, NoReturn
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class Success(Generic[T]):
    value: T

@dataclass
class Failure:
    error: str

Result = Union[Success[T], Failure]

def assert_never(x: NoReturn) -> NoReturn:
    raise AssertionError("Unhandled type: {}".format(type(x).__name__))

def proccessResult(result: Result) -> str:
    if (isinstance(result, Success)):
        return str(result.value)
    elif isinstance(result, Failure):
        return str(result.error)
    else:
        assert_never(result)

if __name__ == "__main__":
    print("running adt.py...")
    result1: Result[int] = Success(5)
    result2: Result[int] = Failure("broken")
    print(result1)
    print(result2)
