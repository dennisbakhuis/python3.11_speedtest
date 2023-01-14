import json
from pathlib import Path
import re
import argparse


def collect_output(data_path: str) -> None:
    """Collect data and create summary as JSON."""
    path = Path(data_path)
    files = path.glob('*.out')

    speedtest = {}
    for file_name in files:
        language = file_name.stem[10:].capitalize()

        with open(file_name, 'r') as f:
            last_line = f.readlines()[-1].strip()

        time = re.findall(r'\d+\.\d+', last_line)

        if time:
            time = round(float(time[0]), ndigits=4)
            print(f"{language:<10} -> {time}")
            speedtest[language] = time

    # sort by speed
    speedtest = {x[0]: x[1] for x in sorted(speedtest.items(), key=lambda x: x[1])}

    with open(path / 'speedtest_results.json', 'w') as f:
        json.dump(speedtest, f, indent=4)


def main(arguments=None):
    """Main loop in arg parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--speedtest-data-path",
        help="Path with all `.out` files from the speedtest.",
        required=True,
    )

    args = parser.parse_args(arguments)

    collect_output(
        args.speedtest_data_path,
    )


if __name__ == "__main__":
    main()
