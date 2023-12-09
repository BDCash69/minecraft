## Backup Minecraft World
# from datetime import datetime
# import shutil
# now=datetime.now().strftime('%Y-%m-%d %H.%M.%S')
# source = "c:/Users/bcash/Desktop/bedrock-server-1.20.40.01/worlds/The New Server/"
# destination = f"z:/Backup/minecraft/The New Server {now}/"
# shutil.copytree(source, destination)

# print(f'Copied to : {destination}')

import zipfile, os
from datetime import datetime
now=datetime.now().strftime('%Y-%m-%d %H.%M.%S')
source = "c:/Users/bcash/Desktop/bedrock_server/worlds/"
destination = f"y:/minecraft/Server_World_Backups_{now}.zip"


def zip_folder(path_to_folder, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(path_to_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zf.write(file_path, os.path.relpath(file_path, path_to_folder))


# Example usage zip_folder('/Users/johndoe/Documents/my_folder', '/Users/johndoe/Documents/my_folder.zip')

if __name__ == '__main__':
    zip_folder(source, destination)
    print(f'Saved to : {destination}')