from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .non_void_function_signature import NonVoidFunctionSignature
from .void_function_signature import VoidFunctionSignature
from .void_function_signature_that_takes_actual_result import VoidFunctionSignatureThatTakesActualResult

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def void(self, value: VoidFunctionSignature) -> FunctionSignature:
        return FunctionSignature(__root__=_FunctionSignature.Void(**dict(value), type="void"))

    def non_void(self, value: NonVoidFunctionSignature) -> FunctionSignature:
        return FunctionSignature(__root__=_FunctionSignature.NonVoid(**dict(value), type="nonVoid"))

    def void_that_takes_actual_result(self, value: VoidFunctionSignatureThatTakesActualResult) -> FunctionSignature:
        return FunctionSignature(
            __root__=_FunctionSignature.VoidThatTakesActualResult(**dict(value), type="voidThatTakesActualResult")
        )


class FunctionSignature(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get(
        self,
    ) -> typing.Union[
        _FunctionSignature.Void, _FunctionSignature.NonVoid, _FunctionSignature.VoidThatTakesActualResult
    ]:
        return self.__root__

    def visit(
        self,
        void: typing.Callable[[VoidFunctionSignature], T_Result],
        non_void: typing.Callable[[NonVoidFunctionSignature], T_Result],
        void_that_takes_actual_result: typing.Callable[[VoidFunctionSignatureThatTakesActualResult], T_Result],
    ) -> T_Result:
        if self.__root__.type == "void":
            return void(self.__root__)
        if self.__root__.type == "nonVoid":
            return non_void(self.__root__)
        if self.__root__.type == "voidThatTakesActualResult":
            return void_that_takes_actual_result(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_FunctionSignature.Void, _FunctionSignature.NonVoid, _FunctionSignature.VoidThatTakesActualResult],
        pydantic.Field(discriminator="type"),
    ]


class _FunctionSignature:
    class Void(VoidFunctionSignature):
        type: typing_extensions.Literal["void"]

    class NonVoid(NonVoidFunctionSignature):
        type: typing_extensions.Literal["nonVoid"]

    class VoidThatTakesActualResult(VoidFunctionSignatureThatTakesActualResult):
        type: typing_extensions.Literal["voidThatTakesActualResult"]


FunctionSignature.update_forward_refs()