# Password Generator

A small Python-based password generator with optional Docker packaging. Generates secure, customizable passwords from the command line.

## Features

- Generate strong random passwords
- Control length and character sets (lowercase, uppercase, digits, symbols)
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

If your repository provides a different entrypoint, replace `generate_password.py` with the correct file.

## Docker

Build the image:

   docker build -t password-generator:latest .

If you want an interactive shell to run multiple commands:

   docker run --rm -it password-generator:latest /bin/sh

Notes:
- Ensure the Dockerfile exposes a sensible entrypoint or CMD that runs the generator script or accepts CLI args.


## Contributing

Contributions are welcome. Please open issues/PRs for bugfixes, features, or documentation improvements.

## License

Specify a license (e.g. MIT) in LICENSE file if desired.

## Contact

Created by murtaza2k. Questions or suggestions — open an issue in this repository.
