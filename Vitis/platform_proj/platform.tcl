# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct /home/lars/Documents/MPsocGroup/embedded_new_final/vitisws/platform_proj/platform.tcl
# 
# OR launch xsct and run below command.
# source /home/lars/Documents/MPsocGroup/embedded_new_final/vitisws/platform_proj/platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {platform_proj}\
-hw {/home/lars/Documents/MPsocGroup/embedded_new_final/MPSoC4Drones/hdl/projects/u96v2_sbc_mp4d_2020_2/u96v2_sbc_mp4d_wrapper.xsa}\
-proc {psu_cortexa53_0} -os {standalone} -arch {64-bit} -fsbl-target {psu_cortexa53_0} -out {/home/lars/Documents/MPsocGroup/embedded_new_final/vitisws}

platform write
platform generate -domains 
platform active {platform_proj}
domain active {zynqmp_fsbl}
bsp reload
bsp config stdin "psu_uart_1"
bsp config stdout "psu_uart_1"
bsp write
bsp reload
catch {bsp regenerate}
domain active {standalone_domain}
bsp reload
bsp config stdin "psu_uart_1"
bsp config stdout "psu_uart_1"
bsp write
bsp reload
catch {bsp regenerate}
domain active {zynqmp_pmufw}
bsp reload
bsp config stdin "psu_uart_1"
bsp config stdout "psu_uart_1"
bsp write
bsp reload
catch {bsp regenerate}
platform generate
platform config -updatehw {/home/lars/Documents/MPsocGroup/embedded_new_final/MPSoC4Drones/hdl/projects/u96v2_sbc_mp4d_2020_2/u96v2_sbc_mp4d_wrapper.xsa}
platform clean
platform generate
