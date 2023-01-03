from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

botupmh = ChatBot('botiv1')

words = ['Me siento mal', 'Contamos con una enfermeria en el edificio LT1',
        'Necesito ayuda emocional', 'Puedes contar con tus orientadores, buscalo en tu edificio'
        'Tengo problemas psicologicos o sicologicos','La universidad cuenta con ayuda psicologica'
        '¿Dondé puedo encontral al psicólogo?', 'Para tener una cita puedes acceder al edificion UD1 y agendarla']

trainer = ListTrainer(botupmh)
trainer.train(words)

while True:
    petition = input("Usuario: ") #Aqui en lugar de un input puede tomar
                                  #una variable de js desde la pagina
    response = botupmh.get_response(petition) # Aqui aplica igualmente
    print("Bot: ", response)# Y aqui con un inner.html podriamos imprimir