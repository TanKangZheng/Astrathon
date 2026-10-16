from . import EOACardData

# Python Libraries
import httpx

# --- HTTPX --- #
client: httpx.Client | None = None

# --- API url --- #
api_url = "https://api.echoesofastra.com"
query_url = api_url + "/searchcardsbyname"

# Optionally identify the user
def set_client(headers: dict[str, str] | None = None) -> httpx.Client:
    global client
    if client is not None:
        client.close()

    client = httpx.Client(headers=headers, base_url=api_url)
    return client

def get_client() -> httpx.Client:
    return client if client is not None else set_client()


def search(cardName: str) -> list[EOACardData]:
    response = get_client().get("/searchcardsbyname", params={f"cardName": cardName})
    print(f"Fetching data from {response.url}")
    if (response.status_code == 200):
        data = response.json()
        returnData = []
        rawData = data["Cards"]
        for cardData in rawData:
            returnData.append(EOACardData(cardData))
        return returnData
    else:
        print("Error fetching response!")
        return None