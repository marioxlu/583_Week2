import requests
import json

PINATA_API_KEY = "2a5f9e93c823afbedf96"
PINATA_SECRET_API_KEY = "a9c645d523c9c8417785c7ec5ee52e5a028ce9776a7b89277e0b673368d4e423"
PINATA_BASE_URL = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error: pin_to_ipfs expects a dictionary"

    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY,
    }

    response = requests.post(PINATA_BASE_URL, headers=headers, json=data)

    if response.status_code == 200:
        cid = response.json()["IpfsHash"]
        return cid
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "Error: get_from_ipfs accepts a CID in the form of a string"

    url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json() if content_type == "json" else response.text
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

    assert isinstance(data, dict), "Error: get_from_ipfs should return a dict"
    return data