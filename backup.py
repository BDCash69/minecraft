import zipfile, os
# from datetime import datetime
# now=datetime.now().strftime('%Y-%m-%d %H.%M.%S')
source = "C:/Users/bdcas/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/minecraftWorlds"
output_base = 'C:/Users/bdcas/OneDrive/Desktop/python/minecraft/'

def zip_folder(path_to_folder, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(path_to_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zf.write(file_path, os.path.relpath(file_path, path_to_folder))

def get_first_folder_paths(target_folder):
    folder_paths = []
    entries = os.listdir(target_folder)
    for entry in entries:
        entry_path = os.path.join(target_folder, entry) # Construct the full path to the entry
        # Check if the entry is a directory
        if os.path.isdir(entry_path):
            folder_paths.append(entry_path)
    return folder_paths

worlds = get_first_folder_paths(source)

for world in worlds:
    # Read world name
    txt = os.path.join(world,'levelname.txt')
    with open(txt, 'r') as file:
        world_name = file.read()
    output_path = os.path.join(output_base, f'{world_name}.mcworld')
    zip_folder(world, output_path)
    print('Saved', world_name)