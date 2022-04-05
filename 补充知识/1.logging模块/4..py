import logging
import sys

handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.DEBUG,handlers=[handler])

# 或者指定stream参数
# logging.basicConfig(level=logging.DEBUG,stream=sys.stdout)

logging.info('info')