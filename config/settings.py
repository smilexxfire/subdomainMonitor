from common.utils import read_ini_config
import platform
# 禁用所有警告信息
import warnings
warnings.filterwarnings("ignore")

# 当前系统Windows or Linux
PLATFORM = platform.system()
# 路径设置
import pathlib
relative_directory = pathlib.Path(__file__).parent.parent  # 项目代码相对路径
third_party_dir = relative_directory.joinpath('thirdparty')  # 三方工具目录
result_save_dir = relative_directory.joinpath('result')  # 结果保存目录
module_dir = relative_directory.joinpath('modules')

# 读取配置文件 - subdomain
SUBDOMAIN_MODULE = read_ini_config("subdomain", "module")
SUBDOMAIN_ASSERT_NAME = read_ini_config("subdomain", "assert_name")

# 读取配置文件 - rabbitmq
RABBITMQ_HOST = read_ini_config("rabbitmq", "host")
RABBITMQ_PORT = read_ini_config("rabbitmq", "port")
RABBITMQ_USER = read_ini_config("rabbitmq", "username")
RABBITMQ_PASSWORD = read_ini_config("rabbitmq", "password")
RABBITMQ_QUEUE_NAME = read_ini_config("rabbitmq", "queue_name")

# 读取配置文件 - mongo
MONGO_HOST = read_ini_config("mongo", "host")
MONGO_PORT = read_ini_config("mongo", "port")
MONGO_USER = read_ini_config("mongo", "username")
MONGO_PASSWORD = read_ini_config("mongo", "password")
MONGO_DATABASE = read_ini_config("mongo", "database")