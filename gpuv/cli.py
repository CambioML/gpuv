"""Command line interface for gpuv."""
import typer
from gpuv.server import app as flask_app

app = typer.Typer()


@app.command()
def start():
    print("Starting server...")
    flask_app.run(port=5000)


def cli():
    app()


if __name__ == "__main__":
    cli()
