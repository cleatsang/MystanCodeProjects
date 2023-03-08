"""
File: my_drawing.py
Name:Audrey Tsang
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


SIZE = 100
WIDTH = 800
HEIGHT = 400


def main():
    """
    Title: Ham from 'Toy Story'
    I just thought this piggy was cute so I drew it. ：）
    """
    window = GWindow(width=WIDTH, height=HEIGHT)
    face = GOval(SIZE, SIZE, x=(WIDTH-SIZE)/2, y=(HEIGHT-SIZE)/3*2)
    face.filled = True
    face.fill_color = 'violet'
    face.color = 'black'
    window.add(face)
    r_ear = GOval(SIZE/3, SIZE/3, x=face.x-SIZE/7, y=face.y-SIZE/7)
    r_ear.filled = True
    r_ear.fill_color = 'violet'
    window.add(r_ear)
    l_ear = GOval(SIZE/3, SIZE/3, x=face.x+SIZE-SIZE/5, y=face.y-SIZE/7)
    l_ear.filled = True
    l_ear.fill_color = 'violet'
    window.add(l_ear)
    r_s_ear = GOval(SIZE/6, SIZE/6, x=face.x-SIZE/80, y=face.y-SIZE/80)
    r_s_ear.filled = True
    r_s_ear.fill_color = 'magenta'
    r_s_ear.color = 'magenta'
    window.add(r_s_ear)
    l_s_ear = GOval(SIZE / 6, SIZE / 6, x=face.x+SIZE-SIZE/6, y=face.y - SIZE / 80)
    l_s_ear.filled = True
    l_s_ear.fill_color = 'magenta'
    l_s_ear.color = 'magenta'
    window.add(l_s_ear)
    r_brow = GRect(18, 3, x=face.x+SIZE/4, y=face.y+SIZE/8)
    r_brow.filled = True
    r_brow.fill_color = 'black'
    window.add(r_brow)
    l_brow = GRect(18, 3, x=face.x + SIZE / 1.75, y=face.y + SIZE / 8)
    l_brow.filled = True
    l_brow.fill_color = 'black'
    window.add(l_brow)
    r_eye = GOval(16, 16, x=r_brow.x+1, y=r_brow.y+10)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye)
    l_eye = GOval(16, 16, x=l_brow.x + 1, y=r_brow.y + 10)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    window.add(l_eye)
    nose = GOval(70, 30, x=r_brow.x-10, y=r_brow.y+30)
    nose.filled = True
    nose.fill_color = 'violet'
    nose.color = 'black'
    window.add(nose)
    r_hole = GOval(8, 12, x=r_brow.x+8, y=nose.y+8)
    r_hole.filled = True
    r_hole.fill_color = 'purple'
    r_hole.color = 'black'
    window.add(r_hole)
    l_hole = GOval(8, 12, x=l_brow.x + 2, y=nose.y + 8)
    l_hole.filled = True
    l_hole.fill_color = 'purple'
    l_hole.color = 'black'
    window.add(l_hole)
    word = GLabel("Hello World!", x=face.x, y=face.y-30)
    word.font = 'Helvetica-20'
    word.color = 'navy'
    window.add(word)


if __name__ == '__main__':
    main()
