import json

class ClassCodeGenerator:
    @staticmethod
    def generate_class(json_data):
        class_name = json_data["class_name"]
        attributes = json_data["attributes"]
        methods = json_data["methods"]

        code = f"class {class_name}:\n"

        for attr in attributes:
            code += f"  {attr["name"]}:{attr["type"]}\n"

        code += "\n"
        # Aici urmeaza sa generam definitiile functiilor
        for method in methods:
            args = ", ".join(method["args"])
            code += f"  def {method["name"]}(self, {args}):"
            if method["return_type"] != "None":
                code += f" -> {method["return_type"]}"
            code += "\n"
            code += f"      {method["body"]}\n"

        return code

def main():
    with open("recapitulare.json", "r") as file:
        json_data = json.load(file)
    generated_code = ClassCodeGenerator.generate_class(json_data)
    print(generated_code)
    # TODO: scrieti codul intr-un fisier separat .py (deschidem un fisier nou interfata_mea.py in modul write.)


if __name__ == "__main__":  # -> cod standard
    main()
