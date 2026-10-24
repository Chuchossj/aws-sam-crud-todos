# CRUD de TODOs con AWS SAM

Workshop de arquitectura serverless en AWS para crear una API REST de gestión de tareas (TODOs).

## Arquitectura

La aplicación utiliza:

- Amazon API Gateway para exponer los endpoints REST.
- AWS Lambda con Python 3.13 para ejecutar las operaciones CRUD.
- Amazon DynamoDB para almacenar las tareas.
- AWS SAM para definir y desplegar la infraestructura.
- Amazon CloudWatch para consultar los logs de las funciones.

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/todos` | Crear un TODO |
| GET | `/todos` | Listar todos los TODOs |
| GET | `/todos/{id}` | Consultar un TODO |
| PUT | `/todos/{id}` | Actualizar un TODO |
| DELETE | `/todos/{id}` | Eliminar un TODO |

## Estructura

```text
todo-sam/
├── template.yaml
├── samconfig.toml
├── README.md
├── src/
│   ├── requirements.txt
│   ├── utils.py
│   ├── create_todo.py
│   ├── list_todos.py
│   ├── get_todo.py
│   ├── update_todo.py
│   └── delete_todo.py
└── evidencias/
```

## Despliegue

```bash
sam validate --lint
sam build
sam deploy
```

## Pruebas realizadas

| Prueba | Resultado |
|---|---|
| Crear TODO | 201 |
| Listar TODOs | 200 |
| Consultar TODO | 200 |
| Actualizar TODO | 200 |
| Eliminar TODO | 204 |
| Error por falta de `title` | 400 |
| TODO inexistente | 404 |

## ¿Qué aprendí?

Durante este workshop aprendí a crear y desplegar una aplicación serverless utilizando AWS SAM.

También aprendí a conectar API Gateway, AWS Lambda y DynamoDB para construir una API REST con operaciones CRUD.

Además, aprendí a:

- Definir infraestructura como código con `template.yaml`.
- Validar y desplegar proyectos con AWS SAM.
- Probar endpoints utilizando `curl`.
- Revisar logs de las funciones Lambda en CloudWatch.
- Solucionar errores de despliegue en CloudFormation.
- Utilizar Git y GitHub para versionar y entregar el proyecto.

## Evidencias

Las capturas de las pruebas, errores, logs y despliegue se encuentran en la carpeta:

```text
evidencias/
```
