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