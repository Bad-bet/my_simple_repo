import attrs


@attrs.frozen
class DataInterface:
    html_text: str | None = None
    text: str | None = None
    url: str | None = None


@attrs.frozen
class DataJsonInterface:
    write_json_data: str | None = None
    json_next_tour_name:str | None = None

@attrs.frozen
class DataDBConductorInterface:
    league_idx: str | None = None
    date: list[str] | None = None
    host_command: list[str] | None = None
    guest_command: list[str] | None = None
    host_score: list[int] | None = None
    guest_score: list[int] | None = None
