# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing

import fastapi

from ...core.abstract_fern_service import AbstractFernService
from ...core.exceptions.fern_http_exception import FernHTTPException
from ...core.route_args import get_route_args
from ..commons.types.problem_id import ProblemId


class AbstractHomepageProblemService(AbstractFernService):
    """
    AbstractHomepageProblemService is an abstract class containing the methods that your
    HomepageProblemService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def get_homepage_problems(self) -> typing.List[ProblemId]:
        ...

    @abc.abstractmethod
    def set_homepage_problems(self, *, body: typing.List[ProblemId]) -> None:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_get_homepage_problems(router=router)
        cls.__init_set_homepage_problems(router=router)

    @classmethod
    def __init_get_homepage_problems(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_homepage_problems)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_homepage_problems, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_homepage_problems)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.List[ProblemId]:
            try:
                return cls.get_homepage_problems(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_homepage_problems' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_homepage_problems.__globals__)

        router.get(
            path="/homepage-problems/",
            response_model=typing.List[ProblemId],
            **get_route_args(cls.get_homepage_problems),
        )(wrapper)

    @classmethod
    def __init_set_homepage_problems(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.set_homepage_problems)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.set_homepage_problems, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.set_homepage_problems)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.set_homepage_problems(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'set_homepage_problems' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.set_homepage_problems.__globals__)

        router.post(path="/homepage-problems/", **get_route_args(cls.set_homepage_problems))(wrapper)
