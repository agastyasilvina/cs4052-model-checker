import json
from flask import Flask, request, jsonify
from simple_model_checker.grammar.formula import Formula

app = Flask(__name__)

class CTL:
  def __init__(self, formula : Formula = None, action_map = None):
    self.formula = formula
    self.action_map = action_map

  def get_formula(self):
    return self.formula

  def get_action_map(self):
    return self.action_map

  @staticmethod
  def create_ctl(file_path=None, json_object=None):
    """
    Returns an instance of CTL generated from a JSON file (e.g /data/ctl.json)
    or a JSON object.

    Args:
        file_path (str, optional): The path of the JSON file. Defaults to None.
        json_object (dict, optional): A JSON object (dictionary). Defaults to None.

    Returns:
        CTL: A CTL object.
    """
    if file_path:
      try:
        with open(file_path, 'r') as f:
          data = json.load(f)
      except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
      except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Invalid JSON in file: {file_path}")
    elif json_object:
      data = json_object
    else:
      raise ValueError("Either file_path or json_object must be provided.")

    formula = data.get("formula")
    action_map = {}
    for i in range(97, 123):  # ASCII 'a' to 'z'
      key = chr(i)
      if key in data and isinstance(data[key], list):
        action_map[key] = data[key]

    return CTL(formula, action_map)

@app.route('/create_ctl', methods=['POST'])
def create_ctl_from_api():
  try:
    data = request.get_json()
    if not data:
      return jsonify({"error": "No JSON data provided"}), 400
    ctl_instance = CTL.create_ctl(json_object=data)
    return jsonify({
      "formula": ctl_instance.get_formula(),
      "action_map": ctl_instance.get_action_map()
    })
  except Exception as e:
    return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
  app.run(debug=True)