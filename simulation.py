import tkinter as tk
import random
from math import floor, pi, cos, sin

width = 7
height = 7
piece_size = 52

selected_tile = None
board = {}

to_clear = []
to_fall = []
to_swap = []

window = tk.Tk()

# Load all 6 tile images
piece_type_images = {
    'alpha': tk.PhotoImage(file='alpha-texture.png'),
    'beta': tk.PhotoImage(file='beta-texture.png'),
    'gamma': tk.PhotoImage(file='gamma-texture.png'),
    'lambda': tk.PhotoImage(file='lambda-texture.png'),
    'zeppo': tk.PhotoImage(file='zeppo-texture.png'),
    'zeta': tk.PhotoImage(file='zeta-texture.png'),
    }

class Tile:
    def __init__(self, widget, type, x, y):
        self.widget = widget
        self.type = type
        self.x = x
        self.y = y
        self.ay = None
        self.hrun = None
        self.vrun = None

class MatchRun:
	def __init__(self, n):
		self.n = n

class Swap:
	def __init__(self, topleft, bottomright, orientation):
		self.tl = topleft
		self.br = bottomright
		if orientation == 0:
			self.px = (topleft.x + 0.5) * piece_size
			self.py = topleft.y * piece_size
			self.a = 0
		else:
			self.px = topleft.x * piece_size
			self.py = (topleft.y + 0.5) * piece_size
			self.a = pi / 2
		self.d = 0

piece_type_names = [ 'alpha', 'beta', 'gamma', 'lambda', 'zeppo', 'zeta' ]

def reset(w):
	w.place(x=(selected_tile.x * piece_size), y=(selected_tile.y * piece_size))

def wiggle():
	if len(to_swap) > 0:
		return
	
	if selected_tile != None:
		dx = random.randint(-5, 5)
		dy = random.randint(-5, 5)
		#selected.place_forget()
		selected_tile.widget.place(x=(selected_tile.x * piece_size + dx), y=(selected_tile.y * piece_size + dy))
		window.after(50, wiggle)

def check_move(tile):
	
	dup_board = dict( board )
	
	# swap tiles
	stashed = dup_board[ f'{selected_tile.x},{selected_tile.y}' ]
	dup_board[ f'{selected_tile.x},{selected_tile.y}' ] = tile
	dup_board[ f'{tile.x},{tile.y}' ] = stashed
	
	# ugly but effective
	hrun = 1
	type = tile.type
	for i in range(1,3):
		if selected_tile.x + i >= width:
			break
		if dup_board[ f'{selected_tile.x + i},{selected_tile.y}' ].type == type:
			hrun += 1
		else:
			break
	for i in range(1,3):
		if selected_tile.x - i < 0:
			break
		if dup_board[ f'{selected_tile.x - i},{selected_tile.y}' ].type == type:
			hrun += 1
		else:
			break
	vrun = 1
	for i in range(1,3):
		if selected_tile.y + i >= height:
			break
		if dup_board[ f'{selected_tile.x},{selected_tile.y + i}' ].type == type:
			vrun += 1
		else:
			break
	for i in range(1,3):
		if selected_tile.y - i < 0:
			break
		if dup_board[ f'{selected_tile.x},{selected_tile.y - i}' ].type == type:
			vrun += 1
		else:
			break
	
	if hrun > 2 or vrun > 2:
		return True
	
	hrun = 1
	type = stashed.type
	for i in range(1,3):
		if tile.x + i >= width:
			break
		if dup_board[ f'{tile.x + i},{tile.y}' ].type == type:
			hrun += 1
		else:
			break
	for i in range(1,3):
		if tile.x - i < 0:
			break
		if dup_board[ f'{tile.x - i},{tile.y}' ].type == type:
			hrun += 1
		else:
			break
	vrun = 1
	for i in range(1,3):
		if tile.y + i >= height:
			break
		if dup_board[ f'{tile.x},{tile.y + i}' ].type == type:
			vrun += 1
		else:
			break
	for i in range(1,3):
		if tile.y - i < 0:
			break
		if dup_board[ f'{tile.x},{tile.y - i}' ].type == type:
			vrun += 1
		else:
			break
	
	if hrun > 2 or vrun > 2:
		return True

def btnclick(event):
	global selected_tile
	
	if event.widget.master != frame or len(to_fall) > 0 or len(to_clear) > 0:
		return
	
	#print(event.widget.master)
	
	check_board()
	
	x = window.winfo_pointerx() - window.winfo_rootx()
	y = window.winfo_pointery() - window.winfo_rooty()
	#print( x, y )
	selX = floor(x / piece_size)
	selY = floor(y / piece_size)
	#print(selX, selY)
	
	if selected_tile != None and selected_tile.widget != None:
		reset(selected_tile.widget)
	else:
		window.after(10, wiggle)
		
	if selected_tile == None or selected_tile.widget != event.widget:
		check_tile = board[ f'{selX},{selY}' ]
		
		if selected_tile == None or not ((abs(selX - selected_tile.x) == 1 and selY == selected_tile.y) or (abs(selY - selected_tile.y) == 1 and selX == selected_tile.x)):
			selected_tile = check_tile
		elif selected_tile != None:
			if ( check_move(check_tile) ):
				if abs(selX - selected_tile.x) == 1:
					l, r = None, None
					if selX < selected_tile.x:
						l = check_tile
						r = selected_tile
					else:
						l = selected_tile
						r = check_tile
					to_swap.append( Swap( l, r, 0 ) ) # 0 = horizontal
				elif abs(selY - selected_tile.y) == 1:
					l, r = None, None
					if selY < selected_tile.y:
						l = check_tile
						r = selected_tile
					else:
						l = selected_tile
						r = check_tile
					to_swap.append( Swap( l, r, 1 ) ) # 1 = vertical
				selected_tile = None
			else:
				reset(selected_tile.widget)
				selected_tile = None;
		#selected_tile.widget = event.widget
	else:
		selected_tile = None

def fall():
	if len(to_fall) > 0:
		
		for i in reversed(range(len(to_fall))):
			piece = to_fall[i]
			
			piece.ay += 5
			if piece.ay >= piece.y * piece_size:
				piece.widget.place(x=piece.x * piece_size, y=piece.y * piece_size)
				to_fall.pop(i)
				if len(to_fall) == 0:
					#print("again!")
					check_board()
			else:
				#piece.widget.place_forget()
				piece.widget.place(x=piece.x * piece_size, y=piece.ay)

	r = piece_size / 2
	for i in reversed(range(len(to_swap))):
		swap = to_swap[i]
		swap.d += 0.25
		if swap.d > pi:
			stashx = swap.br.x
			stashy = swap.br.y
			swap.br.x = swap.tl.x
			swap.br.y = swap.tl.y
			swap.tl.x = stashx
			swap.tl.y = stashy
			
			swap.br.widget.place(x=swap.br.x * piece_size, y=swap.br.y * piece_size)
			swap.tl.widget.place(x=swap.tl.x * piece_size, y=swap.tl.y * piece_size)

			stash = board[ f'{swap.tl.x},{swap.tl.y}' ]
			board[ f'{swap.tl.x},{swap.tl.y}' ] = board[ f'{swap.br.x},{swap.br.y}' ]
			board[ f'{swap.br.x},{swap.br.y}' ] = stash



			to_swap.pop(i)
			
			check_board()
		else:
			x = swap.px + r * cos( swap.a + swap.d + pi )
			y = swap.py + r * sin( swap.a + swap.d + pi )
			swap.tl.widget.place(x=x, y=y)
			x = swap.px + r * cos( swap.a + swap.d )
			y = swap.py + r * sin( swap.a + swap.d )
			swap.br.widget.place(x=x, y=y)
			
	window.after( 100, fall )

def check_remove():
	if len(to_clear) > 0:
		tile = to_clear[0]
		board[ f'{tile.x},{tile.y}' ] = None
		tile.widget.place_forget()
		to_clear.pop(0)
		
		for i in reversed(range(tile.y)):
			#print(i)
			above = board[ f'{tile.x},{i}' ]
			#print(f'{tile.x},{i}')
			if above != None:
				to_fall.append( above )
				if above.ay == None:
					above.ay = above.y * piece_size
				above.y += 1
				board[ f'{tile.x},{i+1}' ] = above
				board[ f'{tile.x},{i}' ] = None
		
		#print(board[ f'{tile.x},0' ])
		if board[ f'{tile.x},0' ] == None:
			type = piece_type_names[ random.randint(0,len(piece_type_names) - 1) ]
		
			label = tk.Label(
				master=frame,
				borderwidth=0,
				padx=0, pady=0,
				image=piece_type_images[type],
				width=piece_size,
				height=piece_size)
			label.place(x=tile.x * piece_size, y=0)
			
			new_piece = Tile( label, type, tile.x, 0 )
			to_fall.append(new_piece)
			new_piece.ay = -piece_size
			board[ f'{tile.x},0' ] = new_piece
		
		window.after( 100, check_remove )

def check_board():
	# horizontal
	for i in range(height):
		last = board[ f'0,{i}' ]
		if last == None:
			continue
		last.hrun = MatchRun(1)
		run = last.hrun
		for j in range(1, width):
			if board[ f'{j},{i}' ] != None:
				if board[ f'{j},{i}' ].type == last.type:
					board[ f'{j},{i}' ].hrun = run
					run.n += 1
				else:
					last = board[ f'{j},{i}' ]
					last.hrun = MatchRun(1)
					run = last.hrun
				
	# vert
	for j in range(width):
		last = board[ f'{j},0' ]
		if last == None:
			continue
		last.vrun = MatchRun(1)
		run = last.vrun
		for i in range(1, height):
			if board[ f'{j},{i}' ] != None:
				if board[ f'{j},{i}' ].type == last.type:
					board[ f'{j},{i}' ].vrun = run
					run.n += 1
				else:
					last = board[ f'{j},{i}' ]
					last.vrun = MatchRun(1)
					run = last.vrun
	
	for i in range(height):
		for j in range(width):
			#print( board[ f'{j},{i}' ].hrun.n, board[ f'{j},{i}' ].vrun.n )
			if board[ f'{j},{i}' ] == None:
				continue
			if board[ f'{j},{i}' ].hrun.n > 2 or board[ f'{j},{i}' ].vrun.n > 2:
				to_clear.append( board[ f'{j},{i}' ] )
	
	check_remove()
		

frame = tk.Frame( master=window, width=(piece_size * width), height=(piece_size * height) )
frame.pack()

for i in range(height):
	for j in range(width):
		#frame = tk.Frame( master=window, width=50, height=50 )
		#frame.grid(row=i, column=j)
		
		type = piece_type_names[ random.randint(0,len(piece_type_names) - 1) ]
		
		label = tk.Label(
			master=frame,
			borderwidth=0,
			padx=0, pady=0,
			image=piece_type_images[type],
			width=piece_size,
			height=piece_size)
		label.place(x=(j * piece_size), y=(i * piece_size))
		
		board[ f'{j},{i}' ] = Tile( label, type, j, i )

window.bind("<Button-1>", btnclick)

window.after( 500, check_board )

fall()

window.mainloop()
