# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(FormAction):

#     def name(self) -> Text:
#         return "health_check_form"

#     @staticmethod
#     def required_slots(tracker: Tracker)->List[Text]:
#         """ A List of required slots that the form has to fill"""
#         print("required_slots(tracker: Tracker)")
#         return ["fever","flu","sesakNafas","sakitTenggorokan","batuk"]

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(template="utter_submit")

#         return []

class ValidateRestaurantForm(Action):
    def name(self) -> Text:
        return "health_check_form"

    # @staticmethod
    # def cuisine_db() -> List[Text]:
    #     """Database of supported cuisines"""

    #     return ["caribbean", "chinese", "french"]


    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict,
    ) -> List[EventType]:
        required_slots = ["fever","flu","sesakNafas","sakitTenggorokan","batuk"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return[SlotSet("requested_slot", slot_name)]

        return[SlotSet("requested_slot",None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_health_record", Fever=tracker.get_slot("fever"), Flu=tracker.get_slot("flu"), SesakNafas=tracker.get_slot("sesakNafas"), SakitTenggorokan=tracker.get_slot("sakitTenggorokan"), batuk=tracker.get_slot("batuk"))

class ActionHealthAssumption(Action):
    def name(self) -> Text:
        return "action_health_assumption"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) ->List[Dict[Text, Any]]:
        Fever=tracker.get_slot("fever")
        Flu=tracker.get_slot("flu")
        SesakNafas=tracker.get_slot("sesakNafas")
        SakitTenggorokan=tracker.get_slot("sakitTenggorokan")
        batuk=tracker.get_slot("batuk")

        x = 0
        
        if (Fever == "Iya"):
            x+=1
        if (Flu == "Iya"):
            x+=1
        if (SesakNafas == "Iya"):
            x+=1
        if (SakitTenggorokan == "Iya"):
            x+=1
        if (batuk == "Iya"):
            x+=1

        if x < 3:
            return[dispatcher.utter_message(template="utter_please_take_multivitamin")]
        else :
            return[dispatcher.utter_message(template="utter_please_go_to_doctor")]