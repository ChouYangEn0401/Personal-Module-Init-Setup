from abc import abstractmethod, ABC
from typing import TypeVar, Dict, Generic, TypedDict
from enum import Enum
from dataclasses import dataclass


class IStepEnum(Enum):
    pass

ISE = TypeVar("ISE", bound=IStepEnum)
class IPayload(Generic[ISE], Dict[ISE, bool]):
    """Generic payload mapping Enum steps to bool flags"""
    pass
class PayloadBase(Dict[ISE, bool]):
    """Generic payload mapping Enum steps to bool flags"""
    def __getitem__(self, key: ISE) -> bool: ...
    def __setitem__(self, key: ISE, value: bool) -> None: ...

@dataclass
class IContext:
    pass

class IFacadeTask(ABC):
    @abstractmethod
    def run_task(self, context: IContext, *args, **kwargs): pass


