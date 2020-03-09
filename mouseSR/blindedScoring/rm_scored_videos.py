import os
import shutil


def rm_scored_videos(Dir_toBeScored, Dir_scored):
    # First get a full list of all folders in the two directories with all extra stuff removed
    # Note the naming conventions in
    #   Dir_toBeScored: 'foldername'
    #   Dir_scored: 'foldername_initials'

    allFolders_toBeScored = os.listdir(Dir_toBeScored)
    allFolders_scored = [item.split('_')[0] for item in os.listdir(Dir_scored)]

    for folder in allFolders_toBeScored:
        if folder not in allFolders_scored:
            continue
        shutil.rmtree(os.path.join(Dir_toBeScored, folder), ignore_errors=True)
