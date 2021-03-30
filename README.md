<p align=center>
    <img src="image.gif" width="500">
</p>

<p align=center>
    <img src="https://img.shields.io/circleci/build/github/kkent030315/twitcasting-realtime-chat?style=for-the-badge">
    <img src="https://img.shields.io/pypi/v/twitcasting-realtime-chat?style=for-the-badge">
    <img src="https://img.shields.io/github/license/kkent030315/twitcasting-realtime-chat?style=for-the-badge">
</p>

# twitcasting-realtime-chat
An unofficial comment viewer CLI for TwitCasting lives

# Usage

1. Install

```bash
pip install twitcasting-realtime-chat
```

2. Import

```python3
from twitcasting_realtime_chat import TwcsRealtimeChat
```

3. Use

```python3
instance = TwcsRealtimeChat(auto_reconnect=True)
instance.run(user_id="user_id")
```

# License

MIT