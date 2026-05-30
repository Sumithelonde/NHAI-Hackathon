from src.api.verify import verify

def authenticate(
    image,
    embedding_path,
    liveness_passed
):

    if not liveness_passed:
        return {
            "success": False,
            "message": "Liveness Failed"
        }

    result = verify(
        image,
        embedding_path
    )

    return {
        "success": result["match"],
        "score": result["score"]
    }