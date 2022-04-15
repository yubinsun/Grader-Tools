This module is used to grade all verilog project file. It needs 
Vivodo installed. Change parameters in run.py. Run run.py to use
the module.

What you need for minimal:
- test.tcl
- run.sh"
- Your own testbench that is modified with \*key\*={Value} pairs. The Value should be printed out to console using "\$monitor"


Steps:
- Change the testbench with the \*key\*={Value} pairs. These pairs are the ones saved into the report.  
- Change test.tcl. Add filenames, and name of the TB module to run.
- Change run.sh or run.bat with the Vivado path. Add any other command you want to run before the simulation.
- Change run.py with testbench files, submission path, sensitive fields (\*key\*={Value} pairs) for reports, and the report name.




\\
11/27/2021:
Add testbench example (test.tcl, run.bat/run.sh for each system)
Add pre_porcessor.py file in tb special for lab 4 (112L), because 
students can rename the data_memory instance to any name. 

4/15/2022:
Updated steps. 
