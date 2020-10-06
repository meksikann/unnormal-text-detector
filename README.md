# unnormal-text-detector
python Server to check set of sentences for unormality
##install
 ```pip install -r requirements.txt```

## start ASGI server (uvicorn)

```
uvicorn server.main:app --reload
```

##See Docs
```
http://127.0.0.1:8000/docs
```
 

##Test
```
curl --location --request POST 'http://127.0.0.1:8000/api/language_check' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text":"This idwds a test for language check server"
}'
```
