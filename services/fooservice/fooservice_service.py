#This is a generated service template
from flask import Blueprint
from pydantic import BaseModel

class FooserviceService(Services):
    
    def _validate(args):
        pass
    
    def _logics(self, req) -> (BaseModel, int):
        pass

    def retrieve(self, req: BaseModel) -> (BaseModel, int):
        pass
        
class FooserviceController(Controllers, FooserviceService):

    def __init__(self, blueprint: Blueprint, endpoint: str, methods: List[str]):
        super().__init__(blueprint, endpoint, methods)

    def controller(self):
        try:
            return super().done()
        except FundamentalException as e:
            return super().catcher(err_response, e)
