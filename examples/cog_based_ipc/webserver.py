from quart import Quart
from nextcord.ext import ipc


app = Quart(__name__)
ipc_client = ipc.Client(
    secret_key="my_secret_key"
)  # secret_key must be the same as your server


@app.route("/")
async def index():
    member_count = await ipc_client.request(
        "member_count", guild_id=500525882226769931  # TODO Remove
    )  # get the member count of server with ID 12345678

    return str(member_count)  # display member count


if __name__ == "__main__":
    app.run()
