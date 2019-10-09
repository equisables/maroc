#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import random
# import requests
# import HTMLParser

CONFIG_INI = "config.ini"

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Hello(object):

    def __init__(self):
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        self.start_blocking()


    def Annee_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	annee = '{}'.format(intent_message.slots.annee.first().value)
	if (annee == "1997" or annee == "quand"):
	  say = u"D'après ce que m'ont raconté de vieilles trophistes, 1997 est l'année de naissance du 4L Trophy. J'ai entendu dire qu'elles n'étaient que 3 à concourir cette année là"
	elif annee == "date de naissance":
	  say = u"D'après ce que m'ont raconté de vieilles trophistes, 1997 est l'année de naissance du 4L Trophy. J'ai entendu dire qu'elles n'étaient que 3 à concourir cette année la"
	elif (annee == "2001" or annee == u"commencé"):
	  say = u"2001, c'est l'année qui marque l'essort du rodetrip. L'école supérieure de commerce de Rennes aide à l'organisation du raid et permet ainsi son développement."
	elif annee == "histoire":
	  say = u"Le petit prince"
	elif annee == "2005":
	  say = u"En 2005, le raid compte pas moins de 460 équipages. Cela commence à en faire du monde !"
	elif annee == "2008":
	  say = u"Cette année-la, j'étirais mes suspensions fatiguées, tandis que 1000 4L s'affrontaient dans le désert marocain"
	elif annee == "2020":
	  say = u"Aujourd'hui, en 2020, c'est pas loin de 1500 voitures qui se retrouvent à participer au 4L Trophy"
	else:
	  say = u"Je n'ai pas d'information sur cette date"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Annee")


    def Climat_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	climat = '{}'.format(intent_message.slots.climat.first().value)
	if climat == "aride":
	  say = u"Ouais, comme la région de marakech !"
	elif (climat == "chaud" or climat == u"météo" or climat == "climat"):
	  say = u"Au Maroc, les étés sont chauds et secs, surtout lorsque souffle le sirocco brulant ou le chergui, vent d'été venant du Sahara. Mais les hivers sont froids et pluvieux avec gel et neige. C'est fou !"
	else:
	  say = u"Je ne pige rien"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Climat")


    def Paysage_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	paysage = '{}'.format(intent_message.slots.paysage.first().value)
	if (paysage == "oasis" or paysage == "plateaux" or paysage == "plaines" or paysage == "montagnes" or paysage == "paysage"):
	  say = u"Le Maroc est un pays avec une très grande diversité de paysages : montagnes, désert, plaines, plateaux, oasis et pleins d'autres choses encore !"
	else:
	  say = u"Je ne pige rien"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Paysage")


    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
    	if coming_intent == 'equisables:Annee':
	    self.Annee_callback(hermes, intent_message)
    	elif coming_intent == 'equisables:Paysage':
	    self.Paysage_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Climat':
	    self.Climat_callback(hermes, intent_message)


    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Hello()
