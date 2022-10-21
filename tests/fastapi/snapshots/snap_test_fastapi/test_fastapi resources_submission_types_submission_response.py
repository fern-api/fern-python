# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.problem_id import ProblemId
from .code_execution_update import (
    CodeExecutionUpdate as resources_submission_types_code_execution_update_CodeExecutionUpdate,
)
from .exception_info import ExceptionInfo
from .terminated_response import TerminatedResponse

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def server_initialized(self) -> SubmissionResponse:
        return SubmissionResponse(__root__=_SubmissionResponse.ServerInitialized(type="serverInitialized"))

    def problem_initialized(self, value: ProblemId) -> SubmissionResponse:
        return SubmissionResponse(
            __root__=_SubmissionResponse.ProblemInitialized(type="problemInitialized", value=value)
        )

    def workspace_initialized(self) -> SubmissionResponse:
        return SubmissionResponse(__root__=_SubmissionResponse.WorkspaceInitialized(type="workspaceInitialized"))

    def server_errored(self, value: ExceptionInfo) -> SubmissionResponse:
        return SubmissionResponse(__root__=_SubmissionResponse.ServerErrored(**dict(value), type="serverErrored"))

    def code_execution_update(
        self, value: resources_submission_types_code_execution_update_CodeExecutionUpdate
    ) -> SubmissionResponse:
        return SubmissionResponse(
            __root__=_SubmissionResponse.CodeExecutionUpdate(type="codeExecutionUpdate", value=value)
        )

    def terminated(self, value: TerminatedResponse) -> SubmissionResponse:
        return SubmissionResponse(__root__=_SubmissionResponse.Terminated(**dict(value), type="terminated"))


class SubmissionResponse(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _SubmissionResponse.ServerInitialized,
        _SubmissionResponse.ProblemInitialized,
        _SubmissionResponse.WorkspaceInitialized,
        _SubmissionResponse.ServerErrored,
        _SubmissionResponse.CodeExecutionUpdate,
        _SubmissionResponse.Terminated,
    ]:
        return self.__root__

    def visit(
        self,
        server_initialized: typing.Callable[[], T_Result],
        problem_initialized: typing.Callable[[ProblemId], T_Result],
        workspace_initialized: typing.Callable[[], T_Result],
        server_errored: typing.Callable[[ExceptionInfo], T_Result],
        code_execution_update: typing.Callable[
            [resources_submission_types_code_execution_update_CodeExecutionUpdate], T_Result
        ],
        terminated: typing.Callable[[TerminatedResponse], T_Result],
    ) -> T_Result:
        if self.__root__.type == "serverInitialized":
            return server_initialized()
        if self.__root__.type == "problemInitialized":
            return problem_initialized(self.__root__.value)
        if self.__root__.type == "workspaceInitialized":
            return workspace_initialized()
        if self.__root__.type == "serverErrored":
            return server_errored(self.__root__)
        if self.__root__.type == "codeExecutionUpdate":
            return code_execution_update(self.__root__.value)
        if self.__root__.type == "terminated":
            return terminated(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[
            _SubmissionResponse.ServerInitialized,
            _SubmissionResponse.ProblemInitialized,
            _SubmissionResponse.WorkspaceInitialized,
            _SubmissionResponse.ServerErrored,
            _SubmissionResponse.CodeExecutionUpdate,
            _SubmissionResponse.Terminated,
        ],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionResponse.Validators.validate
            def validate(value: typing.Union[_SubmissionResponse.ServerInitialized, _SubmissionResponse.ProblemInitialized, _SubmissionResponse.WorkspaceInitialized, _SubmissionResponse.ServerErrored, _SubmissionResponse.CodeExecutionUpdate, _SubmissionResponse.Terminated]) -> typing.Union[_SubmissionResponse.ServerInitialized, _SubmissionResponse.ProblemInitialized, _SubmissionResponse.WorkspaceInitialized, _SubmissionResponse.ServerErrored, _SubmissionResponse.CodeExecutionUpdate, _SubmissionResponse.Terminated]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _SubmissionResponse.ServerInitialized,
                            _SubmissionResponse.ProblemInitialized,
                            _SubmissionResponse.WorkspaceInitialized,
                            _SubmissionResponse.ServerErrored,
                            _SubmissionResponse.CodeExecutionUpdate,
                            _SubmissionResponse.Terminated,
                        ]
                    ],
                    typing.Union[
                        _SubmissionResponse.ServerInitialized,
                        _SubmissionResponse.ProblemInitialized,
                        _SubmissionResponse.WorkspaceInitialized,
                        _SubmissionResponse.ServerErrored,
                        _SubmissionResponse.CodeExecutionUpdate,
                        _SubmissionResponse.Terminated,
                    ],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [
                    typing.Union[
                        _SubmissionResponse.ServerInitialized,
                        _SubmissionResponse.ProblemInitialized,
                        _SubmissionResponse.WorkspaceInitialized,
                        _SubmissionResponse.ServerErrored,
                        _SubmissionResponse.CodeExecutionUpdate,
                        _SubmissionResponse.Terminated,
                    ]
                ],
                typing.Union[
                    _SubmissionResponse.ServerInitialized,
                    _SubmissionResponse.ProblemInitialized,
                    _SubmissionResponse.WorkspaceInitialized,
                    _SubmissionResponse.ServerErrored,
                    _SubmissionResponse.CodeExecutionUpdate,
                    _SubmissionResponse.Terminated,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[
                _SubmissionResponse.ServerInitialized,
                _SubmissionResponse.ProblemInitialized,
                _SubmissionResponse.WorkspaceInitialized,
                _SubmissionResponse.ServerErrored,
                _SubmissionResponse.CodeExecutionUpdate,
                _SubmissionResponse.Terminated,
            ],
            values.get("__root__"),
        )
        for validator in SubmissionResponse.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True


class _SubmissionResponse:
    class ServerInitialized(pydantic.BaseModel):
        type: typing_extensions.Literal["serverInitialized"]

        class Config:
            frozen = True

    class ProblemInitialized(pydantic.BaseModel):
        type: typing_extensions.Literal["problemInitialized"]
        value: ProblemId

        class Config:
            frozen = True

    class WorkspaceInitialized(pydantic.BaseModel):
        type: typing_extensions.Literal["workspaceInitialized"]

        class Config:
            frozen = True

    class ServerErrored(ExceptionInfo):
        type: typing_extensions.Literal["serverErrored"]

        class Config:
            frozen = True

    class CodeExecutionUpdate(pydantic.BaseModel):
        type: typing_extensions.Literal["codeExecutionUpdate"]
        value: resources_submission_types_code_execution_update_CodeExecutionUpdate

        class Config:
            frozen = True

    class Terminated(TerminatedResponse):
        type: typing_extensions.Literal["terminated"]

        class Config:
            frozen = True


SubmissionResponse.update_forward_refs()
