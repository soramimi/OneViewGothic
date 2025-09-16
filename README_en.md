# OneVine Gothic

A custom monospace font combining the best of both worlds for programming with mixed Latin and Japanese text.

![sample image](https://soramimi.github.io/OneVineGothic/sample.png)

## Overview

OneVine Gothic is a composite font that merges:
- **Intel One Mono** - A typeface designed specifically for source code
- **VL Gothic** - High-quality Japanese font

This creates a cohesive coding font that maintains proper monospace characteristics while providing excellent support for Japanese characters (Kanji, Hiragana, Katakana).

## Features

- **Monospace design** - Perfect for code editors and terminals
- **ASCII characters** - Clean, readable Latin characters from Intel One Mono font
- **Japanese characters** - Full support for Japanese text from VL Gothic
- **Consistent metrics** - Unified ascent, descent, and line spacing
- **Programming optimized** - Designed specifically for source code readability

## Prerequisites

- **FontForge** - Required for building the font
- **Python** - For running the build script
- **Make** - For using the Makefile (optional)

## Building the Font

### Using Make (Recommended)

```bash
# Download source fonts and build
make

# Install the font to system
make install

# View font information
make scan

# Clean generated files
make clean
```

### Manual Build

```bash
# Ensure source fonts are available
python makefont.py
```

## Installation

### Windows
1. Build the font using the instructions above
2. Right-click on `OneVine-Gothic-Regular.ttf`
3. Select "Install" or "Install for all users"

### macOS
1. Double-click `OneVine-Gothic-Regular.ttf`
2. Click "Install Font" in Font Book

### Linux
```bash
# Copy to user fonts directory
cp OneVine-Gothic-Regular.ttf ~/.local/share/fonts/

# Refresh font cache
fc-cache -fv
```

## Usage

Configure your editor or terminal to use "OneVine Gothic" as the font family.

### Popular Editors

**VS Code**
```json
{
    "editor.fontFamily": "OneVine Gothic, monospace"
}
```

**Vim/Neovim**
```vim
set guifont=OneVine\ Gothic:h12
```

**Emacs**
```elisp
(set-face-attribute 'default nil :font "OneVine Gothic-12")
```

## Source Fonts

- **Intel One Mono**: [Intel One Mono](https://github.com/intel/intel-one-mono)
- **VL Gothic**: [VL Gothic Font Family](http://vlgothic.dicey.org/)

## License

This project combines fonts with different licenses:
- Intel One Mono font is licensed under the SIL Open Font License
- VL Gothic is licensed under a BSD-style license

Please refer to the original font licenses for usage terms.

## Contributing

Feel free to open issues or submit pull requests to improve the font generation process or documentation.

## Troubleshooting

### FontForge not found
Make sure FontForge is installed and available in your PATH.

### Build fails
Ensure both source fonts are present in the `original/` directory. Run `make download` to fetch them automatically.

### Font not appearing in applications
Try refreshing your system's font cache:
- Windows: Restart the application
- macOS: Restart Font Book
- Linux: Run `fc-cache -fv`
