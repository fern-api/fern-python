# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .node_id import NodeId
from .singly_linked_list_value import SinglyLinkedListValue


class SinglyLinkedListNodeAndListValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    full_list: SinglyLinkedListValue = pydantic.Field(alias="fullList")

    class Partial(typing_extensions.TypedDict):
        node_id: typing_extensions.NotRequired[NodeId]
        full_list: typing_extensions.NotRequired[SinglyLinkedListValue]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SinglyLinkedListNodeAndListValue.Validators.root
            def validate(values: SinglyLinkedListNodeAndListValue.Partial) -> SinglyLinkedListNodeAndListValue.Partial:
                ...

            @SinglyLinkedListNodeAndListValue.Validators.field("node_id")
            def validate_node_id(v: NodeId, values: SinglyLinkedListNodeAndListValue.Partial) -> NodeId:
                ...

            @SinglyLinkedListNodeAndListValue.Validators.field("full_list")
            def validate_full_list(v: SinglyLinkedListValue, values: SinglyLinkedListNodeAndListValue.Partial) -> SinglyLinkedListValue:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[[SinglyLinkedListNodeAndListValue.Partial], SinglyLinkedListNodeAndListValue.Partial]
            ]
        ] = []
        _node_id_validators: typing.ClassVar[
            typing.List[SinglyLinkedListNodeAndListValue.Validators.NodeIdValidator]
        ] = []
        _full_list_validators: typing.ClassVar[
            typing.List[SinglyLinkedListNodeAndListValue.Validators.FullListValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [SinglyLinkedListNodeAndListValue.Partial], SinglyLinkedListNodeAndListValue.Partial
            ],
        ) -> typing.Callable[[SinglyLinkedListNodeAndListValue.Partial], SinglyLinkedListNodeAndListValue.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"]
        ) -> typing.Callable[
            [SinglyLinkedListNodeAndListValue.Validators.NodeIdValidator],
            SinglyLinkedListNodeAndListValue.Validators.NodeIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_list"]
        ) -> typing.Callable[
            [SinglyLinkedListNodeAndListValue.Validators.FullListValidator],
            SinglyLinkedListNodeAndListValue.Validators.FullListValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "node_id":
                    cls._node_id_validators.append(validator)
                if field_name == "full_list":
                    cls._full_list_validators.append(validator)
                return validator

            return decorator

        class NodeIdValidator(typing_extensions.Protocol):
            def __call__(self, v: NodeId, *, values: SinglyLinkedListNodeAndListValue.Partial) -> NodeId:
                ...

        class FullListValidator(typing_extensions.Protocol):
            def __call__(
                self, v: SinglyLinkedListValue, *, values: SinglyLinkedListNodeAndListValue.Partial
            ) -> SinglyLinkedListValue:
                ...

    @pydantic.root_validator
    def _validate(cls, values: SinglyLinkedListNodeAndListValue.Partial) -> SinglyLinkedListNodeAndListValue.Partial:
        for validator in SinglyLinkedListNodeAndListValue.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("node_id")
    def _validate_node_id(cls, v: NodeId, values: SinglyLinkedListNodeAndListValue.Partial) -> NodeId:
        for validator in SinglyLinkedListNodeAndListValue.Validators._node_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("full_list")
    def _validate_full_list(
        cls, v: SinglyLinkedListValue, values: SinglyLinkedListNodeAndListValue.Partial
    ) -> SinglyLinkedListValue:
        for validator in SinglyLinkedListNodeAndListValue.Validators._full_list_validators:
            v = validator(v, values=values)
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
