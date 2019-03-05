import bot

def test_correct_address():
    msg = '@rl7877 requesting for some eth at 0x0ds9dczbxczcnzxczbxc to get started with Ocean Protocol'
    assert bot.fetch_address(msg) == '0x0ds9dczbxczcnzxczbxc'

def test_blank_address():
    msg = '@rl7877 requesting for some eth at to get started with Ocean Protocol'
    assert bot.fetch_address(msg) == ''