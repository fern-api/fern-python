# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .....commons.types.language import Language
from .file_info_v_2 import FileInfoV2


class GetBasicSolutionFileResponse(pydantic.BaseModel):
    solution_file_by_language: typing.Dict[Language, FileInfoV2] = pydantic.Field(alias="solutionFileByLanguage")

    class Partial(typing_extensions.TypedDict):
        solution_file_by_language: typing_extensions.NotRequired[typing.Dict[Language, FileInfoV2]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetBasicSolutionFileResponse.Validators.root
            def validate(values: GetBasicSolutionFileResponse.Partial) -> GetBasicSolutionFileResponse.Partial:
                ...

            @GetBasicSolutionFileResponse.Validators.field("solution_file_by_language")
            def validate_solution_file_by_language(solution_file_by_language: typing.Dict[Language, FileInfoV2], values: GetBasicSolutionFileResponse.Partial) -> typing.Dict[Language, FileInfoV2]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GetBasicSolutionFileResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GetBasicSolutionFileResponse.Validators._RootValidator]] = []
        _solution_file_by_language_pre_validators: typing.ClassVar[
            typing.List[GetBasicSolutionFileResponse.Validators.SolutionFileByLanguageValidator]
        ] = []
        _solution_file_by_language_post_validators: typing.ClassVar[
            typing.List[GetBasicSolutionFileResponse.Validators.SolutionFileByLanguageValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> GetBasicSolutionFileResponse.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["solution_file_by_language"]
        ) -> typing.Callable[
            [GetBasicSolutionFileResponse.Validators.SolutionFileByLanguageValidator],
            GetBasicSolutionFileResponse.Validators.SolutionFileByLanguageValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "solution_file_by_language":
                    if pre:
                        cls._solution_file_by_language_pre_validators.append(validator)
                    else:
                        cls._solution_file_by_language_post_validators.append(validator)
                return validator

            return decorator

        class SolutionFileByLanguageValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, FileInfoV2], __values: GetBasicSolutionFileResponse.Partial
            ) -> typing.Dict[Language, FileInfoV2]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GetBasicSolutionFileResponse.Partial) -> GetBasicSolutionFileResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: GetBasicSolutionFileResponse.Partial) -> GetBasicSolutionFileResponse.Partial:
        for validator in GetBasicSolutionFileResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: GetBasicSolutionFileResponse.Partial) -> GetBasicSolutionFileResponse.Partial:
        for validator in GetBasicSolutionFileResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("solution_file_by_language", pre=True)
    def _pre_validate_solution_file_by_language(
        cls, v: typing.Dict[Language, FileInfoV2], values: GetBasicSolutionFileResponse.Partial
    ) -> typing.Dict[Language, FileInfoV2]:
        for validator in GetBasicSolutionFileResponse.Validators._solution_file_by_language_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("solution_file_by_language", pre=False)
    def _post_validate_solution_file_by_language(
        cls, v: typing.Dict[Language, FileInfoV2], values: GetBasicSolutionFileResponse.Partial
    ) -> typing.Dict[Language, FileInfoV2]:
        for validator in GetBasicSolutionFileResponse.Validators._solution_file_by_language_post_validators:
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
