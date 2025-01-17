import asyncio
import pickle
from typing import Any, Optional

from AIMXT.AIMXT import AdminAgent, AdminAgentConfig, Processor, MessageHandler, EventHandler, AgentDetail
from AIMXT.AIMXT.AIMXT import uniffi_set_event_loop


class Admin(AdminAgent, Processor, MessageHandler, EventHandler):

    def __init__(self, name="admin", port=8888):
        self.return_response: Optional[Any] = None  # Explicitly specify type for clarity
        super().__init__(config=AdminAgentConfig(name=name, port=port), processor=self, on_message=self, on_event=self)

    async def run(self, inputs: bytes):
        # Placeholder for execution logic
        pass

    async def on_message(self, agent_id: str, data: bytes, time: int):
        # Handle incoming messages
        print(f"Message received from agent {agent_id} at {time}: {data}")
        pass

    def run_admin(self, inputs: bytes, workers):
        import asyncio

        try:
            # Try to get the running event loop
            event_loop = asyncio.get_running_loop()
        except RuntimeError:
            # No running event loop, create a new one
            event_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(event_loop)
            return event_loop.run_until_complete(self.arun_admin(inputs, workers))

        # If the loop is already running, schedule the coroutine in the running loop
        if event_loop.is_running():
            # Schedule the coroutine and wait for completion
            future = asyncio.ensure_future(self.arun_admin(inputs, workers), loop=event_loop)
            return event_loop.run_until_complete(future)
        else:
            # If no loop is running, run the coroutine with asyncio.run()
            return asyncio.run(self.arun_admin(inputs, workers))

    async def arun_admin(self, inputs: bytes, workers):
        uniffi_set_event_loop(asyncio.get_event_loop())
        await self.start(inputs, workers)
        return self.return_response

    async def execute_task(self, input: Any):
        # Execute specific tasks
        print(f"Executing task with input: {input}")
        pass

    async def on_agent_connected(self, topic: str, agent_id: AgentDetail):
        # Handle agent connection events
        print(f"Agent connected on topic '{topic}': {agent_id}")
        pass

    async def broadcast_data(self, message: Any):
        # Serialize and broadcast the data to all connected agents
        print(f"Broadcasting message: {message}")
        await self.broadcast(pickle.dumps(message))

    async def stop_admin(self):
        """Gracefully stop the Admin agent."""
        print("Stopping Admin agent...")
        await self.stop()
