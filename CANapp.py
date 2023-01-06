import time
import can
from can.interface import Bus

can.rc['interface'] = 'vector'
can.rc['channel'] = '0', '1'
can.rc['bitrate'] = 500000


bus = Bus()




def main():
    logger = can.Logger('bus_log.csv', 'a')
    notifier = can.Notifier(bus, [can.Printer(), logger])
    try:
        while True:
            time.sleep(0.001)
    except KeyboardInterrupt:
        bus.shutdown()
        notifier.stop()


# if __name__ == "__main__":
#     main()
