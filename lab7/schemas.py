
# PASCO Capstone data format schemas

from typing import List, Dict
from pydantic import BaseModel


class DataSubSet(BaseModel):
    label: str
    rows: List[tuple] = []

    def __iter__(self):
        return iter(self.rows)


class DataSet(BaseModel):
    session: str
    subsets: Dict[str, DataSubSet] = {}

    def __getitem__(self, key):
        return self.subsets[key]

    def __iter__(self):
        return iter(self.subsets)


class Data:
    sets: Dict[str, DataSet] = {}

    def __getitem__(self, key):
        return self.sets[key]
    
    def __iter__(self):
        return iter(self.sets)
