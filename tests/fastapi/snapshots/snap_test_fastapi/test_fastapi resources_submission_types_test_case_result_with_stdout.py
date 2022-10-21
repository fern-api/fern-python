# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_result import TestCaseResult


class TestCaseResultWithStdout(pydantic.BaseModel):
    result: TestCaseResult
    stdout: str

    class Partial(typing_extensions.TypedDict):
        result: typing_extensions.NotRequired[TestCaseResult]
        stdout: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseResultWithStdout.Validators.root
            def validate(values: TestCaseResultWithStdout.Partial) -> TestCaseResultWithStdout.Partial:
                ...

            @TestCaseResultWithStdout.Validators.field("result")
            def validate_result(v: TestCaseResult, values: TestCaseResultWithStdout.Partial) -> TestCaseResult:
                ...

            @TestCaseResultWithStdout.Validators.field("stdout")
            def validate_stdout(v: str, values: TestCaseResultWithStdout.Partial) -> str:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TestCaseResultWithStdout.Partial], TestCaseResultWithStdout.Partial]]
        ] = []
        _result_validators: typing.ClassVar[typing.List[TestCaseResultWithStdout.Validators.ResultValidator]] = []
        _stdout_validators: typing.ClassVar[typing.List[TestCaseResultWithStdout.Validators.StdoutValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TestCaseResultWithStdout.Partial], TestCaseResultWithStdout.Partial]
        ) -> typing.Callable[[TestCaseResultWithStdout.Partial], TestCaseResultWithStdout.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["result"]
        ) -> typing.Callable[
            [TestCaseResultWithStdout.Validators.ResultValidator], TestCaseResultWithStdout.Validators.ResultValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"]
        ) -> typing.Callable[
            [TestCaseResultWithStdout.Validators.StdoutValidator], TestCaseResultWithStdout.Validators.StdoutValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "result":
                    cls._result_validators.append(validator)
                if field_name == "stdout":
                    cls._stdout_validators.append(validator)
                return validator

            return decorator

        class ResultValidator(typing_extensions.Protocol):
            def __call__(self, v: TestCaseResult, *, values: TestCaseResultWithStdout.Partial) -> TestCaseResult:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: TestCaseResultWithStdout.Partial) -> str:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TestCaseResultWithStdout.Partial) -> TestCaseResultWithStdout.Partial:
        for validator in TestCaseResultWithStdout.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("result")
    def _validate_result(cls, v: TestCaseResult, values: TestCaseResultWithStdout.Partial) -> TestCaseResult:
        for validator in TestCaseResultWithStdout.Validators._result_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("stdout")
    def _validate_stdout(cls, v: str, values: TestCaseResultWithStdout.Partial) -> str:
        for validator in TestCaseResultWithStdout.Validators._stdout_validators:
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
