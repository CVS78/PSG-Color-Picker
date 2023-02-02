
#CVS78 - https://github.com/CVS78
#PSG Color Picker is provided 'as is'


import PySimpleGUI as sg
import PIL.ImageGrab
import pyautogui as pg
from PIL import ImageGrab

#==========Constants========#
USE_FADE_IN = True

#==========Themes==========#
Color_Picker_Dark= {'BACKGROUND': '#19232D',
             'TEXT': '#e7e7e7',
             'INPUT': '#32414B',
             'TEXT_INPUT': '#e7e7e7',
             'SCROLL': '#505F69',
             'BUTTON': ('#e7e7e7', '#32414B'),
             'PROGRESS': ('#505F69', '#32414B'),
             'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0
             }
sg.theme_add_new('Theme_Dark', Color_Picker_Dark)

Color_Picker_Color = {'BACKGROUND': '#2a3950',
             'TEXT': '#e7e7e7',
             'INPUT': '#725a7a',
             'TEXT_INPUT': '#e7e7e7',
             'SCROLL': '#725a7a',
             'BUTTON': ('#e7e7e7', '#725a7a'),
             'PROGRESS': ('#c56d86', '#725a7a'),
             'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
             }
sg.theme_add_new('Theme_Color', Color_Picker_Color)

Color_Picker_Light = {'BACKGROUND': '#DDDDDD',
             'TEXT': '#3a99fd',
             'INPUT': '#3a99fd',
             'TEXT_INPUT': '#ffffff',
             'SCROLL': '#3a99fd',
             'BUTTON': ('#ffffff', '#3a99fd'),
             'PROGRESS': ('#3a99fd', '#3a99fd'),
             'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0, 
             }
sg.theme_add_new('Theme_Light', Color_Picker_Light)

theme = sg.user_settings_get_entry('-theme-', None)
sg.theme(theme)
#==========List of Themes==========#
mytheme=['Theme_Dark', 'Theme_Light', 'Theme_Color']

#===========Save Image Function==========#
def save_element_as_file(element, filename):
    """
    Saves any element as an image file.  Element needs to have an underlyiong Widget available (almost if not all of them do)
    :param element: The element to save
    :param filename: The filename to save to. The extension of the filename determines the format (jpg, png, gif, ?)
    """
    widget = element.Widget
    box = (widget.winfo_rootx(), widget.winfo_rooty(), widget.winfo_rootx() + widget.winfo_width(), widget.winfo_rooty() + widget.winfo_height())
    grab = ImageGrab.grab(bbox=box,all_screens=True)
    grab.save(filename)
       
#==========Make Window==========#
def make_window(use_fade_in=True, alpha=1):
    left= [
            [sg.Graph((100,100), (0,100), (100,0), key='-GRAPH-',expand_x=1)],
            [sg.Text('Preview selection:',justification='center',expand_x=1,font=('Arial',10))],
            [sg.Graph((100,20),(0,100),(100,0),k='preview',background_color='#000000',expand_y=1,expand_x=1)],
            
            ]

    list = sg.user_settings_get_entry('-list-', [])
    right = [
            [sg.Table(values=list, headings=['Hex Color'],
            num_rows=10,
            hide_vertical_scroll=True,
            sbar_relief='flat',
            k='-row-',
            justification='right',
            def_col_width=200,
            max_col_width=200,header_relief=0,
            border_width=0,
            header_background_color='#ffffff',
            header_text_color='#000000',
            background_color='#000000',
            enable_events=True,
            selected_row_colors='#e7e7e7 on #353535',
            
            select_mode=sg.TABLE_SELECT_MODE_BROWSE,
            expand_x=1,
            expand_y=1,
            font=('Arial',11)
            ) ],
            
            ]

    menu = [
            
            [sg.Button('Save Palette as Image',  key='-SAVE-', expand_y=1,expand_x=1,p=1,font=('Arial',10)),
             sg.OptionMenu(mytheme,
                      default_value = sg.user_settings_get_entry('-theme-', 'Theme_Dark'),
                      key='-BMENU-',
                      expand_y=1,expand_x=1,p=1,auto_size_text=True,
                     ),
             sg.Button('Info',  key='-INFO-', expand_y=1,expand_x=1,p=1,font=('Arial',10)),        
                     
                     
                     ],
             
            ]

    palette = [

            [sg.Graph((100,34.6),(0,100),(100,0),k='palette',background_color='#000000',expand_y=1,expand_x=1,enable_events=True)],
            ]


    buttons = [
                [sg.Button('Copy',k='-selection-', border_width=0,expand_x=1,p=1,font=('Arial',10)),
                sg.Button('Copy  All',k='-all-', border_width=0, expand_x=1,p=1,font=('Arial',10)),
                sg.Button('Delete',k='-delete-', border_width=0,expand_x=1,p=1,font=('Arial',10)),
                sg.Button('Delete  All',k='deletebuttonall', border_width=0,expand_x=1,p=1,font=('Arial',10))]
                ]
    



    layout = [ 
             [sg.Frame('', menu,border_width=0,element_justification='left',size=(319, 27)),],
              
             [ sg.Frame('Picker', left,border_width=2,expand_y=1,expand_x=1,element_justification='center',font=('Arial',10)),
              sg.Frame('List', right,border_width=2,expand_y=1,expand_x=1,k='W2',element_justification='center',font=('Arial',10))],
             [ sg.Frame('', buttons,border_width=0,element_justification='left',size=(319, 27)),],
             [sg.Frame('Palette', palette,border_width=2,element_justification='left',expand_x=1,expand_y=1),],
               
                
            ]
    
    window = sg.Window('PSG_Color_Picker',
                        layout, keep_on_top=True,no_titlebar=False,
                        grab_anywhere=False,
                        finalize=True,
                        enable_close_attempted_event=True,
                        icon=b'iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAAFRmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS41LjAiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIgogICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIgogICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iCiAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyIKICAgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIKICAgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9InNSR0IgSUVDNjE5NjYtMi4xIgogICB4bXA6TW9kaWZ5RGF0ZT0iMjAyMi0xMS0yMlQxMjowOTowMiswMTowMCIKICAgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMi0xMS0yMlQxMjowOTowMiswMTowMCIKICAgdGlmZjpYUmVzb2x1dGlvbj0iNzIvMSIKICAgdGlmZjpZUmVzb2x1dGlvbj0iNzIvMSIKICAgdGlmZjpSZXNvbHV0aW9uVW5pdD0iMiIKICAgdGlmZjpJbWFnZVdpZHRoPSI1MTIiCiAgIHRpZmY6SW1hZ2VMZW5ndGg9IjUxMiIKICAgZXhpZjpDb2xv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',
                        location=sg.user_settings_get_entry('-location-', (None, None)),
                        font=('Arial',10),
                        alpha_channel=0
                       )




    if use_fade_in == True:
        for i in range(1,int(alpha*100)):               # fade in
            window.set_alpha(i/100)
            event, values = window.read(timeout=0.3)
            if event != sg.TIMEOUT_KEY:
                window.set_alpha(1)
                break
           
        
        
    else:
        window.set_alpha(alpha)
        
#==========Short Keys==========#
    window.bind('<F3>', '-COPY-')
    window.bind('<Escape>', 'stop')
#==============================#
    xc=0
    yc=0
    ac=30.4
    bc=98
    listx = []
    listx.clear()
    for color in list:
        window['palette'].draw_rectangle((xc,yc),(ac,bc), fill_color=color,line_color=None)
        xc+=30.4
        yc+=0
        ac+=30.4
        bc+=0  
        listx.append(xc)
    while True:
        event, values = window.read(timeout=100)       
        if event in ('Exit', sg.WINDOW_CLOSE_ATTEMPTED_EVENT) or event == sg.WIN_CLOSED:
            sg.user_settings_set_entry('-location-', window.current_location())  # The line of code to save the position before exiting
            sg.user_settings_set_entry('-theme-', values['-BMENU-'])
            sg.user_settings_set_entry('-list-', list) 
            break
        #window.force_focus()
        pos = pg.position()
        x = pos[0]
        y= pos[1]
        rgb = PIL.ImageGrab.grab(include_layered_windows=True, all_screens=True).load()[x, y]
        hex_color = sg.rgb(*rgb)           
        window['-GRAPH-'].update(background_color=hex_color)
#==========Events==========#
        if event == '-COPY-':
            if len(list)>9:
                x,y = window.current_location()
                loc=(x+10,y+35)
                sg.popup_ok('Max 10 colors!',    
                        background_color='#e77534',
                        grab_anywhere=False,
                        text_color='white',
                        keep_on_top=True,
                        font=('Arial',10),
                        no_titlebar=True,
                        non_blocking=False,
                        location=loc
                        )   
            else:
                window['-row-'].enable_events=False
                window['preview'].update(background_color='#000000')
                sg.clipboard_set(hex_color)
                list.append(hex_color.upper())
                window['-row-'].update(list) 
                window['palette'].draw_rectangle((xc,yc),(ac,bc), fill_color=hex_color,line_color=None) 
                xc+=30.4
                yc+=0
                ac+=30.4
                bc+=0  
                listx.append(xc)            
        if event == '-selection-': 
            val= values['-row-']
            if val != []:
                x,y = window.current_location()
                loc=(x+150,y+100)
                sg.clipboard_set(list[val[0]]) 
                sg.popup_no_buttons('Copied',
                            background_color='#e77534',
                            no_titlebar=True,
                            grab_anywhere=False,
                            text_color='white',
                            keep_on_top=True,
                            font=('Arial',10),
                            auto_close=True,
                            auto_close_duration=1,
                            location=loc,
                            non_blocking=False,) 
            else:
                x,y = window.current_location()
                loc=(x+110,y+100) 
                sg.popup_no_buttons('Please select a color',
                            background_color='#e77534',
                            no_titlebar=True,
                            grab_anywhere=False,
                            text_color='white',
                            keep_on_top=True,
                            font=('Arial',10),
                            auto_close=True,
                            auto_close_duration=2,
                            location=loc,
                            non_blocking=False,)    
        if event == '-row-':
            val= values['-row-']
            if val != []:
                window['preview'].update(background_color=list[val[0]])
            else:
                pass
        if event == '-delete-': 
            val= values['-row-']
            if val != []:
                list.pop(val[0])
                window['-row-'].update(list) 
                window['preview'].update(background_color='#000000')
                ixc = listx[val[0]]  
                select_figure = window['palette'].get_figures_at_location((ixc-5,0))
                window['palette'].delete_figure(select_figure)
                xc-=30.4
                yc-=0
                ac-=30.4
                bc-=0  
                listx.pop(val[0])
                window['palette'].erase()
                xc=0
                yc=0
                ac=30.4
                bc=98
                listx.clear()
                for color in list:
                    window['palette'].draw_rectangle((xc,yc),(ac,bc), fill_color=color,line_color=None)
                    xc+=30.4
                    yc+=0
                    ac+=30.4
                    bc+=0  
                    listx.append(xc)
            else:
                pass 
        if event =='deletebuttonall': 
                list.clear()
                window['palette'].erase()
                window['-row-'].update(list) 
                window['preview'].update(background_color='#000000')
                xc=0
                yc=0
                ac=30.4
                bc=98
                listx.clear()


        if event == '-all-':
            if list != []:
                x,y = window.current_location()
                loc=(x+150,y+100)
                sg.clipboard_set(', '.join(list))
                sg.popup_no_buttons('Copied',
                            background_color='#e77534',
                            no_titlebar=True,
                            grab_anywhere=False,
                            text_color='white',
                            keep_on_top=True,
                            font=('Arial',10),
                            auto_close=True,
                            auto_close_duration=1,
                            location=loc,
                            non_blocking=False)
            else:
                x,y = window.current_location()
                loc=(x+120,y+100)
                sg.popup_no_buttons('Nothing to Copy',
                            background_color='#e77534',
                            no_titlebar=True,
                            grab_anywhere=False,
                            text_color='white',
                            keep_on_top=True,
                            font=('Arial',10),
                            auto_close=True,
                            auto_close_duration=2,
                            location=loc,
                            non_blocking=False)
                
        if event == 'stop':
            x,y = window.current_location()
            loc=(x+105,y+100)
            answer = sg.popup_yes_no('Restore Picking',
                        background_color='#e77534',
                        no_titlebar=True,
                        grab_anywhere=False,
                        text_color='white',
                        keep_on_top=True,
                        font=('Arial',10),
                        location=loc,
                        non_blocking=False)
            if answer == 'No': 
                theme= sg.theme(values['-BMENU-'])
                sg.user_settings_set_entry('-location-', window.current_location())  # The line of code to save the position before exiting
                sg.user_settings_set_entry('-theme-', theme)
                sg.user_settings_set_entry('-list-', list) 
                break                   
        if event == '-INFO-':
            x,y = window.current_location()
            loc=(x+83,y+100)
            sg.popup_ok('PSG Color Picker by CVS78\nPowered By PySimple GUI\n\nShortkeys:\n- F3 = Pick Hex Color\n- Escape = Stop Picking',
                        no_titlebar=True,
                        grab_anywhere=False,
                        keep_on_top=True,
                        font=('Arial',10),
                        location=loc,
                        non_blocking=False) 
        if event == '-SAVE-' :
            filename = sg.popup_get_file('', save_as=True,
                                        no_window=True,
                                        default_extension='.png',
                                        initial_folder='.',
                                        file_types=(('*.png','*.*'),))
            if filename != '':
                save_element_as_file(window['palette'], filename)
                x,y = window.current_location()
                loc=(x+130,y+100)
                sg.popup_ok('Image saved',
                            background_color='#e77534',
                            no_titlebar=True,
                            grab_anywhere=False,
                            text_color='white',
                            keep_on_top=True,
                            font=('Arial',10),
                            location=loc,
                            non_blocking=False)
            else:
                pass
        if values['-BMENU-'] != sg.theme():
            x,y = window.current_location()
            loc=(x+105,y+100)
            answer = sg.popup_ok('The App must close\nfor apply changes!',
                        background_color='#e77534',
                        no_titlebar=True,
                        grab_anywhere=False,
                        text_color='white',
                        keep_on_top=True,
                        font=('Arial',10),
                        location=loc,
                        non_blocking=False) 
            theme= sg.theme(values['-BMENU-'])
            sg.user_settings_set_entry('-location-', window.current_location())  # The line of code to save the position before exiting
            sg.user_settings_set_entry('-theme-', theme)
            sg.user_settings_set_entry('-list-', list) 
            break
            
                
            
                
        
            
    window.close()




#==========Main==========# 
def main():
    make_window(use_fade_in=True,alpha=1)
    
if __name__ == '__main__':
    main()


