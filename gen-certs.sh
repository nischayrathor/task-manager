#!/usr/bin/env bash

# Script to bootstrap SSL Certficates

mkdir certs/

## Genrate CA Certificate
openssl req -new -nodes -text -out certs/root.csr \
  -keyout certs/root.key -subj "/CN=nischay.in"

openssl x509 -req -in certs/root.csr -text -days 3650 \
  -signkey certs/root.key -out certs/root.crt

## Creating Server certificate
openssl req -new -nodes -text -out certs/server.csr \
  -keyout certs/server.key -subj "/CN=pg.nischay.in"

openssl x509 -req -in certs/server.csr -text -days 1325 \
  -CA certs/root.crt -CAkey certs/root.key -CAcreateserial \
  -out certs/server.crt

## Using certs

## at server side
## server.crt and server.key should be stored on the server

## At Client side
## and root.crt should be stored on the client so the client can verify that the server's leaf certificate was signed by its trusted root certificate.