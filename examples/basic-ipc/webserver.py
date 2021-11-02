from quart import Quart
from nextcord.ext import ipc


app = Quart(__name__)
ipc_client = ipc.Client(secret_key="my_secret_key")  # secret_key must be the same as your server


@app.route("/")
async def index():
    # get the member count of the guild with the id 12345678
    member_count = await ipc_client.request("get_member_count", guild_id=12345678)
    # display member count
    return str(member_count)


if __name__ == "__main__":
    app.run()
