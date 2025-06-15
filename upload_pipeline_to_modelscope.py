import dotenv

dotenv.load_dotenv(override=True)

from modelscope.hub.constants import Licenses, ModelVisibility
from modelscope.hub.api import HubApi


save_path = "/share_2/luoxin/projects/OmniGen2/pretrained_models/omnigen2_pipe_model_fuse_v17"

api = HubApi()
api.login(YOUR_ACCESS_TOKEN)

owner_name = 'user'
model_name = 'my-test-model'
model_id = f"{owner_name}/{model_name}"

api.create_model(
    model_id,
    visibility=ModelVisibility.PUBLIC,
    license=Licenses.APACHE_V2,
    chinese_name="我的测试模型"
)

api.upload_folder(
    repo_id=f"{owner_name}/{model_name}",
    folder_path=save_path,
    commit_message='upload model folder to repo',
)