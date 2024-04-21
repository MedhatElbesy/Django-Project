from django.shortcuts import render, get_object_or_404, reverse, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import CategorySerializer
from .models import Category
from categories.form import CategoryModelForm

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  def retrieve(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      return Response(serializer.data)
    except Category.DoesNotExist:
      return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

  def create(self, request):
    try:
      serializer = CategorySerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def show(self, request, id):
    try:
      project = Category.objects.get(id=id)
      serializer = CategorySerializer(project)
      return Response(serializer.data)
    except Category.DoesNotExist:
      return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    try:
      payment = Category.objects.all()
      serializer = CategorySerializer(payment, many=True)
      return Response(serializer.data)
    except Category.DoesNotExist:
      return Response({'error': 'No Category found'}, status=status.HTTP_404_NOT_FOUND)
    
  def update(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      serializer = self.get_serializer(instance, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
    except Category.DoesNotExist:
      return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

  def delete(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      instance.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
      return Response({'error': 'Category Not Found'}, status=status.HTTP_404_NOT_FOUND)

# Crud Operations
def index(request):
  categories = Category.objects.all()
  return render(request, template_name="categories/crud/index.html",
  context={"categories": categories})

def category_create(request):
  form = CategoryModelForm()
  if request.method == "POST":
    form = CategoryModelForm(request.POST ,request.FILES)
    if form.is_valid():
      category = form.save()
      return redirect(category.show_url)
  return render(request , template_name="categories/crud/create.html"
    ,context={"form": form})

def category_update(request, id):
  category = get_object_or_404(Category, pk=id)
  if request.method == "POST":
      category.name = request.POST["name"]
      category.description = request.POST["description"]
      category.save()
      url = reverse("category_index")
      return redirect(url)
  return render(request, template_name="categories/crud/update.html", context= {"category": category})

def category_show(request, id):
  category = get_object_or_404(Category, pk=id)
  return render(request, template_name="categories/crud/show.html",
  context={"category": category})

def category_delete(request,id):
  category = get_object_or_404(Categories, pk=id)
  category.delete()
  url = reverse("category_index")
  return redirect(url)
