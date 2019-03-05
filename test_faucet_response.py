import bot

def test_correct_response():
    address = '0x679D63F719f4F179c0AFfc16DEA71e1C2C843e33'
    assert bot.send_eth(address) == 200

def test_error_response():
    address = '0x679D63F719f4F179c0AFfc16DEA71e1C2Cdsdsdsdsdsdsd'
    assert bot.send_eth(address) == 404

def test_repeat_request_response():
    address = '0x679D63F719f4F179c0AFfc16DEA71e1C2Cdsdsdsdsdsdsd'
    assert bot.send_eth(address) == 503