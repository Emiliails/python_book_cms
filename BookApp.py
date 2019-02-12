uis = {} 

def show_window(name):
    w = uis[name]
    if w:
        w.show()

def hide_window(name):
    w = uis[name]
    if w:
        w.hide()

def get_window(name):
    w = uis[name]
    if w:
        return w
    return NULL
