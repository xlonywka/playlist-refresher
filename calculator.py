import ipcalc
def calc(ip):
    mas = []
    for x in ipcalc.Network(str(ip)+'/24'):
        mas.append(x)
    return(mas)
