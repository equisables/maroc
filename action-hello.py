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
	elif annee == "lentement":
	  say = u"TEST"
	else:
	  say = u"Je n'ai pas d'information sur cette date"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Annee")


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


    def Paysage_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
	paysage = '{}'.format(intent_message.slots.paysage.first().value)
	if (paysage == "oasis" or paysage == "plateaux" or paysage == "plaines" or paysage == "montagnes" or paysage == "paysage"):
	  say = u"Le Maroc est un pays avec une très grande diversité de paysages : montagnes, désert, plaines, plateaux, oazisse et pleins d'autres choses encore !"
	else:
	  say = u"Je ne pige rien"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Paysage")


    def Trophy_callback(self, hermes, intent_message):
	hermes.publish_end_session(intent_message.session_id, "")

	print '[Received] intent : {}'.format(intent_message.intent.intent_name)
	trophy = '{}'.format(intent_message.slots.trophy.first().value)
        if trophy == "souple":
          say = u"Clothilde a une conduite très souple. Merci encore !"
        elif trophy == "souplesse":
          say = u"Clothilde a une conduite très souple. Merci encore !"
        elif trophy == "conduisez":
          say = u"En vrai c'est moi qui conduit le plus souvent, mais ne leur dites pas, c'est un secret"
        elif trophy == "conducteurs":
          say = u"En vrai c'est moi qui conduit le plus souvent, mais ne leur dites pas, c'est un secret"
        elif trophy == "conducteur":
          say = u"En vrai c'est moi qui conduit le plus souvent, mais ne leur dites pas, c'est un secret"
        elif trophy == "vite":
          say = u"Hadrien se moque vraissemblablement de mon vieil age. Il faut cesser d'écraser l'accelerateur jeune homme"
        elif trophy == "vitesse":
          say = u"Hadrien se moque vraissemblablement de mon vieil age. Il faut cesser d'écraser l'accelerateur jeune homme"
        elif trophy == "dort":
          say = u"Je vous présente Hadrien, le mec s'endort dès qu'il s'assied côté passager"
        elif trophy == "dormeur":
          say = u"Je vous présente Hadrien, le mec s'endort dès qu'il s'assied côté passager"
        elif trophy == "sendort":
          say = u"Je vous présente Hadrien, le mec s'endort dès qu'il s'assied côté passager"
        elif trophy == "lambiance":
          say = u"L'ambianceur de notre équipage c'est surement l'enceinte stéréo. Je dis ça, je ne dis rien"
        elif trophy == "ambiance":
          say = u"L'ambianceur de notre équipage c'est surement l'enceinte stéréo. Je dis ça, je ne dis rien"
        elif trophy == "ambiancez":
          say = u"La plupart du temps j'ambiance tout le monde avec mon klaxon"
        elif trophy == "lent":
          say = u"Pour le coup, je ne suis pas de toute jeunesse. Donc on ira à mon rythme OK ?"
        elif trophy == "pas vite":
          say = u"Pour le coup, je ne suis pas de toute jeunesse. Donc on ira à mon rythme OK ?"
        elif trophy == "doucement":
          say = u"Pour le coup, je ne suis pas de toute jeunesse. Donc on ira à mon rythme OK ?"
        elif trophy == "lentement":
          say = u"Pour le coup, je ne suis pas de toute jeunesse. Donc on ira à mon rythme OK ?"
        elif trophy == "raleur":
          say = u"Who! Who! Je ne veux pas de problème. Il me reste de la route à faire"
        elif trophy == "rale":
          say = u"Who! Who! Je ne veux pas de problème. Il me reste de la route à faire"
        elif trophy == "ralent":
          say = u"Who! Who! Je ne veux pas de problème. Il me reste de la route à faire"
        elif trophy == "raleuse":
          say = u"Who! Who! Je ne veux pas de problème. Il me reste de la route à faire"
        elif trophy == "4L Trophy":
          say = u"C'est un rallye raid qui a 23 ans. Le but c'est de faire une course dans une 4L dans le désert marocain"
        elif trophy == "Hamada":
          say = u"C'est le troisième type de désert présent au maroc. En gros c'est une étendue rocailleuse à perte de vue"
        elif trophy == "religion":
          say = u"Le peuple marocain est majoritairement de religion musulmane"
        elif trophy == "musulmans":
          say = u"Le peuple marocain est majoritairement de religion musulmane"
        elif trophy == "Reg":
          say = u"C'est ce qui caractérise un désert de pierres"
        elif trophy == "lecole":
          say = u"Ils font un master en management des systèmes d'informations et du numérique"
        elif trophy == "master":
          say = u"Ils font un master en management des systèmes d'informations et du numérique"
        elif trophy == "etudes":
          say = u"Ils font un master en management des systèmes d'informations et du numérique"
        elif trophy == "etude":
          say = u"Ils font un master en management des systèmes d'informations et du numérique"
        elif trophy == "motive":
          say = u"Notre première motivation, c'est d'apporter de la technologie aux enfants marocains"
        elif trophy == "motivation":
          say = u"Notre première motivation, c'est d'apporter de la technologie aux enfants marocains"
        elif trophy == "motives":
          say = u"Notre première motivation, c'est d'apporter de la technologie aux enfants marocains"
        elif trophy == "buzz":
          say = u"J'avoue que je suis principalement à l'origine du beuhzze"
        elif trophy == "linkedin":
          say = u"Je me souviens de la publicité line queu dine qu'a tourné Hadrien pour faire la promo de l'asso. J'étais rouge à cette triste époque"
        elif trophy == "followers":
          say = u"Je sais, je sais, des centaines de personnes me suivent. Une voiture qui parle, c'est délirant"
        elif trophy == "repute":
          say = u"Je sais, je sais, des centaines de personnes me suivent. Une voiture qui parle, c'est délirant"
        elif trophy == "internet":
          say = u"La reusta des réseaux internet, c'est moi"
        elif trophy == "je seche":
          say = u"JE SECHE JE SECHE"
        elif trophy == "logo":
          say = u"Le logo est plutôt sympa. Il véhicule la bienveillance et l'esprit d'équipe"
        elif trophy == "facebook":
          say = u"N'hésitez pas à me suivre sur fesse bouque sous le nom de page : et qui sable tiret 4L Trophy 2020"
        elif trophy == "reseaux":
          say = u"N'hésitez pas à me suivre sur fesse bouque sous le nom de page : et qui sable tiret 4L Trophy 2020"
        elif trophy == "videos":
          say = u"On a tourné quel que vidéos pas piqué des hannetons. Elles retracent le parcous d'équisables jusqu'à aujourd'hui"
        elif trophy == "films":
          say = u"On a tourné quel que vidéos pas piqué des hannetons. Elles retracent le parcous d'équisables jusqu'à aujourd'hui"
        elif trophy == "site":
          say = u"Rien de mieux qu'un site internet pour une bonne visibilité waibe. Découvrez et qui sable point F R, et faites un petit don en passant"
        elif trophy == "site internet":
          say = u"Rien de mieux qu'un site internet pour une bonne visibilité waibe. Découvrez et qui sable point F R, et faites un petit don en passant"
        elif trophy == "insta":
          say = u"Sur insta, vous retrouverez des photos coquines de moi. On m'a décaissé d'après les rumeurs."
        elif trophy == "instagram":
          say = u"Sur insta, vous retrouverez des photos coquines de moi. On m'a décaissé d'après les rumeurs."
        elif trophy == "photos de la 4L":
          say = u"Sur insta, vous retrouverez des photos coquines de moi. On m'a décaissé d'après les rumeurs."
        elif trophy == "photos de toi":
          say = u"Sur insta, vous retrouverez des photos coquines de moi. On m'a décaissé d'après les rumeurs."
        elif trophy == "don":
          say = u"Chaque équipage doit ramener 30 kilos de denrées alimentaires pour la croix rouge. Mais aussi des fournitures scolaires et sportives pour les enfants du désert marocain. Ensuite ils peuvent faire d'autres dons s'ils le souhaitent"
	elif trophy == "dons":
          say = u"Chaque équipage doit ramener 30 kilos de denrées alimentaires pour la croix rouge. Mais aussi des fournitures scolaires et sportives pour les enfants du désert marocain. Ensuite ils peuvent faire d'autres dons s'ils le souhaitent"
        elif trophy == "enfants":
          say = u"L'objectif du 4L Trophy c'est de récolter des dons financiers et matériels afin de construire des écoles en plein désert"
        elif trophy == "recolter des dons materiels":
          say = u"L'objectif du 4L Trophy c'est de récolter des dons financiers et matériels afin de construire des écoles en plein désert"
        elif trophy == "recolter des dons financiers":
          say = u"L'objectif du 4L Trophy c'est de récolter des dons financiers et matériels afin de construire des écoles en plein désert"
        elif trophy == "lobjectif du 4L Trophy":
          say = u"L'objectif du 4L Trophy c'est de récolter des dons financiers et matériels afin de construire des écoles en plein désert"
        elif trophy == "croixrouge":
          say = u"La croix rouge est chargée de collecter 10 kilos de denrées alimentaires par équipage, pour en distribuer aux familles pauvres en france"
        elif trophy == "regiment":
          say = u"Ah non non ! On ne part pas au front. Je suis trop vieille pour ça"
        elif trophy == "smala":
          say = u"Eh ! Nous ne sommes pas si nombreux. Juste moi, Clothilde et Hadrien. C'est tout"
        elif trophy == "tribu":
          say = u"Eh ! Nous ne sommes pas si nombreux. Juste moi, Clothilde et Hadrien. C'est tout"
        elif trophy == "clan":
          say = u"Eh ! On est pas dans clash of Clan. Il faut parler d'équipe"
        elif (trophy == "ecurie" or trophy == "numero" or trophy == "numero dequipage"):
          say = u"Hadrien, Clothilde et moi même représentons l'écurie 235 du 4L Trophy"
        elif trophy == "equipage":
          say = u"Hadrien, Clothilde et moi même représentons l'équipage 235"
        elif (trophy == "individu" or trophy == "drole dindividu" or trophy == "dindividu a bord" or trophy == "combien a bord"):
          say = u"Ils sont deux individus à mon bord : Clothilde et Hadrien"
        elif trophy == "bande":
          say = u"Je te présente ma bande : Clothilde et Hadrien"
        elif trophy == "troupe":
          say = u"Ma petite troupe c'est deux jeunes et une vieille"
#        elif trophy == "clothilde":
#          say = u"Clothilde a 22 ans et vit à Lyon. Elle est consultante S A P chez H R C Consulting aie ti, et fan de GOTE"
#        elif trophy == "hadrien":
#          say == u"Hadrien a 23 ans et il est de région parisienne. Il est chef de projet digital à Grand Vision, mais c'est surtout un déjanté de la clef à molette"
#        elif (trophy == "h r c" or trophy == "H R C Consulting" or trophy == "entreprise francaise" or trophy == "entreprise" or trophy == "boite"):
#          say = u"H R C Consulting est mon créateur. C'est une entreprise en conseil en organisation et en systèmes d'informations spécialisé sur S A P. Ils sont basés à Lyon, mais interviennent partout en France"
        elif trophy == "equisables":
          say = u"Equisables est une jeune association qui prône l'accès aux outils numériques. Ses membres sont vraiment cool"
        elif trophy == "jean jacques rey":
          say = u"Cet ex-cadre de la grande distribution est tout simplement le mec génial qui à inventé le 4L Trophy"
        elif trophy == "createur du 4L Trophy":
          say = u"C'est jean jacques rey, cet ex-cadre de la grande distribution est tout simplement le mec génial qui a inventé le 4L Trophy"
        elif (trophy == "combien dedition" or trophy == "depuis quand" or trophy == "quel age le rally raid" or trophy == "quel age la course"):
          say = u"La course fête sa 23 ième année"
        elif (trophy == "a qui cette voiture" or trophy == "a qui cette 4L" or trophy == "a qui cette caisse" or trophy == "vous appartient" or trophy == "achete la voiture" or trophy == "achete la 4L" or trophy == "achete la caisse" or trophy == "tappartiens a lassociation" or trophy == "quelle association" or trophy == "quelle équipe" or trophy == "cours avec qui" or trophy == "tappartiens a qui"):
          say = u"J'appartiens à l'association équisables depuis avril 2019"
#        elif (trophy == "surnom" or trophy == "ptit prenom" or trophy == "ptit nom" or trophy == "votre truc" or trophy == "assistant vocal" or trophy == "chatbot" or trophy == "tu tappelles" or trophy == "assistant vocal" or trophy == "chatbot" or trophy == "ton prenom" or trophy == "ton nom"):
#          say = u"Je m'appelle Snips, mais c'est titine pour les intimes"
#        elif (trophy == "inventeur" or trophy == "creer" or trophy == "cree" or trophy == "createur" or trophy == "qui tas cree"):
#          say = u"H R C Consulting est mon créateur. C'est ausi un des sponsors de équisables"
#        elif (trophy == "compose de quoi" or trophy == "technologie" or trophy "compose comment" or trophy == "marche comment" or trophy == "technologies"):
#          say = u"Je suis l'assemblage d'un raspberryPI, de snips mais aussi de capteurs. Pour t'entendre j'ai aussi des micros"
#        elif trophy == "pilote":
#          say = u"Impossible à dire, je ne veux pas de problème"
#        elif trophy == "passager":
#          say = u"Il n'y a pas de passager, mais que des pilotes"
#        elif (trophy == "mecanique" or trophy == "mecano"):
#          say = u"On a le chef mécano, c'est Hadrien. Sa doctrine : tant que ça tiens, alors ça passe"
        else:
          say = u"Je ne comprends rien"
	hermes.publish_start_session_notification(intent_message.site_id, say, "Trophy")


    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
    	if coming_intent == 'equisables:Annee':
	    self.Annee_callback(hermes, intent_message)
    	elif coming_intent == 'equisables:Paysage':
	    self.Paysage_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Climat':
	    self.Climat_callback(hermes, intent_message)
	elif coming_intent == 'equisables:Trophy':
	    self.Trophy_callback(hermes, intent_message)


    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Hello()
