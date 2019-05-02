class cpu_percent:
    '''Keep track of cpu usage.'''

    def __init__(self):
        self.last = ps.cpu_times()

    def update(self):
        '''CPU usage is specific CPU time passed divided by total CPU time passed.'''

        last = self.last
        current = ps.cpu_times()

        total_time_passed = sum([current.__dict__.get(key, 0) - last.__dict__.get(key, 0) for key in current.attrs])

        #only keeping track of system and user time
        sys_time = current.system - last.system
        usr_time = current.user - last.user

        self.last = current

        if total_time_passed > 0:
            sys_percent = 100 * sys_time / total_time_passed
            usr_percent = 100 * usr_time / total_time_passed
            return sys_percent + usr_percent
        else:
            return 0

    def get_cpu_temperature(self):
        """
        Get CPU temperature.
        """
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp = float(f.read()) / 1000.0

        return temp

