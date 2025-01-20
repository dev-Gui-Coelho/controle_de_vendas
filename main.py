from assets.imports import *
from assets.colors import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.theme1 = ctk.set_appearance_mode('system')
        self.resizable(height=True, width=False)
        self.font = ctk.CTkFont(family='Imprima', size=12)
        self.geometry('850x500')
        self.title('Controle Vendas')
        self.lbl_title = ctk.CTkLabel(self, text='Teste', font=('Imprima', 25), text_color=var_primary_key)
        self.lbl_title.place(x=400,y=15)

        self.switch_var = ctk.StringVar(value='dark')
        self.btn_switch_theme = ctk.CTkSwitch(self, text=" ", command=self.switch_mode, variable=self.switch_var, onvalue="light", offvalue="dark", progress_color=var_white_color, fg_color=var_white_color, button_color=var_black_color)
        self.btn_switch_theme.place(x=800, y=15)

        #Campos Do Cliente#
        self.frame_lbl_client = ctk.CTkFrame(self, width=50, height=30, fg_color=var_primary_key, corner_radius=20).place(x=20, y=70) 
        self.frame_lbl2_client = ctk.CTkFrame(self, width=55, height=30, fg_color=var_primary_key, bg_color=var_primary_key).place(x=40, y=70) 

        self.lbl_client_name = ctk.CTkLabel(self, text='Cliente:', height=20,font=('Imprima', 13),text_color=var_black_color,bg_color=var_primary_key ,).place(x=38, y=75)

        self.ipt_client = ctk.CTkEntry(self, fg_color=var_white_color, border_width=0, height=30, width=200,bg_color=var_white_color , text_color=var_black_color)
        self.ipt_client.place(x=95, y=70)

    def ver_mode_color_light(self) -> bool:
        if self.switch_var.get() == 'light' or self.btn_switch_theme.get() == 'light':
            return True
    
    def change_to_light_mode(self) -> None:
            self.theme1 = ctk.set_appearance_mode('light')
            self.btn_switch_theme = ctk.CTkSwitch(self, text=" ", command=self.switch_mode, variable=self.switch_var, onvalue="light", offvalue="dark", progress_color=var_black_color, button_color=var_white_color)

    def change_to_dark_mode(self) -> None:
            self.theme1 = ctk.set_appearance_mode('dark')
            self.btn_switch_theme = ctk.CTkSwitch(self, text=" ", command=self.switch_mode, variable=self.switch_var, onvalue="light", offvalue="dark", fg_color=var_white_color, button_color=var_black_color)

    def switch_mode(self) -> None:
        if self.ver_mode_color_light():
            return self.change_to_light_mode()
        else:
            return self.change_to_dark_mode()


if __name__ == '__main__':
    app = App()
    app.mainloop()