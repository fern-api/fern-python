# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class StoppedResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StoppedResponse.Validators.root
            def validate(values: StoppedResponse.Partial) -> StoppedResponse.Partial:
                ...

            @StoppedResponse.Validators.field("submission_id")
            def validate_submission_id(v: SubmissionId, values: StoppedResponse.Partial) -> SubmissionId:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[StoppedResponse.Partial], StoppedResponse.Partial]]
        ] = []
        _submission_id_validators: typing.ClassVar[typing.List[StoppedResponse.Validators.SubmissionIdValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[StoppedResponse.Partial], StoppedResponse.Partial]
        ) -> typing.Callable[[StoppedResponse.Partial], StoppedResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [StoppedResponse.Validators.SubmissionIdValidator], StoppedResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, v: SubmissionId, *, values: StoppedResponse.Partial) -> SubmissionId:
                ...

    @pydantic.root_validator
    def _validate(cls, values: StoppedResponse.Partial) -> StoppedResponse.Partial:
        for validator in StoppedResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: StoppedResponse.Partial) -> SubmissionId:
        for validator in StoppedResponse.Validators._submission_id_validators:
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
