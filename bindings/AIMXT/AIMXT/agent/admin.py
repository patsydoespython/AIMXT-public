from loguru import logger

from .common import AgentCommon
from AIMXT.AIMXT import AgentDetail
from AIMXT.core.admin import Admin


class CoreAdmin(Admin, AgentCommon):
    def __init__(self, name, port, workers=None, server_mode=False):
        """
        Initialize the CoreAdmin class.

        :param name: Name of the admin instance
        :param port: Port to bind the admin instance
        :param workers: List of workers (default is an empty list)
        :param server_mode: Boolean indicating whether server mode is enabled
        """
        if workers is None:
            workers = []

        self.__server_mode = server_mode
        self.__workers = workers
        self.__connected_agents = []

        super().__init__(name, port)
        AgentCommon.__init__(self)

        logger.debug(f"CoreAdmin initialized with name: {name}, port: {port}, server_mode: {server_mode}")

    async def run(self, inputs: bytes):
        """
        Run the admin logic. Placeholder for implementation.

        :param inputs: Input data in bytes
        """
        try:
            logger.info(f"Admin on_run triggered. ID: {self.details().id}, Inputs: {inputs}")
            # Placeholder for actual logic
        except Exception as e:
            logger.error(f"Error during run execution: {e}")

    async def on_agent_connected(self, topic: str, agent: AgentDetail):
        """
        Handle agent connection events.

        :param topic: Topic of the connection event
        :param agent: AgentDetail object representing the connected agent
        """
        try:
            self.__connected_agents.append(agent)
            logger.info(f"Agent connected: {agent.id} on topic: {topic}. Total agents: {len(self.__connected_agents)}")
        except Exception as e:
            logger.error(f"Error while handling agent connection: {e}")

    async def on_message(self, agent_id: str, data: bytes, time: int):
        """
        Handle incoming messages from agents.

        :param agent_id: ID of the agent sending the message
        :param data: Message payload in bytes
        :param time: Timestamp of the message
        """
        try:
            logger.debug(f"Message received from agent {agent_id} at {time}. Data size: {len(data)} bytes")
            await self._on_message_handler(agent_id, data, time)
        except Exception as e:
            logger.error(f"Error processing message from agent {agent_id}: {e}")

    def get_connected_agents(self):
        """
        Retrieve the list of connected agents.

        :return: List of connected agents
        """
        return self.__connected_agents

    def is_server_mode(self):
        """
        Check if server mode is enabled.

        :return: Boolean indicating server mode status
        """
        return self.__server_mode

    def add_worker(self, worker):
        """
        Add a worker to the admin.

        :param worker: Worker instance to be added
        """
        if worker not in self.__workers:
            self.__workers.append(worker)
            logger.info(f"Worker added: {worker}. Total workers: {len(self.__workers)}")
        else:
            logger.warning(f"Worker {worker} is already present in the list.")

    def remove_worker(self, worker):
        """
        Remove a worker from the admin.

        :param worker: Worker instance to be removed
        """
        try:
            self.__workers.remove(worker)
            logger.info(f"Worker removed: {worker}. Remaining workers: {len(self.__workers)}")
        except ValueError:
            logger.warning(f"Worker {worker} not found in the list.")
