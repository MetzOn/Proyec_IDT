import uuid
import datetime as dt
def generate_random_id():
    myuuid= uuid.uuid4()
    newuuid= str(myuuid).split("-")[0]
    currentdate = str(dt.datetime.now()).split(" ")
    currenttime = currentdate[1].split(".")[0].replace(":","_")
    return f"{currentdate[0]}-{currenttime}-{newuuid}"

