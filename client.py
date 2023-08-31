#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect

def Client():
    with connect("ws://localhost:7127") as websocket:
        websocket.send("Hello This is Wasim!")
        message = websocket.recv()
        print(f"Received: {message}")
        msg2 = websocket.recv()
        

Client()