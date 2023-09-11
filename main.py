import speech_recognition as sr

def perintah():
    dengar = sr.Recognizer()
    with sr.Microphone() as source:
        print('==============')
        print('Siap mendengarkan Kamu...')
        suara = dengar.listen(source, phrase_time_limit=5)
        try:
                print('==============')
                print('Pesan diterima!')
                print('==============')
                print('Tunggu sebentar ya...')
                listening = dengar.recognize_google(suara, language='id-ID')
                print(listening)

        except:
                pass
        return listening
def run_alicia():
    Layanan = perintah()
    print(Layanan)
run_alicia()