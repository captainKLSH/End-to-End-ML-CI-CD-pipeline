import logging
import os
from datetime import datetime

logFile=f"{datetime.now().strftime('%m/%d/%Y::%H:%M%S')}.log"
logPath=os.path.join(os.getcwd(),"logs",logFile)
os.makedirs(logPath,exist_ok=True)

logFilePath=os.path.join(logPath,logFile)
logging.basicConfig(
    filename=logFilePath,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

