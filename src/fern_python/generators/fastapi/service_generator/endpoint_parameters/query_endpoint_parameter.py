import fern.ir.pydantic as ir_types

from fern_python.codegen import AST

from ...context import FastApiGeneratorContext
from ...external_dependencies import FastAPI
from .endpoint_parameter import EndpointParameter


class QueryEndpointParameter(EndpointParameter):
    def __init__(self, context: FastApiGeneratorContext, query_parameter: ir_types.services.QueryParameter):
        super().__init__(context=context)
        self._query_parameter = query_parameter

    def get_name(self) -> str:
        return QueryEndpointParameter.get_variable_name_of_query_parameter(self._query_parameter)

    def get_type(self) -> AST.TypeHint:
        return self._context.pydantic_generator_context.get_type_hint_for_type_reference(
            self._query_parameter.value_type
        )

    def get_default(self) -> AST.Expression:
        value_type = self._query_parameter.value_type.get_as_union()
        return FastAPI.Query(
            is_optional=value_type.type == "container" and value_type.container.get_as_union().type == "optional",
            variable_name=self.get_name(),
            wire_value=self._query_parameter.name.wire_value,
        )

    @staticmethod
    def get_variable_name_of_query_parameter(query_parameter: ir_types.services.QueryParameter) -> str:
        return query_parameter.name.snake_case