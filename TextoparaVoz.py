from gtts import gTTS

def texto_para_voz(texto, audio):
    tts = gTTS(texto, lang='pt-br')

    tts.save(audio)

texto = """Onde fica a rua turusbigo, turusbango? No fuvioco da esquina."""

audio = "QueméNeymar.mp3"

texto_para_voz(texto, audio)
print(f"Audio salco como {audio}")