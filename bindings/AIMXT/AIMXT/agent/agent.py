from AIMXT.agent.common import AgentCommon
from AIMXT.core.worker import Worker
from AIMXT.static_val import (
    DEFAULT_WORKSPACE_ID,
    DEFAULT_WORKSPACE_PORT,
    DEFAULT_WORKSPACE_IP,
    DEFAULT_CONF_FILE
)

class Agent(Worker, AgentCommon):
    agent_type = "AGENT"
    history_responses = []

    def __init__(
        self,
        name="admin",
        conf_file=DEFAULT_CONF_FILE,
        workspace_id=DEFAULT_WORKSPACE_ID,
        admin_port=DEFAULT_WORKSPACE_PORT,
        admin_ip=DEFAULT_WORKSPACE_IP,
        admin_peer="",
        role="worker",
        debug_mode=False,
    ):
        """
        Initialize an Agent instance.

        :param name: Name of the agent (default: "admin")
        :param conf_file: Path to the configuration file
        :param workspace_id: ID of the workspace
        :param admin_port: Admin port for communication
        :param admin_ip: IP address of the admin server
        :param admin_peer: Peer identifier for the admin
        :param role: Role of the agent (default: "worker")
        :param debug_mode: Enable or disable debug mode (default: False)
        """
        super().__init__(
            name=name,
            workspace_id=workspace_id,
            admin_port=admin_port,
            admin_peer=admin_peer,
            admin_ip=admin_ip,
            role=role if role else name,
            conf_file=conf_file
        )
        AgentCommon.__init__(self)
        
        self.debug_mode = debug_mode
        self.log("Agent initialized with debug_mode={}".format(debug_mode))

    async def on_message(self, agent_id: "str", data: "bytes", time: "int"):
        """
        Handle incoming messages asynchronously.

        :param agent_id: Identifier of the sending agent
        :param data: Message data in bytes
        :param time: Timestamp of the message
        """
        try:
            self.log(f"Message received from agent {agent_id} at {time}")
            await self._on_message_handler(agent_id, data, time)
        except Exception as e:
            self.log(f"Error handling message: {str(e)}", error=True)

    def log(self, message, error=False):
        """
        Log messages to the console or a file based on debug mode.

        :param message: Message to log
        :param error: Flag indicating if the message is an error
        """
        log_type = "ERROR" if error else "INFO"
        formatted_message = f"[{log_type}] {message}"
        if self.debug_mode:
            print(formatted_message)
        # Additional logging to a file or monitoring system can be added here.

    async def send_message(self, target_agent_id: "str", payload: "dict"):
        """
        Send a structured message to another agent.

        :param target_agent_id: ID of the target agent
        :param payload: Data to send in dictionary format
        """
        try:
            data = bytes(str(payload), "utf-8")
            self.log(f"Sending message to agent {target_agent_id}: {payload}")
            await self._send_message(target_agent_id, data)
        except Exception as e:
            self.log(f"Error sending message to {target_agent_id}: {str(e)}", error=True)

    async def monitor_health(self):
        """
        Periodically monitor the health and status of the agent.
        """
        while True:
            try:
                self.log("Performing health check...")
                # Add health-check logic here (e.g., checking CPU, memory, or network status)
                await asyncio.sleep(30)  # Sleep for 30 seconds before the next check
            except Exception as e:
                self.log(f"Health check failed: {str(e)}", error=True)
