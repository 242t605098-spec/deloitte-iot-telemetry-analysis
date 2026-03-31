from datetime import datetime

def convert_to_epoch(time_str):
    dt = datetime.fromisoformat(time_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


# ✅ FORMAT 1
def convertFromFormat1(jsonObject):
    locationParts = jsonObject["location"].split("/")

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": convert_to_epoch(jsonObject["timestamp"]),  # ✅ FIXED
        "location": {
            "country": locationParts[0],
            "city": locationParts[1],
            "area": locationParts[2],
            "factory": locationParts[3],
            "section": locationParts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }


# ✅ FORMAT 2
def convertFromFormat2(jsonObject):
    locationParts = jsonObject["device"]["location"].split("/")

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": convert_to_epoch(jsonObject["timestamp"]),  # ✅ FIXED
        "location": {
            "country": locationParts[0],
            "city": locationParts[1],
            "area": locationParts[2],
            "factory": locationParts[3],
            "section": locationParts[4]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }
