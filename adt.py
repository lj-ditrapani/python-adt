from typing import TypeVar, Generic, Union, NoReturn
from dataclasses import dataclass

# T = TypeVar('T')

@dataclass
class Success:
    value: int

@dataclass
class Failure:
    error: str

Result = Union[Success, Failure]

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
    result1: Result = Success(5)
    result2: Result = Failure("broken")
    print(result1)
    print(result2)
