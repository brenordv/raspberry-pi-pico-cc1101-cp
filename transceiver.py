from cpc.cpc import *

spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)
cs = DigitalInOut(board.GP5)
gdo0 = DigitalInOut(board.GP6)
sync_word = "666A"
rx = CC1101(spi, cs, gdo0, 50000, 434400000, sync_word)


def setup_tx():
    rx.setupTX()


def transmit(msg):
    rx.sendData2(msg, sync_word)


def wait_for_messages():
    rx.setupRX()
    while True:
        yield rx.receiveData2(0x17)  # 0x19
