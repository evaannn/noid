
-- Configure UART for 9600 baud (NodeMCU default = 115200)
uart.setup(0, 9600, 8, 0, 1, 1) 
tmr.delay(250 * 1000) 

print("\nNODEMCU_READY") 
dofile("main.lua")
