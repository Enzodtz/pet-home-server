from core.models import Pet, PetImage
from rest_framework import permissions, serializers, status
from rest_framework.response import Response


class PetSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = "__all__"
        extra_kwargs = {
            "user": {
                "default": serializers.CurrentUserDefault(),
            },
        }

    def get_images(self, pet):
        images = PetImage.objects.filter(pet=pet)

        urls = []
        for image_obj in images:
            urls.append(image_obj.image.url)

        return urls

    def validate(self, data):
        request = self.context.get("request")

        images = request.FILES.getlist("images")

        if len(images) > 0:
            data["images"] = images
            return data
        else:
            raise serializers.ValidationError({"images": "You must submit an image."})

    def create(self, validated_data):
        images = validated_data.pop("images")

        pet = Pet.objects.create(**validated_data)

        for image in images:
            PetImage.objects.create(image=image, pet=pet)

        return pet
