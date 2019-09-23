# game by M81V4N

## INIT PART
import random as r

class Hero():
	def __init__(self, name, hp, dmg, pacify):
		self.name = name
		self.hp = hp
		self.dmg = dmg
		self.pacify = pacify
		self.spared = 0
		self.kills = 0
		self.alive = True


	def __str__(self):
		debug = ("\n"+self.name + "\n"+
			  str(self.hp)+"\n"+
			  str(self.dmg)+"\n"+
			  str(self.kills)+"\n"+
			  str(self.alive))
		return debug

	def turn(self):
		if self.alive == True:
			print("\nHERO " + self.name + ", " + str(self.hp) + " HP, " + str(self.dmg) + " DMG, " + str(self.pacify) + "% PACIFY")
			print("Choose your action: "
				  "\n1. CHECK"
				  "\n2. ATTACK"
				  "\n3. PACIFY")
			try:
				choice = input("NUMBER: ")

				if choice == 2:
					print("\nChoose enemy to attack:")
					if monster1.alive == True:
						print("(1): " + monster1.name)
					if monster2.alive == True:
						print("(2): " + monster2.name)
					if monster3.alive == True:
						print("(3): " + monster3.name)
					try:
						choice = input("NUMBER: ")
						if choice == 1:
							choice = monster1
						if choice == 2:
							choice = monster2
						if choice == 3:
							choice = monster3
						self.attack(choice)
					except (AttributeError, ValueError, NameError, SyntaxError):
						print("Not a correct number.")

				elif choice == 1:
					print("\nChoose enemy to check:")
					if monster1.alive == True:
						print("(1): " + monster1.name)
					if monster2.alive == True:
						print("(2): " + monster2.name)
					if monster3.alive == True:
						print("(3): " + monster3.name)
					try:
						choice = input("NUMBER: ")
						if choice == 1:
							choice = monster1
						if choice == 2:
							choice = monster2
						if choice == 3:
							choice = monster3
						print(choice)
					except (AttributeError, ValueError, NameError, SyntaxError):
						print("Not a correct number.")

				elif choice == 3:
					print("\nChoose enemy to pacify:")
					if monster1.alive == True:
						print("(1): " + monster1.name)
					if monster2.alive == True:
						print("(2): " + monster2.name)
					if monster3.alive == True:
						print("(3): " + monster3.name)
					try:
						choice = input("NUMBER: ")
						if choice == 1:
							choice = monster1
						if choice == 2:
							choice = monster2
						if choice == 3:
							choice = monster3
						if r.randint(1, 100) <= hero1.pacify:
							choice.alive = False
							print("\nMonster " + choice.name + " don't want to fight anymore.")
							self.spared += 1
						else:
							print("\n...But nothing happend.")
					except (AttributeError, ValueError, NameError, SyntaxError):
						print("Not a correct number.")

				else:
					print("\nNo such option.")

			except (AttributeError, ValueError, NameError, SyntaxError):
				print("Not a correct number.")



	def attack(self, target):
		if target.alive == False:
			print("\nThis monster is already dead.")
		if target.alive == True:
			target.hp -= self.dmg
			print("\nHero "+self.name + " attacked monster " + target.name + " and dealt " + str(self.dmg)+ " DMG.")
			print("Monster "+target.name + " have "+str(target.hp)+" HP left!")

			if target.alive == True:
				if target.hp <= 0:
					target.alive = False
					print("\nMonster " + target.name + " has been slaughtered.")
					self.kills += 1
					print("HERO "+self.name + " have " + str(self.kills) + " kills now.")

	def gameOver(self):
		
		allSpare = hero1.spared+hero2.spared+hero3.spared
		allKills = hero1.kills+hero2.kills+hero3.kills
		#NAPRAW RATIO BY BYLO W SKALI OD 1 DO 100
		if allKills == 0 or allSpare == 0:
			ratio = 0
		else:
			ratio = allSpare / allKills

		debug = ("""\n\n\n\n\n...Welp, I guess that's it.
			     The story of Great Albertus, Strong Brigitta and Mighty Christopher is over.

			     During your journey you murdered """+str(hero1.kills+hero2.kills+hero3.kills)+""" people.
			     However, you saved """+str(hero1.spared+hero2.spared+hero3.spared)+""" life beings.
			  
			     Your Humanity Ratio equals """+ str(ratio)+".")
			     #satyryczny tekst w zaleznosci od wyskokosci ratio

		debug += ("\nYou made it to "+str(day)+" day.")

		print(debug)
		
		raw_input("\nPress ENTER to end all of this...")
		exit("game by M81V4N")


class Monster():
	def __init__(self):
		self.name = r.choice(names)
		self.hp = r.randint(2,20)
		self.dmg = r.randint(1,10)
		self.alive = True

	def __str__(self):
		debug = "\nMONSTER "+self.name+", "+str(self.hp)+" HP, "+str(self.dmg)+" DMG"
		return debug

	def turn(self):
		if self.alive == True:
			while True:
				choice = r.randint(1, 3)
				if choice == 1:
					if hero1.alive == True:
						hero1.hp -= self.dmg
						if hero1.hp <= 0:
							hero1.alive = False
							print("HERO " + hero1.name + " got killed by MONSTER " + self.name + "!")
						else:
							print("HERO " + hero1.name + " got attacked by MONSTER " + self.name + " and now have " + str(hero1.hp) + " HP.")
						break
				if choice == 2:
					if hero2.alive == True:
						hero2.hp -= self.dmg
						if hero2.hp <= 0:
							hero2.alive = False
							print("HERO " + hero2.name + " got killed by MONSTER " + self.name + "!")
						else:
							print("HERO " + hero2.name + " got attacked by MONSTER " + self.name + " and now have " + str(hero2.hp) + " HP.")
						break
				if choice == 3:
					if hero3.alive == True:
						hero3.hp -= self.dmg
						if hero3.hp <= 0:
							hero3.alive = False
							print("HERO " + hero3.name + " got killed by MONSTER " + self.name + "!")
						else:
							print("HERO " + hero3.name + " got attacked by MONSTER " + self.name + " and now have " + str(hero3.hp) + " HP.")
						break

def battle():
	while (hero1.alive == True or hero2.alive == True or hero3.alive == True) == True and (monster1.alive == True or monster2.alive == True or monster3.alive == True) == True:

		#heros
		hero1.turn()
		if (hero1.alive == False and hero2.alive == False and hero3.alive == False) == True or (monster1.alive == False and monster2.alive == False and monster3.alive == False) == True:
			break
		raw_input("\nPress ENTER to continue.")
		hero2.turn()
		if (hero1.alive == False and hero2.alive == False and hero3.alive == False) == True or (monster1.alive == False and monster2.alive == False and monster3.alive == False) == True:
			break
		raw_input("\nPress ENTER to continue.")
		hero3.turn()
		if (hero1.alive == False and hero2.alive == False and hero3.alive == False) == True or (monster1.alive == False and monster2.alive == False and monster3.alive == False) == True:
			break
		raw_input("\nPress ENTER to begin MONSTERS turn.\n\n")
		##
		#monsters
		monster1.turn()
		monster2.turn()
		monster3.turn()
		raw_input("\nPress ENTER to begin HEROES turn.")

def event():
	done = False
	while done == False:
		choice = r.randint(1,1)
		if choice == 1:
			if hero1.alive == False:
				hero1.alive = True
				hero1.hp = 50
				print("\nAfter fight, when you just wanted to bury "+ hero1.name+", he just woke up.")
				done = True
				break
			elif hero2.alive == False:
				hero2.alive = True
				hero2.hp = 50
				print("\nSurprisngly, "+hero2.name+" is ready to fight once again!")
				done = True
				break
			elif hero3.alive == False:
				hero3.alive = True
				hero3.hp = 50
				print("\nLuckily you meet doctor Ivan, that revived " + hero3.name + ".")
				break
			else:
				print("\nYou rested a while, and you are ready to fight again!")
				break

		if choice == 2:
			print("items are work in progress")
			break

		if choice == 3:
			print("cos")
			break

		if choice == 4:
			print('xd')
			break

names = ("Dummy","Groom","Volt-A-Mort","The Bad Guy","Rat","Senegal")

items = {"Bandage":10,"PrayE":20,"L-Hero":50}
eq = ["Bandage","Bandage","Bandage","PrayE","PrayE"]

day = 1

hero1 = Hero("Albertus", 100, 25, 45)
hero2 = Hero("Brigitta", 120, 15, 60)
hero3 = Hero("Christopher", 80, 17, 90)


## GAME PART

#



while True:

	monster1 = Monster()
	monster2 = Monster()
	monster3 = Monster()
	print("\n\nD A Y  "+str(day))
	battle()

	if (hero1.alive == True and hero2.alive == True and hero3.alive == True) == False:
		hero1.gameOver()
	
	elif (monster1.alive == True and monster2.alive == True and monster3.alive == True) == False:
		raw_input("Monsters are defeated! Press ENTER to end fight!")
		
		event()

		day += 1
		print("\n\nDay finished!")
		raw_input("\nPress ENTER to begin new day.")

	else:
		raw_input("Weird error occurred... Press ENTER to see what happens next...")
