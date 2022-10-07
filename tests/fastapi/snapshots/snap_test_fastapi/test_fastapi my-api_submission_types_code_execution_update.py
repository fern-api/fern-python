from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .building_executor_response import BuildingExecutorResponse
from .errored_response import ErroredResponse
from .finished_response import FinishedResponse
from .graded_response import GradedResponse
from .graded_response_v_2 import GradedResponseV2
from .invalid_request_response import InvalidRequestResponse
from .recorded_response_notification import RecordedResponseNotification
from .recording_response_notification import RecordingResponseNotification
from .running_response import RunningResponse
from .stopped_response import StoppedResponse
from .workspace_ran_response import WorkspaceRanResponse

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def building_executor(self, value: BuildingExecutorResponse) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(
            __root__=_CodeExecutionUpdate.BuildingExecutor(**dict(value), type="buildingExecutor")
        )

    def running(self, value: RunningResponse) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.Running(**dict(value), type="running"))

    def errored(self, value: ErroredResponse) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.Errored(**dict(value), type="errored"))

    def stopped(self, value: StoppedResponse) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.Stopped(**dict(value), type="stopped"))

    def graded(self, value: GradedResponse) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.Graded(**dict(value), type="graded"))

    def graded_v_2(self, value: GradedResponseV2) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.GradedV2(**dict(value), type="gradedV2"))

    def workspace_ran(self, value: WorkspaceRanResponse) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.WorkspaceRan(**dict(value), type="workspaceRan"))

    def recording(self, value: RecordingResponseNotification) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.Recording(**dict(value), type="recording"))

    def recorded(self, value: RecordedResponseNotification) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.Recorded(**dict(value), type="recorded"))

    def invalid_request(self, value: InvalidRequestResponse) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.InvalidRequest(**dict(value), type="invalidRequest"))

    def finished(self, value: FinishedResponse) -> CodeExecutionUpdate:
        return CodeExecutionUpdate(__root__=_CodeExecutionUpdate.Finished(**dict(value), type="finished"))


class CodeExecutionUpdate(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _CodeExecutionUpdate.BuildingExecutor,
        _CodeExecutionUpdate.Running,
        _CodeExecutionUpdate.Errored,
        _CodeExecutionUpdate.Stopped,
        _CodeExecutionUpdate.Graded,
        _CodeExecutionUpdate.GradedV2,
        _CodeExecutionUpdate.WorkspaceRan,
        _CodeExecutionUpdate.Recording,
        _CodeExecutionUpdate.Recorded,
        _CodeExecutionUpdate.InvalidRequest,
        _CodeExecutionUpdate.Finished,
    ]:
        return self.__root__

    def visit(
        self,
        building_executor: typing.Callable[[BuildingExecutorResponse], T_Result],
        running: typing.Callable[[RunningResponse], T_Result],
        errored: typing.Callable[[ErroredResponse], T_Result],
        stopped: typing.Callable[[StoppedResponse], T_Result],
        graded: typing.Callable[[GradedResponse], T_Result],
        graded_v_2: typing.Callable[[GradedResponseV2], T_Result],
        workspace_ran: typing.Callable[[WorkspaceRanResponse], T_Result],
        recording: typing.Callable[[RecordingResponseNotification], T_Result],
        recorded: typing.Callable[[RecordedResponseNotification], T_Result],
        invalid_request: typing.Callable[[InvalidRequestResponse], T_Result],
        finished: typing.Callable[[FinishedResponse], T_Result],
    ) -> T_Result:
        if self.__root__.type == "buildingExecutor":
            return building_executor(self.__root__)
        if self.__root__.type == "running":
            return running(self.__root__)
        if self.__root__.type == "errored":
            return errored(self.__root__)
        if self.__root__.type == "stopped":
            return stopped(self.__root__)
        if self.__root__.type == "graded":
            return graded(self.__root__)
        if self.__root__.type == "gradedV2":
            return graded_v_2(self.__root__)
        if self.__root__.type == "workspaceRan":
            return workspace_ran(self.__root__)
        if self.__root__.type == "recording":
            return recording(self.__root__)
        if self.__root__.type == "recorded":
            return recorded(self.__root__)
        if self.__root__.type == "invalidRequest":
            return invalid_request(self.__root__)
        if self.__root__.type == "finished":
            return finished(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[
            _CodeExecutionUpdate.BuildingExecutor,
            _CodeExecutionUpdate.Running,
            _CodeExecutionUpdate.Errored,
            _CodeExecutionUpdate.Stopped,
            _CodeExecutionUpdate.Graded,
            _CodeExecutionUpdate.GradedV2,
            _CodeExecutionUpdate.WorkspaceRan,
            _CodeExecutionUpdate.Recording,
            _CodeExecutionUpdate.Recorded,
            _CodeExecutionUpdate.InvalidRequest,
            _CodeExecutionUpdate.Finished,
        ],
        pydantic.Field(discriminator="type"),
    ]

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[
                _CodeExecutionUpdate.BuildingExecutor,
                _CodeExecutionUpdate.Running,
                _CodeExecutionUpdate.Errored,
                _CodeExecutionUpdate.Stopped,
                _CodeExecutionUpdate.Graded,
                _CodeExecutionUpdate.GradedV2,
                _CodeExecutionUpdate.WorkspaceRan,
                _CodeExecutionUpdate.Recording,
                _CodeExecutionUpdate.Recorded,
                _CodeExecutionUpdate.InvalidRequest,
                _CodeExecutionUpdate.Finished,
            ],
            values.get("__root__"),
        )
        for validator in CodeExecutionUpdate.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _CodeExecutionUpdate.BuildingExecutor,
                            _CodeExecutionUpdate.Running,
                            _CodeExecutionUpdate.Errored,
                            _CodeExecutionUpdate.Stopped,
                            _CodeExecutionUpdate.Graded,
                            _CodeExecutionUpdate.GradedV2,
                            _CodeExecutionUpdate.WorkspaceRan,
                            _CodeExecutionUpdate.Recording,
                            _CodeExecutionUpdate.Recorded,
                            _CodeExecutionUpdate.InvalidRequest,
                            _CodeExecutionUpdate.Finished,
                        ]
                    ],
                    typing.Union[
                        _CodeExecutionUpdate.BuildingExecutor,
                        _CodeExecutionUpdate.Running,
                        _CodeExecutionUpdate.Errored,
                        _CodeExecutionUpdate.Stopped,
                        _CodeExecutionUpdate.Graded,
                        _CodeExecutionUpdate.GradedV2,
                        _CodeExecutionUpdate.WorkspaceRan,
                        _CodeExecutionUpdate.Recording,
                        _CodeExecutionUpdate.Recorded,
                        _CodeExecutionUpdate.InvalidRequest,
                        _CodeExecutionUpdate.Finished,
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
                        _CodeExecutionUpdate.BuildingExecutor,
                        _CodeExecutionUpdate.Running,
                        _CodeExecutionUpdate.Errored,
                        _CodeExecutionUpdate.Stopped,
                        _CodeExecutionUpdate.Graded,
                        _CodeExecutionUpdate.GradedV2,
                        _CodeExecutionUpdate.WorkspaceRan,
                        _CodeExecutionUpdate.Recording,
                        _CodeExecutionUpdate.Recorded,
                        _CodeExecutionUpdate.InvalidRequest,
                        _CodeExecutionUpdate.Finished,
                    ]
                ],
                typing.Union[
                    _CodeExecutionUpdate.BuildingExecutor,
                    _CodeExecutionUpdate.Running,
                    _CodeExecutionUpdate.Errored,
                    _CodeExecutionUpdate.Stopped,
                    _CodeExecutionUpdate.Graded,
                    _CodeExecutionUpdate.GradedV2,
                    _CodeExecutionUpdate.WorkspaceRan,
                    _CodeExecutionUpdate.Recording,
                    _CodeExecutionUpdate.Recorded,
                    _CodeExecutionUpdate.InvalidRequest,
                    _CodeExecutionUpdate.Finished,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True


class _CodeExecutionUpdate:
    class BuildingExecutor(BuildingExecutorResponse):
        type: typing_extensions.Literal["buildingExecutor"]

        class Config:
            frozen = True

    class Running(RunningResponse):
        type: typing_extensions.Literal["running"]

        class Config:
            frozen = True

    class Errored(ErroredResponse):
        type: typing_extensions.Literal["errored"]

        class Config:
            frozen = True

    class Stopped(StoppedResponse):
        type: typing_extensions.Literal["stopped"]

        class Config:
            frozen = True

    class Graded(GradedResponse):
        type: typing_extensions.Literal["graded"]

        class Config:
            frozen = True

    class GradedV2(GradedResponseV2):
        type: typing_extensions.Literal["gradedV2"]

        class Config:
            frozen = True

    class WorkspaceRan(WorkspaceRanResponse):
        type: typing_extensions.Literal["workspaceRan"]

        class Config:
            frozen = True

    class Recording(RecordingResponseNotification):
        type: typing_extensions.Literal["recording"]

        class Config:
            frozen = True

    class Recorded(RecordedResponseNotification):
        type: typing_extensions.Literal["recorded"]

        class Config:
            frozen = True

    class InvalidRequest(InvalidRequestResponse):
        type: typing_extensions.Literal["invalidRequest"]

        class Config:
            frozen = True

    class Finished(FinishedResponse):
        type: typing_extensions.Literal["finished"]

        class Config:
            frozen = True


CodeExecutionUpdate.update_forward_refs()