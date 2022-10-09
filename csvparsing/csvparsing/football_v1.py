import csv
import typing
import io
from csvparsing.utils import list_to_dict, str_to_list, clean_text


def parse_file(inp: io.TextIOWrapper, delimiter:str=',') -> dict:
    header = inp.readline()
    header = [ clean_text(item) for item in header.split(delimiter) ]
    for line in inp:
        line = line.split(delimiter)
        val = dict()
        for idx, item in enumerate(line):
            val[header[idx]] = clean_text(item)
        yield val


def parse_list(inp:list, delimiter:str=','):
    header = inp[0]
    header = [ clean_text(item) for item in header.split(delimiter) ]
    body = inp[1:]
    return [
        list_to_dict(header, str_to_list(row)) for row in inp[1:]
    ]


def parse_next_line(inp=None) -> dict:
    if isinstance(inp, str):
        print("Using str", inp)
        with open(inp, mode='r') as inp_f:
            content = csv.DictReader(inp_f, delimiter=',')
            for line in content:
                yield line
    elif isinstance(inp, list):
        print("Using list", inp)
        for row in parse_list(inp):
            yield row
    elif isinstance(inp, io.TextIOWrapper):
        print("Using io.TextIOWrapper")
        for line in parse_file(inp):
            yield line
    else:
        raise TypeError(
            (
            "`inp` accepted one of: str, list, io.TextIOWrapper."
            " Not `{}`".format(inp.__class__.__name__)
            )
        )

def get_name_and_diff(inp: dict) -> typing.Tuple[str, int]:
    team = inp["Team"]
    goals_for = int(inp["Goals For"])
    goals_against = int(inp["Goals Against"])
    diff = goals_for - goals_against
    return (team, abs(diff))


def get_min_score_difference(inp_file: str) -> typing.Tuple[str, int]:
    return min(
        map(
            lambda x: get_name_and_diff(x),
            parse_next_line(inp_file)
        ),
        key=lambda x: x[1]
    )


def main():
    print(get_min_score_difference("./input.csv"))


if __name__ == "__main__":
    main()

