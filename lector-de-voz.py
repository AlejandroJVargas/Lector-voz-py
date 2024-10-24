import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
engine.setProperty("rate", rate - 100)
engine.setProperty("voice", voices[0].id)


while True:
    texto = (
        input("Pon lo que quieras, cuando quieras salir, pon salir: ").lower().strip()
    )
    if texto == "salir":
        break
    engine.say(texto)
    engine.runAndWait()

print("Proceso terminado")
