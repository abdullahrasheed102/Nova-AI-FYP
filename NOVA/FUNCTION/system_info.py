import psutil

def get_system_info():
    system_info = []

    # Battery information
    battery = psutil.sensors_battery()
    if battery:
        battery_info = f'Battery {battery.percent}%{" (Plugged In)" if battery.power_plugged else ""}'
        if not battery.power_plugged:
            battery_info += f', Time Left: {battery.secsleft // 3600} hours'
        system_info.append(battery_info)
    else:
        system_info.append('Battery No battery found')

    # CPU information
    cpu_info = f'CPU Cores {psutil.cpu_count(logical=True)} (Physical: {psutil.cpu_count(logical=False)})'
    cpu_info += f', Usage {psutil.cpu_percent(interval=1)}%'
    system_info.append(cpu_info)

    # Memory information
    memory = psutil.virtual_memory()
    memory_info = f'Total Memory {round(memory.total / (1024 ** 3), 2)}GB, Used {round(memory.used / (1024 ** 3), 2)}GB, Free {round(memory.free / (1024 ** 3), 2)}GB and Usage: {memory.percent}%'
    system_info.append(memory_info)

    # Disk information
    disk = psutil.disk_usage('/')
    disk_info = f'Total Disk {round(disk.total / (1024 ** 3), 2)}GB, Used {round(disk.used / (1024 ** 3), 2)}GB, Free {round(disk.free / (1024 ** 3), 2)}GB and Usage: {disk.percent}%'
    system_info.append(disk_info)

    return ', '.join(system_info)

# if __name__ == "__main__":
#     system_info = get_system_info()
#     print(system_info)
