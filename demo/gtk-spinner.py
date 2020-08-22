import asyncio
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import asyncio_glib
asyncio.set_event_loop_policy(asyncio_glib.GLibEventLoopPolicy())

async def do_something(win):
    win.spinner.start()
    await asyncio.sleep(5)
    win.remove(win.spinner)
    win.add(win.label)
    win.show_all()

    for i in range(10, 0, -1):
        await asyncio.sleep(1)
        win.label.props.label = "Closing in %d seconds" % i

class Window(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.spinner = Gtk.Spinner()
        self.label = Gtk.Label(label="Done")

        self.set_default_size(320, 320)
        self.add(self.spinner)
        self.show_all()

async def main():
    win = Window()
    await do_something(win)

if __name__ == '__main__':
    loop = asyncio_glib.GLibEventLoop(handle_sigint=True)
    loop.run_until_complete(main())
    loop.close()
