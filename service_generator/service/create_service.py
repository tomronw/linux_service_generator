import os
import pathlib
import string
import sys
import typer
from service_generator.create_go_service import create_go_ser
from service_generator.create_python_service import create_p_service


class CreateService:

    def __init__(self):
        if sys.platform.startswith("linux"):
            return
        else:
            typer.secho("Must be used with Linux Distributions!", fg=typer.colors.RED)
            sys.exit(1)

    @staticmethod
    def delete_service(service_name: string):
        typer.secho("Deleting and reloading daemon", fg=typer.colors.YELLOW)

        d_cmds = ["sudo systemctl stop {}.service".format(service_name),
                  "rm -r /lib/systemd/system/{}.service".format(service_name),
                  "sudo systemctl daemon-reload"]
        [os.system(c) for c in d_cmds]
        return pathlib.Path("/lib/systemd/system/{}.service".format(service_name)).is_file()

    @staticmethod
    def create(file_path: string, user: string = None,
               service_name: string = None) -> bool:
        # decides lang.
        s = file_path.split('.')
        s.reverse()

        if s[0] == "go":
            return create_go_ser(file_path, user, service_name)
        elif s[0] == "py":
            return create_p_service(file_path, user, service_name)
        else:
            typer.secho("Not valid file extension.", fg=typer.colors.RED)
            return False
