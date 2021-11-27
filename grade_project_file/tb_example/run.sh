# For linux

# Pre process : find IF_pipe_stage instance name 
python3 pre_proc.py
#
/tools/Xilinx/Vivado/2020.1/bin/vivado -mode batch -source test.tcl -nolog -nojournal -notrace
