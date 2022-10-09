from Utils import lista_usuarios_back
from tkinter import *

# cores
co0 = "#fae8e8"  # rosa
co1 = "#d9d9d9"  # cinza
co2 = "#1a1d1a"  # preta

# Informações do modulo
NAME = 'Lista'
REQUIRED_PERMISSIONS_REG  = [None]
REQUIRED_PERMISSIONS_RATE = [
    [3, 4, 5]  # pelo menos uma das 3
]
REQUIRED_PERMISSIONS_VIEW = [None]

module_frame = None

# executa o modulo e retorna
def run(frame_parent):

    global module_frame
    module_frame=Frame(frame_parent, bg=co0)
    module_frame.columnconfigure(0, minsize = 0, weight = 1)
    module_frame.grid(row=0, column=0, sticky="nsew")

    from Front.Scrollbar import add_scrollbar
    module_frame = add_scrollbar(module_frame)
    module_frame.columnconfigure(0, minsize = 0, weight = 1)
    module_frame.grid(row=0, column=0, sticky="nsew")

    # importa o usuário logado
    from Users.Authentication import CURRENT_USER

    # cria uma lista com os usuários a serem avaliados pelo usuário logado
    grade_submitted = lista_usuarios_back.get_users(CURRENT_USER.email)[0]
    grade_to_submit = lista_usuarios_back.get_users(CURRENT_USER.email)[1]

    # função de criar frame
    # row e column referem-se a posição do frame
    def criar_frame(quadro, row, column, sticky, background = co0):
        frame = Frame(quadro, background=background)
        frame.grid(row = row, column = column, sticky = sticky, padx = 5, pady = 5)
        return frame

    # cria widget do tipo label
    def criar_label(quadro, text, font, r, c, sticky='n'):
        Label(quadro, text=text, font=font, background = co0, justify=LEFT).grid(row=r, column=c, sticky= sticky)

    def criar_button(quadro, text, font, r, c, command, sticky='n'):
        Button(quadro, text = text, font = font, background = co0, justify=RIGHT, fg=co2, command=command,
               width=13, height=0, activebackground='#c5a8b0').grid(row=r, column=c, sticky= sticky)

    # frame com os dados do usuário que está logado
    frame_user = criar_frame(module_frame, 0, 0, "nsew")

    # importa a função que transforma role_id em nome da role
    from Models.Role import get_role_name

    # ###testes
    # user_group_members = handler.find_data_list_by_field_value_csv(Settings.USERS_PATH, 'group_id', grupo_id)
    #



    criar_label(frame_user, 'Meu Perfil', 'Calibri, 30', 0, 0)

    criar_label(frame_user, get_role_name(CURRENT_USER.role_id), 'Calibri, 12',1, 0, "w")
    criar_label(frame_user, CURRENT_USER.name, 'Calibri, 12',2, 0, "w")

    # frame com os usuários que devem ser analisados por quem está logado
    frame_avaliados = criar_frame(module_frame, 1, 0, "nsew")
    frame_avaliados.columnconfigure(0, minsize = 0, weight = 1)
    criar_label(frame_avaliados, 'Integrantes ainda não Avaliados', 'Calibri, 14', 0, 0, "w")

    indice = 2

    for user_to_submit in grade_to_submit:

        frame_to_rate = criar_frame(frame_avaliados, indice, 0, "ew")
        frame_to_rate.columnconfigure(0, minsize = 0, weight = 1)
        criar_label(frame_to_rate, get_role_name(user_to_submit['role_id']), 'Calibri, 12', 0, 0, "w")  # linha para teste
        criar_label(frame_to_rate, user_to_submit['name'], 'Calibri, 12', 1, 0, "w")  # linha para teste
        criar_button(frame_to_rate, 'Avaliar', 'Calibri, 12', 1, 1, lambda u=user_to_submit: avaliar(u['id']), "e")  # linha para teste
        indice = indice + 1


        criar_label(frame_avaliados, 'Integrantes já Avaliados', 'Calibri, 14', indice, 0, "w")

    indice = indice + 1

    for user_submited in grade_submitted:

        frame_rated = criar_frame(frame_avaliados, indice, 0, "ew")
        frame_rated.columnconfigure(0, minsize = 0, weight = 1)
        criar_label(frame_rated, get_role_name(user_submited['role_id']), 'Calibri, 12', 0, 0, "w")  # linha para teste
        criar_label(frame_rated, user_submited['name'], 'Calibri, 12', 1, 0, "w")  # linha para teste
        # criar_button(frame_rated, 'Editar Avaliação', 'Calibri, 12', 1, 1, "e")  # linha para teste
        indice = indice + 1


    return module_frame

def avaliar (id):
    from Front.Modules import avaliacao_teste
    global module_frame
    avaliacao_teste.run(module_frame.master, id)
