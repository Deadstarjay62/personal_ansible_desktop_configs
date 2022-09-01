#!/usr/bin/env python3

# from:
# https://www.pragmaticlinux.com/2020/06/check-the-raspberry-pi-cpu-temperature/


def main():
    """
    Program to demonstrate how to obtain the current value of the CPU temperature.
    """
    print('Current CPU temperature is {:.2f}°C.'.format(get_cpu_temp()))
    print('CPU begins throttling at 60°C, and reaches critical at 80°C.')


def get_cpu_temp():
    """
    Obtains the current value of the CPU temperature.
    :returns: Current value of the CPU temperature if successful, zero value otherwise.
    :rtype: float
    """
    # The first line in this file holds the CPU temperature as an integer times 1000.
    # Read the first line and remove the newline character at the end of the string.
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        line = f.readline().strip()
    # Give the result back to the caller.
    return float(line) / 1000 if line.isdigit() else 0.0


if __name__ == "__main__":
    main()
