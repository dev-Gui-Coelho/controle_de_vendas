from assets.imports import *
from assets.colors import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.theme1 = ctk.set_appearance_mode('system')
        self.resizable(height=True, width=False)
        self.font = ctk.CTkFont(family='Imprima', size=12)
        self.geometry('850x500')
        self.iconbitmap('assets/img/logoBlack.ico')
        self.title('Controle Vendas')
        self.lbl_title = ctk.CTkLabel(self, text='Controle de Vendas', font=('Imprima', 25), text_color=var_primary_key)
        self.lbl_title.place(x=310,y=15)

        self.switch_var = ctk.StringVar(value='dark')
        self.btn_switch_theme = ctk.CTkSwitch(self, text=" ", command=self.switch_mode, variable=self.switch_var, onvalue="light", offvalue="dark", progress_color=var_black_color,button_color=var_white_color)
        self.btn_switch_theme.place(x=800, y=15)

        #Campos Do Cliente#

        self.frame_lbl_client = ctk.CTkFrame(self, width=50, height=30, fg_color=var_primary_key, corner_radius=20).place(x=70, y=100) 
        self.frame_lbl2_client = ctk.CTkFrame(self, width=55, height=30, fg_color=var_primary_key, bg_color=var_primary_key).place(x=90, y=100) 

        self.lbl_client_name = ctk.CTkLabel(self, text='Cliente:', height=20,font=('Imprima', 13),text_color=var_black_color,bg_color=var_primary_key ,).place(x=88, y=105)
        var_name_client = ctk.StringVar()
        self.ipt_client = ctk.CTkEntry(self, fg_color=var_white_color,border_width=0, height=30, width=200,bg_color=var_white_color , text_color=var_black_color, textvariable=var_name_client)
        self.ipt_client.place(x=145, y=100)

        #Campo Valores e Parcelas#

        self.frame_lbl_value = ctk.CTkFrame(self, width=50, height=30, fg_color=var_primary_key, corner_radius=20).place(x=500, y=100) 
        self.frame_lbl2_value = ctk.CTkFrame(self, width=55, height=30, fg_color=var_primary_key, bg_color=var_primary_key).place(x=525, y=100) 

        self.lbl_value = ctk.CTkLabel(self, text='Valor:', height=20,font=('Imprima', 13),text_color=var_black_color,bg_color=var_primary_key ,).place(x=530, y=105)
        var_value_client = ctk.StringVar()
        self.ipt_value = ctk.CTkEntry(self ,fg_color=var_white_color, border_width=0, height=30, width=100,bg_color=var_white_color , text_color=var_black_color, textvariable=var_value_client)
        self.ipt_value.place(x=580, y=100)

        self.frame_lbl_parcelas = ctk.CTkFrame(self, width=50, height=30, fg_color=var_primary_key, corner_radius=20).place(x=500, y=180) 
        self.frame_lbl2_parcelas = ctk.CTkFrame(self, width=55, height=30, fg_color=var_primary_key, bg_color=var_primary_key).place(x=525, y=180) 
        self.lbl_parcelas= ctk.CTkLabel(self, text='Parcelas:', height=20,font=('Imprima', 13),text_color=var_black_color,bg_color=var_primary_key ,).place(x=520, y=185)

        var_parcelas_vendas = ctk.IntVar()
        self.ipt_parcelas = ctk.CTkOptionMenu(self, values=('1x','2x','3x'), width=100, height=30,  fg_color=var_white_color, text_color=var_black_color, corner_radius=0, button_color=var_primary_key, button_hover_color=var_white_color, dropdown_fg_color=var_white_color, dropdown_text_color=var_black_color, dropdown_hover_color=var_primary_key, variable=var_parcelas_vendas)
        self.ipt_parcelas.place(x=580, y=180)
        
        #DATA CAMPOS#

        self.frame_lbl_datas = ctk.CTkFrame(self, width=50, height=30, fg_color=var_primary_key, corner_radius=20).place(x=500, y=260) 
        self.frame_lbl2_datas = ctk.CTkFrame(self, width=55, height=30, fg_color=var_primary_key, bg_color=var_primary_key).place(x=525, y=260) 
        self.lbl_datas= ctk.CTkLabel(self, text='Data:', height=20,font=('Imprima', 13),text_color=var_black_color,bg_color=var_primary_key ,).place(x=530, y=265)

        var_data_venda = ctk.StringVar()
        self.ipt_data = ctk.CTkEntry(self ,fg_color=var_white_color, placeholder_text='No formato 10/11/2003',border_width=0, height=30, width=100,bg_color=var_white_color , text_color=var_black_color, textvariable=var_data_venda)
        self.ipt_data.place(x=580, y=260)

        self.frame_lbl_produtos = ctk.CTkFrame(self, width=50, height=30, fg_color=var_primary_key, corner_radius=20).place(x=70, y=180) 
        self.frame_lbl2_produtos = ctk.CTkFrame(self, width=55, height=30, fg_color=var_primary_key, bg_color=var_primary_key).place(x=90, y=180) 

        self.lbl_produtos = ctk.CTkLabel(self, text='Produtos:', height=20,font=('Imprima', 13),text_color=var_black_color,bg_color=var_primary_key ,).place(x=77, y=184)

        self.ipt_produtos = ctk.CTkTextbox(self, width=200, height=200, fg_color=var_white_color,corner_radius=0, text_color=var_black_color,scrollbar_button_color=var_primary_key)
        self.ipt_produtos.place(x=145, y=180)

        self.vender = ctk.CTkButton(self, text='Vender', width=100, fg_color=var_primary_key, text_color=var_black_color, hover_color=var_white_color).place(x=430, y=350)
        self.limpar = ctk.CTkButton(self, text='Limpar', width=100, fg_color=var_primary_key, text_color=var_black_color, hover_color=var_white_color, command=self.limpar).place(x=560, y=350)
        self.sair = ctk.CTkButton(self, text='Sair', width=100, fg_color=var_primary_key, text_color=var_black_color, hover_color=var_white_color, command=self.exit_confirmation).place(x=690, y=350)

    def ver_mode_color_dark(self) -> bool:
        if self.switch_var.get() == 'dark' or self.btn_switch_theme.get() == 'dark':
            return True
    
    def change_to_light_mode(self) -> None:
            self.theme1 = ctk.set_appearance_mode('light')
            self.btn_switch_theme = ctk.CTkSwitch(self, text=" ", command=self.switch_mode, variable=self.switch_var, onvalue="light", offvalue="dark", progress_color=var_black_color, button_color=var_white_color)

    def change_to_dark_mode(self) -> None:
            self.theme1 = ctk.set_appearance_mode('dark')
            self.btn_switch_theme = ctk.CTkSwitch(self, text=" ", command=self.switch_mode, variable=self.switch_var, onvalue="light", offvalue="dark", button_color=var_black_color, progress_color=var_white_color)

    def switch_mode(self) -> None:
        if self.ver_mode_color_dark():
            return self.change_to_dark_mode()
        else:
            return self.change_to_light_mode()

    def exit_app(self) -> None:
        self.destroy()

    def exit_confirmation(self) -> None:
        if messagebox.askyesno('CONFIRMAÇÃO', 'Deseja sair?'):
            self.exit_app()
        else:
            pass
    
    def limpar(self):
        self.ipt_client.setvar(' ')
    

if __name__ == '__main__':
    app = App()
    app.mainloop()