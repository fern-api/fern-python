# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing

import fastapi
import starlette

from ....core.abstract_fern_service import AbstractFernService
from ....core.exceptions.fern_http_exception import FernHTTPException
from ....core.route_args import get_route_args
from ...commons.types.language import Language
from ..types.execution_session_response import ExecutionSessionResponse
from ..types.get_execution_session_state_response import GetExecutionSessionStateResponse


class AbstractExecutionSesssionManagementService(AbstractFernService):
    """
    AbstractExecutionSesssionManagementService is an abstract class containing the methods that your
    ExecutionSesssionManagementService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def create_execution_session(self, *, language: Language) -> ExecutionSessionResponse:
        """
        Returns sessionId and execution server URL for session. Spins up server.
        """
        ...

    @abc.abstractmethod
    def get_execution_session(self, *, session_id: str) -> typing.Optional[ExecutionSessionResponse]:
        """
        Returns execution server URL for session. Returns empty if session isn't registered.
        """
        ...

    @abc.abstractmethod
    def stop_execution_session(self, *, session_id: str) -> None:
        """
        Stops execution session.
        """
        ...

    @abc.abstractmethod
    def get_execution_sessions_state(self) -> GetExecutionSessionStateResponse:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_create_execution_session(router=router)
        cls.__init_get_execution_session(router=router)
        cls.__init_stop_execution_session(router=router)
        cls.__init_get_execution_sessions_state(router=router)

    @classmethod
    def __init_create_execution_session(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.create_execution_session)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "language":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.create_execution_session, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.create_execution_session)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> ExecutionSessionResponse:
            try:
                return cls.create_execution_session(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'create_execution_session' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.create_execution_session.__globals__)

        router.post(
            path="/sessions/create-session/{language}",
            response_model=ExecutionSessionResponse,
            description=cls.create_execution_session.__doc__,
            **get_route_args(cls.create_execution_session, default_tag="submission"),
        )(wrapper)

    @classmethod
    def __init_get_execution_session(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_execution_session)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "session_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_execution_session, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_execution_session)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Optional[ExecutionSessionResponse]:
            try:
                return cls.get_execution_session(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_execution_session' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_execution_session.__globals__)

        router.get(
            path="/sessions/{session_id}",
            response_model=typing.Optional[ExecutionSessionResponse],
            description=cls.get_execution_session.__doc__,
            **get_route_args(cls.get_execution_session, default_tag="submission"),
        )(wrapper)

    @classmethod
    def __init_stop_execution_session(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.stop_execution_session)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "session_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.stop_execution_session, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.stop_execution_session)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.stop_execution_session(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'stop_execution_session' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.stop_execution_session.__globals__)

        router.delete(
            path="/sessions/stop/{session_id}",
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=cls.stop_execution_session.__doc__,
            **get_route_args(cls.stop_execution_session, default_tag="submission"),
        )(wrapper)

    @classmethod
    def __init_get_execution_sessions_state(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_execution_sessions_state)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_execution_sessions_state, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_execution_sessions_state)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> GetExecutionSessionStateResponse:
            try:
                return cls.get_execution_sessions_state(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_execution_sessions_state' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_execution_sessions_state.__globals__)

        router.get(
            path="/sessions/execution-sessions-state",
            response_model=GetExecutionSessionStateResponse,
            description=cls.get_execution_sessions_state.__doc__,
            **get_route_args(cls.get_execution_sessions_state, default_tag="submission"),
        )(wrapper)