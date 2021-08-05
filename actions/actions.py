# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SessionStarted, ActionExecuted, SlotSet, EventType, ActionExecutionRejected
from rasa_sdk.executor import CollectingDispatcher
import random
import logging

logger = logging.getLogger(__name__)

class ActionAppt(Action):

    def name(self) -> Text:
        return "action_appt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        appts = ["none", "single", "multiple"]
        returnEvents = []
        num_appts = appts[random.randint(0,2)]
        returnEvents.append(SlotSet("num_appts", num_appts))
        logger.debug(f"num_appts: {num_appts}")
        return returnEvents

