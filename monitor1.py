from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
import time

log = core.getLogger()

LINK_CAPACITY = 1000000  # bytes/sec (adjust if needed)

class Monitor(object):

    def __init__(self):
        core.openflow.addListeners(self)

        self.total_bytes = 0
        self.last_time = time.time()

        # call function every 5 seconds
        Timer(5, self.print_stats, recurring=True)

    def _handle_PacketIn(self, event):
        packet_size = len(event.ofp.data)
        self.total_bytes += packet_size

    def print_stats(self):
        current_time = time.time()
        time_diff = current_time - self.last_time

        if time_diff == 0:
            return

        used_bandwidth = self.total_bytes / time_diff

        unused_bandwidth = LINK_CAPACITY - used_bandwidth
        if unused_bandwidth < 0:
            unused_bandwidth = 0

        utilization = (used_bandwidth / LINK_CAPACITY) * 100

        print("\n===== NETWORK UTILIZATION =====")
        print("Total Bytes:", self.total_bytes)
        print("Used Bandwidth (Bytes/sec): %.2f" % used_bandwidth)
        print("Unused Bandwidth (Bytes/sec): %.2f" % unused_bandwidth)
        print("Utilization (%%): %.2f%%" % utilization)

        # reset for next cycle
        self.total_bytes = 0
        self.last_time = current_time


def launch():
    core.registerNew(Monitor)