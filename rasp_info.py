"""
This script:
- to store in PG database some monitoring information from the PI
- and then graph them with GRAFANA

repo is here:
https://github.com/renaudrenaud/raspi_zero2_monitoring

it uses pyembedded lib from:
https://pypi.org/project/pyembedded/

pip3 install psutil - required for pyembedded
pip3 install pyembedded
"""

from time import sleep
from pg_monitor import PG
from pyembedded.raspberry_pi_tools.raspberrypi import PI


# script is running where PG is installed
someUri = "postgres://postgres:postgres@127.0.0.1:5432"

# DB class
mybase = PG(someUri)
print(str(mybase.clsVersion()))

# Let's go for embedded information
pi = PI()

if __name__ == '__main__':
    while True:

        print(pi.get_ram_info())
        print(pi.get_disk_space())
        cpuU = pi.get_cpu_usage()
        print("Wifi: " + pi.get_connected_ip_addr(network='wlan0'))
        print("RJ45: " + pi.get_connected_ip_addr(network='eth0'))
        cpuT = pi.get_cpu_temp()

        # CPU Speed calculation
        f = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
        cpuSpeed = int(int(f.read()) / 1000)
        f.close()

        # -- insert temperature
        req = "insert into public.rpiz2_temperature (f_measure, t_time) values (" + str(cpuT) + ", current_timestamp)"
        mybase.clsExecute(req)
        
        # -- insert cpu_usage
        req = "insert into public.rpiz2_cpu_usage (f_cpu_usage, t_time) values (" + str(cpuU) + ", current_timestamp)"
        mybase.clsExecute(req)
        
        # -- insert cpu_Speed
        req = "insert into public.rpiz2_cpu_speed (f_cpu_speed, t_time) values (" + str(cpuSpeed) + ", current_timestamp)"
        mybase.clsExecute(req)
        
        
        sleep(10)
