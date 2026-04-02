import asyncio
import websockets
import json, sys

# Fake JWT (replace with Auth0 token later)


async def run_agent(agent_id="branch-1"):
    uri = "ws://localhost:8765"

    TOKEN = json.dumps({
        "tenant_id": "branch-123",
        "agent_id": agent_id
    })
    async with websockets.connect(uri) as websocket:
        # Send auth message
        await websocket.send(json.dumps({
            "type": "auth",
            "token": TOKEN
        }))

        response = await websocket.recv()
        print(f"🔐 Auth response: {response}")

        # Listen for jobs
        async for message in websocket:
            data = json.loads(message)
            print(f"🖨️ Received job: {data}")

            if data.get("type") == "payment":
                print(f"➡️ Payment: {data['content']}")
            elif data.get("type") == "ship":
                print(f"➡️ Shipping: {data['content']}")

asyncio.run(run_agent(len(sys.argv) > 1 and sys.argv[1] or "branch-1"))