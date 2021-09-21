import os

dirs = [
    os.path.join("data","PetImages"),
    os.path.join("VGGmodel" , "checkpoints"),
    os.path.join("base_log_dir" , "tensorboard_log_dir"),
    "utils",

]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass

files = [
    "dvc.yaml",
    "_config.yaml",
    ".gitignore",
    os.path.join("utils","__init__.py")


]

for file_ in files:
    with open(file_,"w") as f:
        pass
