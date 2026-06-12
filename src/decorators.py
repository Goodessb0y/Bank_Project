from __future__ import annotations

import functools
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования выполнения функции.

    Логирует:
    - успешное завершение функции
    - возникновение исключений с типом ошибки и входными параметрами

    Работа:
    - Если filename указан, лог записывается в файл
    - Если filename не указан, лог выводится в stdout

    Логи:
    - Успех:
        <function_name> ok

    - Ошибка:
        <function_name> error: <ExceptionType>. Inputs: (<args>), {<kwargs>}
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            def write(message: str) -> None:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)

            try:
                result = func(*args, **kwargs)
                write(f"{func.__name__} ok")
                return result
            except Exception as e:
                write(
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                raise

        return cast(F, wrapper)

    return decorator
