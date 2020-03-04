from statistics import median
from hx711 import HX711


class FootScale(HX711):

    def __init__(self, dout_pin=5, pd_sck_pin=6, slope=1, offset=0, measure_count=3):
        super(FootScale, self).__init__(dout_pin=dout_pin, pd_sck_pin=pd_sck_pin, gain=64, channel='A')
        self.slope=slope
        self.offset=offset
        self.measure_count = measure_count
        self.reset()

    def _measure(self):
        raw_value = median(self.get_raw_data(times=self.measure_count))
        return (raw_value - self.offset) / self.slope

    @property
    def weight(self):
        return round(self._measure(), 1)

    def calibrate(self):
        raw_value = median(self.get_raw_data(times=25))
        self.offset = raw_value


class ScalesController:
    def __init__(self):
        self.scale_left = FootScale(dout_pin=5, pd_sck_pin=6)
        self.scale_right = FootScale(dout_pin=13, pd_sck_pin=19)
        self.scale_left.calibrate()
        self.scale_right.calibrate()

    def readings(self):
        wl = self.scale_left.weight
        wr = self.scale_right.weight
        return wl, wr
