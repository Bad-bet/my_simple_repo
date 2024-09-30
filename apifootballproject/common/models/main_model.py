import attrs


@attrs.frozen
class History:
    score: int | None = None
    un_score: int | None = None


@attrs.frozen
class Command:
    host: str | None = None
    guest: str | None = None
    history: History | None = None


@attrs.frozen
class Game:
    game: str | None = None
    date: str | None = None
    # добавить котировки БК


@attrs.frozen
class League:
    league_id: int | None = None
    commands: Command | None = None
    game: Game | None = None

