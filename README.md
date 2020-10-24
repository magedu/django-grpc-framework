# django-grpc-framework
Django gRPC Framework

### Generating code

```shell script
python manage.py compileprotos
```

### Clean generated code

```shell script
python manage.py cleanprotos
```

### Run gRPC server

```shell script
python manage.py rungrpcserver
```

### settings
```python
GRPC_FRAMEWORK = {
    'PROTOBUF_DIR': 'protos', # protobuf files directory
    'TMP_DIR': '.generated', # generated files temporary directory
    'BIND': '127.0.0.1:5051', # gRPC server bind address and port
    'MAX_WORKERS': 8 # gRPC server worker number
}
```