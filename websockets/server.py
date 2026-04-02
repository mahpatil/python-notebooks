import asyncio
import websockets
import json

# In-memory "registry" of connected agents
CONNECTED_AGENTS = {}

# Fake token validation (replace with Auth0 validation later)
def validate_token(token):
    try:
        # For demo: token is just JSON string
        data = json.loads(token)
        return data  # contains tenant_id + agent_id
    except:
        return None

async def handler(websocket):
    try:
        # Expect first message to be auth
        auth_message = await websocket.recv()
        auth_data = json.loads(auth_message)

        token = auth_data.get("token")
        identity = validate_token(token)

        if not identity:
            await websocket.send(json.dumps({"error": "unauthorized"}))
            return

        tenant_id = identity["tenant_id"]
        agent_id = identity["agent_id"]

        key = f"{tenant_id}:{agent_id}"
        CONNECTED_AGENTS[key] = websocket

        print(f"✅ Agent connected: {key}")

        await websocket.send(json.dumps({"status": "connected"}))
        
        # For demo: trigger dispatch in background without blocking handler
        asyncio.create_task(dispatch(agent_id))

        # Keep connection alive
        async for message in websocket:
            print(f"📩 Received from {key}: {message}")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        # Cleanup
        for k, v in list(CONNECTED_AGENTS.items()):
            if v == websocket:
                del CONNECTED_AGENTS[k]
                print(f"🔌 Disconnected: {k}")

# Simulate dispatching a job after some time
async def dispatch(agent_id="branch-1"):
    await asyncio.sleep(5)  # wait for client to connect

    tenant_id = "branch-123"
    key = f"{tenant_id}:{agent_id}"

    ws = CONNECTED_AGENTS.get(key)
    if ws:
        job = {
            "type": "payment",
            "jobId": f"job-{key}",
            "content": "Payment for John Doe"
        }
        await ws.send(json.dumps(job))
        print(f"🚀 Sent job to {key}")
    else:
        print("⚠️ Agent not connected")

async def main():
    server = await websockets.serve(handler, "localhost", 8765)
    print("🌐 Server started on ws://localhost:8765")

    await asyncio.gather(
        server.wait_closed(),
    #     dispatch()
    )

asyncio.run(main())