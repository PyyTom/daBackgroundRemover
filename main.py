from rembg import remove
from PIL import Image
import flet as fl
def main(page:fl.Page):
    def xit(e):
        page.window_destroy()
    def select(e:fl.FilePickerResultEvent):
        if e.files is not None:
            selected=''
            for f in e.files:
                selected+=(f.path).split('/')[-1]+'\n'
                input = Image.open(f.path)
                output = remove(input)
                output.save((f.path).split('.')[0] + '_w_bg.' + (f.path).split('.')[1])
            page.dialog = d
            d.content=fl.Text(selected)
            d.open = True
            page.update()
    d = fl.AlertDialog(title=fl.Text('BACKGROUND SUCCESSFULLY REMOVED FROM:'))
    filepicker=fl.FilePicker(on_result=select)
    page.overlay.append(filepicker)
    page.add(fl.Row(controls=[fl.Text('DA BACKGROUND REMOVER')],alignment=fl.MainAxisAlignment.CENTER),
             fl.Row(controls=[fl.ElevatedButton('SELECT FILES',on_click=lambda _:filepicker.pick_files(allow_multiple=True))],alignment=fl.MainAxisAlignment.CENTER),
             fl.Row(controls=[fl.IconButton(on_click=xit,icon=fl.icons.EXIT_TO_APP,icon_color='red',icon_size=50)],alignment=fl.MainAxisAlignment.CENTER))
fl.app(target=main)