# Project

A query redshift poc using lambda 


## Tabla de Contenidos

- [Requirements](#requirements)
- [Architecture](#architecture)
- [Instalation](#instalation)
- [Use](#use)
- [Evidences](#evidences)
- [Contribution](#contribution)
- [References](#references)


## Requirements

aws account

## Architecture

![architecture_1](./img/architecture_1.png)

## Instalation

-download psycopg2 from https://github.com/jkehler/awslambda-psycopg2 (in this poc we used psycopg2 3.7 the same as in lambda configuration) and upload lambda layer


-lambda code implementation in aws console

-redshift table implementation in aws console


## Use


##### Lambda

code

![lambda_1](./src/img/lambda_1.PNG)

workspace

![lambda_2](./src/img/lambda_2.PNG)

##### Redshift

table

![s3_2](./src/img/s3_2.PNG)


## Evidences



![aws_1](./src/img/aws_1.PNG)

![aws_2](./src/img/aws_2.PNG)


## Contribution

A yml could be added where the aws services are deployed

## References

all things aws

https://www.youtube.com/watch?v=A1zf7DveiUY&t=536s

psycopg2 repository

https://github.com/jkehler/awslambda-psycopg2