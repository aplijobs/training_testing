class ExternalLibrary:
    def fetch_data(self, param: str) -> str:
        return f"Data for {param}"


class DataProcessor:
    def __init__(self, external_library: ExternalLibrary):
        self.external_library = external_library

    def process(self, param: str) -> str:
        try:
            data = self.external_library.fetch_data(param)
            return data.upper()
        except Exception as e:
            return f"Error: {str(e)}"
