import os
from dataclasses import dataclass
from typing import ClassVar

from dotenv import load_dotenv, set_key, find_dotenv
from pathlib import Path


@dataclass(frozen = True)
class ProgramSettings:


    @staticmethod
    def get_setting(key: str) -> str | None:
        load_dotenv()
        return os.environ.get(key)


    @staticmethod
    def set_setting(key: str, value: str) -> None:
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        os.environ[key] = value
        set_key(dotenv_path, key, value)
