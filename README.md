# lakitu-connexion

This is intended to act as the interface layer for lakitu.  It takes advantage of swagger and swagger-codegen-cli to build the model and controller.
It then uses the source code to connect lakitu to the interface.  

To run go to:
```
/codegen
```
and run
```
./build.sh server
```

To clean the generated source code
```
./build.sh clean
```

To remove the swagger-codegen-cli as well do:
```
./build.sh deep-clean
```
