#script for EECS 112L lab4
exec rm -rf grading_run_project

if {[catch {
    # create a project file for simulation and set language as Verilog
    create_project grading_run_project grading_run_project -part xc7a200tfbg676-2
    set_property simulator_language Verilog [current_project]
    
    # Add files. Include add files needs for simulation
    add_files -norecurse {ALU.v ALUControl.v control.v data_memory.v EX_pipe_stage.v \
        EX_Forwarding_unit.v Hazard_detection.v ID_pipe_stage.v IF_pipe_stage.v \
        instruction_mem_grade.v mips_32.v mux.v mux4.v pipe_reg.v pipe_reg_en.v\
        register_file.v sign_extend.v tb_mips_32_grade.v }
    
    update_compile_order -fileset sources_1
    
    # tb 1
    # Set the "top" of the simulation. Put in the module name of your testbench.
    set_property top tb_mips_32_grading [get_filesets sim_1]
    # Run the simulation
    set_property top_lib xil_defaultlib [get_filesets sim_1]
    launch_simulation
    run 1500 ns
    close_sim

    # tb 2. If need to run more simulations
    #remove_files tb_mips_32_grade.v instruction_mem_grade.v 
    #add_files instruction_mem_sw.v tb_mips_32_sw.v
    #set_property top tb_mips_32_sw [get_filesets sim_1]
    #set_property top_lib xil_defaultlib [get_filesets sim_1]
    #launch_simulation
    #run 1500 ns
    #close_sim

    # finally clean up the project
    close_project
    exec rm -rf grading_run_project .Xil
    exit
} errmsg]} {
    close_project
    puts "ErrorMsg Catched: $errmsg"
    puts "*CompileError* = {1}"
    exec rm -rf grading_run_project .Xil
    exit
}








