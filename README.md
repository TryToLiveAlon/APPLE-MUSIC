
---

# APPLE MUSIC BOT

A powerful Telegram music bot for voice chats with features like YouTube, Spotify, Resso, AppleMusic, and Soundcloud support.

## 🎯 Features

* YouTube, Spotify, Resso, AppleMusic & Soundcloud support
* Written in Python with Pyrogram and Py-Tgcalls
* Heroku and VPS deployment support
* Channel and group voice chat playback
* Inline search support
* YouTube thumbnail search
* Unlimited queue
* Broadcast messages
* Detailed stats and user analytics
* Block/Unblock user management
* Multi-language support
* Playlist management

## ⚡️ Quick Setup

### Heroku Deployment

[![Deploy on Heroku](https://img.shields.io/badge/Deploy%20On%20Heroku-purple?style=for-the-badge\&logo=heroku)](https://dashboard.heroku.com/new?template=https://github.com/TryToLiveAlone/Apple-Music)

### 🖇 VPS Deployment

```bash
git clone https://github.com/TryToLiveAlone/Apple-Music && cd Apple-Music
bash setup
```

* Fill [Extra Variables](https://github.com/TryToLiveAlone/Apple-Music/blob/master/sample.env):
  `nano .env` → edit → `CTRL+X`, then `y`, then `Enter`
* Install tmux:
  `sudo apt install tmux && tmux`
* Run the bot:
  `bash start`
* To exit tmux session:
  Press `Ctrl+b`, then `d`

## ⚙️ Config Variables

**Required variables:**

* `API_ID` — Get from [my.telegram.org](https://my.telegram.org)
* `API_HASH` — From [my.telegram.org](https://my.telegram.org)
* `BOT_TOKEN` — From [@BotFather](https://t.me/BotFather)
* `MONGO_DB_URI` — MongoDB database URI
* `LOG_GROUP_ID` — Telegram group ID for logging
* `OWNER_ID` — Your Telegram user ID
* `STRING_SESSION` — Pyrogram string session (v2)

**Optional variables:**

* `SPOTIFY_CLIENT_ID`
* `SPOTIFY_CLIENT_SECRET`
* `HEROKU_API_KEY`
* `HEROKU_APP_NAME`

👉 See [**config docs**](https://github.com/TryToLiveAlone/Apple-Music/blob/master/config/README.md) for the full list of variables.

## 🤝 Support

* Join [**APPLE\_MUSIC\_SUPPORT**](https://t.me/TryToLiveAlone) for help and updates

## 📃 License

This project is licensed under the [**MIT License**](https://github.com/TryToLiveAlone/Apple-Music/blob/master/LICENSE)

## 🙋‍♂️ Developer

* 👨‍💻 **Developer:** [TryToLiveAlone](https://t.me/TryToLiveAlone)

---

Let me know if you'd like this saved as a `README.md` file or published to GitHub.
