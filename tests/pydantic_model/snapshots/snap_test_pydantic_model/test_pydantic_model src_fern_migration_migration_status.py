import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MigrationStatus(str, enum.Enum):
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    FINISHED = "FINISHED"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        finished: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self.value == "RUNNING":
            return running()
        if self.value == "FAILED":
            return failed()
        if self.value == "FINISHED":
            return finished()

        # the above checks are exhaustive, but this is necessary to satisfy the type checker
        raise RuntimeError()
