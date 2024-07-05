from rest_framework import serializers

from .models import Header, Navbar, Tarif, Travel


class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class NavbarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'


class NavbarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = '__all__'


class NavbarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'