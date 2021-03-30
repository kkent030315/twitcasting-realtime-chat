import sys
sys.path.append("../src/")

from twitcasting_realtime_chat import TwcsRealtimeChat 


def main() -> None:
    try:
        instance = TwcsRealtimeChat(auto_reconnect=True)
        instance.run(user_id="izayoikaede")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

