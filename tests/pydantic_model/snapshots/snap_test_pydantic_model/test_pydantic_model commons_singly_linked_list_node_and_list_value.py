import typing

import pydantic
import typing_extensions

from .node_id import NodeId
from .singly_linked_list_value import SinglyLinkedListValue


class SinglyLinkedListNodeAndListValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    full_list: SinglyLinkedListValue = pydantic.Field(alias="fullList")

    @pydantic.validator("node_id")
    def _validate_node_id(cls, node_id: NodeId) -> NodeId:
        for validator in SinglyLinkedListNodeAndListValue.Validators._node_id:
            node_id = validator(node_id)
        return node_id

    @pydantic.validator("full_list")
    def _validate_full_list(cls, full_list: SinglyLinkedListValue) -> SinglyLinkedListValue:
        for validator in SinglyLinkedListNodeAndListValue.Validators._full_list:
            full_list = validator(full_list)
        return full_list

    class Validators:
        _node_id: typing.ClassVar[typing.List[typing.Callable[[NodeId], NodeId]]] = []
        _full_list: typing.ClassVar[typing.List[typing.Callable[[SinglyLinkedListValue], SinglyLinkedListValue]]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"]
        ) -> typing.Callable[[typing.Callable[[NodeId], NodeId]], typing.Callable[[NodeId], NodeId]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_list"]
        ) -> typing.Callable[
            [typing.Callable[[SinglyLinkedListValue], SinglyLinkedListValue]],
            typing.Callable[[SinglyLinkedListValue], SinglyLinkedListValue],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "node_id":
                    cls._node_id.append(validator)
                elif field_name == "full_list":
                    cls._full_list.append(validator)
                else:
                    raise RuntimeError("Field does not exist on SinglyLinkedListNodeAndListValue: " + field_name)

                return validator

            return decorator

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
