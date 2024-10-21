import subprocess, os

assets_folder = "./assets/"
if not os.path.exists(assets_folder):
    os.makedirs(assets_folder)

files = {
    "rmvpe/rmvpe.pt": "https://huggingface.co/Rejekts/project/resolve/main/rmvpe.pt",
    "hubert/hubert_base.pt": "https://huggingface.co/Rejekts/project/resolve/main/hubert_base.pt",
    "pretrained_v2/D40k.pth": "https://huggingface.co/Rejekts/project/resolve/main/D40k.pth",
    "pretrained_v2/G40k.pth": "https://huggingface.co/Rejekts/project/resolve/main/G40k.pth",
    "pretrained_v2/f0D40k.pth": "https://huggingface.co/Rejekts/project/resolve/main/f0D40k.pth",
    "pretrained_v2/f0G40k.pth": "https://huggingface.co/Rejekts/project/resolve/main/f0G40k.pth",
}

for file, link in files.items():
    file_path = os.path.join(assets_folder, file)
    if not os.path.exists(file_path):
        try:
            print(f"Downloading {file} from {link}...")
            process = subprocess.Popen(
                ["wget", link, "-O", file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            for line in process.stdout:
                print(line, end="")  # Print each line as it's received
            process.wait()  # Wait for the process to finish
            if process.returncode != 0:
                print(f"Error downloading {file}")
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {file}: {e}")
