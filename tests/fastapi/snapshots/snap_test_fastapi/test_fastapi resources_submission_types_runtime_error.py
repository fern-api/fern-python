# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class RuntimeError(pydantic.BaseModel):
    message: str

    class Partial(typing_extensions.TypedDict):
        message: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @RuntimeError.Validators.root
            def validate(values: RuntimeError.Partial) -> RuntimeError.Partial:
                ...

            @RuntimeError.Validators.field("message")
            def validate_message(message: str, values: RuntimeError.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[RuntimeError.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[RuntimeError.Validators._RootValidator]] = []
        _message_pre_validators: typing.ClassVar[typing.List[RuntimeError.Validators.MessageValidator]] = []
        _message_post_validators: typing.ClassVar[typing.List[RuntimeError.Validators.MessageValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[[RuntimeError.Validators._RootValidator], RuntimeError.Validators._RootValidator]:
            def decorator(validator: RuntimeError.Validators._RootValidator) -> RuntimeError.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["message"], *, pre: bool = False
        ) -> typing.Callable[[RuntimeError.Validators.MessageValidator], RuntimeError.Validators.MessageValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "message":
                    if pre:
                        cls._message_pre_validators.append(validator)
                    else:
                        cls._message_post_validators.append(validator)
                return validator

            return decorator

        class MessageValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: RuntimeError.Partial) -> str:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: RuntimeError.Partial) -> RuntimeError.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: RuntimeError.Partial) -> RuntimeError.Partial:
        for validator in RuntimeError.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: RuntimeError.Partial) -> RuntimeError.Partial:
        for validator in RuntimeError.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("message", pre=True)
    def _pre_validate_message(cls, v: str, values: RuntimeError.Partial) -> str:
        for validator in RuntimeError.Validators._message_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("message", pre=False)
    def _post_validate_message(cls, v: str, values: RuntimeError.Partial) -> str:
        for validator in RuntimeError.Validators._message_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
