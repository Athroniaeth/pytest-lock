import inspect
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class SignatureLock:
    is_class: bool
    is_method: bool
    is_builtin: bool
    is_function: bool
    return_annotation: str

    parameters: List[str]
    parameters_type: List[str]

    @classmethod
    def from_function(cls, function: Callable) -> "SignatureLock":
        signature = inspect.signature(function)

        return cls(
            is_class=inspect.isclass(function),
            is_method=inspect.ismethod(function),
            is_builtin=inspect.isbuiltin(function),
            is_function=inspect.isfunction(function),
            return_annotation=f"{signature.return_annotation}",
            parameters=[f"{p.name}" for p in signature.parameters.values()],
            parameters_type=[f"{p.annotation}" for p in signature.parameters.values()],
        )
