# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .function_implementation_for_multiple_languages import FunctionImplementationForMultipleLanguages
from .parameter import Parameter


class VoidFunctionDefinition(pydantic.BaseModel):
    parameters: typing.List[Parameter]
    code: FunctionImplementationForMultipleLanguages

    class Partial(typing_extensions.TypedDict):
        parameters: typing_extensions.NotRequired[typing.List[Parameter]]
        code: typing_extensions.NotRequired[FunctionImplementationForMultipleLanguages]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @VoidFunctionDefinition.Validators.root
            def validate(values: VoidFunctionDefinition.Partial) -> VoidFunctionDefinition.Partial:
                ...

            @VoidFunctionDefinition.Validators.field("parameters")
            def validate_parameters(parameters: typing.List[Parameter], values: VoidFunctionDefinition.Partial) -> typing.List[Parameter]:
                ...

            @VoidFunctionDefinition.Validators.field("code")
            def validate_code(code: FunctionImplementationForMultipleLanguages, values: VoidFunctionDefinition.Partial) -> FunctionImplementationForMultipleLanguages:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[VoidFunctionDefinition.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[VoidFunctionDefinition.Validators._RootValidator]] = []
        _parameters_pre_validators: typing.ClassVar[
            typing.List[VoidFunctionDefinition.Validators.ParametersValidator]
        ] = []
        _parameters_post_validators: typing.ClassVar[
            typing.List[VoidFunctionDefinition.Validators.ParametersValidator]
        ] = []
        _code_pre_validators: typing.ClassVar[typing.List[VoidFunctionDefinition.Validators.CodeValidator]] = []
        _code_post_validators: typing.ClassVar[typing.List[VoidFunctionDefinition.Validators.CodeValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [VoidFunctionDefinition.Validators._RootValidator], VoidFunctionDefinition.Validators._RootValidator
        ]:
            def decorator(
                validator: VoidFunctionDefinition.Validators._RootValidator,
            ) -> VoidFunctionDefinition.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["parameters"], *, pre: bool = False
        ) -> typing.Callable[
            [VoidFunctionDefinition.Validators.ParametersValidator],
            VoidFunctionDefinition.Validators.ParametersValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["code"], *, pre: bool = False
        ) -> typing.Callable[
            [VoidFunctionDefinition.Validators.CodeValidator], VoidFunctionDefinition.Validators.CodeValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "parameters":
                    if pre:
                        cls._parameters_pre_validators.append(validator)
                    else:
                        cls._parameters_post_validators.append(validator)
                if field_name == "code":
                    if pre:
                        cls._code_pre_validators.append(validator)
                    else:
                        cls._code_post_validators.append(validator)
                return validator

            return decorator

        class ParametersValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[Parameter], __values: VoidFunctionDefinition.Partial
            ) -> typing.List[Parameter]:
                ...

        class CodeValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: FunctionImplementationForMultipleLanguages, __values: VoidFunctionDefinition.Partial
            ) -> FunctionImplementationForMultipleLanguages:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: VoidFunctionDefinition.Partial) -> VoidFunctionDefinition.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: VoidFunctionDefinition.Partial) -> VoidFunctionDefinition.Partial:
        for validator in VoidFunctionDefinition.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: VoidFunctionDefinition.Partial) -> VoidFunctionDefinition.Partial:
        for validator in VoidFunctionDefinition.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("parameters", pre=True)
    def _pre_validate_parameters(
        cls, v: typing.List[Parameter], values: VoidFunctionDefinition.Partial
    ) -> typing.List[Parameter]:
        for validator in VoidFunctionDefinition.Validators._parameters_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("parameters", pre=False)
    def _post_validate_parameters(
        cls, v: typing.List[Parameter], values: VoidFunctionDefinition.Partial
    ) -> typing.List[Parameter]:
        for validator in VoidFunctionDefinition.Validators._parameters_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("code", pre=True)
    def _pre_validate_code(
        cls, v: FunctionImplementationForMultipleLanguages, values: VoidFunctionDefinition.Partial
    ) -> FunctionImplementationForMultipleLanguages:
        for validator in VoidFunctionDefinition.Validators._code_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("code", pre=False)
    def _post_validate_code(
        cls, v: FunctionImplementationForMultipleLanguages, values: VoidFunctionDefinition.Partial
    ) -> FunctionImplementationForMultipleLanguages:
        for validator in VoidFunctionDefinition.Validators._code_post_validators:
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
