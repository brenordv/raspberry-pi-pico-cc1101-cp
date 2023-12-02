# Raspberry Pi Pico + CC1101
This is a simple project to make 1 Pi Pico communicate to another using CC1101 transceiver modules.
In every video I watched, this seemed very easy, but I had a lot of trouble getting it to work, so I'm
creating this repo to hopefully help others struggling with this setup.

## How does it work
On one board I've setup two buttons:
1. Button 1 (Blue): Select a random word from a list
2. Button 2 (Green): Uses the CC1101 to send the message.

When the message is sent, the other board will receive it and display it on the OLED screen.

To define who's sending and who's receiving, just change the boolean in the `main.py` file.

As sender/transmitter:
```python
if __name__ == "__main__":
    main(is_sender=True)
```

As a receiver:
```python
if __name__ == "__main__":
    main(is_sender=False)
```


## Hardware
1. Raspberry Pi Pico x2
2. SSD1306 OLED Display x2
3. CC1101 Transceiver Module x2
4. Buttons x2
5. 10k Ohm Resistor x4
6. A bunch of wires.


## Software
1. Circuit Python 8.2.8 [(Download)](https://downloads.circuitpython.org/bin/raspberry_pi_pico_w/en_US/adafruit-circuitpython-raspberry_pi_pico_w-en_US-8.2.8.uf2)
2. (Parts of) Adafruit Circuit Bundle `8.x-mpy-20231130`  [(Download)](https://objects.githubusercontent.com/github-production-release-asset-2e65be/72229984/402c4145-2d91-4b36-9611-dac865fb0de2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231201%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231201T031457Z&X-Amz-Expires=300&X-Amz-Signature=db471f36a0e5b022c78e886ed9d0621814de1b8410e3d676b6b30316f6d4938a&X-Amz-SignedHeaders=host&actor_id=28983571&key_id=0&repo_id=72229984&response-content-disposition=attachment%3B%20filename%3Dadafruit-circuitpython-bundle-8.x-mpy-20231130.zip&response-content-type=application%2Foctet-stream)

> To make things more convenient, I included the lib folder with what I needed from the bundle.


## How to setup a Raspberry Pi Pico
1. Clone the repo
2. Copy everything but `.images` and `.datasheets` to the root of the Pico.
3. Edit the `code.py` file to change the boolean to `True` or `False` depending on if you want to send or receive.


## Images
Here are some images of the breadboard with all setup and the schematic.
![Schematic](.images/board_schematic.png)
![Board Overview](.images/board_overview.jpeg)
![Board CC1101 POV 1](.images/board_cc1101_pov1.jpeg)
![Board CC1101 POV 2](.images/board_cc1101_pov2.jpeg)


## Demo video

[Demo Video on TikTok](https://vm.tiktok.com/ZM6RJtgdC/)


## Datasheets
1. [Raspberry Pi Pico W](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf)
2. [SSD1306](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf)
3. [CC1101](https://www.ti.com/lit/ds/symlink/cc1101.pdf?ts=1638329135087&ref_url=https%253A%252F%252Fwww.google.com%252F)

I also provided those datasheets in the `.datasheets` folder.
