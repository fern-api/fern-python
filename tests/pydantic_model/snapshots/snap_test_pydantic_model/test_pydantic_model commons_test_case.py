# This file was auto-generated by Fern from our API Definition.

# type: ignore
# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .variable_value import VariableValue


class TestCase(pydantic.BaseModel):
    id: str
    params: typing.List[VariableValue]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCase.Validators.field("id")
            def validate_id(v: str, values: TestCase.Partial) -> str:
                ...

            @TestCase.Validators.field("params")
            def validate_params(v: typing.List[VariableValue], values: TestCase.Partial) -> typing.List[VariableValue]:
                ...
        """

        _id_validators: typing.ClassVar[typing.List[TestCase.Validators.IdValidator]] = []
        _params_validators: typing.ClassVar[typing.List[TestCase.Validators.ParamsValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"]
        ) -> typing.Callable[[TestCase.Validators.IdValidator], TestCase.Validators.IdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["params"]
        ) -> typing.Callable[[TestCase.Validators.ParamsValidator], TestCase.Validators.ParamsValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "id":
                    cls._id_validators.append(validator)
                if field_name == "params":
                    cls._params_validators.append(validator)
                return validator

            return decorator

        class IdValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: TestCase.Partial) -> str:
                ...

        class ParamsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[VariableValue], *, values: TestCase.Partial
            ) -> typing.List[VariableValue]:
                ...

    @pydantic.validator("id")
    def _validate_id(cls, v: str, values: str) -> str:
        for validator in TestCase.Validators._id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("params")
    def _validate_params(
        cls, v: typing.List[VariableValue], values: typing.List[VariableValue]
    ) -> typing.List[VariableValue]:
        for validator in TestCase.Validators._params_validators:
            v = validator(v, values=values)
        return v

    class Partial(typing.TypedDict):
        id: typing_extensions.NotRequired[str]
        params: typing_extensions.NotRequired[typing.List[VariableValue]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
