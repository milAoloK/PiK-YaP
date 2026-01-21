from adapter import ThirdPartyAdapter
from third_party import ThirdPartyMessenger


def test_third_party_adapter_send():
    messenger = ThirdPartyMessenger()
    adapter = ThirdPartyAdapter(messenger)

    assert adapter.send("Hello Adapter") is True
    