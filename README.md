# CRUD de TODOs con AWS SAM

Workshop de arquitectura serverless en AWS para crear una API REST de gestión de tareas (TODOs).

## Arquitectura

La aplicación utiliza:

- Amazon API Gateway para exponer los endpoints REST.
- AWS Lambda con Python 3.13 para ejecutar las operaciones CRUD.
- Amazon DynamoDB para almacenar las tareas.
- AWS SAM para definir y desplegar toda la infraestructura como código.

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| POST | /todos | Crear un TODO |
| GET | /todos | Listar todos los TODOs |
| GET | /todos/{id} | Consultar un TODO |
| PUT | /todos/{id} | Actualizar un TODO |
| DELETE | /todos/{id} | Eliminar un TODO |

## Estructura

todo-sam/
├── template.yaml
├── samconfig.toml
├── src/
│   ├── requirements.txt
│   ├── utils.py
│   ├── create_todo.py
│   ├── list_todos.py
│   ├── get_todo.py
│   ├── update_todo.py
│   └── delete_todo.py
└── README.md

## Despliegue

```bash
sam validate --lint
sam build
sam deploy

