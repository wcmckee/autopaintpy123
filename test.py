from sys import argv

script, filename = argv
import autopy as ap
from autopy.mouse import LEFT_BUTTON
from autopy.bitmap import *
import time
import random


def open_fold():
    txt = open(filename)
    print "Here's your file %r:" % filename
    print txt.read()
    print "Type the filename again:"
    file_again = raw_input("> ")
    txt_again = open(file_again)
    print txt_again.read()
open_fold()

def rect_move():
    
    start = random.randint(300, 600)
    mid = random.randint(600, 900)
    bottom = random.randint(900, 1200)

    ap.mouse.move(start, 800)
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(.1)
    print "# click"
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.1)
    print '# left down'
    ap.mouse.smooth_move(mid, bottom)
    ap.mouse.smooth_move(start, bottom)
    ap.mouse.smooth_move(bottom, mid)
    ap.mouse.smooth_move(start, mid)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(.1)
    print '# left release'

def test2():
    ap.mouse.move(500,300)
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(.1)
    print "# click"
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.1)
    print '# left down'
    ap.mouse.smooth_move(800,300)
    ap.mouse.smooth_move(800, 900)
    ap.mouse.smooth_move(500, 900)
    ap.mouse.smooth_move(500,300)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(.1)
    print '# left release'
    
def test3():
    
    top = random.randint(600,1200)
    side = random.randint(900,950)
    bot = random.randint(300,400)
    ap.mouse.move(top,300)
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(.1)
    print "# click"
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.1)
    print '# left down'
    ap.mouse.smooth_move(bot,top)
    ap.mouse.smooth_move(bot,side)
    ap.mouse.smooth_move(top,side)
    ap.mouse.smooth_move(top,bot)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(.1)
    print '# left release'
    
def symbol():
    
    ran_top = random.randint(600,700)
    ran_bleh = random.randint(900,950)
    ran_bottom = random.randint(1000,1050)
    ran_side = random.randint(1300,1350)
    ran_two = random.randint(300,500)
    
    ap.mouse.move(600, 600)
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(.1)
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.1)
    ap.mouse.smooth_move(ran_top, ran_bleh)
    time.sleep(.1)
    ap.mouse.smooth_move(ran_two, ran_bleh)
    time.sleep(.1)
    ap.mouse.smooth_move(ran_bottom, ran_two)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(.1)
    
def blank():
    hp = ap.bitmap.capture_screen().get_color(500,600)
    print hp
    hex(ap.bitmap.capture_screen().get_color(hp)

def where_is_the_monkey_i_say():
    """Look for the monkey. Tell me if you found it."""
    monkey = ap.bitmap.Bitmap.open('monkey.png')
    barrel = ap.bitmap.Bitmap.open('barrel.png')

    pos = barrel.find_bitmap(monkey)
    if pos:
        print "We found him! He's at %s!" % str(pos)
    else:
        print "There is no monkey... what kind of barrel is this?!"

where_is_the_monkey_i_say()

    
##def screen_option():
 ##   ap.screen.get_size()
   # print ap.screen.get_size()

##def screen_cap():
 #   Bitmap.capture_screen(rect=None)
  #  Bitmap.save(folder)

#screen_cap()


##for x in range(0,5):
   # symbol()
#screen_option
                
                  
##  move_forward
         
##for x in range(0, 3):
  ##  rect_move()