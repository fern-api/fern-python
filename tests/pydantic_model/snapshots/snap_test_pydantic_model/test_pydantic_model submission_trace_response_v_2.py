# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.debug_variable_value import DebugVariableValue
from .expression_location import ExpressionLocation
from .stack_information import StackInformation
from .submission_id import SubmissionId
from .traced_file import TracedFile


class TraceResponseV2(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    line_number: int = pydantic.Field(alias="lineNumber")
    file: TracedFile
    return_value: typing.Optional[DebugVariableValue] = pydantic.Field(alias="returnValue")
    expression_location: typing.Optional[ExpressionLocation] = pydantic.Field(alias="expressionLocation")
    stack: StackInformation
    stdout: typing.Optional[str]

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        line_number: typing_extensions.NotRequired[int]
        file: typing_extensions.NotRequired[TracedFile]
        return_value: typing_extensions.NotRequired[typing.Optional[DebugVariableValue]]
        expression_location: typing_extensions.NotRequired[typing.Optional[ExpressionLocation]]
        stack: typing_extensions.NotRequired[StackInformation]
        stdout: typing_extensions.NotRequired[typing.Optional[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TraceResponseV2.Validators.root
            def validate(values: TraceResponseV2.Partial) -> TraceResponseV2.Partial:
                ...

            @TraceResponseV2.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: TraceResponseV2.Partial) -> SubmissionId:
                ...

            @TraceResponseV2.Validators.field("line_number")
            def validate_line_number(line_number: int, values: TraceResponseV2.Partial) -> int:
                ...

            @TraceResponseV2.Validators.field("file")
            def validate_file(file: TracedFile, values: TraceResponseV2.Partial) -> TracedFile:
                ...

            @TraceResponseV2.Validators.field("return_value")
            def validate_return_value(return_value: typing.Optional[DebugVariableValue], values: TraceResponseV2.Partial) -> typing.Optional[DebugVariableValue]:
                ...

            @TraceResponseV2.Validators.field("expression_location")
            def validate_expression_location(expression_location: typing.Optional[ExpressionLocation], values: TraceResponseV2.Partial) -> typing.Optional[ExpressionLocation]:
                ...

            @TraceResponseV2.Validators.field("stack")
            def validate_stack(stack: StackInformation, values: TraceResponseV2.Partial) -> StackInformation:
                ...

            @TraceResponseV2.Validators.field("stdout")
            def validate_stdout(stdout: typing.Optional[str], values: TraceResponseV2.Partial) -> typing.Optional[str]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[TraceResponseV2.Validators.SubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[TraceResponseV2.Validators.SubmissionIdValidator]
        ] = []
        _line_number_pre_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.LineNumberValidator]] = []
        _line_number_post_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.LineNumberValidator]] = []
        _file_pre_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.FileValidator]] = []
        _file_post_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.FileValidator]] = []
        _return_value_pre_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.ReturnValueValidator]] = []
        _return_value_post_validators: typing.ClassVar[
            typing.List[TraceResponseV2.Validators.ReturnValueValidator]
        ] = []
        _expression_location_pre_validators: typing.ClassVar[
            typing.List[TraceResponseV2.Validators.ExpressionLocationValidator]
        ] = []
        _expression_location_post_validators: typing.ClassVar[
            typing.List[TraceResponseV2.Validators.ExpressionLocationValidator]
        ] = []
        _stack_pre_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.StackValidator]] = []
        _stack_post_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.StackValidator]] = []
        _stdout_pre_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.StdoutValidator]] = []
        _stdout_post_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.StdoutValidator]] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> TraceResponseV2.Validators._RootValidator:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [TraceResponseV2.Validators.SubmissionIdValidator], TraceResponseV2.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["line_number"]
        ) -> typing.Callable[
            [TraceResponseV2.Validators.LineNumberValidator], TraceResponseV2.Validators.LineNumberValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["file"]
        ) -> typing.Callable[[TraceResponseV2.Validators.FileValidator], TraceResponseV2.Validators.FileValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["return_value"]
        ) -> typing.Callable[
            [TraceResponseV2.Validators.ReturnValueValidator], TraceResponseV2.Validators.ReturnValueValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expression_location"]
        ) -> typing.Callable[
            [TraceResponseV2.Validators.ExpressionLocationValidator],
            TraceResponseV2.Validators.ExpressionLocationValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stack"]
        ) -> typing.Callable[[TraceResponseV2.Validators.StackValidator], TraceResponseV2.Validators.StackValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"]
        ) -> typing.Callable[[TraceResponseV2.Validators.StdoutValidator], TraceResponseV2.Validators.StdoutValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "line_number":
                    if pre:
                        cls._line_number_pre_validators.append(validator)
                    else:
                        cls._line_number_post_validators.append(validator)
                if field_name == "file":
                    if pre:
                        cls._file_pre_validators.append(validator)
                    else:
                        cls._file_post_validators.append(validator)
                if field_name == "return_value":
                    if pre:
                        cls._return_value_pre_validators.append(validator)
                    else:
                        cls._return_value_post_validators.append(validator)
                if field_name == "expression_location":
                    if pre:
                        cls._expression_location_pre_validators.append(validator)
                    else:
                        cls._expression_location_post_validators.append(validator)
                if field_name == "stack":
                    if pre:
                        cls._stack_pre_validators.append(validator)
                    else:
                        cls._stack_post_validators.append(validator)
                if field_name == "stdout":
                    if pre:
                        cls._stdout_pre_validators.append(validator)
                    else:
                        cls._stdout_post_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: TraceResponseV2.Partial) -> SubmissionId:
                ...

        class LineNumberValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: TraceResponseV2.Partial) -> int:
                ...

        class FileValidator(typing_extensions.Protocol):
            def __call__(self, __v: TracedFile, __values: TraceResponseV2.Partial) -> TracedFile:
                ...

        class ReturnValueValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[DebugVariableValue], __values: TraceResponseV2.Partial
            ) -> typing.Optional[DebugVariableValue]:
                ...

        class ExpressionLocationValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[ExpressionLocation], __values: TraceResponseV2.Partial
            ) -> typing.Optional[ExpressionLocation]:
                ...

        class StackValidator(typing_extensions.Protocol):
            def __call__(self, __v: StackInformation, __values: TraceResponseV2.Partial) -> StackInformation:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: TraceResponseV2.Partial) -> typing.Optional[str]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TraceResponseV2.Partial) -> TraceResponseV2.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TraceResponseV2.Partial) -> TraceResponseV2.Partial:
        for validator in TraceResponseV2.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TraceResponseV2.Partial) -> TraceResponseV2.Partial:
        for validator in TraceResponseV2.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: TraceResponseV2.Partial) -> SubmissionId:
        for validator in TraceResponseV2.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: TraceResponseV2.Partial) -> SubmissionId:
        for validator in TraceResponseV2.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("line_number", pre=True)
    def _pre_validate_line_number(cls, v: int, values: TraceResponseV2.Partial) -> int:
        for validator in TraceResponseV2.Validators._line_number_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("line_number", pre=False)
    def _post_validate_line_number(cls, v: int, values: TraceResponseV2.Partial) -> int:
        for validator in TraceResponseV2.Validators._line_number_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("file", pre=True)
    def _pre_validate_file(cls, v: TracedFile, values: TraceResponseV2.Partial) -> TracedFile:
        for validator in TraceResponseV2.Validators._file_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("file", pre=False)
    def _post_validate_file(cls, v: TracedFile, values: TraceResponseV2.Partial) -> TracedFile:
        for validator in TraceResponseV2.Validators._file_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("return_value", pre=True)
    def _pre_validate_return_value(
        cls, v: typing.Optional[DebugVariableValue], values: TraceResponseV2.Partial
    ) -> typing.Optional[DebugVariableValue]:
        for validator in TraceResponseV2.Validators._return_value_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("return_value", pre=False)
    def _post_validate_return_value(
        cls, v: typing.Optional[DebugVariableValue], values: TraceResponseV2.Partial
    ) -> typing.Optional[DebugVariableValue]:
        for validator in TraceResponseV2.Validators._return_value_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expression_location", pre=True)
    def _pre_validate_expression_location(
        cls, v: typing.Optional[ExpressionLocation], values: TraceResponseV2.Partial
    ) -> typing.Optional[ExpressionLocation]:
        for validator in TraceResponseV2.Validators._expression_location_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expression_location", pre=False)
    def _post_validate_expression_location(
        cls, v: typing.Optional[ExpressionLocation], values: TraceResponseV2.Partial
    ) -> typing.Optional[ExpressionLocation]:
        for validator in TraceResponseV2.Validators._expression_location_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stack", pre=True)
    def _pre_validate_stack(cls, v: StackInformation, values: TraceResponseV2.Partial) -> StackInformation:
        for validator in TraceResponseV2.Validators._stack_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stack", pre=False)
    def _post_validate_stack(cls, v: StackInformation, values: TraceResponseV2.Partial) -> StackInformation:
        for validator in TraceResponseV2.Validators._stack_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=True)
    def _pre_validate_stdout(cls, v: typing.Optional[str], values: TraceResponseV2.Partial) -> typing.Optional[str]:
        for validator in TraceResponseV2.Validators._stdout_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=False)
    def _post_validate_stdout(cls, v: typing.Optional[str], values: TraceResponseV2.Partial) -> typing.Optional[str]:
        for validator in TraceResponseV2.Validators._stdout_post_validators:
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
        allow_population_by_field_name = True
