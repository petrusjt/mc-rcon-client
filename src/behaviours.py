import json

from aiomcrcon import Client


async def stop_server(client: Client) -> None:
    response = await client.send_cmd("stop")


async def reload_datapacks(client: Client) -> None:
    response = await client.send_cmd("reload")


async def init_server_rules(client: Client) -> None:
    with open("init_cmds.json") as file:
        cmds = json.load(file)
    for cmd in cmds:
        response = await client.send_cmd(cmd)


async def manual_command_input(client: Client) -> None:
    cmd = input("Command: ")
    while cmd != "exit_rcon":
        response = await client.send_cmd(cmd)
        print(response)
        cmd = input("Command: ")
