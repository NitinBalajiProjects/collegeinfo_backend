import pandas as pd

class ExcelToJsonUtil:
    """Utility class to convert Excel files to JSON format."""
    
    @staticmethod
    def convert_to_json(excel_path: str, orient: str = "records", indent: int = 4) -> str:
        """
        Reads an Excel file and converts it to JSON.
        
        :param excel_path: Path to the Excel file.
        :param orient: JSON format orientation (default: "records").
        :param indent: Indentation for pretty-printing (default: 4).
        :return: JSON string representation of the Excel data.
        """
        try:
            df = pd.read_excel(excel_path)
            return df.to_json(orient=orient, indent=indent)
        except Exception as e:
            return f"Error: {e}"
        
