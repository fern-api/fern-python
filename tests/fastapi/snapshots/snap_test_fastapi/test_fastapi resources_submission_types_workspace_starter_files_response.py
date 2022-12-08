# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.language import Language
from .workspace_files import WorkspaceFiles


class WorkspaceStarterFilesResponse(pydantic.BaseModel):
    files: typing.Dict[Language, WorkspaceFiles]

    class Partial(typing_extensions.TypedDict):
        files: typing_extensions.NotRequired[typing.Dict[Language, WorkspaceFiles]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceStarterFilesResponse.Validators.root
            def validate(values: WorkspaceStarterFilesResponse.Partial) -> WorkspaceStarterFilesResponse.Partial:
                ...

            @WorkspaceStarterFilesResponse.Validators.field("files")
            def validate_files(files: typing.Dict[Language, WorkspaceFiles], values: WorkspaceStarterFilesResponse.Partial) -> typing.Dict[Language, WorkspaceFiles]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[WorkspaceStarterFilesResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[WorkspaceStarterFilesResponse.Validators._RootValidator]] = []
        _files_pre_validators: typing.ClassVar[
            typing.List[WorkspaceStarterFilesResponse.Validators.FilesValidator]
        ] = []
        _files_post_validators: typing.ClassVar[
            typing.List[WorkspaceStarterFilesResponse.Validators.FilesValidator]
        ] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [WorkspaceStarterFilesResponse.Validators._RootValidator],
            WorkspaceStarterFilesResponse.Validators._RootValidator,
        ]:
            def decorator(
                validator: WorkspaceStarterFilesResponse.Validators._RootValidator,
            ) -> WorkspaceStarterFilesResponse.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["files"], *, pre: bool = False
        ) -> typing.Callable[
            [WorkspaceStarterFilesResponse.Validators.FilesValidator],
            WorkspaceStarterFilesResponse.Validators.FilesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "files":
                    if pre:
                        cls._files_pre_validators.append(validator)
                    else:
                        cls._files_post_validators.append(validator)
                return validator

            return decorator

        class FilesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, WorkspaceFiles], __values: WorkspaceStarterFilesResponse.Partial
            ) -> typing.Dict[Language, WorkspaceFiles]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: WorkspaceStarterFilesResponse.Partial
            ) -> WorkspaceStarterFilesResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: WorkspaceStarterFilesResponse.Partial) -> WorkspaceStarterFilesResponse.Partial:
        for validator in WorkspaceStarterFilesResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: WorkspaceStarterFilesResponse.Partial) -> WorkspaceStarterFilesResponse.Partial:
        for validator in WorkspaceStarterFilesResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("files", pre=True)
    def _pre_validate_files(
        cls, v: typing.Dict[Language, WorkspaceFiles], values: WorkspaceStarterFilesResponse.Partial
    ) -> typing.Dict[Language, WorkspaceFiles]:
        for validator in WorkspaceStarterFilesResponse.Validators._files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("files", pre=False)
    def _post_validate_files(
        cls, v: typing.Dict[Language, WorkspaceFiles], values: WorkspaceStarterFilesResponse.Partial
    ) -> typing.Dict[Language, WorkspaceFiles]:
        for validator in WorkspaceStarterFilesResponse.Validators._files_post_validators:
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
