import PySimpleGUI as sg
from  time import sleep
from threading import Thread
sg.theme('DarkBlue')

layout = [

    [sg.Text('', font=('Helvetica', 20, 'bold'),size=(10, 5),k = '-respiracao-',justification = 'c',
                 expand_x = True, text_color = 'green', visible=False,
                 p = ((0,0),(80,0))
                 
                 
                 )]+

    [sg.ProgressBar(max_value=94, orientation='v', 
                    size_px=(10, 30), key='-TEXT-',
                    expand_x = True,expand_y = True, 
                    border_width = 0,
                    relief='groove',
                    bar_color = "#1a2835",
                    visible = False)]      
    # [sg.Text('', 
    #         #  pad=(50, 1), 
    #          relief='groove', 
    #         text_color='yellow', 
    #         font=('Helvetica', 10), 
    #         expand_x = True,
    #         background_color='black',
    #         key='-TEXT-', 
    #         metadata=0, 
    #         border_width = 1,
    #         visible=False)],
            
            # [sg.Combo(values = ['1min', '5min', '10min', '20mim', '30min', '40min', '50min', '1h','2h'], k = '-time-',
            #  default_value = '30min',font=("Helvetica", 14, "bold"),
            #  enable_events=True)]


]
botoes = [[sg.Button('Iniciar/Parar',expand_x = True,font=("Helvetica", 14, "bold"),border_width = 0), sg.Button('Sair',expand_x = True,font=("Helvetica", 14, "bold"),border_width = 0) ]]
botoes = [[sg.Frame('',botoes, background_color = "white", border_width = 0, element_justification = 'c', grab = True, expand_x = True, p = (0,0))]]
layout = layout + botoes
layout = [[sg.Frame('',layout, background_color = "#1a2835", border_width = 0, element_justification = 'c')]]
window = sg.Window('Title', layout,
                   finalize=True, 
                   keep_on_top=True, 
                    # return_keyboard_events = True,
                    # size = (800,100),
                    no_titlebar=True,
                    grab_anywhere=True,
                    # transparent_color = "#1a2835",
                    background_color = "white",
                    element_justification='c',
                    text_justification= 'c',
                    margins = (0,0),
                    # border_depth = 2,
                    # progress_bar_color = ("#1a2835", 'black'),
                   resizable=True)



contando = False
def Barra_de_progresso(window):
    global contando
    # tempo = int(round(tempo, 0))
    SYMBOL_SQUARE = '█'        
    largura_janela = window.TKroot.winfo_width()
    nova_largura = int(largura_janela/10)+12
    window['-TEXT-'].set_size((10,10))
    inc = -1
    window['-respiracao-'].update(visible=True)
    window['-TEXT-'].update(visible=True)

    while contando: 
        inc = inc+1

        if inc <= 93:
            sleep(0.01)  
            if inc == 0:                         
                window['-respiracao-'].update(text_color = 'green')
                window['-TEXT-'].update(bar_color = ('green','#1a2835'))
                window['-respiracao-'].update('▼'*5+'\nINSPIRE\n'+'▲'*5) 

            window['-TEXT-'].update_bar(inc)
        else:
            sleep(0.1)   
            if inc == 94:    
                window['-respiracao-'].update(text_color = 'yellow')
                window['-TEXT-'].update(bar_color = ('yellow','#1a2835'))
                window['-respiracao-'].update('▲'*5+'\nEXPIRE\n'+'▼'*5)    
            inc2 = int(186-inc)
            window['-TEXT-'].update_bar(inc2)
        if inc == 187:
            inc = -1
    window['-respiracao-'].update('')
    window['-TEXT-'].update('')
    window['-respiracao-'].update(visible=False)
    window['-TEXT-'].update_bar(visible=False)

tm = 100
sg.timer_start()
sg.timer_start()

while True:

    event, values = window.read()
    # contando = True
    # Thread(target=Barra_de_progresso, args = [(window)],daemon=True).start()
    # if sg.timer_stop() >= 
    # contando = not contando   
    # tf = round(sg.timer_stop()/1000,1)
    # if tf >=20:
    #     print(tf)  
    #     sg.timer_start()
    #     contando = not contando         
    #     Thread(target=Barra_de_progresso, args = [(window)],daemon=True).start()




    if event in [sg.WINDOW_CLOSED, 'Sair']:
        break
    elif event == 'Iniciar/Parar':
        contando = not contando         
        Thread(target=Barra_de_progresso, args = [(window)],daemon=True).start()

    # elif event == '-time-':
    #     d = {i:j for i,j in zip(['1min','5min', '10min', '20mim', '30min', '40min', '50min', '1h','2h'],[15,10,20,30,40,50,60,120])}

    #     t = values['-time-']
    #     tempo = d[t]
    #     tm = tempo*1000*60
    #     window.refresh()
    #     print(round(sg.timer_stop()/1000,1))


        
        # if t not in [None, '']:
        #     contando = not contando
        #     while contando:
                # Thread(target=Barra_de_progresso, args = [(window)],daemon=True).join()
                # Barra_de_progresso(window)
                # sleep(tempo)






window.close()
