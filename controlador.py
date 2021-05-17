from factura import Factura

class Controlador:
    def __init__(self):
        self.listaFacturas = {}
        self.productos = {"Naranja":10,"Oliva":20,"Caqui":5}

    def getNumFacturas(self):
        return len(self.listaFacturas)

    def getProductos(self):
        lista=""
        for i in self.productos:
            lista += i+"\n"
        return lista

    def anyadirFactura(self,factura):
        if factura.getId() not in self.listaFacturas:
            self.listaFacturas[factura.getId()] = factura
            return True
        else:
            return False

    def anyadirLineaFactura(self,id,prod,cant):
        if id in self.listaFacturas:
            if prod in self.productos:
                base=self.productos[prod]*int(cant)
                self.listaFacturas[id].anyadirLineaFactura(prod,cant,base)
                return True
        return False



    def mostrarFacturas(self,pagarFactura,op2,dni=""):
        lista=[]
        for clave,valor in self.listaFacturas.items():
            if valor.getPagada()==pagarFactura:
                if op2==1:
                    lista.append("Id_Factura: "+str(clave)+"\nFecha: "+str(valor.getFecha())+"\nNif Emisor: "+valor.getNifE()+"\nNif Receptor: "+valor.getNifR()+"\nLineas Factura: "+valor.mostrarLineasFactura()+"\nBase: "+str(valor.getBase())+"\nIva: "+str(valor.getIVA())+"\nTotal: "+str(valor.getTotal()))
                if op2==2 and valor.getNifE()==dni:
                    lista.append("Id_Factura: "+str(clave)+"\nFecha: "+str(valor.getFecha())+"\nNif Emisor: "+valor.getNifE()+"\nNif Receptor: "+valor.getNifR()+"\nLineas Factura: "+valor.mostrarLineasFactura()+"\nBase: "+str(valor.getBase())+"\nIva: "+str(valor.getIVA())+"\nTotal: "+str(valor.getTotal()))
                if op2==3 and valor.getNifR()==dni:
                    lista.append("Id_Factura: "+str(clave)+"\nFecha: "+str(valor.getFecha())+"\nNif Emisor: "+valor.getNifE()+"\nNif Receptor: "+valor.getNifR()+"\nLineas Factura: "+valor.mostrarLineasFactura()+"\nBase: "+str(valor.getBase())+"\nIva: "+str(valor.getIVA())+"\nTotal: "+str(valor.getTotal()))
    
        return lista



    def facturaPagada(self,id_fact):
        if id_fact in self.listaFacturas:
            self.listaFacturas[id_fact].pagarFactura()
            return True

        return False

    
