import os
import shutil
import subprocess
import time


def cron():
    while True:
        try:
            CRON_URL = os.environ['CRON_URL']
        except ValueError as exc:
            raise ValueError('') from exc
        if not CRON_URL:
            raise ValueError('CRON_URL is empty.')

        if shutil.which('curl'):
            try:
                subprocess.run(['curl', '-I', CRON_URL])
            except ValueError as exc:
                raise ValueError(' A problem occurred with curl.') from exc
        elif shutil.which('wget'):
            try:
                subprocess.run(['wget', '-S', '--spider', '-O-', CRON_URL])
            except ValueError as exc:
                raise ValueError(' A problem occurred with wget.') from exc
        else:
            raise ValueError('This system doesn\'t install curl and wget.')

        time.sleep(60)


if __name__ == '__main__':
    cron()
