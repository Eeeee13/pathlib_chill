
from pathlib import Path
import shutil
import os


class ppathlib:

    def _found_dir_path(self, dir_name: str) -> str:
        _dir_list =  list(Path.home().glob(f'**/{dir_name}')) # нахожу путь к заданной директории 
        file_path = _dir_list[0]
        return file_path

    def found_root_dirs(self)-> list[str]:
        root: str = Path.home()
        first_dirs: list[str] 
        first_dirs = [dir_.name for dir_ in root.iterdir() if dir_.is_dir()] # достаю все папки из корневой
        return first_dirs
    
    def found_all_dirs_in_your_dir(self, dir_name: str)-> list[str]: 
        _dir_path = self._found_dir_path(dir_name)
        list_dirs: list[str]
        list_dirs = [dir_.name for dir_ in _dir_path.iterdir() if dir_.is_dir()] # достаю все папки из заданной дерриктории 
        return list_dirs
    
    def rename_file(self, file_name: str, new_name:str)-> str:
        file_path = self._found_dir_path(file_name)
        file_path.rename(new_name)
        return f"{file_name} has been rename into {new_name}"
    
    def move_file(self, file_name: str, new_place_name:str )-> str:
        file_path = self._found_dir_path(file_name)

        for file in Path(file_path).glob(file_name):
            shutil.move(os.path.join(file_name,file), new_place_name)
            return f"file has been moved to {new_place_name}"
        
    def change_suffix(self, file_name: str, new_suffix: str) -> str:
        file_path = self._found_dir_path(file_name)
        file_path.with_suffix(new_suffix) 
        return "suffix has been change"

    



        