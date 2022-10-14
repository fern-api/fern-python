# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .....commons.types.variable_type import VariableType
from .parameter import Parameter


class VoidFunctionSignatureThatTakesActualResult(pydantic.BaseModel):
    parameters: typing.List[Parameter]
    actual_result_type: VariableType = pydantic.Field(alias="actualResultType")

    class Partial(typing_extensions.TypedDict):
        parameters: typing_extensions.NotRequired[typing.List[Parameter]]
        actual_result_type: typing_extensions.NotRequired[VariableType]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @VoidFunctionSignatureThatTakesActualResult.Validators.root
            def validate(values: VoidFunctionSignatureThatTakesActualResult.Partial) -> VoidFunctionSignatureThatTakesActualResult.Partial:
                ...

            @VoidFunctionSignatureThatTakesActualResult.Validators.field("parameters")
            def validate_parameters(v: typing.List[Parameter], values: VoidFunctionSignatureThatTakesActualResult.Partial) -> typing.List[Parameter]:
                ...

            @VoidFunctionSignatureThatTakesActualResult.Validators.field("actual_result_type")
            def validate_actual_result_type(v: VariableType, values: VoidFunctionSignatureThatTakesActualResult.Partial) -> VariableType:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [VoidFunctionSignatureThatTakesActualResult.Partial],
                    VoidFunctionSignatureThatTakesActualResult.Partial,
                ]
            ]
        ] = []
        _parameters_validators: typing.ClassVar[
            typing.List[VoidFunctionSignatureThatTakesActualResult.Validators.ParametersValidator]
        ] = []
        _actual_result_type_validators: typing.ClassVar[
            typing.List[VoidFunctionSignatureThatTakesActualResult.Validators.ActualResultTypeValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [VoidFunctionSignatureThatTakesActualResult.Partial], VoidFunctionSignatureThatTakesActualResult.Partial
            ],
        ) -> typing.Callable[
            [VoidFunctionSignatureThatTakesActualResult.Partial], VoidFunctionSignatureThatTakesActualResult.Partial
        ]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["parameters"]
        ) -> typing.Callable[
            [VoidFunctionSignatureThatTakesActualResult.Validators.ParametersValidator],
            VoidFunctionSignatureThatTakesActualResult.Validators.ParametersValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["actual_result_type"]
        ) -> typing.Callable[
            [VoidFunctionSignatureThatTakesActualResult.Validators.ActualResultTypeValidator],
            VoidFunctionSignatureThatTakesActualResult.Validators.ActualResultTypeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "parameters":
                    cls._parameters_validators.append(validator)
                if field_name == "actual_result_type":
                    cls._actual_result_type_validators.append(validator)
                return validator

            return decorator

        class ParametersValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[Parameter], *, values: VoidFunctionSignatureThatTakesActualResult.Partial
            ) -> typing.List[Parameter]:
                ...

        class ActualResultTypeValidator(typing_extensions.Protocol):
            def __call__(
                self, v: VariableType, *, values: VoidFunctionSignatureThatTakesActualResult.Partial
            ) -> VariableType:
                ...

    @pydantic.root_validator
    def _validate(
        cls, values: VoidFunctionSignatureThatTakesActualResult.Partial
    ) -> VoidFunctionSignatureThatTakesActualResult.Partial:
        for validator in VoidFunctionSignatureThatTakesActualResult.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("parameters")
    def _validate_parameters(
        cls, v: typing.List[Parameter], values: VoidFunctionSignatureThatTakesActualResult.Partial
    ) -> typing.List[Parameter]:
        for validator in VoidFunctionSignatureThatTakesActualResult.Validators._parameters_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("actual_result_type")
    def _validate_actual_result_type(
        cls, v: VariableType, values: VoidFunctionSignatureThatTakesActualResult.Partial
    ) -> VariableType:
        for validator in VoidFunctionSignatureThatTakesActualResult.Validators._actual_result_type_validators:
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
