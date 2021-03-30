import sys
sys.path.append("../src/")

import threading
import time
import os
import signal
from twitcasting_realtime_chat import TwcsRealtimeChat


def thread_worker():
    try:
        instance = TwcsRealtimeChat(auto_reconnect=True)
        instance.run(user_id="izayoikaede")
    except KeyboardInterrupt:
        pass


def main():
    thread = threading.Thread(target=thread_worker)
    thread.start()

    time.sleep(3)
    
    os.kill(os.getpid(), signal.SIGTERM)


if __name__ == "__main__":
    main()

