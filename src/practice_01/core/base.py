from abc import abstractmethod, ABC
from typing import TypedDict
from dataclasses import dataclass
from enum import Enum

class IStepEnum(Enum):
    pass

class IPayload(TypedDict):
    pass

@dataclass
class IContext:
    pass

class IMainFacade(ABC):
    def __init__(self, payload: IPayload, context: IContext):
        self._payload = payload
        self._context = context

    @abstractmethod
    def workflow_execution(self, *args, **kwargs):
        raise NotImplementedError
        # ### NOTE: IDEA ###
        for step in kwargs["steps"]:
            if self._payload[step]:
                getattr(self, f"_{step}")()
        # ### NOTE: IDEA ###

