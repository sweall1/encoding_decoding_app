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
        #making a list of ranom words, but saving first and last original letter
        for x in range(len(text)):
            q = text[x][0] + ''.join(random.sample(text[x][1:-1], len(text[x][1:-1]))) + text[x][-1]
            w.append(q)

        # adding data to string
        string_value = ''
        for ele in w:
            string_value += ele
            string_value += ' '

        data.text = string_value
        data.save()
        return data


class DecoderSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Decoder
        fields = '__all__'

    def create(self, validated_data):

        data = Decoder.objects.create(**validated_data)

        text = validated_data.pop('text')
        #looking for values between -weird- and after second -weird-
        result = re.search('-weird-(.*)-weird-(.*)', text)
        #spliting data into lists
        between_weird = result.group(1).split(" ")
        after_weird = result.group(2).split(" ")
        #removing all empty elements from lists
        word_list = list(filter(None, between_weird))
        key_word_list = list(filter(None, after_weird))
        #replacing words basing on first and last letter and lenght of word
        changed_word_count = 0
        for x in range(len(word_list)):
            for y in range(len(key_word_list)):
                if word_list[x][0] == key_word_list[y][0] and\
                        word_list[x][-1] == key_word_list[y][-1] and\
                        len(word_list[x]) == len(key_word_list[y]):

                    changed_word_count += 1
                    word_list[x] = key_word_list[y]

                #cheking if any given word matches the sentence
        if changed_word_count == 0:
            raise serializers.ValidationError(
                {'text': 'None of the given words matches'})
        #adding data to string
        string_value = ''
        for ele in word_list:
            string_value += ele
            string_value += ' '

        data.text = string_value
        data.save()
        return data
