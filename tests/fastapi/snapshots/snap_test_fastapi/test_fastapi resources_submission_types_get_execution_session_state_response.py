# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .execution_session_state import ExecutionSessionState


class GetExecutionSessionStateResponse(pydantic.BaseModel):
    states: typing.Dict[str, ExecutionSessionState]
    num_warming_instances: typing.Optional[int] = pydantic.Field(alias="numWarmingInstances")
    warming_session_ids: typing.List[str] = pydantic.Field(alias="warmingSessionIds")

    class Partial(typing_extensions.TypedDict):
        states: typing_extensions.NotRequired[typing.Dict[str, ExecutionSessionState]]
        num_warming_instances: typing_extensions.NotRequired[typing.Optional[int]]
        warming_session_ids: typing_extensions.NotRequired[typing.List[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetExecutionSessionStateResponse.Validators.root
            def validate(values: GetExecutionSessionStateResponse.Partial) -> GetExecutionSessionStateResponse.Partial:
                ...

            @GetExecutionSessionStateResponse.Validators.field("states")
            def validate_states(v: typing.Dict[str, ExecutionSessionState], values: GetExecutionSessionStateResponse.Partial) -> typing.Dict[str, ExecutionSessionState]:
                ...

            @GetExecutionSessionStateResponse.Validators.field("num_warming_instances")
            def validate_num_warming_instances(v: typing.Optional[int], values: GetExecutionSessionStateResponse.Partial) -> typing.Optional[int]:
                ...

            @GetExecutionSessionStateResponse.Validators.field("warming_session_ids")
            def validate_warming_session_ids(v: typing.List[str], values: GetExecutionSessionStateResponse.Partial) -> typing.List[str]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[[GetExecutionSessionStateResponse.Partial], GetExecutionSessionStateResponse.Partial]
            ]
        ] = []
        _states_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators.StatesValidator]
        ] = []
        _num_warming_instances_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators.NumWarmingInstancesValidator]
        ] = []
        _warming_session_ids_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators.WarmingSessionIdsValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [GetExecutionSessionStateResponse.Partial], GetExecutionSessionStateResponse.Partial
            ],
        ) -> typing.Callable[[GetExecutionSessionStateResponse.Partial], GetExecutionSessionStateResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["states"]
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators.StatesValidator],
            GetExecutionSessionStateResponse.Validators.StatesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["num_warming_instances"]
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators.NumWarmingInstancesValidator],
            GetExecutionSessionStateResponse.Validators.NumWarmingInstancesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["warming_session_ids"]
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators.WarmingSessionIdsValidator],
            GetExecutionSessionStateResponse.Validators.WarmingSessionIdsValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "states":
                    cls._states_validators.append(validator)
                if field_name == "num_warming_instances":
                    cls._num_warming_instances_validators.append(validator)
                if field_name == "warming_session_ids":
                    cls._warming_session_ids_validators.append(validator)
                return validator

            return decorator

        class StatesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[str, ExecutionSessionState], *, values: GetExecutionSessionStateResponse.Partial
            ) -> typing.Dict[str, ExecutionSessionState]:
                ...

        class NumWarmingInstancesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[int], *, values: GetExecutionSessionStateResponse.Partial
            ) -> typing.Optional[int]:
                ...

        class WarmingSessionIdsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[str], *, values: GetExecutionSessionStateResponse.Partial
            ) -> typing.List[str]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: GetExecutionSessionStateResponse.Partial) -> GetExecutionSessionStateResponse.Partial:
        for validator in GetExecutionSessionStateResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("states")
    def _validate_states(
        cls, v: typing.Dict[str, ExecutionSessionState], values: GetExecutionSessionStateResponse.Partial
    ) -> typing.Dict[str, ExecutionSessionState]:
        for validator in GetExecutionSessionStateResponse.Validators._states_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("num_warming_instances")
    def _validate_num_warming_instances(
        cls, v: typing.Optional[int], values: GetExecutionSessionStateResponse.Partial
    ) -> typing.Optional[int]:
        for validator in GetExecutionSessionStateResponse.Validators._num_warming_instances_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("warming_session_ids")
    def _validate_warming_session_ids(
        cls, v: typing.List[str], values: GetExecutionSessionStateResponse.Partial
    ) -> typing.List[str]:
        for validator in GetExecutionSessionStateResponse.Validators._warming_session_ids_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
