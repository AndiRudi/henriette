# This is the henriette console. It displays all basic information of the system
# and allows full control over all systems.
import urwid
import urwid.widget

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]

# header
header_txt = urwid.Text(('banner', u" Henriette Operating Sytem Console"), align='center')
map_header_text = urwid.AttrMap(header_txt, 'streak')
header = urwid.Filler(map_header_text, 'top')

# body
body_txt = urwid.Text(('banner', u" Henriette Operating Sytem Console"), align='center')
map_body_txt = urwid.AttrMap(body_txt, 'streak')
content = urwid.Filler(map_body_txt, 'top')
background = urwid.AttrMap(urwid.SolidFill(' '),'bg')
body = urwid.Overlay(content, background, 'center', ('relative', 100), 'middle', 10)

# footer
footer_txt = urwid.Text(('streak', u" Rudsen 2016"), align='center')
map_footer_txt = urwid.AttrMap(footer_txt, 'streak')


#interior = urwid.Filler(urwid.Pile([map1, map2]))
#window = urwid.LineBox(interior)

frame = urwid.Frame(body, map_header_text, map_footer_txt)

loop = urwid.MainLoop(frame, palette, unhandled_input=exit_on_q)
loop.run()
