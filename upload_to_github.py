import os
import subprocess
import sys

# === CONFIGURATION ===
folder_path = r"C:\ComfyUI"
repo_url = "git@github.com:Lins0415/ComfyUI_for_Image_to_Video_and_3D_Model.git"  # SSH URL only!

try:
    print(f"📁 Changing directory to: {folder_path}")
    os.chdir(folder_path)

    print("🔧 Initializing Git (if not already)...")
    subprocess.run(["git", "init"], check=True)

    # 🔍 Check if remote 'origin' exists
    result = subprocess.run(["git", "remote"], capture_output=True, text=True)
    remotes = result.stdout.strip().split()

    if "origin" in remotes:
        print("🔄 Remote 'origin' already exists. Updating URL...")
        subprocess.run(["git", "remote", "set-url", "origin", repo_url], check=True)
    else:
        print("🔗 Adding remote 'origin'...")
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)

    print("➕ Staging all files...")
    subprocess.run(["git", "add", "."], check=True)

    print("💬 Committing changes...")
    subprocess.run(["git", "commit", "-m", "Initial SSH upload to GitHub"], check=True)

    print("🌿 Setting branch to 'main'...")
    subprocess.run(["git", "branch", "-M", "main"], check=True)

    print("🚀 Pushing to GitHub via SSH...")
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

    print("\n✅ Done! Your project is now uploaded to GitHub.")

except subprocess.CalledProcessError as e:
    print(f"\n❌ Git command failed:\n{e}")

