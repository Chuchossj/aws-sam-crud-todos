import json


def handler(event, context):
    batch_item_failures = []

    for record in event.get("Records", []):
        try:
            message = json.loads(record["body"])

            event_type = message.get("eventType")
            todo = message.get("data", {})

            # Solo procesar eventos de TODOs completados
            if event_type != "todo.completed":
                continue

            title = todo.get("title", "")

            # Simular un fallo para probar los reintentos y la DLQ
            if "#fail" in title:
                raise RuntimeError(
                    f"Fallo simulado para el TODO: {title}"
                )

            print(
                f"Notificación procesada correctamente: "
                f"TODO '{title}' completado. "
                f"ID: {todo.get('id')}"
            )

        except Exception as exc:
            print(
                f"Error procesando mensaje "
                f"{record.get('messageId')}: {exc}"
            )

            batch_item_failures.append({
                "itemIdentifier": record["messageId"]
            })

    return {
        "batchItemFailures": batch_item_failures
    }
