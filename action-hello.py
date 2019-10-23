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

#OK
    def Annee_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	annee = '{}'.format(intent_message.slots.annee.first().value)
	if annee == "1997":
	  say = u"D'après ce que m'ont raconté de vieilles trophistes, 1997 est l'année de naissance du 4L Trophy. J'ai entendu dire qu'elles n'étaient que 3 à concourir cette année là"
	elif annee == "quand":
	  say = u"D'après ce que m'ont raconté de vieilles trophistes, 1997 est l'année de naissance du 4L Trophy. J'ai entendu dire qu'elles n'étaient que 3 à concourir cette année la"
	elif annee == "date de naissance":
	  say = u"D'après ce que m'ont raconté de vieilles trophistes, 1997 est l'année de naissance du 4L Trophy. J'ai entendu dire qu'elles n'étaient que 3 à concourir cette année la"
	elif annee == "2001":
	  say = u"2001, c'est l'année qui marque l'essort du rodetrip.  L'école supérieure de commerce de Reines.  aide à l'organisation du raid et permet ainsi son développement."
	elif annee == "commence":
	  say = u"2001, c'est l'année qui marque l'essort du rodetrip. L'école supérieure de commerce de Rennes aide à l'organisation du raid et permet ainsi son développement."
	elif annee == "histoire":
	  say = u"2001, c'est l'année qui marque l'essort du rodetrip. L'école supérieure de commerce de Rennes aide à l'organisation du raid et permet ainsi son développement."
	elif annee == "2005":
	  say = u"En 2005, le raid compte pas moins de 460 équipages. Cela commence à en faire du monde !"
	elif annee == "2008":
	  say = u"Cette année-la, j'étirais mes suspensions fatiguées, tandis que mille.  4L s'affrontaient dans le désert marocain"
	elif annee == "2020":
	  say = u"Aujourd'hui, en 2020, c'est pas loin de 1500 voitures qui se retrouvent à participer au 4L Trophy. La course a 23 ans"
	else:
	  say = u"Je n'ai pas d'information sur cette date"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Annee")

#OK
    def Climat_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	climat = '{}'.format(intent_message.slots.climat.first().value)
	if climat == "aride":
	  say = u"Ouais, comme la région de marakech !"
	elif (climat == "chaud" or climat == "climat"):
	  say = u"Au Maroc, les étés sont chauds et secs, surtout lorsque souffle le sirocco brulant ou le chergui, vent d'été venant du Sahara. Mais les hivers sont froids et pluvieux avec gel et neige. C'est fou !"
	elif climat == "meteo":
	  say = u"Au Maroc, les étés sont chauds et secs, surtout lorsque souffle le sirocco brulant ou le chergui, vent d'été venant du Sahara. Mais les hivers sont froids et pluvieux avec gel et neige. C'est fou !"
	else:
	  say = u"Je ne pige rien"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Climat")

#OK
    def Paysage_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	paysage = '{}'.format(intent_message.slots.paysage.first().value)
	if (paysage == "oasis" or paysage == "plateaux" or paysage == "plaines" or paysage == "montagnes" or paysage == "paysage"):
	  say = u"Le Maroc est un pays avec une très grande diversité de paysages : montagnes, désert, plaines, plateaux, oazisse et pleins d'autres choses encore !"
	else:
	  say = u"Je ne pige rien"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Paysage")


    def Personnalite_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        personnalite = '{}'.format(intent_message.slots.personnalite.first().value)
        if (personnalite == "souple" or personnalite == "souplesse"):
          say = u"Clothilde a une conduite très souple. Merci encore !"
        elif (personnalite == "conduisez" or personnalite == "conducteurs" or personnalite == "conducteur"):
          say = u"En vrai c'est moi qui conduit le plus souvent, mais ne leur dites pas, c'est un secret"
        elif (personnalite == "vite" or personnalite == "vitesse"):
          say = u"Hadrien se moque vraissemblablement de mon vieil age. Il faut cesser d'écraser l'accelerateur jeune homme"
        elif (personnalite == "dort" or personnalite == "dormeur" or personnalite == "sendort"):
          say = u"Je vous présente Hadrien, le mec s'endort dès qu'il s'assied côté passager"
        elif (personnalite == "lambiance" or personnalite == "ambiance"):
          say = u"L'ambianceur de notre équipage c'est surement l'enceinte stéréo. Je dis ça, je ne dis rien"
        elif personnalite == "ambiancez":
          say = u"La plupart du temps j'ambiance tout le monde avec mon klaxon"
        elif (personnalite == "lent" or personnalite == "pas vite" or personnalite == "doucement" or qui == "lentement"):
          say = u"Pour le coup, je ne suis pas de toute jeunesse. Donc on ira à mon rythme OK ?"
        elif (personnalite == "raleur" or personnalite == "rale" or personnalite == "ralent" or personnalite == "raleuse"):
          say = u"Who! Who! Je ne veux pas de problème. Il me reste de la route à faire"
        else:
          say = u"Je ne comprends rien"
        hermes.publish_start_session_notification(intent_message.site_id, say, "Personnalite")


    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
    	if coming_intent == 'equisables:Annee':
	    self.Annee_callback(hermes, intent_message)
    	elif coming_intent == 'equisables:Paysage':
	    self.Paysage_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Climat':
	    self.Climat_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Personnalite':
	    self.Personnalite_callback(hermes, intent_mesage)


    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Hello()
