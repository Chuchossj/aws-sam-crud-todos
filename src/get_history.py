from boto3.dynamodb.conditions import Key

from utils import audit_table, response


def handler(event, context):
    todo_id = event["pathParameters"]["id"]

    result = audit_table.query(
        KeyConditionExpression=Key("todoId").eq(todo_id),
        ScanIndexForward=True,
    )

    return response(200, {
        "todoId": todo_id,
        "count": len(result.get("Items", [])),
        "history": result.get("Items", []),
    })
