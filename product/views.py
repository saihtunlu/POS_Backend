from .models import Product,  Tag, Vendor, ProductImage, Variation, Option
from location.models import LocationProduct, Location
from location.serializers import LocationProductSerializers
import json
from category.models import Category2
from account.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics, pagination
from rest_framework.response import Response
from .serializers import ProductSerializers, ProductImageSerializers, ExportProductSerializers, VariationSerializers, TagSerializers, OptionSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser


class Products(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        product_serializer = ProductSerializers(product, many=True)
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)


class SingleProduct(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        mainData = request.data
        data = json.loads(mainData['product'])
        print(data)
        images = data['images']
        locations = data['locations']
        variations = data['variations']
        options = data['options']
        obj, created = Category2.objects.get_or_create(
            label=data['category']
        )
        if not created:
            category_rs = obj
        else:
            category_rs = created
        tagsArray = []
        for tag in data['tags']:
            instanceTag, createdTag = Tag.objects.get_or_create(
                name=tag
            )
            if not createdTag:
                tagsArray.append(instanceTag)
            else:
                tagsArray.append(createdTag)

        instanceVendor, createdVendor = Vendor.objects.get_or_create(
            name=data['vendor']
        )
        if not createdVendor:
            vendor_rs = instanceVendor
        else:
            vendor_rs = createdVendor
        product = Product.objects.create(
            vendor=vendor_rs, category=category_rs)
        product.tags.set(tagsArray)
        product_serializer = ProductSerializers(product, data=data)
        if product_serializer.is_valid():
            product_serializer.save()
            if images:
                for number in range(len(images)):
                    new_image = ProductImage(product=product)
                    array = {"image": None}
                    array['image'] = mainData['image'+str(number)]
                    image_serializer = ProductImageSerializers(
                        new_image, data=array)
                    if image_serializer.is_valid():
                        image_serializer.save()
            if locations and len(locations) > 0:
                for location in locations:
                    selected_location = get_object_or_404(
                        Location, id=int(location['location']))
                    new_location = LocationProduct(
                        product=product, location=selected_location)
                    location_serializer = LocationProductSerializers(
                        new_location, data=location)
                    if location_serializer.is_valid():
                        location_serializer.save()
            if options:
                for option in options:
                    new_option = Option(product=product)
                    option_serializer = OptionSerializers(
                        new_option, data=option)
                    if option_serializer.is_valid():
                        option_serializer.save()
            if product.has_variant == True:
                for variation in variations:
                    variation_locations = variation['locations']
                    new_variation = Variation(product=product)
                    variation_serializer = VariationSerializers(
                        new_variation, data=variation)
                    if variation_serializer.is_valid():
                        variation_serializer.save()
                        if variation_locations:
                            for variation_location in variation_locations:
                                if variation_location['location'] != None:
                                    selected_variation_location = get_object_or_404(
                                        Location, id=variation_location['location'])
                                    new_variation_location = LocationProduct(
                                        variation_product=new_variation, location=selected_variation_location)
                                    variation_location_serializer = LocationProductSerializers(
                                        new_variation_location, data=variation_location)
                                    if variation_location_serializer.is_valid():
                                        variation_location_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        data = request.data
        images = data['new_images']
        variations = data['new_variations']
        options = data['new_options']
        product = get_object_or_404(
            Product, id=data['id'])
        if data['is_change_tags'] == True:
            tagsArray = []
            for tag in data['tags']:
                instanceTag, createdTag = Tag.objects.get_or_create(
                    name=tag
                )
                if not createdTag:
                    tagsArray.append(instanceTag)
                else:
                    tagsArray.append(createdTag)
            product.tags.set(tagsArray)
        if data['is_change_vendor'] == True:
            instanceVendor, createdVendor = Vendor.objects.get_or_create(
                name=data['vendor']
            )
            if not createdVendor:
                vendor_rs = instanceVendor
            else:
                vendor_rs = createdVendor
            product.vendor = vendor_rs
        if data['is_change_category'] == True:
            obj, created = Category2.objects.get_or_create(
                label=data['category']
            )
            if not created:
                category_rs = obj
            else:
                category_rs = created
            product.category = category_rs
        product_serializer = ProductSerializers(product, data=data)
        if product_serializer.is_valid():
            product_serializer.save()
            if images and data['is_change_images'] == True:
                ProductImage.objects.filter(product=product).delete()
                for image in images:
                    new_image = ProductImage(product=product)
                    image_serializer = ProductImageSerializers(
                        new_image, data=image)
                    if image_serializer.is_valid():
                        image_serializer.save()
            if options and data['is_change_options'] == True:
                Option.objects.filter(product=product).delete()
                for option in options:
                    new_option = Option(product=product)
                    option_serializer = OptionSerializers(
                        new_option, data=option)
                    if option_serializer.is_valid():
                        option_serializer.save()
            if product.has_variant == True and data['is_change_variations'] == True:
                Variation.objects.filter(product=product).delete()
                for variation in variations:
                    variation_locations = variation['locations']
                    new_variation = Variation(product=product)
                    variation_serializer = VariationSerializers(
                        new_variation, data=variation)
                    if variation_serializer.is_valid():
                        variation_serializer.save()
                        if variation_locations:
                            for variation_location in variation_locations:
                                selected_variation_location = get_object_or_404(
                                    Location, id=variation_location['location_id'])
                                new_variation_location = LocationProduct(
                                    variation_product=new_variation, location=selected_variation_location)
                                variation_location_serializer = LocationProductSerializers(
                                    new_variation_location, data=variation_location)
                                if variation_location_serializer.is_valid():
                                    variation_location_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        product = get_object_or_404(
            Product, id=id)

        product_serializer = ProductSerializers(product, many=False)
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        Product.objects.all().delete()
        return Response('Success', status=status.HTTP_201_CREATED)


class Tags(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    tag_query = get_object_or_404(
        Tag, id=1)
    queryset = tag_query.product_set.all()
    serializer_class = TagSerializers
    pagination_class = pagination.PageNumberPagination


class SingleTag(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        array = []
        for tag in data:
            check = Tag.objects.filter(name=tag['name'])
            if not check:
                tag_serializer = TagSerializers(data=tag, many=False)
                if tag_serializer.is_valid():
                    tag_serializer.save()
                    array.append(tag_serializer.data)
            else:
                tag_serializer = TagSerializers(check[0], many=False)
                array.append(tag_serializer.data)
        return Response(array, status=status.HTTP_201_CREATED)


class ExportToCSV(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        selected_products = request.data['data']
        product = Product.objects.filter(pk__in=selected_products)
        product_serializer = ExportProductSerializers(product, many=True)
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)


class ImportProduct(APIView):
    # parser_classes = [MultiPartParser]
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        products = request.data['data']
        condition = request.data['condition']
        if condition == "AddNew":
            for data in products:
                check = Product.objects.filter(
                    name=data['name'], sku=data['sku'])
                if not check:
                    images = data['images']
                    locations = data['locations']
                    variations = data['variations']
                    options = data['options']
                    obj, created = Category2.objects.get_or_create(
                        label=data['category']
                    )
                    if not created:
                        category_rs = obj
                    else:
                        category_rs = created
                    tags = []
                    for num in range(len(data['tags'])):
                        tags.append(data['tags'][str(num)])
                    tagsArray = []
                    for tag in tags:
                        instanceTag, createdTag = Tag.objects.get_or_create(
                            name=tag
                        )
                        if not createdTag:
                            tagsArray.append(instanceTag)
                        else:
                            tagsArray.append(createdTag)
                    instanceVendor, createdVendor = Vendor.objects.get_or_create(
                        name=data['vendor']
                    )
                    if not createdVendor:
                        vendor_rs = instanceVendor
                    else:
                        vendor_rs = createdVendor

                    product = Product.objects.create(
                        vendor=vendor_rs, category=category_rs)
                    product.tags.set(tagsArray)
                    product_serializer = ProductSerializers(product, data=data)
                    if product_serializer.is_valid():
                        product_serializer.save()
                        if images:
                            for number in range(len(images)):
                                new_image = ProductImage(product=product)
                                image_serializer = ProductImageSerializers(
                                    new_image, data=images[str(number)])
                                if image_serializer.is_valid():
                                    image_serializer.save()
                                else:
                                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        if locations:
                            for number in range(len(locations)):
                                selected_location = get_object_or_404(
                                    Location, id=int(locations[str(number)]['location']))
                                new_location = LocationProduct(
                                    product=product, location=selected_location)
                                location_serializer = LocationProductSerializers(
                                    new_location, data=locations[str(number)])
                                if location_serializer.is_valid():
                                    location_serializer.save()
                                else:
                                    return Response(location_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        if options:
                            for number in range(len(options)):
                                new_option = Option(product=product)
                                option_serializer = OptionSerializers(
                                    new_option, data=options[str(number)])
                                if option_serializer.is_valid():
                                    option_serializer.save()
                                else:
                                    return Response(option_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        if variations:
                            for number in range(len(variations)):
                                if variations[str(number)]['variation_name']:
                                    variation_locations = variations[str(
                                        number)]['locations']
                                    new_variation = Variation(product=product)
                                    variation_serializer = VariationSerializers(
                                        new_variation, data=variations[str(number)])
                                    if variation_serializer.is_valid():
                                        variation_serializer.save()
                                        if variation_locations:
                                            for location_number in range(len(variation_locations)):
                                                selected_variation_location = get_object_or_404(
                                                    Location, id=variation_locations[str(location_number)]['location'])
                                                new_variation_location = LocationProduct(
                                                    variation_product=new_variation, location=selected_variation_location)
                                                variation_location_serializer = LocationProductSerializers(
                                                    new_variation_location, data=variation_locations[str(location_number)])
                                                if variation_location_serializer.is_valid():
                                                    variation_location_serializer.save()
                                                else:
                                                    return Response(variation_location_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                    else:
                                        return Response(variation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if condition == "Override":
            for data in products:
                product = Product.objects.get(
                    name=data['name'], sku=data['sku'])
                if product:
                    images = data['images']
                    locations = data['locations']
                    variations = data['variations']
                    options = data['options']
                    obj, created = Category2.objects.get_or_create(
                        label=data['category']
                    )
                    if not created:
                        category_rs = obj
                    else:
                        category_rs = created
                    tags = []
                    for num in range(len(data['tags'])):
                        tags.append(data['tags'][str(num)])
                    tagsArray = []
                    for tag in tags:
                        instanceTag, createdTag = Tag.objects.get_or_create(
                            name=tag
                        )
                        if not createdTag:
                            tagsArray.append(instanceTag)
                        else:
                            tagsArray.append(createdTag)
                    instanceVendor, createdVendor = Vendor.objects.get_or_create(
                        name=data['vendor']
                    )
                    if not createdVendor:
                        vendor_rs = instanceVendor
                    else:
                        vendor_rs = createdVendor
                    product.vendor = vendor_rs
                    product.category = category_rs
                    product.tags.set(tagsArray)
                    product_serializer = ProductSerializers(product, data=data)
                    if product_serializer.is_valid():
                        product_serializer.save()
                        if images:
                            ProductImage.objects.filter(
                                product=product).delete()
                            for number in range(len(images)):
                                new_image = ProductImage(product=product)
                                image_serializer = ProductImageSerializers(
                                    new_image, data=images[str(number)])
                                if image_serializer.is_valid():
                                    image_serializer.save()
                                else:
                                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        if locations:
                            LocationProduct.objects.filter(
                                product=product).delete()
                            for number in range(len(locations)):
                                selected_location = get_object_or_404(
                                    Location, id=int(locations[str(number)]['location']))
                                new_location = LocationProduct(
                                    product=product, location=selected_location)
                                location_serializer = LocationProductSerializers(
                                    new_location, data=locations[str(number)])
                                if location_serializer.is_valid():
                                    location_serializer.save()
                                else:
                                    return Response(location_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        if options:
                            Option.objects.filter(product=product).delete()
                            for number in range(len(options)):
                                new_option = Option(product=product)
                                option_serializer = OptionSerializers(
                                    new_option, data=options[str(number)])
                                if option_serializer.is_valid():
                                    option_serializer.save()
                                else:
                                    return Response(option_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        if variations:
                            Variation.objects.filter(product=product).delete()
                            for number in range(len(variations)):
                                if variations[str(number)]['variation_name']:
                                    variation_locations = variations[str(
                                        number)]['locations']
                                    new_variation = Variation(product=product)
                                    variation_serializer = VariationSerializers(
                                        new_variation, data=variations[str(number)])
                                    if variation_serializer.is_valid():
                                        variation_serializer.save()
                                        if variation_locations:
                                            for location_number in range(len(variation_locations)):
                                                selected_variation_location = get_object_or_404(
                                                    Location, id=variation_locations[str(location_number)]['location'])
                                                new_variation_location = LocationProduct(
                                                    variation_product=new_variation, location=selected_variation_location)
                                                variation_location_serializer = LocationProductSerializers(
                                                    new_variation_location, data=variation_locations[str(location_number)])
                                                if variation_location_serializer.is_valid():
                                                    variation_location_serializer.save()
                                                else:
                                                    return Response(variation_location_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                    else:
                                        return Response(variation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response('Success', status=status.HTTP_201_CREATED)
