from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DirectPinScanner
from kmk.keys import KC
from kmk.extensions.rgb import RGB
from kmk.extensions.OLED import OLED

keyboard = KMKKeyboard()

# GPIO pins for your 6 switches
keyboard.col_pins = (
    'GP26', 
    'GP27', 
    'GP28', 
    'GP29', 
    'GP6',  
    'GP7',  
)
keyboard.matrix = DirectPinScanner(keyboard.col_pins)

keyboard.keymap = [
    [
        KC.A, 
        KC.B, 
        KC.C, 
        KC.D, 
        KC.E, 
        KC.F, 
    ]
]

rgb_ext = RGB(
    pixel_pin='GP0',
    num_pixels=12,
    rgb_order=(1, 0, 2)
)
keyboard.extensions.append(rgb_ext)

class MyOLED(OLED):
    def draw(self, oled):
        oled.fill(0)
        oled.text("MEOW~", 0, 0, 1)
        oled.show()

oled_ext = MyOLED(
    i2c_num=0,
    i2c_scl='GP5',
    i2c_sda='GP4',
    width=128,
    height=32,
    flip=False
)
keyboard.extensions.append(oled_ext)

if __name__ == '__main__':
    keyboard.go()
