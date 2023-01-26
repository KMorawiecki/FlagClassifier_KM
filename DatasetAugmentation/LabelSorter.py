import os
import shutil


class LabelSorter:
    def sort_labels_in_dir(self, dir_path):
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                dir_name = path.split('.')[0]
                os.mkdir(f'{dir_path}/{dir_name}')
                shutil.move(os.path.join(dir_path, path), f'{dir_path}/{dir_name}')
