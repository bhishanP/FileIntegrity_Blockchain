import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="File Integrity Monitor")

    parser.add_argument(
        "--folder",
        type=str,
        required=True,
        help="Folder to monitor"
    )

    return parser.parse_args()