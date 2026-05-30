from insightface.app import FaceAnalysis

app = FaceAnalysis(
    providers=['CPUExecutionProvider']
)

app.prepare(ctx_id=0)

def get_embedding(image):

    faces = app.get(image)

    if len(faces) == 0:
        return None

    return faces[0].embedding