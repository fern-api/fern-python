# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .invalid_request_cause import InvalidRequestCause
from .submission_request import SubmissionRequest


class InvalidRequestResponse(pydantic.BaseModel):
    request: SubmissionRequest
    cause: InvalidRequestCause

    class Partial(typing_extensions.TypedDict):
        request: typing_extensions.NotRequired[SubmissionRequest]
        cause: typing_extensions.NotRequired[InvalidRequestCause]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @InvalidRequestResponse.Validators.root
            def validate(values: InvalidRequestResponse.Partial) -> InvalidRequestResponse.Partial:
                ...

            @InvalidRequestResponse.Validators.field("request")
            def validate_request(v: SubmissionRequest, values: InvalidRequestResponse.Partial) -> SubmissionRequest:
                ...

            @InvalidRequestResponse.Validators.field("cause")
            def validate_cause(v: InvalidRequestCause, values: InvalidRequestResponse.Partial) -> InvalidRequestCause:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[InvalidRequestResponse.Partial], InvalidRequestResponse.Partial]]
        ] = []
        _request_validators: typing.ClassVar[typing.List[InvalidRequestResponse.Validators.RequestValidator]] = []
        _cause_validators: typing.ClassVar[typing.List[InvalidRequestResponse.Validators.CauseValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[InvalidRequestResponse.Partial], InvalidRequestResponse.Partial]
        ) -> typing.Callable[[InvalidRequestResponse.Partial], InvalidRequestResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["request"]
        ) -> typing.Callable[
            [InvalidRequestResponse.Validators.RequestValidator], InvalidRequestResponse.Validators.RequestValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["cause"]
        ) -> typing.Callable[
            [InvalidRequestResponse.Validators.CauseValidator], InvalidRequestResponse.Validators.CauseValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "request":
                    cls._request_validators.append(validator)
                if field_name == "cause":
                    cls._cause_validators.append(validator)
                return validator

            return decorator

        class RequestValidator(typing_extensions.Protocol):
            def __call__(self, v: SubmissionRequest, *, values: InvalidRequestResponse.Partial) -> SubmissionRequest:
                ...

        class CauseValidator(typing_extensions.Protocol):
            def __call__(
                self, v: InvalidRequestCause, *, values: InvalidRequestResponse.Partial
            ) -> InvalidRequestCause:
                ...

    @pydantic.root_validator
    def _validate(cls, values: InvalidRequestResponse.Partial) -> InvalidRequestResponse.Partial:
        for validator in InvalidRequestResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("request")
    def _validate_request(cls, v: SubmissionRequest, values: InvalidRequestResponse.Partial) -> SubmissionRequest:
        for validator in InvalidRequestResponse.Validators._request_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("cause")
    def _validate_cause(cls, v: InvalidRequestCause, values: InvalidRequestResponse.Partial) -> InvalidRequestCause:
        for validator in InvalidRequestResponse.Validators._cause_validators:
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
