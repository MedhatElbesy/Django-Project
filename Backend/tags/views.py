from django.shortcuts import render,get_object_or_404, reverse, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import TagsSerializer
from .models import Tags
from tags.form import TagModelForm

# Create your views here.

class TagsViewSet(viewsets.ModelViewSet):
  queryset = Tags.objects.all()
  serializer_class = TagsSerializer

  def retrieve(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      return Response(serializer.data)
    except Tags.DoesNotExist:
      return Response({'error': 'Tags not found'}, status=status.HTTP_404_NOT_FOUND)

  def create(self, request):
    try:
      serializer = TagsSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def show(self, request, id):
    try:
      project = Tags.objects.get(id=id)
      serializer = TagsSerializer(project)
      return Response(serializer.data)
    except Tags.DoesNotExist:
      return Response({'error': 'Tags Not Found'}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    try:
      payment = Tags.objects.all()
      serializer = TagsSerializer(payment, many=True)
      return Response(serializer.data)
    except Tags.DoesNotExist:
      return Response({'error': 'No Tags found'}, status=status.HTTP_404_NOT_FOUND)
    
  def update(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      serializer = self.get_serializer(instance, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
    except Tags.DoesNotExist:
      return Response({'error': 'Tags not found'}, status=status.HTTP_404_NOT_FOUND)

  def delete(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      instance.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    except Tags.DoesNotExist:
      return Response({'error': 'Tags Not Found'}, status=status.HTTP_404_NOT_FOUND)

# Tags Dashboard Crud Operations
def index(request):
  tags = Tags.objects.all()
  return render(request, template_name="tags/crud/index.html",
  context={"tags": tags})

def tag_create(request):
  form = TagModelForm()
  if request.method == "POST":
    form = TagModelForm(request.POST ,request.FILES)
    if form.is_valid():
      tag = form.save()
      return redirect(tag.show_url)
  return render(request , template_name="tags/crud/create.html"
    ,context={"form": form})

def tag_update(request, id):
  tag = get_object_or_404(Tags, pk=id)
  if request.method == "POST":
      tag.name = request.POST["name"]
      tag.save()
      url = reverse("tag-show", args=[id])
      return redirect(url)
  return render(request, template_name="tags/crud/update.html", context= {"tag": tag})

def tag_show(request, id):
  tag = get_object_or_404(Tags, pk=id)
  return render(request, template_name="tags/crud/show.html",
  context={"tag": tag})

def tag_delete(request,id):
  tag = get_object_or_404(Tags, pk=id)
  tag.delete()
  url = reverse("tag-home")
  return redirect(url)