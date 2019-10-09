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
	if (annee == "1997" or annee == "date de naissance" or annee == "quand"):
	  say = u"D'après ce que m'ont raconté de vieilles trophistes, 1997 est l'année de naissance du 4L Trophy. J'ai entendu dire qu'elles n'étaient que 3 à concourir cette année là"
	elif (annee == "2001" or annee == "commencé" or annee == "histoire"):
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


    def Climat_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	climat = '{}'.format(intent_message.slots.climat.first().value)
	if climat == "aride":
	  say = u"Ouais, comme la région de marakech !"
	elif climat == "chaud" or climat == "météo" or climat == "climat":
	  say = u"Au Maroc, les étés sont chauds et secs, surtout lorsque souffle le sirocco brulant ou le chergui, vent d'été venant du Sahara. Mais les hivers sont froids et pluvieux avec gel et neige. C'est fou !"
	else:
	  say = u"Je ne pige rien"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Climat")


    def Paysage_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	paysage = '{}'.format(intent_message.slots.paysage.first().value)
	if paysage == "oasis" or paysage == "plateaux" or paysage == "plaines" or paysage == "montagnes" or paysage == "paysage":
	  say = u"Le Maroc est un pays avec une très grande diversité de paysages : montagnes, désert, plaines, plateaux, oasis et pleins d'autres choses encore !"
	else:
	  say = u"Je ne pige rien"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Paysage")


    def Quoi_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	quoi = '{}'.format(intent_message.slots.quoi.first().value)
	if quoi == "4L Trophy":
	  say = u"C'est un rallye aid qui a 23 ans. Le but c'est de faire une course dans une 4L dans le désert marocain"
	elif quoi == "Hamada":
	  say = u "C'est le troisième type de désert présent au maroc. En gros c'est une étendue rocailleuse à perte de vue"
	elif quoi == "religion" or quoi == "musulmans":
	  say = u"Le peuple marocain est majoritairement de religion musulmane"
	elif quoi == "Reg":
	  say = u"C'est ce qui caractérise un désert de pierres"
	elif quoi == "4L Trophy":
	  say = u"C'est un rally aid qui a 23 ans. Le but c'est de faire une course dans une 4L dans le désert marocain"
	elif quoi == "l'école" or quoi == "master" or quoi == "études" or quoi == "étude":
	  say = u"Ils font un master en management des systèmes d'informations et du numérique"
	elif quoi == "motivé" or quoi == "motivation" or quoi == "motivés":
	  say = u"Notre première motivation, c'est d'apporter de la technologie aux enfants marocains"
	else:
	  say = u"qui quoi ? j'ai rien pigé"
        hermes.publish_start_session_notification(intent_message.site_id, say, "Quoi")


    def Qui_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	qui = '{}'.format(intent_message.slots.qui.first().value)
	if qui == "clothilde":
	  say = u"Clothilde a 22 ans et vit à Lyon. Elle est consultante S A P chez H R C Consulting aie ti, et fan de GOTE"
	elif qui == "hadrien":
	  say == u"Hadrien a 23 ans et il est de région parisienne. Il est chef de projet digital à Grand Vision, mais c'est surtout un déjanté de la clef à molette"
	elif qui == "h r c" or qui == "H R C Consulting" or qui == "entreprise française" or qui == "entreprise" or qui == "boite":
	  say = u"H R C Consulting est mon créateur. C'est une entreprise en conseil en organisation et en systèmes d'informations spécialisé sur S A P. Ils sont basés à Lyon, mais interviennent partout en France"
	elif qui == "equisables":
	  say = u"Equisables est une jeune association qui prône l'accès aux outils numériques. Ses membres sont vraiment cool"
	elif qui == "jean jacques rey":
	  say = u"Cet ex-cadre de la grande distribution est tout simplement le mec génial qui à inventé le 4L Trophy"
	elif qui == "créateur du 4L Trophy":
	  say = u"C'est jean jacques rey, cet ex-cadre de la grande distribution est tout simplement le mec génial qui a inventé le 4L Trophy"
	elif qui == "combien d'édition" or qui == "depuis quand" or qui == "quel age le rally aid" or qui == "quel age la course":
	  say = u"La course fête sa 23 ième année"
	elif qui == "à qui cette voiture" or qui == "à qui cette 4L" or qui == "à qui cette caisse" or qui == "vous appartient" or qui == "acheté la voiture" or qui == "acheté la 4L" or qui == "acheté la caisse" or qui == "t'appartiens à l'association" or qui == "quelle association" or qui == "quelle équipe" or qui == "cours avec qui" or qui == "t'appartiens à qui":
	  say = u"J'appartiens à l'association équisables depuis avril 2019"
	elif qui == "surnom" or qui == "ptit prénom" or qui == "ptit nom" or qui == "votre truc" or qui == "assistant vocal" or qui == "chatbot" or qui == "tu tappelles" or qui == "assistant vocal" or qui == "chatbot" or qui == "ton prénom" or qui == "ton nom":
	  say = u"Je m'appelle Snips, mais c'est titine pour les intimes"
	elif qui == "inventeur" or qui == "créer" or qui == "créé" or qui == "créateur" or qui == "qui t'as créé":
	  say = u"H R C Consulting est mon créateur. C'est ausi un des sponsors de équisables"
	elif qui == "composé de quoi" or qui == "technologie" or qui "composé comment" or qui == "marche comment" or qui == "technologies":
	  say = u"Je suis l'assemblage d'un raspberryPI, de snips mais aussi de capteurs. Pour t'entendre j'ai aussi des micros"
	elif qui == "pilote":
	  say = u"Impossible à dire, je ne veux pas de problème"
	elif qui == "passager":
	  say = u"Il n'y a pas de passager, mais que des pilotes"
	elif qui == "mécanique" or qui == "mécano":
	  say = u"On a le chef mécano, c'est Hadrien. Sa doctrine : tant que ça tiens, alors ça passe"
	else:
	  say = u"qui quoi ? j'ai rien pigé"
        hermes.publish_start_session_notification(intent_message.site_id, say, "Qui")


    def Pub_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	pub = '{}'.format(intent_message.slots.pub.first().value)
	if pub == "buzz":
	  say = u"J'avoue que je suis principalement à l'origine du beuzz"
	elif pub == "linkedin":
	  say = u"Je me souviens de la publicité LinkedIn qu'a tourné Hadrien pour faire la promo de l'asso. J'étais rouge à cette triste époque"
	elif pub == "followers" or qui == "réputé":
	  say = u"Je sais, je sais, des centaines de personnes me suivent. Une voiture qui parle, c'est délirant"
	elif pub == "internet":
	  say = u"La resta des réseaux internet, c'est moi"
	elif pub == "je seche":
	  say = u"JE SECHE JE SECHE"
	elif pub == "logo":
	  say = u"Le logo est plutôt sympa. Il véhicule la bienveillance et l'esprit d'équipe"
	elif pub == "facebook" or qui == "réseaux":
	  say = u"N'hésitez pas à me suivre sur Facebook sous le nom de page : equisables tiret 4L Trophy 2020"
	elif pub == "vidéos" or qui == "films":
	  say = u"On a tourné quelques vidéos pas piqué des hannetons. Elles retracent le parcous d'équisables jusqu'à aujourd'hui"
	elif pub == "site" or qui == "site internet":
	  say = u"Rien de mieux qu'un site internet pour une bonne visibilité web. Découvrez equisables point F R, et faites un petit don en passant"
	elif pub == "insta" or qui == "instagram" or qui == "photos de la 4L" or qui == "photos de toi":
	  say = u"Sur insta, vous retrouverez des photos coquines de moi. On m'a décaissé d'après les rumeurs."
	else:
	  say = u"Je ne pige rien"
        hermes.publish_start_session_notification(intent_message.site_id, say, "Pub")


    def Solidarite_callback(self, hermes, intent_message):
	hermes.publish_end_session(intent_message.session_id, "")

	print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	solidarite = '{}'.format(intent_message.slots.solidarite.first().value)
	if solidarite == "don" or solidarite == "dons":
	  say = u"Chaque équipage doit ramener 30 kilos de denrées alimentaires pour la croix rouge. Mais aussi des fournitures scolaires et sportives pour les enfants du désert marocain. Ensuite ils peuvent faire d'autres dons s'ils le souhaitent"
	elif solidarite == "enfants" or solidarite == "récolter des dons matériels" or solidarite == "récolter des dons financiers" or solidarite == "l'objectif du 4L Trophy":
	  say = u"L'objectif du 4L Trophy c'est de récolter des dons financiers et matériels afin de construire des écoles en plein désert"
	elif solidarite == "croixrouge":
	  say = u"La croix rouge est chargée de collecter 10 kilos de denrées alimentaires par équipage, pour en distribuer aux familles pauvres en france"
	else:
	  say = u"Il faut rester solidaire"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Solidarite")


    def Equipage_callback(self, hermes, intent_message):
	hermes.publish_end_session(intent_message.session_id, "")

	print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	equipage = '{}'.format(intent_message.slots.equipage.first().value)
	if equipage == "régiment":
	  say = u"Ah non non ! On ne part pas au front. Je suis trop vieille pour ça"
	elif equipage == "smala":
	  say = u"Eh ! Nous ne sommes pas si nombreux. Juste moi, Clothilde et Hadrien. C'est tout"
	elif equipage == "tribu":
	  say = u"Eh ! Nous ne sommes pas si nombreux. Juste moi, Clothilde et Hadrien. C'est tout"
	elif equipage == "clan":
	  say = u"Eh ! On est pas dans clash of Clan. Il faut parler d'équipe"
	elif equipage == "écurie" or equipage == "numéro" or equipage == "numéro d'équipage":
	  say = u"Hadrien, Clothilde et moi même représentons l'écurie 235 du 4L Trophy"
	elif equipage == "équipage":
	  say = u"Hadrien, Clothilde et moi même représentons l'équipage 235"
	elif equipage == "individu" or equipage == "drôle dindividu" or equipage == "d'individu à bord" or equipage == "combien à bord":
	  say = u"Ils sont deux individus à mon bord : Clothilde et Hadrien"
	elif equipage == "bande":
	  say = u"Je te présente ma bande : Clothilde et Hadrien"
	elif equipage == "troupe":
	  say = u"Ma petite troupe c'est deux jeunes et une vieille"
	else:
	  say = u"Il faut rester une équipe"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Equipage")


    def Personnalite_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	personnalite = '{}'.format(intent_message.slots.personnalite.first().value)
	if personnalite == "souple" or personnalite == "souplesse":
	  say = u"Clothilde a une conduite très souple. Merci encore !"
	elif personnalite == "conduisez" or personnalite == "conducteurs" or personnalite == "conducteur":
	  say = u"En vrai c'est moi qui conduit le plus souvent, mais ne leur dites pas, c'est un secret"
	elif personnalite == "vite" or personnalite == "vitesse":
	  say = u"Hadrien se moque vraissemblablement de mon vieil age. Il faut cesser d'écraser l'accelerateur jeune homme"
	elif personnalite == "dort" or personnalite == "dormeur" or personnalite == "s'endort":
	  say = u"Je vous présente Hadrien, le mec s'endort dès qu'il s'assied côté passager"
	elif personnalite == "l'ambiance" or personnalite == "ambiance":
	  say = u"L'ambianceur de notre équipage c'est surement l'enceinte stéréo. Je dis ça, je ne dis rien"
	elif personnalite == "ambiancez":
	  say = u"La plupart du temps j'ambiance tout le monde avec mon klaxon"
	elif personnalite == "lent" or personnalite == "pas vite" or personnalite == "doucement" or qui == "lentement":
	  say = u"Pour le coup, je ne suis pas de toute jeunesse. Donc on ira à mon rythme OK ?"
	elif personnalite == "raleur" or personnalite == "rale" or personnalite == "ralent" or personnalite == "raleuse":
	  say = u"Who! Who! Je ne veux pas de problème. Il me reste de la route à faire"
	else:
	  say = u"Je ne comprends rien"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Personnalite")

    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
    	if coming_intent == 'equisables:Annee':
	    self.Annee_callback(hermes, intent_message)
    	elif coming_intent == 'equisables:Qui':
	    self.Qui_callback(hermes, intent_message)
    	elif coming_intent == 'equisables:Quoi':
	    self.Quoi_callback(hermes, intent_message)
    	elif coming_intent == 'equisables:Paysage':
	    self.Paysage_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Climat':
	    self.Climat_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Pub':
	    self.Pub_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Solidarite':
	    self.Solidarite_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Equipage':
	    self.Equipage_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Personnalite':
	    self.Personnalite_callback(hermes, intent_message)


    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Hello()
