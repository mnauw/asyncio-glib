import asyncio
import asyncio_glib
from gi.repository import Gtk


class Demo:
    def __init__(self):
        self.future = asyncio.get_event_loop().create_future()

        self.window = Gtk.Window()
        button = Gtk.Button.new_with_label('Click here')
        button.connect('clicked', self.button_clicked)
        self.window.add(button)
        self.window.show_all()

    def button_clicked(self, widget):
        print('button clicked')
        self.window.close()
        self.future.set_result(None)


async def main():
    # Uncomment the following line and everything works.
    # asyncio.get_event_loop().call_later(1, heartbeat)
    demo = Demo()
    await demo.future
    print('future finished')


def heartbeat():
    asyncio.get_event_loop().call_later(1, heartbeat)
    print('tick')


if __name__ == '__main__':
    # asyncio.set_event_loop_policy(asyncio_glib.GLibEventLoopPolicy())
    # loop = asyncio.get_event_loop()
    loop = asyncio_glib.GLibEventLoop(handle_sigint=True)
    # this sets some module global that avoids nasty __del__ trigger at exit
    # asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()
