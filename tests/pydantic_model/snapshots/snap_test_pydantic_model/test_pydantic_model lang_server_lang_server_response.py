# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class LangServerResponse(pydantic.BaseModel):
    response: typing.Any

    class Partial(typing_extensions.TypedDict):
        response: typing_extensions.NotRequired[typing.Any]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @LangServerResponse.Validators.root
            def validate(values: LangServerResponse.Partial) -> LangServerResponse.Partial:
                ...

            @LangServerResponse.Validators.field("response")
            def validate_response(v: typing.Any, values: LangServerResponse.Partial) -> typing.Any:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[LangServerResponse.Partial], LangServerResponse.Partial]]
        ] = []
        _response_validators: typing.ClassVar[typing.List[LangServerResponse.Validators.ResponseValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[LangServerResponse.Partial], LangServerResponse.Partial]
        ) -> typing.Callable[[LangServerResponse.Partial], LangServerResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["response"]
        ) -> typing.Callable[
            [LangServerResponse.Validators.ResponseValidator], LangServerResponse.Validators.ResponseValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "response":
                    cls._response_validators.append(validator)
                return validator

            return decorator

        class ResponseValidator(typing_extensions.Protocol):
            def __call__(self, v: typing.Any, *, values: LangServerResponse.Partial) -> typing.Any:
                ...

    @pydantic.root_validator
    def _validate(cls, values: LangServerResponse.Partial) -> LangServerResponse.Partial:
        for validator in LangServerResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("response")
    def _validate_response(cls, v: typing.Any, values: LangServerResponse.Partial) -> typing.Any:
        for validator in LangServerResponse.Validators._response_validators:
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
