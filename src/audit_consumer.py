import json

from utils import audit_table


def handler(event, context):
    batch_item_failures = []

    for record in event.get("Records", []):
        try:
            # Leer el mensaje recibido desde SQS
            message = json.loads(record["body"])

            todo = message["data"]
            event_id = message["eventId"]
            event_type = message["eventType"]
            occurred_at = message["occurredAt"]

            # Construir el registro de auditoría
            item = {
                "todoId": todo["id"],
                "sk": f"{occurred_at}#{event_id}",
                "eventId": event_id,
                "eventType": event_type,
                "occurredAt": occurred_at,
                "source": message.get("source", "todos-api"),
                "todo": todo,
            }

            # Guardar el evento evitando duplicados
            try:
                audit_table.put_item(
                    Item=item,
                    ConditionExpression=(
                        "attribute_not_exists(todoId) "
                        "AND attribute_not_exists(sk)"
                    ),
                )
            except audit_table.meta.client.exceptions.ConditionalCheckFailedException:
                # El evento ya existe: no es necesario guardarlo otra vez
                pass

        except Exception as exc:
            print(f"Error procesando mensaje {record.get('messageId')}: {exc}")

            batch_item_failures.append({
                "itemIdentifier": record["messageId"]
            })

    return {
        "batchItemFailures": batch_item_failures
    }
