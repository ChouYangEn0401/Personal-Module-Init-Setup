from enum import Enum

from src.practice_02.core.basis_types import ExamplePayload, ExampleContext, ExampleStep


def example_facade(
        payload: ExamplePayload,
        EventBindings: dict,
        context: ExampleContext,
        *args, **kwargs
):
    ## this will run through all `EventBindings`
    # for step, task_cls in EventBindings.items():
    #     if payload[step]:
    #         task_cls().run_task(context)

    ## this will run through all item from `payload` user provided
    for enum_tag, boolean_flag in payload.items():
        if payload.get(enum_tag, False):
            if isinstance(enum_tag, str):
                EventBindings[enum_tag]().run_task(context)
            elif isinstance(enum_tag, Enum):
                EventBindings[enum_tag.value]().run_task(context)

