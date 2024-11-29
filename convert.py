from PIL import Image
import os

# Open source images
print("Loading source images.")
adaptive = Image.open(os.path.join("source", 'adaptive.png'))
print("adaptive.png loaded")
background = Image.open(os.path.join("source", 'background.png'))
print("background.png loaded")
legacy = Image.open(os.path.join("source", 'legacy.png'))
print("legacy.png loaded")

# file names
file_names = {
  "adaptive_foreground": "adaptiveproduct_youtube_foreground_color_108.png",
  "adaptive_background": "adaptiveproduct_youtube_background_color_108.png",
  "legacy": "ic_launcher.png",
  "rounded": "ic_launcher_round.png"
}

# Define sizes
sizes = {
  "mipmap-mdpi": [48, 108],
  "mipmap-hdpi": [72, 162],
  "mipmap-xhdpi": [96, 216],
  "mipmap-xxhdpi": [144, 324],
  "mipmap-xxxhdpi": [192, 432],
}

# generate icons
for folder_name, size in sizes.items():
  legacy_size = size[0]
  adaptive_size = size[1]

  print(f"Generating {folder_name} [adaptive: {adaptive_size}] [legacy: {legacy_size}]")

  os.makedirs(folder_name, exist_ok=True)

  resized_adaptive = adaptive.resize((adaptive_size, adaptive_size), Image.Resampling.LANCZOS)
  resized_background = background.resize((adaptive_size,adaptive_size), Image.Resampling.LANCZOS)
  resized_legacy = legacy.resize((legacy_size,legacy_size), Image.Resampling.LANCZOS)
  resized_rounded = legacy.resize((legacy_size,legacy_size), Image.Resampling.LANCZOS)

  resized_adaptive.save(os.path.join(folder_name, file_names['adaptive_foreground']))
  print("adaptive_foreground resized and saved.")
  resized_background.save(os.path.join(folder_name, file_names['adaptive_background']))
  print("adaptive_background resized and saved.")
  resized_legacy.save(os.path.join(folder_name, file_names['legacy']))
  print("legacy resized and saved.")
  resized_rounded.save(os.path.join(folder_name, file_names['rounded']))
  print("legacy_rounded resized and saved.")


print("All done.")