import attrs


@attrs.define
class Command:
    host: str | None = None
    guest: str | None = None
    host_analytics_data: dict | None = None
    guest_analytics_data: dict | None = None
    total_predict: dict | None = None
    history_host: list[dict] | None = None
    history_guest: list [dict]| None = None


@attrs.frozen
class Game:
    game: str | None = None
    date: str | None = None
    host_position: str | None =None
    guest_position: str | None =None
    # добавить котировки БК


@attrs.frozen
class League:
    league_name: str | None = None
    game: Game | None = None
    commands: Command | None = None


