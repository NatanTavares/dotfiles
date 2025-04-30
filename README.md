🛠️ Dotfiles

This repository holds my personal configuration files for various tools like Hyprland, Waybar, Neovim, Ghostty, and more. Managed using GNU Stow, making it easy to symlink configs into ~/.config.

📦 Requirements

Before using these dotfiles, make sure the following are installed:
```bash
sudo pacman -S git stow
```

🧪 Clone the Repo
```bash
git clone https://github.com/NatanTavares/dotfiles.git
cd dotfiles
```

🧷 Apply Configurations with Stow
Each folder in the repo represents a config (e.g., waybar, nvim, wofi). Use stow to symlink them to your home directory.

Example:
```bash
stow waybar
stow nvim
stow wofi
```

| This will symlink each folder into ~/.config, e.g. dotfiles/waybar/config → ~/.config/waybar/config


🔄 Updating Configs

If you update a config file inside this repo, the symlinked file will reflect changes immediately — no need to restow unless you move or rename files.

🧹 Removing Configs

To remove a config symlinked with stow:

```bash
stow -D waybar
```

This will safely unlink the files without deleting them from your repo.

🧠 Notes

    - Some modules (like Waybar's custom MPRIS script) may require additional tools like playerctl or fonts (e.g., Nerd Fonts).

    - Make sure waybar/custom/ scripts are executable (chmod +x).

