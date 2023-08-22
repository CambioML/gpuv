import argparse
import subprocess
from gpuv.server import app


def run_gpustat():
    try:
        result = subprocess.check_output(["gpustat"], universal_newlines=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print("Error running gpustat.")
        print(e.output)
    except FileNotFoundError:
        print(
            "Error: gpustat not found. Please ensure it's installed and available in PATH."
        )


def start_flask_server():
    app.run(debug=False)


def main():
    parser = argparse.ArgumentParser(
        description="gpuv: Visualize GPU information from gpustat."
    )
    parser.add_argument(
        "-g", "--get", action="store_true", help="Fetch and display GPU stats"
    )
    parser.add_argument(
        "-s", "--start-server", action="store_true", help="Start Flask server"
    )

    args = parser.parse_args()

    if args.get:
        run_gpustat()
    elif args.start_server:
        start_flask_server()
    else:
        print(
            "gpuv: Use -g or --get to fetch and display GPU stats or -s or --start-server to start the Flask server."
        )


if __name__ == "__main__":
    main()
