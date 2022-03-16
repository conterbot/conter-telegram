from telebot import types
import telebot
from ipcamara import ipcamara
from contador_vehiculos import contador_vehiculos
from datetime import datetime

def estado_trafico():
    umbral_med = 4
    umbral_alto = 10
    umbral_congestion = 20
    lista_de_valores = []
    promedio_fecha_hora = {}
    resultado_trafico = []
    while True:
        ipcamara()
        promedio_por_ciclo = contador_vehiculos() 

        lista_de_valores.append(promedio_por_ciclo)
        
        if len(lista_de_valores) == 4:
            
            promedio_por_ciclo = round(sum(lista_de_valores)/len(lista_de_valores))
            fecha_ahora = datetime.now()
            promedio_fecha_hora ['fecha_hora']= fecha_ahora
            promedio_fecha_hora ['promedio_hora'] = promedio_por_ciclo
            #print(promedio_por_ciclo)
            #print(lista_de_promedios)

            trafico_bajo = promedio_por_ciclo < umbral_med
            trafico_medio = umbral_med < promedio_por_ciclo< umbral_alto 
            trafico_alto = umbral_alto < promedio_por_ciclo < umbral_congestion
            trafico_congestionado =  promedio_por_ciclo > umbral_congestion

            el_trafico_es_bajo = trafico_bajo == True
            el_trafico_es_medio = trafico_medio == True
            el_trafico_es_alto = trafico_alto == True
            el_trafico_es_congestionado = trafico_congestionado == True

            if el_trafico_es_bajo:
                resultado = "Tráfico bajo"
            elif el_trafico_es_medio:
                resultado = "Tráfico medio"
            elif el_trafico_es_alto:
                resultado = "Tráfico alto"
            elif el_trafico_es_congestionado:
                resultado = "Tráfico congestionado"

            lista_de_valores = []
            resultado_trafico.append(resultado)
            print(resultado_trafico)
            return resultado_trafico


token= "5191407649:AAFMTmCMrcCLyxtv6gqC6tcrs4l71VE_308"
bot = telebot.TeleBot(token)
bot.delete_webhook() #No tocar

@bot.message_handler(commands=["ayuda"])
def inline(message):
    bot.send_message(message.chat.id, "Para utilizar Conter y obtener el estado del tráfico, sólo tenés que seleccionar la opción del lugar que necesitás saber dentro del chat, y te proporcionaremos la info en instantes! Estamos trabajando para llegar a más localidades próximamente 🤗")

@bot.message_handler(commands=["opensource"])
def inline(message):
    bot.send_message(message.chat.id, "https://github.com/conterbot/conter-telegram")

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    if c.data == 'opcion1':
        bot.send_message(c.message.chat.id, "Estoy analizando la calle, espera un momento...")
        bot.send_message(c.message.chat.id, estado_trafico())
    if c.data == 'opcion2':
        bot.send_message(c.message.chat.id, 'Estaremos aquí proximamente!')
    if c.data == 'opcion3':
        bot.send_message(c.message.chat.id, 'Tendremos más opciones dentro de poco!')
        '''key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Rca. Argentina y Mcal. Lopez", callback_data="opcion1")
        but_2 = types.InlineKeyboardButton(text="Venezuela y Mcal. Lopez", callback_data="opcion2")
        but_3 = types.InlineKeyboardButton(text="Otras localidades", callback_data="opcion3")
        key.add(but_1, but_2, but_3)
        bot.send_message(c.message.chat.id, 'Esto es una prueba', reply_markup=key)'''
@bot.message_handler(commands=["start"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Rca. Argentina y Mcal. Lopez", callback_data="opcion1")
    but_2 = types.InlineKeyboardButton(text="Venezuela y Mcal. Lopez", callback_data="opcion2")
    but_3 = types.InlineKeyboardButton(text="Otras localidades", callback_data="opcion3")
    key.add(but_1, but_2, but_3)
    bot.send_message(message.chat.id, "Hola! Soy ConterBot, un sistema de conteo y reporte del estado del tráfico en tiempo real. \n Elige una ubicacion para continuar", reply_markup=key)

bot.infinity_polling()
