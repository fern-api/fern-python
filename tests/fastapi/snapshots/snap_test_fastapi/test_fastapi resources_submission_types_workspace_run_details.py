# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2


class WorkspaceRunDetails(pydantic.BaseModel):
    exception_v_2: typing.Optional[ExceptionV2] = pydantic.Field(alias="exceptionV2")
    exception: typing.Optional[ExceptionInfo]
    stdout: str

    class Partial(typing_extensions.TypedDict):
        exception_v_2: typing_extensions.NotRequired[typing.Optional[ExceptionV2]]
        exception: typing_extensions.NotRequired[typing.Optional[ExceptionInfo]]
        stdout: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceRunDetails.Validators.root
            def validate(values: WorkspaceRunDetails.Partial) -> WorkspaceRunDetails.Partial:
                ...

            @WorkspaceRunDetails.Validators.field("exception_v_2")
            def validate_exception_v_2(exception_v_2: typing.Optional[ExceptionV2], values: WorkspaceRunDetails.Partial) -> typing.Optional[ExceptionV2]:
                ...

            @WorkspaceRunDetails.Validators.field("exception")
            def validate_exception(exception: typing.Optional[ExceptionInfo], values: WorkspaceRunDetails.Partial) -> typing.Optional[ExceptionInfo]:
                ...

            @WorkspaceRunDetails.Validators.field("stdout")
            def validate_stdout(stdout: str, values: WorkspaceRunDetails.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[WorkspaceRunDetails.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[WorkspaceRunDetails.Validators._RootValidator]] = []
        _exception_v_2_pre_validators: typing.ClassVar[
            typing.List[WorkspaceRunDetails.Validators.ExceptionV2Validator]
        ] = []
        _exception_v_2_post_validators: typing.ClassVar[
            typing.List[WorkspaceRunDetails.Validators.ExceptionV2Validator]
        ] = []
        _exception_pre_validators: typing.ClassVar[typing.List[WorkspaceRunDetails.Validators.ExceptionValidator]] = []
        _exception_post_validators: typing.ClassVar[typing.List[WorkspaceRunDetails.Validators.ExceptionValidator]] = []
        _stdout_pre_validators: typing.ClassVar[typing.List[WorkspaceRunDetails.Validators.StdoutValidator]] = []
        _stdout_post_validators: typing.ClassVar[typing.List[WorkspaceRunDetails.Validators.StdoutValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [WorkspaceRunDetails.Validators._RootValidator], WorkspaceRunDetails.Validators._RootValidator
        ]:
            def decorator(
                validator: WorkspaceRunDetails.Validators._RootValidator,
            ) -> WorkspaceRunDetails.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception_v_2"], *, pre: bool = False
        ) -> typing.Callable[
            [WorkspaceRunDetails.Validators.ExceptionV2Validator], WorkspaceRunDetails.Validators.ExceptionV2Validator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception"], *, pre: bool = False
        ) -> typing.Callable[
            [WorkspaceRunDetails.Validators.ExceptionValidator], WorkspaceRunDetails.Validators.ExceptionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"], *, pre: bool = False
        ) -> typing.Callable[
            [WorkspaceRunDetails.Validators.StdoutValidator], WorkspaceRunDetails.Validators.StdoutValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "exception_v_2":
                    if pre:
                        cls._exception_v_2_pre_validators.append(validator)
                    else:
                        cls._exception_v_2_post_validators.append(validator)
                if field_name == "exception":
                    if pre:
                        cls._exception_pre_validators.append(validator)
                    else:
                        cls._exception_post_validators.append(validator)
                if field_name == "stdout":
                    if pre:
                        cls._stdout_pre_validators.append(validator)
                    else:
                        cls._stdout_post_validators.append(validator)
                return validator

            return decorator

        class ExceptionV2Validator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[ExceptionV2], __values: WorkspaceRunDetails.Partial
            ) -> typing.Optional[ExceptionV2]:
                ...

        class ExceptionValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[ExceptionInfo], __values: WorkspaceRunDetails.Partial
            ) -> typing.Optional[ExceptionInfo]:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: WorkspaceRunDetails.Partial) -> str:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: WorkspaceRunDetails.Partial) -> WorkspaceRunDetails.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: WorkspaceRunDetails.Partial) -> WorkspaceRunDetails.Partial:
        for validator in WorkspaceRunDetails.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: WorkspaceRunDetails.Partial) -> WorkspaceRunDetails.Partial:
        for validator in WorkspaceRunDetails.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("exception_v_2", pre=True)
    def _pre_validate_exception_v_2(
        cls, v: typing.Optional[ExceptionV2], values: WorkspaceRunDetails.Partial
    ) -> typing.Optional[ExceptionV2]:
        for validator in WorkspaceRunDetails.Validators._exception_v_2_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception_v_2", pre=False)
    def _post_validate_exception_v_2(
        cls, v: typing.Optional[ExceptionV2], values: WorkspaceRunDetails.Partial
    ) -> typing.Optional[ExceptionV2]:
        for validator in WorkspaceRunDetails.Validators._exception_v_2_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception", pre=True)
    def _pre_validate_exception(
        cls, v: typing.Optional[ExceptionInfo], values: WorkspaceRunDetails.Partial
    ) -> typing.Optional[ExceptionInfo]:
        for validator in WorkspaceRunDetails.Validators._exception_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception", pre=False)
    def _post_validate_exception(
        cls, v: typing.Optional[ExceptionInfo], values: WorkspaceRunDetails.Partial
    ) -> typing.Optional[ExceptionInfo]:
        for validator in WorkspaceRunDetails.Validators._exception_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=True)
    def _pre_validate_stdout(cls, v: str, values: WorkspaceRunDetails.Partial) -> str:
        for validator in WorkspaceRunDetails.Validators._stdout_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=False)
    def _post_validate_stdout(cls, v: str, values: WorkspaceRunDetails.Partial) -> str:
        for validator in WorkspaceRunDetails.Validators._stdout_post_validators:
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
        extra = pydantic.Extra.forbid
