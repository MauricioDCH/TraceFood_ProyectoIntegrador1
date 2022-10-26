from django.shortcuts import render

from pymongo import MongoClient
client = MongoClient('mongodb+srv://vguerraz:TwD374X@cluster0.ieqcc.mongodb.net/test')
db = client['TraceFood']

from traceFoodApp.models import Proveedor, Res, Producto, Ficha_Recepcion, Reporte

def resesView(request):
    reses = Res.objects.all()
    return render(request, 'resesView.html', {'reses' : reses})

def resesEdit(request, res_id):
    res = Res.objects.filter(id=res_id)
    return render(request, 'resesEdit.html', {'res': res})

def resesForm(request):
    if request.method == 'POST':
        peso = request.POST.get("peso")
        nacimiento = request.POST.get("fecha_nacimiento")
        muerte = request.POST.get("fecha_muerte")
        granja = request.POST.get("id_granja")
        estado = request.POST.get("estado")
        r = Res(id_granja=granja, fecha_nacimiento=nacimiento, fecha_muerte=muerte, peso=peso, estado=estado)
        r.save()
    return render(request, 'resesForm.html')

def proveedorForm(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        nit = request.POST.get("nit")
        correo = request.POST.get("correo")
        numero_contacto = request.POST.get("numero_contacto")
        direccion = request.POST.get("direccion")
        municipio = request.POST.get("municipio")
        departamento = request.POST.get("departamento")
        pais = request.POST.get("pais")
        certificaciones = request.POST.get("certificaciones")
        rol = request.POST.get("rol")
        p = Proveedor(nit=nit, nombre=nombre, correo=correo, 
        numero_contacto=numero_contacto, direccion=direccion, municipio=municipio,
        departameno=departamento, pais=pais, certificaciones=certificaciones, rol=rol)
        p.save()
    return render(request, 'proveedorForm.html')
    #return redirect("distribuidorForm.html")

def recepcionForm(request):
    if request.method == 'POST':
        receptor = request.POST.get("id_receptor")
        producto = request.POST.get("id_producto")
        fecha = request.POST.get("fecha_recepcion")
        direccion = request.POST.get("direccion_recepcion")
        temperatura = request.POST.get("temperatura")
        estado = request.POST.get("estado")
        comentarios = request.POST.get("comentarios")
        res = request.POST.get("id_res")
        if res == "0":
            res = Producto.objects.filter(id_producto=producto).values_list('id_res')

        f = Ficha_Recepcion(id_receptor = receptor, id_res = res, id_producto = producto, fecha_recepcion = fecha,
        direccion_recepcion = direccion, temperatura = temperatura, estado = estado, comentarios = comentarios)
        f.save()
    return render(request, 'fichaRecepcionForm.html')