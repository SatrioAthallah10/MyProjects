from tkinter import *
from deep_translator import GoogleTranslator
import speech_recognition as mulut

def terjemah():
    masukan = boxmasukan.get()
    if masukan.strip() != "":
        keluaran = GoogleTranslator(source='auto', target='en').translate(masukan)
        labelkeluaran.config(text=f"Translated text: {keluaran}")
    else:
        labelkeluaran.config(text="Teks tidak valid")

def inputsuara():
    suara = mulut.Recognizer()
    with mulut.Microphone() as source:
        labelkeluaran.config(text="Silahkan berbicara")
        wnd.update()
        try:
            audio = suara.listen(source, timeout=5)
            teks = suara.recognize_google(audio, language="id-ID")
            boxmasukan.delete(0, END)
            boxmasukan.insert(0, teks)
            terjemah()
        except mulut.WaitTimeoutError:
            labelkeluaran.config(text="Suara tidak terdeteksi")
        except mulut.UnknownValueError:
            labelkeluaran.config(text="Mohon ulangi lagi")
        except mulut.RequestError:
            labelkeluaran.config(text="Mohon cek koneksi anda sebelum mencoba lagi")

wnd = Tk()
wnd.title("Aplikasi Penerjemah Bahasa Indonesia - Inggris")
wnd.geometry("400x250")
wnd.resizable(False, False)

labelmasukan = Label(wnd, text="Ketik atau ucapkan kalimat yang ingin diterjemahkan:")
labelmasukan.pack(pady=10)

boxmasukan = Entry(wnd, width=50)
boxmasukan.pack()

tombolterjemah = Button(wnd, text="Terjemahkan", command=terjemah)
tombolterjemah.pack(pady=5)

tombolbicara = Button(wnd, text="Tekan tombol untuk bicara", command=inputsuara)
tombolbicara.pack(pady=5)

labelkeluaran = Label(wnd, text="Translated text: ", wraplength=350, justify="left")
labelkeluaran.pack(pady=10)

wnd.mainloop()
