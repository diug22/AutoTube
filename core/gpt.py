import requests
import json
import gpt4free
from gpt4free import Provider

class GPTTube:
    def __init__(self, like, propmpt):
        self.like = like
        self.prompt = propmpt
        self.message = ""
    
    def send_chat_message(self):
        response = gpt4free.Completion.create(Provider.You, prompt=self.message)
        return response

    def make_message(self, quantity, start, end) :
        self.message += "Escribe " + str(quantity) + " textos en formato csv de esta manera, "
        self.message += "en la primera columna de los archivos escribiras un mensaje del estilo " + self.like + " sobre " + self.prompt + "al principio de ese mensaje escribe" + start + " y al final " + end +" en la segunda columna escribe un posible titulo para un video que hable sobre ese tema, no muy largo"
        self.message += " quiero que solo respondas con el texto del csv sin cabeceras"
        


gpt = GPTTube("Imaginemos por un momento esto, Encuentras una puerta dimensional que te lleva a un mundo de fantasía lleno de criaturas mágicas y seres extraordinarios. Puedes quedarte allí el tiempo que desees, pero cada vez que atraviesas la puerta, pierdes un año de tu vida en el mundo real. ¿Explorarías este mundo mágico a pesar del costo? ¡Tú, qué harías?", "misterio")
gpt.make_message(10, "Imaginemos por un momento esto", "no olvides darle like y compartir para mas historias asi")
print(gpt.send_chat_message())
    