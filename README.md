# mc-rcon

This is a simple RCON client for Minecraft built on top of https://github.com/Iapetus-11/aio-mc-rcon.

## Usage
#### Note
This assumes you run Python 3 via the `py` command.

```
py src/mcrcon.py <flag>
```
Exactly one these flags must be present:
- `-q`, `--quit`: stops the server (sends `stop` command)
- `-r`, `--reload`: reloads the datapacks (sends `reload` command)
- `--init`: sends the commands found in init_cmds.json
- `--manual`: allows the user to manually type commands to be sent to the server

#### Note
Feel free to change the contents of init_cmds.json. The file in the repo contains
the commands **I** usually start a server with.

## config.ini

Contains details about your server's rcon configuration so the script can connect
and execute commands on it.

