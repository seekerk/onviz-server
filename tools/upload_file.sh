#!/bin/bash

# Скрипт для тестовой отправки файла на сервер

set -e

NAME=$(date +%s).txt

echo "test file" > ${NAME}

echo "===== Send ${NAME}"

curl -T ${NAME} -u user:12345 ftp://localhost:2121/ || echo "===== SERVER ERROR!!!"

rm ${NAME}
