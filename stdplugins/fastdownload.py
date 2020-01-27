"""
command: .url 

"""
import aria2p
from telethon import events
import asyncio
import os
from uniborg.util import admin_cmd

cmd = "aria2c --enable-rpc --rpc-listen-all=false --rpc-listen-port 6800  --max-connection-per-server=10 --rpc-max-request-size=1024M --seed-time=0.01 --min-split-size=10M --follow-torrent=mem --split=10 --daemon=true"

aria2_is_running = os.system(cmd)

aria2 = aria2p.API(
		aria2p.Client(
			host="http://localhost",
			port=6800,
			secret=""
		)
	)


@borg.on(admin_cmd(pattern="ariaurl ?(.*)"))
async def download_url(event):
	if event.fwd_from:
		return
	# var = event.text[5:]
	input_str = event.pattern_match.group(1)
	uris = []
	uris.append[input_str]
	print(uris[0])	
	# uris = ""
	# uris = [var]
	await asyncio.sleep(5)
	#Add URL Into Queue 
	try:	
		download = aria2.add_uris(uris[0], options=None, position=None)
	except Exception as e:
		await event.edit("`Error:\n`"+str(e))
		return

	gid = download.gid
	complete = None
	while complete != True:
		file = aria2.get_download(gid)
		complete = file.is_complete
		try:
			msg = "**Downloading File:** "+str(file.name) +"\n + \
				**Speed:** "+ str(file.download_speed_string())+"\n + \
				**Progress:** "+str(file.progress_string())+"\n + \
				**Total Size:** "+str(file.total_length_string())+"\n + \
				**ETA:**  "+str(file.eta_string())+"\n +" 	
			await event.edit(msg)
			await asyncio.sleep(10)
		except Exception as e:
			print(str(e))
			pass	
			
	await event.edit("**File Downloaded Successfully:** `{}`".format(file.name))
