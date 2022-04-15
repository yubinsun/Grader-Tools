# For linux

# add commands you want to run before the simulation
# 

# Pre process : find IF_pipe_stage instance name 
# Pre process is only needed for lab 4 of 112L, a special case.
# python3 pre_proc.py
#

# Vivado address and flags.
/tools/Xilinx/Vivado/2020.1/bin/vivado -mode batch -source test.tcl -nolog -nojournal -notrace
