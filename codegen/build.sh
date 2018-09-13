#!/bin/bash

if [ $1 = "server" ]
then
    if [ ! -f swagger-codegen-cli.jar ]
    then
        wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
    fi
    mkdir ../src-gen
    mkdir ../src-gen/swagger_server
    cd ../src-gen/swagger_server/
    ln -s ../../src/server_impl/
    cd ../../codegen
    java -jar swagger-codegen-cli.jar generate \
    -i ../src/swagger_def/swagger.yaml \
    -l python-flask \
    -DsupportPython2=true \
    -o ../src-gen/ \
    -t ./templates \
    --verbose
    cd ../src-gen/
    python -m swagger_server
elif [ $1 = "clean" ]
then
    if [ -d ../src-gen ]
    then
        rm -rf ../src-gen
    fi
elif [ $1 = "deep-clean" ]
then
    if [ -d ../src-gen ]
    then
        rm -rf ../src-gen
    fi
    if [ -f swagger-codegen-cli.jar ]
    then
        rm swagger-codegen-cli.jar
    fi
else
    echo "Unrecognized build command"
fi