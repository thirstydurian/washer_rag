from huggingface_hub import hf_hub_download
import os

# 현재 스크립트가 있는 디렉토리 (data/models)
current_dir = os.path.dirname(os.path.abspath(__file__))

print(f"다운로드 경로: {current_dir}")

model_path = hf_hub_download(
    repo_id="mykor/A.X-4.0-Light-gguf",
    filename="A.X-4.0-Light-Q4_K_M.gguf",
    local_dir=current_dir,
    local_dir_use_symlinks=False
)

print(f"✅ 모델 다운로드 완료: {model_path}")