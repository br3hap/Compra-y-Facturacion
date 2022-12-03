from django.shortcuts import render, redirect

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model =  Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    # permission_required="inv.add_categoria"
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    # success_message="Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    # permission_required="inv.change_categoria"
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    # success_message="Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    permission_required="inv.delete_categoria"
    model=Categoria
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:categoria_list")
    # success_message="Categoría Eliminada Satisfactoriamente"


class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model =  SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    # permission_required="inv.add_categoria"
    model=SubCategoria
    template_name="inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    # success_message="Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    # permission_required="inv.change_categoria"
    model=SubCategoria
    template_name="inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    # success_message="Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    permission_required="inv.delete_categoria"
    model=SubCategoria
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:subcategoria_list")
    # success_message="Categoría Eliminada Satisfactoriamente"


class MarcaView(LoginRequiredMixin, generic.ListView):
    model =  Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class MarcaNew(LoginRequiredMixin, generic.CreateView):
    # permission_required="inv.add_categoria"
    model=Marca
    template_name="inv/marca_form.html"
    context_object_name = "obj"
    form_class=MarcaForm
    success_url=reverse_lazy("inv:marca_list")
    # success_message="Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    # permission_required="inv.change_categoria"
    model=Marca
    template_name="inv/marca_form.html"
    context_object_name = "obj"
    form_class=MarcaForm
    success_url=reverse_lazy("inv:marca_list")
    # success_message="Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

# class MarcaDel(LoginRequiredMixin, generic.DeleteView):
#     permission_required="inv.delete_categoria"
#     model=SubCategoria
#     template_name='inv/catalogos_del.html'
#     context_object_name='obj'
#     success_url=reverse_lazy("inv:marca_list")
    # success_message="Categoría Eliminada Satisfactoriamente"

def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/catalogos_del.html'

    if not marca:
        return redirect("inv:marca_list")
    
    if request.method =='GET':
        contexto = {'obj':marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        return redirect("inv:marca_list")

    return render(request, template_name, contexto )


class UMView(LoginRequiredMixin, generic.ListView):
    model =  UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class UMNew(LoginRequiredMixin, generic.CreateView):
    # permission_required="inv.add_categoria"
    model = UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = "obj"
    form_class=UnidadMedidaForm
    success_url=reverse_lazy("inv:um_list")
    # success_message="Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class UMEdit(LoginRequiredMixin, generic.UpdateView):
    # permission_required="inv.change_categoria"
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = "obj"
    form_class=UnidadMedidaForm
    success_url=reverse_lazy("inv:um_list")
    # success_message="Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/catalogos_del.html'

    if not um:
        return redirect("inv:um_list")
    
    if request.method =='GET':
        contexto = {'obj':um}

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect("inv:um_list")

    return render(request, template_name, contexto )


class ProductoView(LoginRequiredMixin, generic.ListView):
    model =  Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class ProductoNew(LoginRequiredMixin, generic.CreateView):
    # permission_required="inv.add_categoria"
    model = Producto
    template_name="inv/producto_form.html"
    context_object_name = "obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    # success_message="Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    # permission_required="inv.change_categoria"
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = "obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    # success_message="Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/catalogos_del.html'

    if not prod:
        return redirect("inv:producto_list")
    
    if request.method =='GET':
        contexto = {'obj':prod}

    if request.method == 'POST':
        prod.estado = False
        prod.save()
        return redirect("inv:producto_list")

    return render(request, template_name, contexto )

