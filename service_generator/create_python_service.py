import os
import string
import sys

import typer

from service_generator.service.activate import activate_service


def create_p_service(file_path: string, user: string = None, service_name: string = None):

    try:
        if service_name is None:
            s = file_path.split('/')
            s.reverse()
            service_name = s[1]
        if user is None:
            user = os.popen("whoami").read().strip("\n")
    except IndexError:
        typer.secho("Invalid filepath given, please use exact directory.", fg=typer.colors.RED)
        sys.exit(1)

    try:

        service_location = "/lib/systemd/system/{}.service".format(service_name)
        f = open(service_location, "w+")

        f.write(("""[Unit]
Description={} system service at boot
After=multi-user.target

[Service]
User={}
Type=simple
ExecStart=/usr/bin/python3 {}
Restart=always

[Install]
WantedBy=multi-user.target\n""".format(service_name, user, file_path)))
        f.close()

        result: bool = activate_service(service_location, file_path, service_name)

        return result

    except Exception as e:
        print("Error creating service: {}".format(e))
        return False
