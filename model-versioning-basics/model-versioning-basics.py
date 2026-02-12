from datetime import datetime

def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    
    models = sorted(
        models,
        key=lambda x: (
            x["accuracy"],
            -x["latency"],
            datetime.fromisoformat(x["timestamp"]).timestamp()
            ),
        reverse=True
    )

    return models[0]["name"]