from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'email', 'bio')

        def validate_name(self, value):
            if len(value) < 2:
                raise serializers.ValidationError("Muallif ismi kamida 2 ta harsdan iborat bolishi kerak😂")
            return value

        def validate_email(self, value):
            allowed_domains = ['gmail.com', 'hotmail.com', 'microsoft.com'] #Bu yoda tasavur qse ozimi klientim qanaqa validatsiya sorasa shuni qildim (Misol uchun bu yoqqa har turli gmaillar bilan kirib bolmaydi yoki kompaniya boshqa gmaillarni taqiqlagan yani konkurent kompaniyalarnikini (Masalan olaylik man microsoft bilan ishlavotgan bosam va uni saytidan royxatdan otish uchun faqat ofitsiyalniy google gmail va microsoft gmail kerak boladi. Ma'lumot uchun hotmail microsft niki))
            domain = value.split ('@')[-1] #Bu yoda split domaindan -1 yani undan oldingi indexdagi malumoyi tekshiradi ya'ni domeindan oldin '@' bormi yoki yo'qligini



            if allowed_domains not in value:
                raise serializers.ValidationError(f"Invalid email. You forgot to write '@' before your domain : {domain}")
            elif  allowed_domains not in value:
                raise serializers.ValidationError(f"❌ {allowed_domains} dan foydalanish mumkin emas! /n Boshqa email bilan urinib ko'ring")  #bu yoda kod prosta sal pal prikol uchn ishlatildi