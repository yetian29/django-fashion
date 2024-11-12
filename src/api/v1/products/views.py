from ninja import Router

router = Router()


@router.get("")
def hello():
    return {"message": "Hello"}
