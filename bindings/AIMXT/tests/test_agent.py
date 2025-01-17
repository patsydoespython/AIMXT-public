from unittest import TestCase

from AIMXT.llm.types.agent import AgentDefinition
from AIMXT.llm.prompt import PromptMessage


class TestAgentDefinition(TestCase):
    def test_intro(self):
        definition = AgentDefinition(
            name="test",
            role="test-role",
            objective="test-objective",
            context="test-context",
        )
        self.assertEqual(definition.intro,
                         {"name": "test", "role": "test-role", "objective": "test-objective",
                          "context": "test-context"})
        prompt_msg = PromptMessage(path="prompts.agent")
        self.assertEqual(definition.prompt, prompt_msg.build(**{
            "name": "test",
            "role": "test-role",
            "objective": "test-objective",
            "context": "test-context",
        }))
