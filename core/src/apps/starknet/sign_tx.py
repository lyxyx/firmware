from typing import TYPE_CHECKING

from trezor.crypto import der
from trezor.crypto.curve import secp256k1
from trezor.crypto.hashlib import sha512
from trezor.lvglui.scrs import lv
from trezor.messages import StarkNetSignedTx, StarkNetSignTx
from trezor.ui.layouts import confirm_final
from trezor.wire import ProcessError

from apps.common import paths
from apps.common.keychain import auto_keychain

from . import ICON, PRIMARY_COLOR

if TYPE_CHECKING:
    from apps.common.keychain import Keychain
    from trezor.wire import Context


@auto_keychain(__name__)
async def sign_tx(
    ctx: Context, msg: StarkNetSignTx, keychain: Keychain
) -> StarkNetSignedTx:
    await paths.validate_path(ctx, keychain, msg.address_n)

    node = keychain.derive(msg.address_n)
    pubkey = node.public_key()

    return StarkNetSignedTx(public_key=pubkey, signature=b"")
