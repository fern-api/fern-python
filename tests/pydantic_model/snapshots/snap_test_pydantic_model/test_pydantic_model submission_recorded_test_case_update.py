# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..v_2.problem.test_case_id import TestCaseId


class RecordedTestCaseUpdate(pydantic.BaseModel):
    test_case_id: TestCaseId = pydantic.Field(alias="testCaseId")
    trace_responses_size: int = pydantic.Field(alias="traceResponsesSize")

    class Partial(typing_extensions.TypedDict):
        test_case_id: typing_extensions.NotRequired[TestCaseId]
        trace_responses_size: typing_extensions.NotRequired[int]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @RecordedTestCaseUpdate.Validators.root
            def validate(values: RecordedTestCaseUpdate.Partial) -> RecordedTestCaseUpdate.Partial:
                ...

            @RecordedTestCaseUpdate.Validators.field("test_case_id")
            def validate_test_case_id(test_case_id: TestCaseId, values: RecordedTestCaseUpdate.Partial) -> TestCaseId:
                ...

            @RecordedTestCaseUpdate.Validators.field("trace_responses_size")
            def validate_trace_responses_size(trace_responses_size: int, values: RecordedTestCaseUpdate.Partial) -> int:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[RecordedTestCaseUpdate.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[RecordedTestCaseUpdate.Validators._RootValidator]] = []
        _test_case_id_pre_validators: typing.ClassVar[
            typing.List[RecordedTestCaseUpdate.Validators.TestCaseIdValidator]
        ] = []
        _test_case_id_post_validators: typing.ClassVar[
            typing.List[RecordedTestCaseUpdate.Validators.TestCaseIdValidator]
        ] = []
        _trace_responses_size_pre_validators: typing.ClassVar[
            typing.List[RecordedTestCaseUpdate.Validators.TraceResponsesSizeValidator]
        ] = []
        _trace_responses_size_post_validators: typing.ClassVar[
            typing.List[RecordedTestCaseUpdate.Validators.TraceResponsesSizeValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> RecordedTestCaseUpdate.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["test_case_id"]
        ) -> typing.Callable[
            [RecordedTestCaseUpdate.Validators.TestCaseIdValidator],
            RecordedTestCaseUpdate.Validators.TestCaseIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses_size"]
        ) -> typing.Callable[
            [RecordedTestCaseUpdate.Validators.TraceResponsesSizeValidator],
            RecordedTestCaseUpdate.Validators.TraceResponsesSizeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "test_case_id":
                    if pre:
                        cls._test_case_id_pre_validators.append(validator)
                    else:
                        cls._test_case_id_post_validators.append(validator)
                if field_name == "trace_responses_size":
                    if pre:
                        cls._trace_responses_size_pre_validators.append(validator)
                    else:
                        cls._trace_responses_size_post_validators.append(validator)
                return validator

            return decorator

        class TestCaseIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: TestCaseId, __values: RecordedTestCaseUpdate.Partial) -> TestCaseId:
                ...

        class TraceResponsesSizeValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: RecordedTestCaseUpdate.Partial) -> int:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: RecordedTestCaseUpdate.Partial) -> RecordedTestCaseUpdate.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: RecordedTestCaseUpdate.Partial) -> RecordedTestCaseUpdate.Partial:
        for validator in RecordedTestCaseUpdate.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: RecordedTestCaseUpdate.Partial) -> RecordedTestCaseUpdate.Partial:
        for validator in RecordedTestCaseUpdate.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("test_case_id", pre=True)
    def _pre_validate_test_case_id(cls, v: TestCaseId, values: RecordedTestCaseUpdate.Partial) -> TestCaseId:
        for validator in RecordedTestCaseUpdate.Validators._test_case_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case_id", pre=False)
    def _post_validate_test_case_id(cls, v: TestCaseId, values: RecordedTestCaseUpdate.Partial) -> TestCaseId:
        for validator in RecordedTestCaseUpdate.Validators._test_case_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses_size", pre=True)
    def _pre_validate_trace_responses_size(cls, v: int, values: RecordedTestCaseUpdate.Partial) -> int:
        for validator in RecordedTestCaseUpdate.Validators._trace_responses_size_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses_size", pre=False)
    def _post_validate_trace_responses_size(cls, v: int, values: RecordedTestCaseUpdate.Partial) -> int:
        for validator in RecordedTestCaseUpdate.Validators._trace_responses_size_post_validators:
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
