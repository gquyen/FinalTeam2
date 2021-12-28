import pgzrun
import random
truc_x=35
truc_y=25
kich_thuoc_o=20
thoi_gian=0
diem = 0
vi_tri_ban_dau='right'
snake_alive = 1
chieu_dai_khung=truc_x*kich_thuoc_o
chieu_rong_khung=truc_y*kich_thuoc_o

def tao_ran():
    global snake_phan_khuc

    snake_phan_khuc=[
        {'x':2,'y':0},
        {'x':1,'y':0},
        {'x':0,'y':0}
    ]

tao_ran()

def tao_thuc_an():
    global thuc_an
    list_thuc_an = []
    for toa_do_thuc_an_x in range(truc_x):
        for toa_do_thuc_an_y in range(truc_y):
            chay = 1
            for phan_khuc in snake_phan_khuc:
                if toa_do_thuc_an_x == phan_khuc['x'] and toa_do_thuc_an_y == phan_khuc['y']:
                    chay = 0
            if chay == 1:
                list_thuc_an.append({'x':toa_do_thuc_an_x,'y':toa_do_thuc_an_y})

    thuc_an = random.choice(list_thuc_an)

tao_thuc_an()

def on_key_down(key):
    global vi_tri_ban_dau
    if key==keys.RIGHT and vi_tri_ban_dau!= 'left':
        vi_tri_ban_dau='right'
    elif key==keys.LEFT and vi_tri_ban_dau!= 'right':
        vi_tri_ban_dau='left'
    elif key ==keys.UP and vi_tri_ban_dau!='down':
        vi_tri_ban_dau='up'
    elif key ==keys.DOWN and vi_tri_ban_dau!= 'up':
        vi_tri_ban_dau='down'

def update(dt):
    global thoi_gian , vi_tri_ban_dau , snake_alive, diem
    thoi_gian+=dt

    if snake_alive == 1:
        if thoi_gian>=0.2:
            vi_tri_tt_x=snake_phan_khuc[0]['x']
            vi_tri_tt_y=snake_phan_khuc[0]['y']
            if vi_tri_ban_dau=='right':
                vi_tri_tt_x+=1
                if vi_tri_tt_x>truc_x:
                    vi_tri_tt_x=0
            elif vi_tri_ban_dau=='left':
                vi_tri_tt_x-=1
                if vi_tri_tt_x<0:
                    vi_tri_tt_x=truc_x-1
            elif vi_tri_ban_dau=='up':
                vi_tri_tt_y-=1
                if vi_tri_tt_y<0:
                    vi_tri_tt_y=truc_y-1
            elif vi_tri_ban_dau=='down':
                vi_tri_tt_y+=1
                if vi_tri_tt_y>truc_y:
                    vi_tri_tt_y=0
            thoi_gian = 0

            chay= 1
            for phan_khuc in snake_phan_khuc:
                if vi_tri_tt_x==phan_khuc['x'] and vi_tri_tt_y ==phan_khuc['y']:
                    chay=0
            if chay == 1:
                snake_phan_khuc.insert(0,{'x': vi_tri_tt_x,'y':vi_tri_tt_y})

                if snake_phan_khuc[0]['x']==thuc_an['x'] and snake_phan_khuc[0]['y']==thuc_an['y']:
                    diem += 1
                    tao_thuc_an()
                else:
                    snake_phan_khuc.pop()
            else:
                snake_alive=0

def draw():
    screen.fill((135,206,250))

    def draw_cell(x,y,color):
        screen.draw.filled_rect(Rect(x*kich_thuoc_o,y*kich_thuoc_o,kich_thuoc_o-1,kich_thuoc_o-1),color=color)
    for phan_khuc in snake_phan_khuc:
        if snake_alive:
            color="dodgerblue"
        else :
            color="mediumslateblue"
            screen.draw.text("BAN DA THUA", (0, 0), fontsize=50, color="blue", background="white")
            screen.draw.text("Diem:", (0, 40), fontsize=30, color="black", background="white")
            screen.draw.text(str(diem), (58, 40), fontsize=30, color="black", background="white")
        draw_cell(phan_khuc['x'],phan_khuc['y'],color)
    draw_cell(thuc_an['x'],thuc_an['y'],"lightcyan")

pgzrun.go()
