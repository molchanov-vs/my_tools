from pydantic import BaseModel


class MetricData(BaseModel):
    
    users: int
    dau: int
    wau: int
    mau: int
    stickness: int 