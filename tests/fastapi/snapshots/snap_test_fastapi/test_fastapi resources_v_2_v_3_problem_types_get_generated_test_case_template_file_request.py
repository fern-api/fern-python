# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_template import TestCaseTemplate


class GetGeneratedTestCaseTemplateFileRequest(pydantic.BaseModel):
    template: TestCaseTemplate

    class Partial(typing_extensions.TypedDict):
        template: typing_extensions.NotRequired[TestCaseTemplate]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetGeneratedTestCaseTemplateFileRequest.Validators.root
            def validate(values: GetGeneratedTestCaseTemplateFileRequest.Partial) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
                ...

            @GetGeneratedTestCaseTemplateFileRequest.Validators.field("template")
            def validate_template(template: TestCaseTemplate, values: GetGeneratedTestCaseTemplateFileRequest.Partial) -> TestCaseTemplate:
                ...
        """

        _pre_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseTemplateFileRequest.Validators._RootValidator]
        ] = []
        _post_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseTemplateFileRequest.Validators._RootValidator]
        ] = []
        _template_pre_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator]
        ] = []
        _template_post_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> GetGeneratedTestCaseTemplateFileRequest.Validators._RootValidator:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["template"]
        ) -> typing.Callable[
            [GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator],
            GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "template":
                    if pre:
                        cls._template_pre_validators.append(validator)
                    else:
                        cls._template_post_validators.append(validator)
                return validator

            return decorator

        class TemplateValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestCaseTemplate, __values: GetGeneratedTestCaseTemplateFileRequest.Partial
            ) -> TestCaseTemplate:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: GetGeneratedTestCaseTemplateFileRequest.Partial
            ) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(
        cls, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(
        cls, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("template", pre=True)
    def _pre_validate_template(
        cls, v: TestCaseTemplate, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> TestCaseTemplate:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._template_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("template", pre=False)
    def _post_validate_template(
        cls, v: TestCaseTemplate, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> TestCaseTemplate:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._template_post_validators:
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
