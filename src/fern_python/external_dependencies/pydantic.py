from fern_python.codegen import AST


def _export(*export: str) -> AST.ClassReference:
    return AST.ClassReference(
        import_=AST.ReferenceImport(
            module=AST.Module.external(
                dependency=AST.Dependency(name="pydantic", version="^1.9.2"),
                module_path=("pydantic",),
            )
        ),
        qualified_name_excluding_import=export,
    )


class Pydantic:

    Field = _export("Field")

    BaseModel = _export("BaseModel")

    PrivateAttr = _export("PrivateAttr")

    class Extra:
        forbid = AST.Expression(_export("Extra", "forbid"))

    @staticmethod
    def root_validator(pre: bool = False) -> AST.FunctionInvocation:
        return AST.FunctionInvocation(
            function_definition=_export("root_validator"),
            args=[AST.Expression(expression=f'pre={"True" if pre else "False"}')],
        )

    @staticmethod
    def validator(field_name: str, pre: bool = False) -> AST.FunctionInvocation:
        return AST.FunctionInvocation(
            function_definition=_export("validator"),
            args=[AST.Expression(expression=f'"{field_name}", pre={"True" if pre else "False"}')],
        )
