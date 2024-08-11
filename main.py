from app_initialization import *
import logging
from src.callback_modal import *
import sys

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)],
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8060)
