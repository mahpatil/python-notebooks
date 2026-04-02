# Overview
Websocket sample using python

# Usage

```
initialize virutal env


cd websockets
python server.py
python client.py agent-001
python client.py agent-001

```

# Server output
🌐 Server started on ws://localhost:8765
✅ Agent connected: branch-123:agent-001
🚀 Sent job to branch-123:agent-001
✅ Agent connected: branch-123:agent-002
🚀 Sent job to branch-123:agent-002

# Client output
🔐 Auth response: {"status": "connected"}
🖨️ Received job: {'type': 'payment', 'jobId': 'job-branch-123:agent-001', 'content': 'Payment for John Doe'}
➡️ Payment: Payment for John Doe