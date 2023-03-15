from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from categories.serializers import CategorySerializer
from .models import Category

# from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Categories(APIView):

    # permission_classes =[IsAuthenticatedOrReadOnly]

    def get(self, request):  # 일정 종류에 맞는 일정 조회
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)

        return Response(
            serializer.data,
        )

    def post(self, request):  # 일정 등록, (할일 : 관리자만허용하게 해야 함)
        serializer = CategorySerializer(
            data=request.data,
        )
        if serializer.is_valid() == True:
            new_category = serializer.save()
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


class CategoryDetail(APIView):

    # permission_classes =[IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):  # 관리자만 허용 (할일 : 관리자만허용하게 해야 함)
        serializer = CategorySerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):  # 관리자만 허용 (할일 : 관리자만허용하게 해야 함)
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
