import asyncio

from AIMXT.AIMXT import enable_log
from AIMXT.task import TaskCoordinator

task_manager = TaskCoordinator(tasks=[], agents=[])

enable_log("INFO")
asyncio.run(task_manager.async_do())
