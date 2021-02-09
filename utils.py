from typing import Tuple, Union, Dict, List

from jsonpath_ng import parse

Mapping = Dict[str, Union["Mapping", str]]


def get_from_list(ls, index=0):
    try:
        return ls[index]
    except IndexError:
        return None


def map_jsonpath(source: dict, mapping: Mapping):
    res = {}
    mappings: List[Tuple[Tuple[str], Union[str, Mapping]]] = [
        ((k,), v) for k, v in mapping.items()
    ]
    while len(mappings) > 0:
        keys, value = mappings.pop()
        if isinstance(value, str):
            inner = res
            for k in keys[:-1]:
                inner[k] = inner.get(k, {})
                inner = res[k]
            inner[keys[-1]] = get_from_list(
                [m.value for m in parse(value).find(source)]
            )
        else:
            for k, v in value.items():
                mappings.append(((tuple(list(k) + [k])), v))
    return res
