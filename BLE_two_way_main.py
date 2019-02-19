# Imports
import ece16ble as bt
import serial, sys
import time
import random

# Global variables
# Ramsin
serial_port = "/dev/cu.usbserial"
peripheral_MAC = "3403DE02C38D"
# centralMAC = "A810871B347B"

# # Eugene
# serial_port = "COM5" 
# peripheral_MAC = "3403DE1C5F56"
# # centralMAC = "3403DE33FB39"

if(__name__ == "__main__") :
  try :
    bt.ble_setup(serial_port, peripheral_MAC)

    bt.ble_connect()

    # ---------------------------------------------------------------------------
    # Here's an example:
    # 1) Continously reading lines of data from the Arduino separated by commas
    # 2) Sending fake heart rate to Arduino every second
    # 3) Sending fake step count to Arduino every second
    # NOTE: YOU MUST CHECK TO SEE IF DATA WAS CORRUPTED OR NOT!!!
    t1 = time.time()
    while(True):

      new_val = bt.ble_read_line(",")
      if(len(new_val)) :
        print(" > " + new_val)

      t2 = time.time()
      if (t2 - t1 >= 1) :
        t1 = t2
        hr_msg = "H" + str(random.randint(0,200)) + ","
        bt.ble_write(hr_msg)
        step_count = "S" + str(random.randint(0,20000)) + ","
        bt.ble_write(step_count)
    # ---------------------------------------------------------------------------

  except Exception as e :
    print("Error: " + str(e))
    bt.ble_close()
