import os
import json
from unittest import result
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

USE_MOCK = True

CACHE_DIR = "cache"

os.makedirs(CACHE_DIR, exist_ok=True)

def get_cache_path(image_path):
    image_id = image_path.replace("\\", "_")
    image_id = image_id.replace("/", "_")
    image_id = image_id.replace(":", "_")
    return os.path.join(CACHE_DIR, image_id + ".json")


load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_image(image_path):

    cache_path = get_cache_path(image_path)

    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            return json.load(f)
        
    if USE_MOCK:

      return {
        "valid_image": True,
        "issue_type": "unknown",
        "object_part": "unknown",
        "severity": "medium",
        "damage_visible": True,
        "risk_flags": []
      }

    image = Image.open(image_path)

    prompt = """
    You are a professional insurance damage assessor.

    Look carefully at the image.

    Return ONLY valid JSON.

    {
    "valid_image": true,
    "issue_type": "",
    "object_part": "",
    "severity": "",
    "damage_visible": true,
    "risk_flags": []
    }

    Rules:

   - Identify visible damage only.
   - If damage cannot be determined, use "unknown".
   - If object is visible and undamaged, use "none".
   - Be specific about object part.
   - Do not guess unseen damage.
   - Return JSON only.

   Allowed issue_type:

   dent
   scratch
   crack
   glass_shatter
   broken_part
   missing_part
   torn_packaging
   crushed_packaging
   water_damage
   stain
   none
   unknown

  Allowed severity:

  none
  low
  medium
  high
  unknown
   """

    try:
        response = model.generate_content(
            [prompt, image]
        )

        result = json.loads(
            response.text.replace(
                "```json", ""
            ).replace(
                "```", ""
            )
        )

    except Exception as e:

      print("VISION ERROR:", e)

      result = {
        "valid_image": True,
        "issue_type": "unknown",
        "object_part": "unknown",
        "severity": "unknown",
        "damage_visible": True,
        "risk_flags": ["manual_review_required"]
      }


    with open(cache_path, "w") as f:
        json.dump(result, f, indent=2)

    return result  