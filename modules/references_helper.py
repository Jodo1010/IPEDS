import json

class Reference:
    
    MASU = {
        'Eastern Michigan University': 169798,
        'Oakland University': 171571,
        'Central Michigan University': 169248,
        'Western Michigan University': 172699,
        'University of Michigan-AA': 170976,
        'University of Michigan-Dearborn': 171137,
        'University of Michigan-Flint': 171146,
        'Wayne State University': 172644,
        'Saginaw Valley State University': 172051,
        'Northern Michigan University': 171456,
        'Michigan Technological University': 171128,
        'Ferris State University': 169910,
        'Michigan State University': 171100,
        'Lake Superior State University': 170639,
        'Grand Valley State University': 170082
    }

    ALL = {}

    @staticmethod
    def get_masu():
        return Reference.MASU

    @staticmethod
    def load_institution_data(file_name='institution_data.txt'):
        try:
            print(f"Attempting to load data from {file_name}...")  # Debugging print
            with open(file_name, 'r') as file:
                Reference.ALL = json.load(file)
                print(f"Successfully loaded institution data from {file_name}.")
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding the JSON data in {file_name}.")
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")

if __name__ == "__main__":

    # print(Reference.get_masu())
    Reference.load_institution_data()
    print(Reference.ALL)
