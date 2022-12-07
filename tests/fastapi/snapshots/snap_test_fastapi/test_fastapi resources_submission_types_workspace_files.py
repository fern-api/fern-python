# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.file_info import FileInfo


class WorkspaceFiles(pydantic.BaseModel):
    main_file: FileInfo = pydantic.Field(alias="mainFile")
    read_only_files: typing.List[FileInfo] = pydantic.Field(alias="readOnlyFiles")

    class Partial(typing_extensions.TypedDict):
        main_file: typing_extensions.NotRequired[FileInfo]
        read_only_files: typing_extensions.NotRequired[typing.List[FileInfo]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceFiles.Validators.root
            def validate(values: WorkspaceFiles.Partial) -> WorkspaceFiles.Partial:
                ...

            @WorkspaceFiles.Validators.field("main_file")
            def validate_main_file(main_file: FileInfo, values: WorkspaceFiles.Partial) -> FileInfo:
                ...

            @WorkspaceFiles.Validators.field("read_only_files")
            def validate_read_only_files(read_only_files: typing.List[FileInfo], values: WorkspaceFiles.Partial) -> typing.List[FileInfo]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[WorkspaceFiles.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[WorkspaceFiles.Validators._RootValidator]] = []
        _main_file_pre_validators: typing.ClassVar[typing.List[WorkspaceFiles.Validators.MainFileValidator]] = []
        _main_file_post_validators: typing.ClassVar[typing.List[WorkspaceFiles.Validators.MainFileValidator]] = []
        _read_only_files_pre_validators: typing.ClassVar[
            typing.List[WorkspaceFiles.Validators.ReadOnlyFilesValidator]
        ] = []
        _read_only_files_post_validators: typing.ClassVar[
            typing.List[WorkspaceFiles.Validators.ReadOnlyFilesValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> WorkspaceFiles.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["main_file"]
        ) -> typing.Callable[
            [WorkspaceFiles.Validators.MainFileValidator], WorkspaceFiles.Validators.MainFileValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["read_only_files"]
        ) -> typing.Callable[
            [WorkspaceFiles.Validators.ReadOnlyFilesValidator], WorkspaceFiles.Validators.ReadOnlyFilesValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "main_file":
                    if pre:
                        cls._main_file_pre_validators.append(validator)
                    else:
                        cls._main_file_post_validators.append(validator)
                if field_name == "read_only_files":
                    if pre:
                        cls._read_only_files_pre_validators.append(validator)
                    else:
                        cls._read_only_files_post_validators.append(validator)
                return validator

            return decorator

        class MainFileValidator(typing_extensions.Protocol):
            def __call__(self, __v: FileInfo, __values: WorkspaceFiles.Partial) -> FileInfo:
                ...

        class ReadOnlyFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.List[FileInfo], __values: WorkspaceFiles.Partial) -> typing.List[FileInfo]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: WorkspaceFiles.Partial) -> WorkspaceFiles.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: WorkspaceFiles.Partial) -> WorkspaceFiles.Partial:
        for validator in WorkspaceFiles.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: WorkspaceFiles.Partial) -> WorkspaceFiles.Partial:
        for validator in WorkspaceFiles.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("main_file", pre=True)
    def _pre_validate_main_file(cls, v: FileInfo, values: WorkspaceFiles.Partial) -> FileInfo:
        for validator in WorkspaceFiles.Validators._main_file_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("main_file", pre=False)
    def _post_validate_main_file(cls, v: FileInfo, values: WorkspaceFiles.Partial) -> FileInfo:
        for validator in WorkspaceFiles.Validators._main_file_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("read_only_files", pre=True)
    def _pre_validate_read_only_files(
        cls, v: typing.List[FileInfo], values: WorkspaceFiles.Partial
    ) -> typing.List[FileInfo]:
        for validator in WorkspaceFiles.Validators._read_only_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("read_only_files", pre=False)
    def _post_validate_read_only_files(
        cls, v: typing.List[FileInfo], values: WorkspaceFiles.Partial
    ) -> typing.List[FileInfo]:
        for validator in WorkspaceFiles.Validators._read_only_files_post_validators:
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
