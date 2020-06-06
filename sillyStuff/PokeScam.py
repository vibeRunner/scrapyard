import keyboard 
import time as t
from pynput.keyboard import Key, Controller
kb = Controller()

t.sleep(3)

print('PokeScam by m81v4n')
print('3 seconds to prepare.')

def switchTabAndWait():
	kb.press(Key.alt_l)
	kb.press(Key.tab)
	t.sleep(0.25) # ile trzyma 
	kb.release(Key.alt_l)
	kb.release(Key.tab)
	t.sleep(0.75) # czas pomiedzy wiadomosciami

def write(text):
	for key in text:
		keyboard.write(key)
		t.sleep(0.1) # co ile wpisuje znak
	keyboard.write('\n')

def loop(endkey='ctrl'):
	while True:
		try:
			write('p!duel @void#3871\n') # osoba pingowana
			switchTabAndWait()
			write('p!accept\n')
			switchTabAndWait()
			for i in range(4): # ma być pazyste, ilość walczenia
				write('p!use 1\n')
				switchTabAndWait()

			if keyboard.is_pressed(endkey):
				print("%s Key pressed." % endkey)
				break
				

		except KeyboardInterrupt:
			print('\nDone Reading input. Keyboard Interupt.')
			break
		except Exception as e:
			break
loop()
