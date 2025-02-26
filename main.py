from fastapi import FastAPI, APIRouter
from configuration import collection
from dataBase.schemas import all_task
from dataBase.models import RenterData
app = FastAPI()
router = APIRouter()


@router.get("/get")
async def get_all_task():
    data = collection.find()
    return all_task(list(data))

@router.post("/add")
async def add_renter_data(renter: RenterData):
    renter_dict = renter.dict()
    inserted = collection.insert_one(renter_dict)
    return {"message": "Data added successfully!!!!", "id": str(inserted.inserted_id)}

app.include_router(router)