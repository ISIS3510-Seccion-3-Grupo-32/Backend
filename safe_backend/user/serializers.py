from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializaer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        def create(self, clean_data):
            user_obj = UserModel.objects.create_user(email=clean_data['email'],
                                                     password=clean_data['password'])
            user_obj.username = clean_data['username']
            user_obj.birth_date = clean_data['birth_date']
            user_obj.save()
            return user_obj

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def chek_user(self, clean_data):
        user = authenticate(email=clean_data['email'],
                            password=clean_data['password'])
        if not user:
            raise ValidationError("user not found")
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: UserModel
        fields: ('email', 'username', 'birth_date')