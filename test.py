import pyarrow.parquet as pq

from tutorials.tutorial_utils import download_droid_robotics
droid_compat_root = download_droid_robotics()
# fd = pq.read_table('tutorials/data/droid_100_minimal/lerobot_compat/data/chunk-000/episode_000000.parquet').to_pandas()
# print(fd.head())
# print(f"{fd.columns=}")
# print(f"{fd.dtypes=}")

# ==========================================
# import glob
# import subprocess
# from pathlib import Path

# DROID_CAMERAS = [
#     "observation.images.exterior_image_1_left",
#     "observation.images.exterior_image_2_left",
#     "observation.images.wrist_image_left",
# ]
# COMPAT_ROOT = Path("tutorials/data/droid_100_minimal/lerobot_compat").resolve()
# PREPROC_ROOT = Path("tutorials/data/droid_100_minimal/preprocessed").resolve()
# PREPROC_MANIFEST = PREPROC_ROOT / "shards/manifest.jsonl"
# PREPROC_STATS = PREPROC_ROOT / "shards/stats.json"
# vlm_exp_dir = sorted(glob.glob("tutorials/checkpoints/*vlm*"))[-1]
# # vlm_ckpt = sorted(glob.glob(f"{vlm_exp_dir}/checkpoints/checkpoint_*.pt"))[-1]

# if PREPROC_MANIFEST.exists() and PREPROC_STATS.exists():
#     print(f"Using existing preprocessed data at {PREPROC_MANIFEST}.")
# else:
#     preprocess_cmd = [
#         "uv",
#         "run",
#         "--group",
#         "preprocessing",
#         "python",
#         "vla_foundry/data/preprocessing/preprocess_robotics_to_tar.py",
#         "--type",
#         "lerobot",
#         "--source_episodes",
#         f"['{COMPAT_ROOT}']",
#         "--output_dir",
#         str(PREPROC_ROOT),
#         "--camera_names",
#         str(DROID_CAMERAS),
#         "--observation_keys",
#         "['observation.state']",
#         "--action_keys",
#         "['action']",
#         "--samples_per_shard",
#         "32",
#         "--config_path",
#         "tutorials/tutorial_utils/robotics_preprocessing_params_tutorial.yaml",
#         "--max_episodes_to_process",
#         "2",
#         "--db_logging",
#         "False",
#     ]
#     print("Running preprocessing:")
#     print(" ".join(preprocess_cmd))
#     subprocess.run(preprocess_cmd, check=True)
# # print(f"VLM checkpoint for backbone: {vlm_ckpt}")
# print(f"DROID manifest: {PREPROC_MANIFEST}")
# print(f"DROID stats:    {PREPROC_STATS}")
# ==========================================

droid_manifest = str(Path("tutorials/data/droid_100_minimal/preprocessed/shards/manifest.jsonl").resolve())
droid_stats = str(Path("tutorials/data/droid_100_minimal/preprocessed/shards/stats.json").resolve())
print(f"{droid_manifest=}")
print(f"{droid_stats=}")