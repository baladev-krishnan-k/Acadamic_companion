#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/planner", tags=["Planner"])

class PlanRequest(BaseModel):
    subject: str
    days_left: int
    hours_per_day: int

@router.post("/create")
async def create_plan(request: PlanRequest):
    total_hours = request.days_left * request.hours_per_day

    plan = f"""
    Study Plan for {request.subject}:
    Total available hours: {total_hours}
    Allocate daily revision and practice evenly.
    """

    return {"plan": plan}

