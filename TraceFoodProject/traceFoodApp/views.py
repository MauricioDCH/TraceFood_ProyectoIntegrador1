from django.shortcuts import *
from django.http import *
from pymongo import *

from traceFoodApp.models import Proveedor, Res, Producto, Ficha_Recepcion, Reporte

from pymongo import MongoClient
client = MongoClient('mongodb+srv://vguerraz:TwD374X@cluster0.ieqcc.mongodb.net/test')
db = client['TraceFood']
ress = db['traceFoodApp_res']
prov = db['traceFoodApp_proveedor']
prod = db['traceFoodApp_producto']
recep = db['traceFoodApp_ficha_recepcion']


def home(request):
   return render(request, 'home.html')

def home_secundario(request):
   return render(request, "home_secundario.html")  

def nosotros(request):
   return render(request, "nosotros.html")

def fechas(fecha_ini):
    año = fecha_ini[0:4]
    mes = fecha_ini[5:7]
    dia = fecha_ini[8:10]
    fecha = año + "-" + mes + "-" + dia
    return fecha

def login(request):
    alerta=False
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        usu = Proveedor.objects.get(correo=user)
        if usu.contrasena == password:
            return redirect('perfil', usuario_id = usu.id)
        else:
            alerta=True
    return render(request, 'login.html', {'alerta' : alerta})

def gestion(request, usuario_id):
    return render(request, 'gestion.html', {'usuario_id':usuario_id})

def resesView(request, usuario_id):
    user = Proveedor.objects.get(id=usuario_id)
    reses = Res.objects.all()
    is_granja = False
    if (user.rol == "granja") or (user.rol == "Granja"):
        is_granja = True
        mis_reses = Res.objects.filter(id_granja=usuario_id)
    else:
        is_granja = False
        mis_reses = Res.objects.all()
    return render(request, 'resesView.html', {'reses' : reses, 'mis_reses' : mis_reses, 'is_granja' : is_granja, 'usuario_id' : usuario_id})

def resesForm(request, usuario_id):
    id_granja = Proveedor.objects.get(id=usuario_id)
    if request.method == 'POST':
        peso = request.POST.get("peso")
        nacimiento = request.POST.get("fecha_nacimiento")
        muerte = request.POST.get("fecha_muerte")
        estado = request.POST.get("estado")
        r = Res(id_granja=id_granja, fecha_nacimiento=nacimiento, fecha_muerte=muerte, peso=peso, estado=estado)
        r.save()
        return redirect('resesView', usuario_id = usuario_id)
    return render(request, 'resesForm.html', {'usuario_id' : usuario_id, 'id_granja' : id_granja})
    
def resesEdit(request, res_id):
    res = Res.objects.filter(id=res_id)
    r = {'id' : res.id}
    fecha_ini = str(res.fecha_muerte)
    fecha = fechas(fecha_ini)
    usuario_id = res.id_granja.id
    if request.method == 'POST':
        peso = request.POST.get("peso")
        muerte = request.POST.get("fecha_muerte")
        estado = request.POST.get("estado")
        x = {'$set': {'peso': peso, 'fecha_muerte' : muerte, 'estado': estado}}
        resultado = ress.find_one_and_update(r, x)
        return redirect('resesView', usuario_id = usuario_id)
    return render(request, 'resesEdit.html', {'res': res, 'fecha': fecha, 'usuario_id' : usuario_id})

def productoView(request, usuario_id):
   user = Proveedor.objects.get(id = usuario_id)
   if (user.rol == "planta de desposte") or (user.rol == "planta_desposte") or (user.rol == "Planta de desposte"):
      is_planta = True
      productos = Producto.objects.filter(id_planta=user)
   else:
      is_planta = False
      productos = Producto.objects.all()
   return render(request, 'productoView.html', {'productos' : productos, 'is_planta' : is_planta, 'usuario_id' : usuario_id})

def productoEdit(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    p = {'id' : producto.id}
    usuario_id = producto.id_planta.id
    if request.method == 'POST':
        corte = request.POST.get("corte")
        estado = request.POST.get("estado")
        peso = request.POST.get("peso")
        x = {'$set': {'corte': corte, 'estado' : estado, 'peso': peso}}
        resultado = prod.find_one_and_update(p, x)
        return redirect('productoView', usuario_id = usuario_id)
    return render(request, 'productoEdit.html', {'producto': producto, 'usuario_id' : usuario_id})

def productoForm(request, usuario_id):
    if request.method == 'POST':
        id_res = request.POST.get("id_res")
        parte = request.POST.get("corte")
        estado = request.POST.get("estado")
        peso = request.POST.get("peso")
        id_planta = Proveedor.objects.get(id=usuario_id)
        res = Res.objects.get(id=id_res)
        p = Producto(id_res=res, id_planta=id_planta, parte=parte, estado=estado, peso=peso)
        p.save()
        return redirect('productoView', usuario_id = usuario_id)
    return render(request, 'productoForm.html', {'usuario_id' : usuario_id})

def productoSearch(request):
   productos = Producto.objects.all()
   print(productos)
   return render(request, 'productoSearch.html', {'productos':productos})

def escanear(request):
   return render(request, "escanear.html")

def escanear_productoR(request, usuario_id):
    return render(request, "escanear_productoR.html", {'usuario_id' : usuario_id})

def perfilView(request, usuario_id):
    perfil = Proveedor.objects.get(id=usuario_id)
    return render(request, 'perfil.html', {'p' : perfil, 'usuario_id' : usuario_id})

def proveedorView(request, usuario_id):
    proveedor = Proveedor.objects.all()
    return render(request, 'proveedorView.html', {'proveedor' : proveedor, 'usuario_id' : usuario_id})

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
        contrasena = request.POST.get("contrasena")
        p = Proveedor(nit=nit, nombre=nombre, correo=correo, numero_contacto=numero_contacto, 
        direccion=direccion, municipio=municipio, departamento=departamento, pais=pais, 
        certificaciones=certificaciones, rol=rol, usuario=correo, contrasena=contrasena)
        p.save()
        return redirect('perfil', usuario_id = p.id)
    return render(request, 'proveedorForm.html')

def proveedorEdit(request, usuario_id):
    user = Proveedor.objects.get(id=usuario_id)
    u = {'id' : user.id}
    if request.method == 'POST':
        nit = request.POST.get("nit")
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        numero = request.POST.get("numero_contacto")
        direccion = request.POST.get("direccion")
        municipio = request.POST.get("municipio")
        departamento = request.POST.get("departamento")
        pais = request.POST.get("pais")
        certificaciones = request.POST.get("certificaciones")
        rol = request.POST.get("rol")
        x = {'$set': {'nit': nit, 'nombre' : nombre, 'correo': correo, 'numero_contacto': numero, 
        'direccion' : direccion, 'municipio': municipio, 'departamento' : departamento, 'pais' : pais,
        'certificaciones': certificaciones, 'rol' : rol}}
        resultado = prov.find_one_and_update(u, x)
        return redirect('perfil', usuario_id = usuario_id)
    return render(request, 'proveedorEdit.html', {'proveedor': user, 'usuario_id' : usuario_id})

def recepcionView(request, usuario_id):
    user = Proveedor.objects.get(id=usuario_id)
    fichas = Ficha_Recepcion.objects.filter(id_receptor=user)
    return render(request, 'recepcionView.html', {'fichas' : fichas, 'usuario_id' : usuario_id})

def recepcionForm(request, usuario_id):
    reses = Res.objects.all()
    productos = Producto.objects.all()
    receptor = Proveedor.objects.get(id=usuario_id)
    if (receptor.rol == "matadero") or (receptor.rol == "Matadero") or (receptor.rol == "planta de desposte") or (receptor.rol == "planta_desposte") or (receptor.rol == "Planta de desposte"):
        is_matadero = True
    else:
        is_matadero = False
    if request.method == 'POST':
        if is_matadero:
            id_res = request.POST.get("id_res")
            res = Res.objects.get(id=id_res)
        else:
            id_producto = request.POST.get("id_producto")
            producto = Producto.objects.get(id=id_producto)
            res = Producto.objects.filter(id_producto=producto).values_list('id_res')
        fecha = request.POST.get("fecha_recepcion")
        direccion = request.POST.get("direccion_recepcion")
        temperatura = request.POST.get("temperatura")
        estado = request.POST.get("estado")
        comentarios = request.POST.get("comentarios")
        if is_matadero:
            f = Ficha_Recepcion(id_receptor = receptor, id_res = res, fecha_recepcion = fecha,
            direccion_recepcion = direccion, temperatura = temperatura, estado = estado, comentarios = comentarios)
        else:
            f = Ficha_Recepcion(id_receptor = receptor, id_res = res, id_producto = producto, fecha_recepcion = fecha,
            direccion_recepcion = direccion, temperatura = temperatura, estado = estado, comentarios = comentarios)
        f.save()
        return redirect('recepcionView', usuario_id = usuario_id)
    return render(request, 'recepcionForm.html', {'usuario_id' : usuario_id, 'reses' : reses, 'productos' : productos, 'is_matadero' : is_matadero})
    
def recepcionEdit(request, ficha_id):
    ficha = Ficha_Recepcion.objects.get(id=ficha_id)
    f = {'id' : ficha_id}
    fecha_ini = str(ficha.fecha_recepcion)
    fecha = fechas(fecha_ini)
    usuario_id = ficha.id_receptor.id
    if (ficha.id_receptor.rol == "matadero") or (ficha.id_receptor.rol == "Matadero"):
        is_matadero = True
        id_producto = "0"
    else:
        is_matadero = False
        id_res = "0"
    if request.method == 'POST':
        fecha = request.POST.get("fecha_recepcion")
        direccion = request.POST.get("direccion_recepcion")
        temperatura = request.POST.get("temperatura")
        estado = request.POST.get("estado")
        comentarios = request.POST.get("comentarios")
        x = {'$set': {'fecha':fecha, 'direccion':direccion, 
        'temperatura':temperatura, 'estado':estado, 'comentarios':comentarios}}
        resultado = recep.find_one_and_update(f, x, return_document = ReturnDocument.AFTER)
        print(resultado)
        return redirect('recepcionView', usuario_id = usuario_id)
    return render(request, 'recepcionEdit.html', {'ficha': ficha, 'fecha': fecha, 'usuario_id' : usuario_id, 'is_matadero' : is_matadero})