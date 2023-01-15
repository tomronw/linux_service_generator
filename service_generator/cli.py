import string
from typing import Optional

import typer

from service_generator import __app_name__, __version__
from service_generator.service.create_service import CreateService

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return


@app.command()
def create(
        file_path: str = typer.Argument(..., help="The absolute path of your .py/.go file"),
        user: Optional[str] = typer.Option(None, "--user", "-u", help="Specify certain Linux user | Service will "
                                                                      "always default to"
                                                                      "`boot` user [optional]"),
        service_name: Optional[str] = typer.Option(None, "--service-name", "-s-n", help="Specify a certain service "
                                                                                        "name (Defaults to parent"
                                                                                        "directory) [optional]")
) -> None:
    """Create new service file (.py/.go) that will run on boot"""
    c: CreateService = CreateService()
    typer.secho("Creating service file for {}".format(file_path), fg=typer.colors.YELLOW)
    created: bool = c.create(file_path, user, service_name)
    if not created:
        typer.secho(
            "Failed creating system service", fg=typer.colors.RED, bold=True
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            "Successfully created system service",
            fg=typer.colors.GREEN, bold=True
        )


@app.command()
def delete(
        service_name: str = typer.Argument(..., help="The name of the service you wish to teardown"),
) -> None:
    """Deletes system service file and performs daemon-reload afterwards"""
    c: CreateService = CreateService()
    created: bool = c.delete_service(service_name)
    if not created:
        typer.secho(
            'Successfully deleted service!', fg=typer.colors.GREEN, bold=True
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            "Failed deleting service, please check if it exists",
            fg=typer.colors.RED, bold=True
        )
