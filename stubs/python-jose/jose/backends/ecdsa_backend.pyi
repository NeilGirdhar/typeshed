from typing import Any

from .base import Key as Key

class ECDSAECKey(Key):
    SHA256: Any
    SHA384: Any
    SHA512: Any
    CURVE_MAP: Any
    CURVE_NAMES: Any
    hash_alg: Any
    curve: Any
    prepared_key: Any
    def __init__(self, key, algorithm) -> None: ...
    def sign(self, msg): ...
    def verify(self, msg, sig): ...
    def is_public(self): ...
    def public_key(self): ...
    def to_pem(self): ...
    def to_dict(self): ...