import os

asset_dir = '../assets/vehicles/jeep'

for filename in os.listdir(asset_dir):
    if filename.startswith('red_'):
        continue  # Skip files already renamed
    old_path = os.path.join(asset_dir, filename)
    new_path = os.path.join(asset_dir, f'red_{filename}')
    os.rename(old_path, new_path)
