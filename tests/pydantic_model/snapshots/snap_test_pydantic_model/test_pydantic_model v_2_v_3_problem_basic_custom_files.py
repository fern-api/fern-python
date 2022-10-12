# This file was auto-generated by Fern from our API Definition.

# type: ignore
# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.language import Language
from .basic_test_case_template import BasicTestCaseTemplate
from .files import Files
from .non_void_function_signature import NonVoidFunctionSignature


class BasicCustomFiles(pydantic.BaseModel):
    method_name: str = pydantic.Field(alias="methodName")
    signature: NonVoidFunctionSignature
    additional_files: typing.Dict[Language, Files] = pydantic.Field(alias="additionalFiles")
    basic_test_case_template: BasicTestCaseTemplate = pydantic.Field(alias="basicTestCaseTemplate")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @BasicCustomFiles.Validators.field("method_name")
            def validate_method_name(v: str, values: BasicCustomFiles.Partial) -> str:
                ...

            @BasicCustomFiles.Validators.field("signature")
            def validate_signature(v: NonVoidFunctionSignature, values: BasicCustomFiles.Partial) -> NonVoidFunctionSignature:
                ...

            @BasicCustomFiles.Validators.field("additional_files")
            def validate_additional_files(v: typing.Dict[Language, Files], values: BasicCustomFiles.Partial) -> typing.Dict[Language, Files]:
                ...

            @BasicCustomFiles.Validators.field("basic_test_case_template")
            def validate_basic_test_case_template(v: BasicTestCaseTemplate, values: BasicCustomFiles.Partial) -> BasicTestCaseTemplate:
                ...
        """

        _method_name_validators: typing.ClassVar[typing.List[BasicCustomFiles.Validators.MethodNameValidator]] = []
        _signature_validators: typing.ClassVar[typing.List[BasicCustomFiles.Validators.SignatureValidator]] = []
        _additional_files_validators: typing.ClassVar[
            typing.List[BasicCustomFiles.Validators.AdditionalFilesValidator]
        ] = []
        _basic_test_case_template_validators: typing.ClassVar[
            typing.List[BasicCustomFiles.Validators.BasicTestCaseTemplateValidator]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"]
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.MethodNameValidator], BasicCustomFiles.Validators.MethodNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["signature"]
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.SignatureValidator], BasicCustomFiles.Validators.SignatureValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["additional_files"]
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.AdditionalFilesValidator], BasicCustomFiles.Validators.AdditionalFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["basic_test_case_template"]
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.BasicTestCaseTemplateValidator],
            BasicCustomFiles.Validators.BasicTestCaseTemplateValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "method_name":
                    cls._method_name_validators.append(validator)
                if field_name == "signature":
                    cls._signature_validators.append(validator)
                if field_name == "additional_files":
                    cls._additional_files_validators.append(validator)
                if field_name == "basic_test_case_template":
                    cls._basic_test_case_template_validators.append(validator)
                return validator

            return decorator

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: BasicCustomFiles.Partial) -> str:
                ...

        class SignatureValidator(typing_extensions.Protocol):
            def __call__(
                self, v: NonVoidFunctionSignature, *, values: BasicCustomFiles.Partial
            ) -> NonVoidFunctionSignature:
                ...

        class AdditionalFilesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[Language, Files], *, values: BasicCustomFiles.Partial
            ) -> typing.Dict[Language, Files]:
                ...

        class BasicTestCaseTemplateValidator(typing_extensions.Protocol):
            def __call__(self, v: BasicTestCaseTemplate, *, values: BasicCustomFiles.Partial) -> BasicTestCaseTemplate:
                ...

    @pydantic.validator("method_name")
    def _validate_method_name(cls, v: str, values: str) -> str:
        for validator in BasicCustomFiles.Validators._method_name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("signature")
    def _validate_signature(
        cls, v: NonVoidFunctionSignature, values: NonVoidFunctionSignature
    ) -> NonVoidFunctionSignature:
        for validator in BasicCustomFiles.Validators._signature_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("additional_files")
    def _validate_additional_files(
        cls, v: typing.Dict[Language, Files], values: typing.Dict[Language, Files]
    ) -> typing.Dict[Language, Files]:
        for validator in BasicCustomFiles.Validators._additional_files_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("basic_test_case_template")
    def _validate_basic_test_case_template(
        cls, v: BasicTestCaseTemplate, values: BasicTestCaseTemplate
    ) -> BasicTestCaseTemplate:
        for validator in BasicCustomFiles.Validators._basic_test_case_template_validators:
            v = validator(v, values=values)
        return v

    class Partial(typing.TypedDict):
        method_name: typing_extensions.NotRequired[str]
        signature: typing_extensions.NotRequired[NonVoidFunctionSignature]
        additional_files: typing_extensions.NotRequired[typing.Dict[Language, Files]]
        basic_test_case_template: typing_extensions.NotRequired[BasicTestCaseTemplate]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
