from review.models import Review #Database
from .serializers import ReviewSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

# class ReviewUserWritePermission(BasePermission):              #Not in Use
#     message = 'Editing '

#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.author == request.user




### GENERIC VIEWS ###
class ReviewList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(author=user)
        return Review.objects
    


class ReviewDetail(generics.RetrieveAPIView):   #RetrieveAPIView only seems to work when pk = int
    serializer_class = ReviewSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Review, slug=item)

    # def get_queryset(self):                                # different method
    #     slug = self.request.query_params.get('slug', None) # removes necessity to use <str:pk>
    #     return Review.objects.filter(slug=slug)

class ReviewListDetailfilter(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.SearchFilter] #similar to ?slug = ...
    search_fields = ['^slug']


class CreateReview(APIView):
    permission_classes = [IsAuthenticated]    #Disable when testing
    parser_classes = [MultiPartParser, FormParser] #FileUploadParser exists, but we're uploading text & image. 

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminReviewDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class EditReview(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class DeleteReview(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer