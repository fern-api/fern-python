# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SubmissionTypeEnum(str, enum.Enum):
    TEST = "TEST"

    def visit(self, test: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubmissionTypeEnum.TEST:
            return test()
