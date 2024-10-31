import attrs


@attrs.frozen
class Command:
    host: str | None = None
    guest: str | None = None
    history_host: list | None = None
    history_guest: list | None = None


@attrs.frozen
class Game:
    game: str | None = None
    date: str | None = None
    # добавить котировки БК


@attrs.frozen
class League:
    league_name: str | None = None
    game: Game | None = None
    commands: Command | None = None


