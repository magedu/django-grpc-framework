import os
import shutil
from pathlib import Path
from django.core.management.base import BaseCommand
from ._config import GrpcFrameworkSettings
from ._utils import LoggingMixIn


class Command(LoggingMixIn, BaseCommand):
    help = 'Compile protobuf files'
    settings = GrpcFrameworkSettings()
    force = False
    verbosity = 1

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('-y', action='store_true', dest='force')

    def rmdir(self, target: Path):
        sub_items = set(x for x in target.iterdir())
        init_file = target.joinpath('__init__.py')
        cache_dir = target.joinpath('__pycache__')
        re_list = False

        if sub_items == {init_file} or sub_items == {init_file, cache_dir}:
            if init_file.lstat().st_size == 0 and self.prompt(f'delete {init_file}'):
                os.remove(init_file)
                re_list = True

        if re_list:
            sub_items = set(x for x in target.iterdir())

        if (not sub_items or sub_items == {cache_dir}) and self.prompt(f'delete {target}/'):
            shutil.rmtree(target)

    def clear(self):
        prefix = self.settings.temporary_dir
        for root, dirs, files in os.walk(prefix, topdown=False):
            for file in files:
                source = Path(root).joinpath(file).absolute()
                target = self.settings.base_dir.joinpath(source.relative_to(prefix))
                if target.exists() and self.prompt(f'delete {target}'):
                    os.remove(target)
            for d in dirs:
                source = Path(root).joinpath(d).absolute()
                target = self.settings.base_dir.joinpath(source.relative_to(prefix))
                self.rmdir(target)

        if self.prompt(f'delete {prefix}'):
            shutil.rmtree(prefix)

    def handle(self, *args, **options):
        self.verbosity = options.get('verbosity')
        self.force = options.get('force', False)
        self.clear()
