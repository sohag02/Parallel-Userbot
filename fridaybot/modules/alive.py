"""Check if fridaybot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time
from uniborg.util import friday_on_cmd, sudo_cmd
from fridaybot import ALIVE_NAME
from fridaybot.Configs import Config
from datetime import datetime
from fridaybot import Lastupdate
from fridaybot.modules import currentversion

#Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = "⭕ **PARALLEL IS:** `ONLINE`\n\n"
pm_caption += "✅ **PARALLEL SYSTEMS STATUS**\n"
pm_caption += "✅ **Telethon Version:** `1.15.0` \n"
pm_caption += "✅ **Python Version:** `3.7.4` \n"
pm_caption += f"✅ **Parallel Version** : `{currentversion}`\n"
pm_caption += f"✅ **Uptime** : `{uptime}` \n"
pm_caption += "✅ **Database Status:**  `Functional`\n"
pm_caption += "✅ **Current Branch** : `master`\n"
pm_caption += "✅ **Heroku Database** : `Working Properly`\n\n"

pm_caption += f"🔷 **My Owner** : {DEFAULTUSER} \n\n"

pm_caption += " **License** : [GNU General Public License v3.0](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += " **Copyright** : By [StarkGang@Github](GitHub.com/StarkGang)\n\n"

pm_caption += "[🇮🇳 Deploy ParallelUserbot 🇮🇳](https://telegra.ph/FRIDAY-06-15)"


@friday.on(friday_on_cmd(pattern=r"alive"))
@friday.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
