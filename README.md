# Password Generator

A small Python-based password generator with optional Docker packaging. Generates secure, customizable passwords from the command line.

## Features

- Generate strong random passwords
- Control length and character sets (lowercase, uppercase, digits, symbols)
- Option to exclude similar characters
- Easy to run locally with Python or inside Docker

## Requirements

- Python 3.8+
- Docker (optional, for containerized usage)

## Installation (local)

1. Clone the repository:

   git clone https://github.com/murtaza2k/password_generator.git
   cd password_generator

2. (Optional) Create and activate a virtual environment:

   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .\.venv\Scripts\activate  # Windows (PowerShell)

3. Install dependencies (if any):

   pip install -r requirements.txt

## Usage (CLI)

Run the main script (adjust file name if different):

   python generate_password.py --length 16 --upper --digits --symbols

Common options:

- `--length N`        : Set password length (default: 12)
- `--lower`           : Include lowercase letters (default: true)
- `--upper`           : Include uppercase letters
- `--digits`          : Include digits
- `--symbols`         : Include punctuation / symbols
- `--exclude-similar` : Exclude similar characters (e.g. `l`, `1`, `I`, `O`, `0`)
- `--count N`         : Generate N passwords

Example:

   python generate_password.py --length 20 --upper --digits --symbols --count 5

If your repository provides a different entrypoint, replace `generate_password.py` with the correct file.

## Docker

Build the image:

   docker build -t password-generator:latest .

Run the container (example running a single command):

   docker run --rm password-generator:latest --length 20 --upper --digits --symbols

If you want an interactive shell to run multiple commands:

   docker run --rm -it password-generator:latest /bin/sh

Notes:
- Ensure the Dockerfile exposes a sensible entrypoint or CMD that runs the generator script or accepts CLI args.

## Examples

Generate one 16-character password with letters and digits:

   python generate_password.py --length 16 --upper --digits

Generate five 24-character passwords including symbols:

   python generate_password.py --length 24 --upper --digits --symbols --count 5

## Contributing

Contributions are welcome. Please open issues/PRs for bugfixes, features, or documentation improvements.

## License

Specify a license (e.g. MIT) in LICENSE file if desired.

## Contact

Created by murtaza2k. Questions or suggestions — open an issue in this repository.