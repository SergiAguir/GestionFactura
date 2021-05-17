class Factura:
    def __init__(self,id,fecha,nifE,nifR):
        self.id = id
        self.fecha = fecha
        self.nifE = nifE
        self.nifR = nifR
        self.pagada = False
        self.base = 0
        self.IVA = 21
        self.total = 0
        self.lFacturas = []

    def getId(self):
        return self.id

    def getFecha(self):
        return self.fecha

    def getNifE(self):
        return self.nifE

    def getNifR(self):
        return self.nifR
    
    def getPagada(self):
        return self.pagada

    def getBase(self):
        return self.base
    
    def getIVA(self):
        return self.IVA

    def getTotal(self):
        return self.total

    def getLFacturas(self):
        return self.lFacturas

    def pagarFactura(self):
        self.pagada = True

    def anyadirLineaFactura(self,prod,cant,base):
        self.base+=base
        self.total=self.base+(self.base*(self.IVA/100))
        self.lFacturas.append((prod,cant,base))

    def mostrarLineasFactura(self):
        lineas=""
        for i in self.lFacturas:
            lineas+=" "+str(i[0])+" "+str(i[1])+" "+str(i[2])+"\n"

        return lineas

    def setTotal(self,total):
        self.total = total