from typing import Union, Tuple

def to_kv(k:str =None, v:Union[int, float] =None) -> Tuple[str, float]:
    """Return a tuple of a string and a float"""
    return (k, v ** 2)

