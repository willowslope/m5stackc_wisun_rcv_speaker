from m5stack import *
from m5ui import *
from uiflow import *
import espnow
import wifiCfg
lcd.setRotation(1)
import hat
import hat

setScreenColor(0x111111)

hat_spk1 = hat.get(hat.SPEAKER)


wifiCfg.wlan_ap.active(True)
espnow.init()

txt = None
NPD = None
counter = None
POWER = None
stop_flag = None



def recv_cb(_):
  global txt,NPD,counter,POWER,stop_flag
  _, _, txt = espnow.recv_data(encoder='str')
  if txt.count('NPD=') > 0:
    NPD = txt.replace('NPD=', '')
    POWER = float(NPD)
    if POWER > 3000:
      setScreenColor(0xff0000)
      lcd.print(((NPD + 'W   ')), 0, 25, 0xff0000)
      axp.setLcdBrightness(100)
    elif POWER >= 0:
      setScreenColor(0x000000)
      lcd.print(((NPD + 'W   ')), 0, 25, 0xffffff)
      axp.setLcdBrightness(50)
    else:
      setScreenColor(0x000000)
      lcd.print(((NPD + 'W   ')), 0, 25, 0x3366ff)
      axp.setLcdBrightness(60)

  pass
espnow.recv_cb(recv_cb)


def buttonA_wasPressed():
  global txt, NPD, counter, POWER, stop_flag
  if stop_flag == True:
    counter = 600
    stop_flag = False
  pass
btnA.wasPressed(buttonA_wasPressed)


wifiCfg.screenShow()
wifiCfg.autoConnect(lcdShow = True)
setScreenColor(0x000000)
lcd.font(lcd.FONT_DejaVu40)
POWER = 0
stop_flag = True
counter = 0
hat_spk1.setVolume(50)
while True:
  if POWER > 4700:
    if stop_flag:
      hat_spk1.tone(1000, 200)
      wait_ms(100)
      hat_spk1.tone(1000, 200)
      wait_ms(700)
  if counter <= 0:
    stop_flag = True
  else:
    counter = (counter if isinstance(counter, int) else 0) + -1
    wait_ms(100)
