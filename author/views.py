from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Author
from .serializers import AuthorSerializer


class AuthorListCreateAPIView(APIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) # manda bu qismda koplab muammola cqdi va shunchun shu bolimni qoshishga majbur bo'ldim

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk): # Butun kod sal zerikarli bo'p qogani uchun bu yoda azgina qiziqarliroq va logichna muhimroq qismni qoshib ketdim ya'ni avtorla kop bo'lganda aynan qaysi birini o'chirish kerakligi haqida soraydi
        author = self.get_object(pk)

        author_name = request.data.get("name")

        if not author_name:
            return Response({"error": "❌ Name is required!"}, status=status.HTTP_400_BAD_REQUEST)

        if author_name.strip().lower() != author.name.lower():
            return Response({"error": "❌ Incorrect name. Please try again."}, status=status.HTTP_400_BAD_REQUEST)

        author.delete()
        return Response({"message": f"✅ Author '{author.name}' deleted successfully"},
                        status=status.HTTP_204_NO_CONTENT)