import os
import socket
import json
import pywal
from settings import OS 
from app import app
from settings import WAL, BACKUP_FILE, WALLPAPER_DIR
from color import COLOR
from wallpaper import WALLPAPER

@app.get("/reset",tags = ["system"])
def reset_all():
    backup = open(BACKUP_FILE)
    data = json.load(backup)
    COLOR.update(data["colors"])
    WALLPAPER.update({
        "current": data["wallpaper"]
    })
    image = pywal.image.get(os.path.join(WALLPAPER_DIR, data["wallpaper"]))
    pywal.wallpaper.change(image)

@app.get("/sys",tags=["system"])
def get_system_info():
    name = socket.gethostname() 
    return { "os":OS, "name":name }

@app.get("/health",tags=["system"])
def check_health():
    return {"connected":True}

