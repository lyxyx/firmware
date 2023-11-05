from typing import TYPE_CHECKING

from trezor.lvglui.scrs import lv
from trezor.messages import StarkNetAddress, StarkNetGetAddress
from trezor.ui.layouts import show_address

from apps.common import paths
from apps.common.keychain import auto_keychain

from . import ICON, PRIMARY_COLOR
from .helper import starknet_address_from_pubkey

if TYPE_CHECKING:
    from apps.common.keychain import Keychain
    from trezor.wire import Context


@auto_keychain(__name__)
async def get_address(
    ctx: Context, msg: StarkNetGetAddress, keychain: Keychain
) -> StarkNetAddress:
    await paths.validate_path(ctx, keychain, msg.address_n)

    node = keychain.derive(msg.address_n)
    pubkey = node.public_key()
    address = starknet_address_from_pubkey(pubkey)

    if msg.show_display:
        path = paths.address_n_to_str(msg.address_n)
        ctx.primary_color, ctx.icon_path = lv.color_hex(PRIMARY_COLOR), ICON
        await show_address(
            ctx,
            address=address,
            address_n=path,
            network="StarkNet",
        )

    return StarkNetAddress(address=address)
