from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="cargo-deepagents",
    version="1.0.0",
    author="kulharir7",
    author_email="",
    description="Complete DeepAgents package with 13 agents and 10 MCP plugins",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kulharir7/cargo-deepagents",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["*.md", "*.toml", "*.py"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "mcp>=1.0.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
    ],
    extras_require={
        "database": ["psycopg2-binary>=2.9.0", "pymongo>=4.0.0"],
        "desktop": ["pyautogui>=0.9.0", "Pillow>=10.0.0"],
        "browser": ["playwright>=1.40.0"],
        "dev": ["pytest>=7.4.0", "black>=23.0.0"],
    },
    entry_points={
        "console_scripts": [
            "deepagents=cargo_deepagents.cli:main",
            "cargo-deepagents=cargo_deepagents.cli:main",
        ],
    },
)
