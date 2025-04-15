def on_hover(e):
    e.control.bgcolor = '#edce80' if e.data == 'true' else '#edebe6'
    e.control.update()
