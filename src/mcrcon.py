import asyncio
import sys
from typing import Callable

from aiomcrcon import Client

import config
from arg_behaviour_mapper import ARG_BEHAVIOUR_MAP


async def main():
    if len(sys.argv) != 2:
        print("Must provide exactly 1 arg!")

    executable = ARG_BEHAVIOUR_MAP.get(sys.argv[1])
    if executable:
        await execute(executable)
    else:
        print("There is no handler for this arg!")


async def execute(executable: Callable[[Client], None]) -> None:
    async with Client(config.HOSTNAME, config.PORT, config.PASSWORD) as client:
        await executable(client)

if __name__ == "__main__":
    asyncio.run(main())
