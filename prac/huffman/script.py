import typing
import copy
import random
import argparse
import sys


class Node:
    def __init__(
        self,
        data: str = "",
        wt: float | int = 1e12
    ):
        self.data = data
        self.wt = wt
        self.left : Node = None
        self.right : Node = None

    def __add__(self, other):
        data = self.data + other.data
        wt = self.wt + other.wt
        return Node(data, wt)

    def __str__(self):
        temp = {
            k: v
            for k, v in self.__dict__.items()
            if not k.startswith('_')
        }
        temp = self.data
        return str(temp)


class HuffmanEncoding:
    def __init__(self, data):
        self.data = data
        self.word_count = dict()
        self.encoding = ""
        self.data_repr = list()
        self.root_node = None
        self._prepare(data)

    def _prepare(self, data):
        for ch in data:
            try:
                self.word_count[ch] += 1
            except KeyError as ke:
                self.word_count[ch] = 1
        self.data_repr = sorted(
            self.word_count.items(),
            key=lambda x: x[1],
            #reverse=True,
        )
        local_repr: list = copy.deepcopy(self.data_repr)
        local_repr = list(map(lambda x: Node(*x), local_repr))
        self._encode(local_repr)

    def _encode(self, data_repr: typing.List[Node]):
        # TODO: Make it general. Now considering at least 2 keys are present
        self._encode_recur(data_repr, None)

    def _encode_recur(self, data_repr: typing.List[Node], combined: Node):
        if len(data_repr) <= 1:
            self.root_node = combined
            return
        first, second = data_repr[:2]
        curr_node = first + second
        data_repr = [curr_node] + data_repr[2:]
        data_repr.sort(key=lambda x: x.wt)
        curr_node.left = first
        curr_node.right = second
        combined = curr_node
        self._encode_recur(data_repr, combined)

    def get_encoding(self):
        temp_node = copy.deepcopy(self.root_node)
        mappings = dict()
        self.encoding = self._get_encoding(mappings, temp_node)
        return mappings

    def _get_encoding(self, mappings, node, enc=""):
        if node.left is None and node.right is None:
            #print(node.data)
            mappings[node.data] = enc
            return
        #print(node.data)
        self._get_encoding(mappings, node.left, enc + "0")
        self._get_encoding(mappings, node.right, enc + "1")

    def get_final_encoded_msg(self) -> str:
        enc = self.get_encoding()
        ans = ''.join(
            [ enc[ch] for ch in self.data ]
        )
        return ans

    def _get_all_nodes(self, node):
        if node is None:
            return
        self._get_all_nodes(node.left)
        self._get_all_nodes(node.right)

    def __str__(self):
        temp = {
            k: v
            for k, v in self.__dict__.items()
            if not k.startswith('_')
        }
        return str(temp)


def basic_encoding(src_msg: str) -> str:
    msg = src_msg[:]
    msg += "$"
    now = msg[0]
    cnt = 1
    tobe = ""
    for ch in msg[1:]:
        if ch == now:
            cnt += 1
        else:
            tobe += f"{cnt}{now}"
            now = ch
            cnt = 1
    if cnt > 1:
        tobe += f"{msg[-1]}{now}"
    return tobe


def main(args: typing.Optional[typing.Sequence[str]]):
    parser = argparse.ArgumentParser()
    msg = "AAABBCAAD"
    parser.add_argument('--msg', type=str, default=msg)
    parser.add_argument('--msg-len', type=int, default=5)
    parser.add_argument('--diff-chr', type=int, default=2)
    parser.add_argument('--rng-seed', type=int, default=3)
    args = parser.parse_args(args)
    items =  [ chr(i) for i in range(ord('A'), ord('Z') + 1) ]
    random.seed(args.rng_seed)
    assert args.diff_chr <= args.msg_len and args.diff_chr >= 2
    while True:
        msg = ''.join(
            [
                items[
                    random.randint(
                        len(items)-args.diff_chr,
                        len(items)-1
                    )
                ]
                for chrs in range(args.msg_len)
            ]
        )
        if len(set(msg)) == args.diff_chr:
            break
    # GFG test
    # Output- f: 0 c: 100 d: 101 a: 1100 b: 1101 e: 111
    #msg = ''.join([
        #x*ch for ch, x in zip(
            #[ 'a', 'b', 'c', 'd', 'e', 'f' ],
            #[ 5, 9, 12, 13, 16, 45 ]
        #)
    #])
    print(f"{msg=}")
    hf = HuffmanEncoding(msg)
    huffman_encoding = hf.get_encoding()
    huffman_encoded_msg = hf.get_final_encoded_msg()
    basic_encoded_msg = basic_encoding(msg)
    print(f"{huffman_encoding=}")
    print(f"{huffman_encoded_msg=}")
    print(f"{basic_encoded_msg=}")
    huffman_vs_basic = {
        "len_basic": len(basic_encoded_msg),
        "len_huffman": len(huffman_encoded_msg)
    }
    print(f"{huffman_vs_basic=}")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

