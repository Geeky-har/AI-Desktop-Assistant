import psutil


def charge():
    battery = psutil.sensors_battery()
    percent = battery.percent
    return percent


def charge_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged     # returns true if plugged in
    plugged = "Plugged In" if plugged else "Not Plugged In"
    return plugged


if __name__ == '__main__':
    print(charge())
    print(charge_status())