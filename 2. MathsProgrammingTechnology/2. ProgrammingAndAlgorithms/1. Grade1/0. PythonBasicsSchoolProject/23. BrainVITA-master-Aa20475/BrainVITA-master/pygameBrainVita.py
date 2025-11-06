import pygame
import math
import os
class hole:
	pos=[0,0]
	radius=0
	empty=False

	def __init__(self,rad):
		self.radius = rad

	def draw(self,screen,color,loc,rads):
		pygame.draw.ellipse(screen,color,[loc[0],loc[1],(rads),(rads)])




FILL = (116, 155, 219)
EMP= (169, 180, 198)
BG = (197, 234, 233)
SEL = (0, 41, 109)
GO = (34, 94, 46)


selected = False

main_menu = True


holestat=[]

for i in range(33):
	if i!=16:
		holestat.append(1)
	else:
		holestat.append(0)

def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")

	return os.path.join(base_path, relative_path)




def calc_rad(size,max):
	return (min(size[0],size[1]))/(max+max+3)

def generate_pos(size,max):
	l = [0,1,5,6]
	posarr = []
	for i in range(33):
		posarr.append([0,0])
	no=0
	radius = calc_rad(size,max)
	rg = (size[0]-((max+max-1)*radius))/2
	tg = (size[1]-((max+max-1)*radius))/2
	y =tg
	for i in range(7):
		if i in l:
			pos = [rg+4*radius,y]
			for j in range(3):
				posarr[no][0]=pos[0]
				posarr[no][1]=pos[1]
				pos[0]+=2*radius
				no+=1
		else:
			pos = [rg,y]
			for k in range(7):
					posarr[no][0]=pos[0]
					posarr[no][1]=pos[1]
					pos[0]+=2*radius
					no+=1
		y+=2*radius
	return posarr

def restart(holestat):
	for i in range(33):
		if i!=16:
			holestat[i]=1
		else:
			holestat[i]=0


def display_board(screen,holes,holepos,size,holestat,selected,prev_step,main_menu,pos):
	l = [0,1,5,6]
	y=110
	no=0
	if main_menu==False:
		if pos[0]>20 and pos[0]<20+calc_rad(size,7) and pos[1]>20 and pos[1]<20+calc_rad(size,7):
			screen.fill(EMP,rect=[20,20,calc_rad(size,7),calc_rad(size,7)])

		else:
			screen.fill(FILL,rect=[20,20,calc_rad(size,7),calc_rad(size,7)])

		for i in range(7):
			if i in l:
				for j in range(3):
					if holestat[no]==1:
						holes[no].draw(screen,FILL,holepos[no],calc_rad(size,7))
					elif holestat[no]==0:
						holes[no].draw(screen,EMP,holepos[no],calc_rad(size,7))
					no+=1
			else:
				for k in range(7):
					if holes[no].empty == False:	
						if holestat[no]==1:
							holes[no].draw(screen,FILL,holepos[no],calc_rad(size,7))
						elif holestat[no]==0:
							holes[no].draw(screen,EMP,holepos[no],calc_rad(size,7))
						no+=1
					else:
						if holestat[no]==1:
							holes[no].draw(screen,FILL,holepos[no],calc_rad(size,7))
						elif holestat[no]==0:
							holes[no].draw(screen,EMP,holepos[no],calc_rad(size,7))
						no+=1
			y+=120
		if selected==True:
			loc = pygame.mouse.get_pos()
			pygame.draw.ellipse(screen,SEL,[loc[0],loc[1],calc_rad(size,7),calc_rad(size,7)])
	else:
		screen.fill(FILL)
		font = pygame.font.SysFont('', 200, True, False)

		text = font.render("BrainVITA",True,SEL)
		screen.blit(text, [size[0]/2-(2.1*180), 240])

		if pos[0]>size[0]/2-(calc_rad(size,7)) and pos[0]<size[0]/2 and pos[1]>500 and pos[1]<500+calc_rad(size,7):
			screen.fill(EMP,rect=[size[0]/2-(calc_rad(size,7)),500,calc_rad(size,7),calc_rad(size,7)])
		else:
			screen.fill(SEL,rect=[size[0]/2-(calc_rad(size,7)),500,calc_rad(size,7),calc_rad(size,7)])


def distane(p1,p2):
	return math.sqrt(((p1[0]-p2[0])*(p1[0]-p2[0]))+((p1[1]-p2[1])*(p1[1]-p2[1])))

def nearest_search(point,array):
	best_point = None
	best_distance = None
	p_loc = None
	i=0
	for current in array:
		x= point[0]-current[0]
		y=point[1]-current[1]
		current_distance = math.sqrt((x*x)+(y*y))
		if best_distance is None or current_distance<best_distance:
			best_distance=current_distance
			best_point=current
			p_loc=i
		i+=1
	return best_point,best_distance,p_loc

def GAME_OVER(holestat,det):
	gg=[]
	for x in range(33):
		if holestat[x]==1:	
			for i in range(4):
			 	#True>>Possible #False>>Not Possible
				if det[x][i]!=None and det[det[x][i]][i]!=None:
					if (holestat[det[x][i]]==1 and holestat[det[det[x][i]][i]]==0):
						gg.append(True)
					else:
						gg.append(False)
		else:
			gg.append(False)			
	if len(set(gg)) == 1 and gg[0]==False and selected==False:
		return True
	else:
		return False

def close_detect(array,radius):
	neightbours = []
	for x in range(33):
		p=[]
		for i in [1,-1]:
			there=False
			n=(array[x][0]+(i*2*radius),array[x][1])
			bp,bd,pl=nearest_search(n,array)
			if bd<1:
				there=True
				p.append(pl)
			if there==False:
				p.append(None)
			there=False
			n=(array[x][0],array[x][1]+(i*2*radius))
			bp,bd,pl=nearest_search(n,array)
			if bd<1:
				there=True
				p.append(pl)
			if there==False:
				p.append(None)

		neightbours.append(p)
	return neightbours

pygame.init()
pygame.mixer.pre_init(44100,16,2,4096)


size = [1000, 1000]

screen = pygame.display.set_mode(size)

pygame.display.set_caption('BrainVITA')
 
clock = pygame.time.Clock()

done = False

mouse_track = False
holes = []
for i in range(33):
	obj = hole(60)
	if i==16:
		obj.empty=True
	else:
		obj.empty=False
	holes.append(obj)
holepos=generate_pos(size,7)

det = close_detect(holepos,calc_rad(size,7))

prev_step = None

#Loading and playing BGM
pygame.mixer.music.load(resource_path("BrainVita.wav"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


while not done:
	pos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			if GAME_OVER(holestat,det)==False and main_menu==False:
				if selected==False:
					if pos[0]>20 and pos[0]<20+calc_rad(size,7) and pos[1]>20 and pos[1]<20+calc_rad(size,7):
						main_menu=True
						restart(holestat)
					best_point,best_distance,p_loc = nearest_search(pos,holepos)
					if best_distance<calc_rad(size,7) and holestat[p_loc]!=0:	
						holestat[p_loc]=0
						selected = True
				else:
					selected=False
					there=False
					pos = pygame.mouse.get_pos()
					u=0
					bp,bd,p_new = nearest_search(pos,holepos)
					if bd<calc_rad(size,7):
						for i in range(4):
							if det[p_loc][i]!=None:
								for j in range(4):
									if det[det[p_loc][i]][j] == p_new and i==j and holestat[det[p_loc][i]]!=0 and holestat[p_new]!=1:
										there = True
										u=i
						if there == True:
							holestat[p_loc]=0
							holestat[det[p_loc][u]]=0
							holestat[p_new] = 1
							prev_step = holestat

							reset = True
						else:
							holestat[p_loc]=1
					else:
						holestat[p_loc]=1
			if main_menu==True:
				if pos[0]>size[0]/2-(calc_rad(size,7)) and pos[0]<size[0]/2 and pos[1]>500 and pos[1]<500+calc_rad(size,7):
					main_menu=False
			if GAME_OVER(holestat,det)==True:
				if pos[0]>20 and pos[0]<20+calc_rad(size,7) and pos[1]>20 and pos[1]<20+calc_rad(size,7):
						main_menu=True
						restart(holestat)


	screen.fill(BG)

	if GAME_OVER(holestat,det)==True:

		font = pygame.font.SysFont('', 80, True, False)

		text = font.render("GAME OVER",True,(0,0,0))

		display_board(screen,holes,holepos,size,holestat,selected,prev_step,main_menu,pos)


		screen.blit(text, [size[0]/2-(2.5*80), size[1]/2])


	else:
		display_board(screen,holes,holepos,size,holestat,selected,prev_step,main_menu,pos)

	pygame.display.flip()

	clock.tick(60)
 
pygame.quit()

input()