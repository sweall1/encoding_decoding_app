from rest_framework import serializers
import random
import re
from .models import Encoder, Decoder


class EncoderSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Encoder
        fields = '__all__'

    def create(self, validated_data):

        data = Encoder.objects.create(**validated_data)
        text = validated_data.pop('text')

        text = re.split('\s+', text)
        w = []

        for x in range(len(text)):
            q = text[x][0] + ''.join(random.sample(text[x][1:-1], len(text[x][1:-1]))) + text[x][-1]
            w.append(q)
        stri = ''
        for ele in w:
            stri += ele
            stri += ' '

        data.text = stri
        data.save()
        return data


class DecoderSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Decoder
        fields = '__all__'

    def create(self, validated_data):

        data = Decoder.objects.create(**validated_data)

        text = validated_data.pop('text')

        result = re.search('-weird-(.*)-weird-(.*)', text)
        a = result.group(1).split(" ")
        b = result.group(2).split(" ")
        word_list = list(filter(None, a))
        key_word_list = list(filter(None, b))

        for x in range(len(word_list)):
            for y in range(len(key_word_list)):
                if word_list[x][0] == key_word_list[y][0] and word_list[x][-1] == key_word_list[y][-1] and len(word_list[x]) == len(key_word_list[y]):
                    word_list[x] = key_word_list[y]

        stri = ''
        for ele in word_list:
            stri += ele
            stri += ' '

        data.text = stri
        data.save()
        return data