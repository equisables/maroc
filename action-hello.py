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
    """Class used to wrap action code with mqtt connection

        Please change the name refering to your application
    """

    def __init__(self):
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        self.start_blocking()

    def Coucou_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        say = ["Salut gros", "Wesh bien ?", "Bonjour l'ami", "Salut pelo", "Wesh, tranquil ou quoi ?", "Hey cousin, ça se passe ?", "Coucou, la forme ?"]
        result_sentence = random.choice(say)
        hermes.publish_start_session_notification(intent_message.site_id, result_sentence, "Coucou")

    def Qui_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	qui = '{}'.format(intent_message.slots.annee.first().value)
	if qui == "clothilde":
	  say = u"Clothilde a 22 ans et vit à Lyon. Elle est consultante S A P chez H R C Consulting aie ti, et fan de GOT"
	elif qui == "hadrien":
	  say == u"Hadrien a 23 ans et il est de région parisienne. Il est chef de projet digital à Grand Vision, mais c'est surtout un déjanté de la clef à molette"
	elif qui == "h r c":
	  say = u"H R C Consulting est mon créateur. C'est une entreprise en conseil en organisation et en systèmes d'informations spécialisé sur S A P. Ils sont basés à Lyon, mais interviennent partout en France"
	elif qui == "equisables":
	  say = u"Equisables est une jeune association qui prône l'accès aux outils numériques. Ses membres sont vraiment cool "
	elif qui == "jean jacques rey":
	  say = u"Cet ex-cade de la grande distribution est tout simplement le mec génial qui à inventer le 4L Trophy"
	elif qui == "créateur":
	  say = u"H R C Consulting est mon créateur. C'est aussi un des sponsors de equisables"
	elif qui == "tu":
	  say = u"Je m'appelle K R 4. Mais c'est titine pour les intimes"
	else:
	  say = u"qui quoi ? j'ai rien pigé"
        hermes.publish_start_session_notification(intent_message.site_id, say, "Qui")

    def Quoi_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	quoi = '{}'.format(intent_message.slots.annee.first().value)
	if quoi == "4L Trophy":
	  say = u"C'est un rallye aid qui a 23 ans. Le but c'est de faire une course dans une 4L dans le désert marocain"
	else:
	  say "qui quoi ? j'ai rien pigé"
        hermes.publish_start_session_notification(intent_message.site_id, say, "Coucou")


    def Annee_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	annee = '{}'.format(intent_message.slots.annee.first().value)
	if annee == "1997":
	  say = u"D'après ce que m'ont raconté de vieilles trophistes, 1997 est l'année de naissance du 4L Trophy. J'ai entendu dire qu'elles n'étaient que 3 à concourir cette année là"
	elif annee == "2001":
	  say = u"2001, c'est l'année qui marque l'essort du rodetrip. L'école supérieure de commerce de Rennes aide à l'organisation du raid et permet ainsi son développement."
	elif annee == "2005":
	  say = u"En 2005, le raid compte pas moins de 460 équipages. Cela commence à en faire du monde !"
	elif annee == "2008":
	  say = u"Cette année-la, j'étirais mes suspensions fatiguées, tandis que 1000 4L s'affrontaient dans le désert marocain"
	elif annee == "2020":
	  say = u"Aujourd'hui, en 2020, c'est pas loin de 1500 voitures qui se retrouvent à participer au 4L Trophy"
	else:
	  say = u"Je n'ai pas d'information sur cette date"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Annee")

    def Ville_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	ville = '{}'.format(intent_message.slots.annee.first().value)
	if ville == "":
	  say = u""
	elif annee == "":
	  say = u""
	else:
	  say = u"Je n'ai pas d'information sur cette ville"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Ville")


    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'equisables:Coucou':
            self.Coucou_callback(hermes, intent_message)
    	if coming_intent == 'equisables:Annee':
	    self.Annee_callback(hermes, intent_message)
    	if coming_intent == 'equisables:Qui':
	    self.Qui_callback(hermes, intent_message)
    	if coming_intent == 'equisables:Quoi':
	    self.Quoi_callback(hermes, intent_message)
    	if coming_intent == 'equisables:Ville':
	    self.Ville_callback(hermes, intent_message)

    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Hello()
