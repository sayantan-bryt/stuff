import sys
import os

def process(s : str, padding : int) -> str:
    if(s.find('-:')) == -1:
        return s + ' ' * (padding - len(s))
    else:
        return ' ' * (padding - len(s)) + s

def format_table(s : str) -> str:
    width = list()
    for line in s.split('\n'):
        if len(line):
            line = [ x.strip() for x in line.split('|')  ]
            width = [ 0 for _ in range(len(line)) ]
    for line in s.split('\n'):
        if len(line):
            line = [ x.strip() for x in line.split('|')  ]
            width = [ max(width[i], len(line[i])) for i in range(len(line)) ]
    ans = ""
    for line in s.split('\n'):
        if len(line):
            line = [ x.strip() for x in line.split('|') if len(line.strip()) ]
            line = [ process(line[i], width[i]) for i in range(len(line)) ]
            line = [ f" {x} " if len(x) else x for x in line ]
            line = "|".join(line)
            ans += f"{line}\n"
    return ans


def process_file(inp_path : str):
    dir_name = os.path.dirname(inp_path)
    file_name, file_ext = os.path.splitext(os.path.basename(inp_path))
    if file_name.startswith("op_") or file_ext != '.md':
        return
    print(inp_path)
    output_file = os.path.join(dir_name, f"op_{file_name}{file_ext}")
    s = open(inp_path, 'r').readlines()
    with open(output_file, 'w') as op:
        idx = 0
        while idx < len(s):
            curr = s[idx]
            if curr.startswith('|') and not s[idx-1].startswith('|') and (s[idx + 1].find("---:") != -1 or s[idx + 1].find(":---") != -1):
                idx += 1
                while idx < len(s) and s[idx].startswith('|'):
                    curr += s[idx]
                    idx += 1
                idx -= 1
                curr = format_table(curr)
            op.write(curr)
            idx += 1


def recur(_path: str, ret: list) -> list:
    if os.path.isdir(_path):
        for _p in os.listdir(_path):
            curr = os.path.join(_path, _p)
            if not os.path.isdir(curr):
                ret.append(curr)
            else:
                recur(os.path.join(_path, _p), ret)
        else:
            return ret
    else:
        ret.append(_path)
        return ret


if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else "inp.txt"
    if os.path.isdir(inp):
        for _file in os.listdir(inp):
            file_path = os.path.join(inp, _file)
            if os.path.isdir(file_path):
                ret = list()
                ret_paths = recur(file_path, ret)
                for _path in ret_paths:
                    process_file(_path)
            else:
                process_file(file_path)
    else:
        process_file(inp)

