import os
import string

import typer


def activate_service(service_location: string, file_path: string,
                     service_name: string) -> bool:
    typer.secho("Activating service", fg=typer.colors.YELLOW)
    cmds = [
            "sudo chmod 644 {}".format(service_location),
            "chmod +x {}".format(file_path),
            "sudo systemctl daemon-reload",
            "sudo systemctl enable {}.service".format(service_name),
            "sudo systemctl start {}.service".format(service_name)
            ]

    [os.system(c) for c in cmds]

    user: str = os.popen("sudo systemctl status {}.service".format(service_name)).read()

    typer.secho("run `sudo systemctl status {}.service` to see status".format(service_name), fg=typer.colors.YELLOW)

    return False if "could not be found." in user else True


