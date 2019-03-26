##File kelas3lib.py##
class kelas3lib:
	def __init__(self, NPM):
		self.NPM = NPM
	def nomorsatu(self):	
		NPM = int(self.NPM)
		char = "#"
		if NPM%3==0:
			char = "*"
		if NPM%3==1:
			char = "#"
		if NPM%3==2:
			char = "+"
		line = []
		line.append(" ##         ##      ########     ##    ##       #####       #######     ########")
		line.append("####       ####      ##    ##    ##    ##      ##   ##     ##     ##    ##      ")
		line.append("  ##         ##          ##      ##    ##     ##     ##           ##    ##      ")
		line.append("  ##         ##         ##       ##    ##     ##     ##     #######     ####### ")
		line.append("  ##         ##        ##        #########    ##     ##           ##          ##")
		line.append("  ##         ##        ##              ##      ##   ##     ##     ##    ##    ##")
		line.append("######     ######      ##              ##       #####       #######      ###### ")
		a=0
		for x in line:
			print(line[a].replace("#", char))
			a+=1
		return

	def nomordua(self):
		print("Input : "+self.NPM)
		x=1
		print("Output : ")
		while x <= 87:
			x+=1
			print("Halo, "+self.NPM+" apa kabar?")

	def nomortiga(self):
		print("Input : "+self.NPM)	
		jumlah = len(self.NPM)
		a = int(self.NPM[jumlah-3])
		b = int(self.NPM[jumlah-2])
		c = int(self.NPM[jumlah-1])
		x=1
		while x <= (a+b+c):
			print("Output : "+self.NPM[jumlah-3:])
			x+=1

	def nomorempat(self):
		print("Input : "+self.NPM)
		jumlah = len(self.NPM)
		print("Output : ")
		print("Halo, "+self.NPM[jumlah-3]+" apa kabar?")

	def nomorlima(self):		
		NPM = list(self.NPM)
		for x in NPM:
			print(x)
		return

	def nomorenam(self):
		NPM = list(self.NPM)
		jum = 0
		for x in NPM:
			jum+=int(x)
		print("Hasil : "+str(jum))
		return

	def nomortujuh(self):
		NPM = list(self.NPM)
		jum = 1
		for x in NPM:
			jum*=int(x)
		print("Hasil : "+str(jum))
		return

	def nomordelapan(self):
		NPM = list(self.NPM)
		for x in NPM:
			if int(x)!=0:
				if int(x)%2==0:
					print(x, end="")
		return

	def nomorsembilan(self):
		NPM = list(self.NPM)
		for x in NPM:
			if int(x)!=0:
				if int(x)%2==1:
					print(x, end = "")
		return

	def nomorsepuluh(self):
		NPM = list(self.NPM)
		for x in NPM:
			if int(x)!=0:
				i = 1
				bil = 0
				while i <= int(x):
					if int(x)%i==0:
						bil+=1
					i+=1
				if bil == 2:
					print(x)
		return