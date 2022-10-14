# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.debug_variable_value import DebugVariableValue
from .expression_location import ExpressionLocation
from .stack_information import StackInformation
from .submission_id import SubmissionId


class TraceResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    line_number: int = pydantic.Field(alias="lineNumber")
    return_value: typing.Optional[DebugVariableValue] = pydantic.Field(alias="returnValue")
    expression_location: typing.Optional[ExpressionLocation] = pydantic.Field(alias="expressionLocation")
    stack: StackInformation
    stdout: typing.Optional[str]

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        line_number: typing_extensions.NotRequired[int]
        return_value: typing_extensions.NotRequired[typing.Optional[DebugVariableValue]]
        expression_location: typing_extensions.NotRequired[typing.Optional[ExpressionLocation]]
        stack: typing_extensions.NotRequired[StackInformation]
        stdout: typing_extensions.NotRequired[typing.Optional[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TraceResponse.Validators.root
            def validate(values: TraceResponse.Partial) -> TraceResponse.Partial:
                ...

            @TraceResponse.Validators.field("submission_id")
            def validate_submission_id(v: SubmissionId, values: TraceResponse.Partial) -> SubmissionId:
                ...

            @TraceResponse.Validators.field("line_number")
            def validate_line_number(v: int, values: TraceResponse.Partial) -> int:
                ...

            @TraceResponse.Validators.field("return_value")
            def validate_return_value(v: typing.Optional[DebugVariableValue], values: TraceResponse.Partial) -> typing.Optional[DebugVariableValue]:
                ...

            @TraceResponse.Validators.field("expression_location")
            def validate_expression_location(v: typing.Optional[ExpressionLocation], values: TraceResponse.Partial) -> typing.Optional[ExpressionLocation]:
                ...

            @TraceResponse.Validators.field("stack")
            def validate_stack(v: StackInformation, values: TraceResponse.Partial) -> StackInformation:
                ...

            @TraceResponse.Validators.field("stdout")
            def validate_stdout(v: typing.Optional[str], values: TraceResponse.Partial) -> typing.Optional[str]:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[TraceResponse.Partial], TraceResponse.Partial]]] = []
        _submission_id_validators: typing.ClassVar[typing.List[TraceResponse.Validators.SubmissionIdValidator]] = []
        _line_number_validators: typing.ClassVar[typing.List[TraceResponse.Validators.LineNumberValidator]] = []
        _return_value_validators: typing.ClassVar[typing.List[TraceResponse.Validators.ReturnValueValidator]] = []
        _expression_location_validators: typing.ClassVar[
            typing.List[TraceResponse.Validators.ExpressionLocationValidator]
        ] = []
        _stack_validators: typing.ClassVar[typing.List[TraceResponse.Validators.StackValidator]] = []
        _stdout_validators: typing.ClassVar[typing.List[TraceResponse.Validators.StdoutValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TraceResponse.Partial], TraceResponse.Partial]
        ) -> typing.Callable[[TraceResponse.Partial], TraceResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [TraceResponse.Validators.SubmissionIdValidator], TraceResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["line_number"]
        ) -> typing.Callable[
            [TraceResponse.Validators.LineNumberValidator], TraceResponse.Validators.LineNumberValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["return_value"]
        ) -> typing.Callable[
            [TraceResponse.Validators.ReturnValueValidator], TraceResponse.Validators.ReturnValueValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expression_location"]
        ) -> typing.Callable[
            [TraceResponse.Validators.ExpressionLocationValidator], TraceResponse.Validators.ExpressionLocationValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stack"]
        ) -> typing.Callable[[TraceResponse.Validators.StackValidator], TraceResponse.Validators.StackValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"]
        ) -> typing.Callable[[TraceResponse.Validators.StdoutValidator], TraceResponse.Validators.StdoutValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                if field_name == "line_number":
                    cls._line_number_validators.append(validator)
                if field_name == "return_value":
                    cls._return_value_validators.append(validator)
                if field_name == "expression_location":
                    cls._expression_location_validators.append(validator)
                if field_name == "stack":
                    cls._stack_validators.append(validator)
                if field_name == "stdout":
                    cls._stdout_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, v: SubmissionId, *, values: TraceResponse.Partial) -> SubmissionId:
                ...

        class LineNumberValidator(typing_extensions.Protocol):
            def __call__(self, v: int, *, values: TraceResponse.Partial) -> int:
                ...

        class ReturnValueValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[DebugVariableValue], *, values: TraceResponse.Partial
            ) -> typing.Optional[DebugVariableValue]:
                ...

        class ExpressionLocationValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[ExpressionLocation], *, values: TraceResponse.Partial
            ) -> typing.Optional[ExpressionLocation]:
                ...

        class StackValidator(typing_extensions.Protocol):
            def __call__(self, v: StackInformation, *, values: TraceResponse.Partial) -> StackInformation:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, v: typing.Optional[str], *, values: TraceResponse.Partial) -> typing.Optional[str]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TraceResponse.Partial) -> TraceResponse.Partial:
        for validator in TraceResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: TraceResponse.Partial) -> SubmissionId:
        for validator in TraceResponse.Validators._submission_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("line_number")
    def _validate_line_number(cls, v: int, values: TraceResponse.Partial) -> int:
        for validator in TraceResponse.Validators._line_number_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("return_value")
    def _validate_return_value(
        cls, v: typing.Optional[DebugVariableValue], values: TraceResponse.Partial
    ) -> typing.Optional[DebugVariableValue]:
        for validator in TraceResponse.Validators._return_value_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("expression_location")
    def _validate_expression_location(
        cls, v: typing.Optional[ExpressionLocation], values: TraceResponse.Partial
    ) -> typing.Optional[ExpressionLocation]:
        for validator in TraceResponse.Validators._expression_location_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("stack")
    def _validate_stack(cls, v: StackInformation, values: TraceResponse.Partial) -> StackInformation:
        for validator in TraceResponse.Validators._stack_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("stdout")
    def _validate_stdout(cls, v: typing.Optional[str], values: TraceResponse.Partial) -> typing.Optional[str]:
        for validator in TraceResponse.Validators._stdout_validators:
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
