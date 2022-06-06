import behaviours

_ARG_BEHAV_CONFIG = {
    ("-q", "--quit"): behaviours.stop_server,
    ("-r", "--reload"): behaviours.reload_datapacks,
    ("--init",): behaviours.init_server_rules,
    ("--manual",): behaviours.manual_command_input,
}

ARG_BEHAVIOUR_MAP = {}

for key, value in _ARG_BEHAV_CONFIG.items():
    for arg in key:
        ARG_BEHAVIOUR_MAP[arg] = value
