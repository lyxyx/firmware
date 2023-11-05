from ubinascii import hexlify

from trezor.crypto.hashlib import blake2b


def starknet_address_from_pubkey(pub_key_bytes: bytes) -> str:
    return f"0x{hexlify(pub_key_bytes).decode()}"
