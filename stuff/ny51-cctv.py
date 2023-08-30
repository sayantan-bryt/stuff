"""
api key : https://511ny.org/developers/help
"""

import argparse
import json
import os
import typing as t
from dotenv import load_dotenv
from urllib.parse import urlencode

import requests


load_dotenv()


def main(sargs: t.Optional[t.Sequence[str]] = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--fname", default="1")
    parser.add_argument("--endpoint", default="cameras", choices=["events", "roadways", "cameras"])
    parser.add_argument("--camera-id", default=None)
    args = parser.parse_args(sargs)

    apikey = os.environ.get("NY_CAMERA_API_KEY")
    query = {
        "key": apikey,
        "format": "json",
    }
    query_str = urlencode(query)
    url = f"https://511ny.org/api/get{args.endpoint}"
    print(f"Using endpoint : {url=}")

    fname = f"op-{args.fname}.txt"
    res = requests.get(f"{url}?{query_str}")
    status_code = res.status_code
    print(f"{status_code=}")
    with open(fname, "w") as f:
        f.write(res.text)

    try:
        data = res.json()
        if not data:
            return 0
        with open(f"{args.endpoint}.json", "w") as f:
            f.write(json.dumps(data, indent=4))
    except:  # noqa
        pass
    return 0
