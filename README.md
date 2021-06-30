DEBUG = False

SECRET_KEY - hidden

Cloud link:
https://encoder-decoder-678.herokuapp.com/

To post data use built-in post field or postman.

http://127.0.0.1:8000/v1/encoder/ create a query e.g:
```
   {
    "text": "This is a veeery shooort sentence"
   }
```

http://127.0.0.1:8000/v2/decoder/ create a query e.g:
```
   {
    "text": "-weird- Tihs is a lnog loonog tset sntceene, wtih smoe big (biiiiig) wdros! -weird- long looong sentence some test This with words! (biiiiig)"
   }
```

Decoder is special characters senstive, so you need to put word with special character to be decoded.

After first "-weird-" put encoded sentence and after second "-weird-" put words to decode.
If none of given "key words" matches, error will be raised.

