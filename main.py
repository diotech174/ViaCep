import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import requests

builder = Gtk.Builder()
builder.add_from_file('form.glade')

class Handler(object):

    def __init__(self, **kwargs):
        super(Handler, self).__init__(**kwargs)

        self.txtCep = builder.get_object('txtCep')
        self.txtLogradouro = builder.get_object('txtLogradouro')
        self.txtComplemento = builder.get_object('txtComplemento')
        self.txtBairro = builder.get_object('txtBairro')
        self.txtLocalidade = builder.get_object('txtLocalidade')
        
    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_btnBuscar_clicked(self, window):
        r = requests('https://viacep.com.br/ws/'+self.txtCep.get_text()+'/json')
        self.txtLogradouro.set_text(r.status_code)


builder.connect_signals(Handler())
window = builder.get_object('main_window')
window.show_all()

if __name__ == '__main__':
    Gtk.main()
        