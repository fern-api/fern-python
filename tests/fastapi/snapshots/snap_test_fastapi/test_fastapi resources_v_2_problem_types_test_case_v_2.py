# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.types.variable_value import VariableValue
from .parameter_id import ParameterId
from .test_case_expects import TestCaseExpects
from .test_case_implementation_reference import TestCaseImplementationReference
from .test_case_metadata import TestCaseMetadata


class TestCaseV2(pydantic.BaseModel):
    metadata: TestCaseMetadata
    implementation: TestCaseImplementationReference
    arguments: typing.Dict[ParameterId, VariableValue]
    expects: typing.Optional[TestCaseExpects]

    class Partial(typing_extensions.TypedDict):
        metadata: typing_extensions.NotRequired[TestCaseMetadata]
        implementation: typing_extensions.NotRequired[TestCaseImplementationReference]
        arguments: typing_extensions.NotRequired[typing.Dict[ParameterId, VariableValue]]
        expects: typing_extensions.NotRequired[typing.Optional[TestCaseExpects]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseV2.Validators.root
            def validate(values: TestCaseV2.Partial) -> TestCaseV2.Partial:
                ...

            @TestCaseV2.Validators.field("metadata")
            def validate_metadata(v: TestCaseMetadata, values: TestCaseV2.Partial) -> TestCaseMetadata:
                ...

            @TestCaseV2.Validators.field("implementation")
            def validate_implementation(v: TestCaseImplementationReference, values: TestCaseV2.Partial) -> TestCaseImplementationReference:
                ...

            @TestCaseV2.Validators.field("arguments")
            def validate_arguments(v: typing.Dict[ParameterId, VariableValue], values: TestCaseV2.Partial) -> typing.Dict[ParameterId, VariableValue]:
                ...

            @TestCaseV2.Validators.field("expects")
            def validate_expects(v: typing.Optional[TestCaseExpects], values: TestCaseV2.Partial) -> typing.Optional[TestCaseExpects]:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[TestCaseV2.Partial], TestCaseV2.Partial]]] = []
        _metadata_validators: typing.ClassVar[typing.List[TestCaseV2.Validators.MetadataValidator]] = []
        _implementation_validators: typing.ClassVar[typing.List[TestCaseV2.Validators.ImplementationValidator]] = []
        _arguments_validators: typing.ClassVar[typing.List[TestCaseV2.Validators.ArgumentsValidator]] = []
        _expects_validators: typing.ClassVar[typing.List[TestCaseV2.Validators.ExpectsValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TestCaseV2.Partial], TestCaseV2.Partial]
        ) -> typing.Callable[[TestCaseV2.Partial], TestCaseV2.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["metadata"]
        ) -> typing.Callable[[TestCaseV2.Validators.MetadataValidator], TestCaseV2.Validators.MetadataValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["implementation"]
        ) -> typing.Callable[
            [TestCaseV2.Validators.ImplementationValidator], TestCaseV2.Validators.ImplementationValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["arguments"]
        ) -> typing.Callable[[TestCaseV2.Validators.ArgumentsValidator], TestCaseV2.Validators.ArgumentsValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expects"]
        ) -> typing.Callable[[TestCaseV2.Validators.ExpectsValidator], TestCaseV2.Validators.ExpectsValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "metadata":
                    cls._metadata_validators.append(validator)
                if field_name == "implementation":
                    cls._implementation_validators.append(validator)
                if field_name == "arguments":
                    cls._arguments_validators.append(validator)
                if field_name == "expects":
                    cls._expects_validators.append(validator)
                return validator

            return decorator

        class MetadataValidator(typing_extensions.Protocol):
            def __call__(self, v: TestCaseMetadata, *, values: TestCaseV2.Partial) -> TestCaseMetadata:
                ...

        class ImplementationValidator(typing_extensions.Protocol):
            def __call__(
                self, v: TestCaseImplementationReference, *, values: TestCaseV2.Partial
            ) -> TestCaseImplementationReference:
                ...

        class ArgumentsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[ParameterId, VariableValue], *, values: TestCaseV2.Partial
            ) -> typing.Dict[ParameterId, VariableValue]:
                ...

        class ExpectsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[TestCaseExpects], *, values: TestCaseV2.Partial
            ) -> typing.Optional[TestCaseExpects]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TestCaseV2.Partial) -> TestCaseV2.Partial:
        for validator in TestCaseV2.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("metadata")
    def _validate_metadata(cls, v: TestCaseMetadata, values: TestCaseV2.Partial) -> TestCaseMetadata:
        for validator in TestCaseV2.Validators._metadata_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("implementation")
    def _validate_implementation(
        cls, v: TestCaseImplementationReference, values: TestCaseV2.Partial
    ) -> TestCaseImplementationReference:
        for validator in TestCaseV2.Validators._implementation_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("arguments")
    def _validate_arguments(
        cls, v: typing.Dict[ParameterId, VariableValue], values: TestCaseV2.Partial
    ) -> typing.Dict[ParameterId, VariableValue]:
        for validator in TestCaseV2.Validators._arguments_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("expects")
    def _validate_expects(
        cls, v: typing.Optional[TestCaseExpects], values: TestCaseV2.Partial
    ) -> typing.Optional[TestCaseExpects]:
        for validator in TestCaseV2.Validators._expects_validators:
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
