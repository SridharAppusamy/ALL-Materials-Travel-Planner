from langchain_core.messages import HumanMessage,AIMessage
from src.chains.itinerary_chain import generate_itinerary
from src.utils.custom_exception import CustomException
from src.utils.logger import get_logger

logger=get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city=""
        self.interests=[]
        self.itinerary=""
        logger.info("initialized travel planner")
    
    def set_city(self,city:str):
        try:
            self.city=city
            self.messages.append(HumanMessage(content=city))
            logger.info("city set succesfully")
        except Exception as e:
            logger.info(f"error while set city:{e}")
            raise CustomException("failed to city",e)
        
    def set_interest(self,interests_str:str):
        try:
            self.interests=[i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("interest set successfully..")
        
        except Exception as e:
            logger.info(f"error while set interest:{e}")
            raise CustomException("failed to interest",e)
        
    
    def create_itineary(self):
        try:
            logger.info(f"creating itineary for city {self.city} and for interest {self.interests}")
            itineary=generate_itinerary(self.city,self.interests)
            self.itinerary=itineary
            self.messages.append(AIMessage(content=itineary))
            logger.info("Itineary  generated successfully")
            return itineary
        except Exception as e:
            logger.info(f"error while create Itineary:{e}")
            raise CustomException("failed to Itineary",e)

        
        
        
