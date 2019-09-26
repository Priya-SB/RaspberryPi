import RPi.GPIO as gp
import time
gp.setmode(gp.BOARD)
sig=[8,10,12,16,18,22,24,26]
for sign in sig:
        gp.setup(sign,gp.OUT)
        gp.output(sign,0)
try:
        signal_arr = [[1,0,0,1,1,0,0,1],[0,1,1,0,0,1,1,0]]
        while True:
                for i in range(2):
                        for j in range(8):
                                gp.output(sig[j],signal_arr[i][j])
                        time.sleep(2)
finally:
        gp.cleanup()