

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

    @staticmethod
    def get_masu():
        return Reference.MASU



if __name__ == "__main__":

    print(Reference.get_masu())

